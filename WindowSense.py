import json  # Writing JSON files for thermostat traits output
import requests  # For HTTP-based API calls
import schedule  # Creates and manages a job to keep the WS updating
import threading  # Enables multiple threads to be running at once
from csv import DictWriter  # For logging to .csv
from datetime import datetime  # To add timestamps to the log
from dotenv import load_dotenv  # Load environment variables from files
from os import path, getenv  # Get API creds from environment variables
from pyowm.owm import OWM  # Convenience wrapper for the OWM API
from sense_hat import SenseHat  # Enables all the SenseHAT functions
from subprocess import run  # Enables running the shutdown command
from time import sleep  # For short delays in animations and loops


class WindowSense:
    """Powers the WindowSense Raspberry Pi SenseHAT project through
    functions that get Nest thermostat traits, pull OpenWeatherMap (OWM)
    temperature forecasts, and draw a dynamic graph on the LED matrix.
    Also provides a way to safely shut down the Pi."""
    # Stores the next 8 hours of OWM forecast temps
    forecast_temps = {
        0: 0.0,
        1: 0.0,
        2: 0.0,
        3: 0.0,
        4: 0.0,
        5: 0.0,
        6: 0.0,
        7: 0.0
        }
    # Settings for the SenseHAT LEDs for brightness, text, colors, etc.
    led_settings = {
        'dim_state': True,
        'rotation': 270,
        'scroll_speed': 0.015,  # In seconds; lower is faster
        'graph_speed': 0.05,  # In seconds; lower is faster
        'red': (255, 0, 0),
        'orange': (255, 127, 0),
        'yellow': (255, 255, 0),
        'green': (0, 255, 0),
        'cyan': (0, 255, 255),
        'azure': (0, 127, 255),
        'blue': (0, 0, 255),
        'purple': (127, 0, 255),
        'white': (255, 255, 255),
        'off': (0, 0, 0)  # Turns pixel(s) off
        }
    # Defines the colors to be used for each row of the forecast graph
    graph_colors = {
        0: 'red',
        1: 'orange',
        2: 'yellow',
        3: 'green',
        4: 'green',
        5: 'cyan',
        6: 'azure',
        7: 'blue'
        }
    # Settings for heat/cool setpoints & display colors
    thermostat_traits = {
        'heat_setpoint': {
            'value': 65,  # Nest returns int; default if no Nest setting
            'text': 'Heat to',
            'color': led_settings['orange']
            },
        'cool_setpoint': {
            'value': 75,  # Nest returns int; default if no Nest setting
            'text': 'Cool to',
            'color': led_settings['blue']
            },
        'temperature': {
            'value': 70.00,  # Nest returns float
            'text': 'Temp',
            'color': led_settings['white']
            },
        'humidity': {
            'value': 50,  # Nest returns int
            'text': 'Hum',
            'color': led_settings['cyan']
            },
        }
    program_settings = {
        'off message': {
            'text': 'Off?',
            'color': led_settings['red']
            },
        'wait message': {
            'text': 'Wait 15s',
            'color': led_settings['red']
            }
        }

    @staticmethod
    def c_to_f(temp_c):
        temp_f = (temp_c * 9/5) + 32
        return temp_f

    def get_thermostat(self):
        """Assembles a Google SDM API call using authentication details
        obtained via the Google Device Access & Cloud Platform consoles.
        Gets ambient & setpoint info from the Nest thermostat."""
        load_dotenv('google_auth.env')
        client_id = getenv('CLIENT_ID')
        client_secret = getenv('CLIENT_SECRET')
        refresh_token = getenv('REFRESH_TOKEN')
        project_id = getenv('PROJECT_ID')
        # Refresh the API token
        params = (
            ('client_id', client_id),
            ('client_secret', client_secret),
            ('refresh_token', refresh_token),
            ('grant_type', 'refresh_token'),
            )
        response = requests.post('https://www.googleapis.com/oauth2/v4/token', params=params)
        response_json = response.json()
        access_token = response_json['token_type'] + ' ' + response_json['access_token']

        # Get devices from Google
        url_get_devices = 'https://smartdevicemanagement.googleapis.com/v1/enterprises/' + project_id + '/devices'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': access_token,
        }
        response = requests.get(url_get_devices, headers=headers)
        response_json = response.json()
        device_0_name = response_json['devices'][0]['name']  # Assumes one Nest

        # Get device traits
        url_get_device = 'https://smartdevicemanagement.googleapis.com/v1/' + device_0_name
        headers = {
            'Content-Type': 'application/json',
            'Authorization': access_token,
        }
        response = requests.get(url_get_device, headers=headers)
        response_json = response.json()
        humidity = response_json['traits']['sdm.devices.traits.Humidity']['ambientHumidityPercent']
        self.thermostat_traits['humidity']['value'] = humidity
        temperature = response_json['traits']['sdm.devices.traits.Temperature']['ambientTemperatureCelsius']
        self.thermostat_traits['temperature']['value'] = round(self.c_to_f(temperature))
        heat_setpoint = response_json['traits']['sdm.devices.traits.ThermostatTemperatureSetpoint']['heatCelsius']
        self.thermostat_traits['heat_setpoint']['value'] = round(self.c_to_f(heat_setpoint))
        #cool_setpoint = response_json['traits']['sdm.devices.traits.ThermostatTemperatureSetpoint']['coolCelsius']
        #self.thermostat_traits['cool_setpoint']['value'] = self.c_to_f(cool_setpoint)

        # Write the Nest data to a file for inspection
        with open("thermostat_traits.json", "w") as thermostat_traits:
            json.dump(response_json, thermostat_traits, indent=4)

        print('Temperature:', temperature)
        print('Humidity:', humidity)
        print('Heat setpoint:', heat_setpoint)
        #print('Cool setpoint:', cool_setpoint)

    def get_forecast(self):
        """Assembles an OpenWeatherMap API call using pyowm, gets the
         forecast temperature for the next eight hours."""
        # Builds pyowm call to the OWM API for a location's hourly temps
        load_dotenv('owm_config.env')
        api_key = getenv('API_KEY')
        lat = float(getenv('LATITUDE'))
        lon = float(getenv('LONGITUDE'))
        print(f"{lat}, {lon}")
        owm = OWM(api_key)
        mgr = owm.weather_manager()
        one_call = mgr.one_call(lat=lat, lon=lon, exclude='minutely,daily', units='imperial')
        for key in self.forecast_temps:
            self.forecast_temps[key] = one_call.forecast_hourly[key].temperature().get('temp')
        print(self.forecast_temps)

        # Logs the forecast temps to a .csv file
        now = datetime.now().isoformat(' ')
        log_timestamp = {'Timestamp': now}
        coords = {'Lat': lat, 'Lon': lon}
        row_dict = {**log_timestamp, **coords, **self.forecast_temps}
        field_names = row_dict.keys()
        file_exists = path.exists('Forecast Log.csv')
        with open('Forecast Log.csv', 'a+', newline='') as forecast_log:
            dict_writer = DictWriter(forecast_log, fieldnames=field_names)
            if not file_exists:
                dict_writer.writeheader()
            dict_writer.writerow(row_dict)

    def draw_graph(self):
        """Creates a stylized graph on the SenseHat RGB LED matrix that
        shows if the forecast temperature for the next eight hours will
        be relative to the min/max temps when you're comfortable inside.
        Each column of the SenseHat RGB LED matrix from left to right
        is one hour.  Each row is equal to half of your comfort range.

        The middle two rows represent comfortable temperatures between
        the Nest setpoints and a good opportunity to open the windows.
        The upper and lower rows mean it may be too hot or cold outside
        to open the windows."""
        leds = self.led_settings
        graph = self.graph_colors
        therm = self.thermostat_traits
        heat = therm['heat_setpoint']['value']
        cool = therm['cool_setpoint']['value']
        midpoint = (heat + cool) / 2
        step_size = (heat - cool) / 2
        sense.clear()
        sense.rotation = self.led_settings['rotation']
        sense.low_light = self.led_settings['dim_state']
        if heat < self.forecast_temps[0] < cool:
            sense.show_message('Someone ought to open up a window!',
                               scroll_speed=leds['scroll_speed'],
                               text_colour=leds['green'],
                               back_colour=leds['off'])
        for key in sorted(self.forecast_temps):
            forecast_temp = self.forecast_temps[key]
            if forecast_temp > midpoint:
                for i in range(4):
                    if forecast_temp > (midpoint + step_size * (3-i)):
                        sense.set_pixel(key, i, leds[graph[i]])
                        sleep(self.led_settings['graph_speed'])
            if midpoint > forecast_temp:
                for i in range(3):
                    if forecast_temp < (midpoint - step_size * i):
                        sense.set_pixel(key, i+4, leds[graph[i+4]])
                        sleep(self.led_settings['graph_speed'])
                if forecast_temp > 32:
                    sense.set_pixel(key, 7, leds[graph[7]])
                    sleep(self.led_settings['graph_speed'])
                if forecast_temp <= 32:
                    sense.set_pixel(key, 7, leds['white'])
                    sleep(self.led_settings['graph_speed'])

    def show_setpoints(self):
        """Displays the Nest thermostat heat and cool setpoints."""
        leds = self.led_settings
        therm = self.thermostat_traits
        heat_setpoint_message = f"{therm['heat_setpoint']['text']} {therm['heat_setpoint']['value']}"
        cool_setpoint_message = f"{therm['cool_setpoint']['text']} {therm['cool_setpoint']['value']}"
        sense.show_message(heat_setpoint_message,
                           scroll_speed=leds['scroll_speed'],
                           text_colour=therm['heat_setpoint']['color'],
                           back_colour=leds['off'])
        sense.show_message(cool_setpoint_message,
                           scroll_speed=leds['scroll_speed'],
                           text_colour=therm['cool_setpoint']['color'],
                           back_colour=leds['off'])
        self.draw_graph()

    def show_ambient(self):
        """Displays the Nest thermostat ambient temperature & humidity."""
        leds = self.led_settings
        therm = self.thermostat_traits
        temp_message = f"{therm['temperature']['text']} {therm['temperature']['value']}"
        humidity_message = f"{therm['humidity']['text']} {therm['humidity']['value']}"
        sense.show_message(temp_message,
                           scroll_speed=leds['scroll_speed'],
                           text_colour=therm['temperature']['color'],
                           back_colour=leds['off'])
        sense.show_message(humidity_message,
                           scroll_speed=leds['scroll_speed'],
                           text_colour=therm['humidity']['color'],
                           back_colour=leds['off'])
        self.draw_graph()

    def toggle_brightness(self):
        """Toggles the SenseHAT between high/low brightness settings."""
        leds = self.led_settings
        leds['dim_state'] = not leds['dim_state']
        sense.low_light = leds['dim_state']

    def turn_off_prompt(self):
        """Asks for confirmation to turn off the Raspberry Pi."""
        leds = self.led_settings
        program = self.program_settings
        sense.show_message(program['off message']['text'],
                           scroll_speed=leds['scroll_speed'],
                           text_colour=program['off message']['color'],
                           back_colour=leds['off']
                           )
        stick = sense.stick.wait_for_event(emptybuffer=True)
        if stick.direction == 'right' and stick.action == 'held':
            self.shutdown()
        else:
            self.draw_graph()

    def shutdown(self):
        """Warns to wait before unplugging & then shuts the Pi down."""
        leds = self.led_settings
        program = self.program_settings
        sense.show_message(program['wait message']['text'],
                           scroll_speed=leds['scroll_speed'],
                           text_colour=program['wait message']['color'],
                           back_colour=leds['off']
                           )
        run(['sudo', 'shutdown', 'now'])

    def refresh(self):
        """Runs through the functions to get thermostat traits, get a
        forecast from OWM, and draw the LED graph."""
        self.get_thermostat()
        self.get_forecast()
        self.draw_graph()


def joystick():
    """While the main thread runs, this event thread checks the SenseHat
    joystick and calls a function based on the input direction."""
    while True:
        sleep(0.25)
        stick = sense.stick.get_events()
        if stick:
            if stick[0].action == 'pressed':
                if stick[0].direction == 'left':
                    WindowSense().toggle_brightness()
                elif stick[0].direction == 'right':
                    WindowSense().turn_off_prompt()
                elif stick[0].direction == 'down':
                    WindowSense().show_setpoints()
                elif stick[0].direction == 'up':
                    WindowSense().show_ambient()
                elif stick[0].direction == 'middle':
                    WindowSense().refresh()


def background():
    """Gets thermostat updates and forecasts periodically to update the
    graph, but reacts when joystick input is received."""
    WindowSense().refresh()
    schedule.every(30).minutes.do(WindowSense().refresh)
    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == '__main__':
    window_sense = WindowSense()
    sense = SenseHat()
    main_thread = threading.Thread(name='background', target=background)
    stick_thread = threading.Thread(name='joystick', target=joystick)
    main_thread.start()
    stick_thread.start()
