import plotly.plotly as py
import json
import time
import datetime

from sense_hat import SenseHat
sense = SenseHat()

with open('./config.json') as config_file:
    plotly_user_config = json.load(config_file)

    py.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])

    url=py.plot([
        {
            'x': [], 'y': [], 'type': 'scatter',
            'stream': {
                'token': plotly_user_config['plotly_streaming_tokens'][0],
                'maxpoints': 200
                }
            }], filename='Raspberry Pi Streaming Example Values')
    print "view your streaming graph here: ", url

stream = py.Stream(plotly_user_config['plotly_streaming_tokens'][0])
stream.open()

while True:
    temp=sense.get_temperature()

    stream.write({'x': datetime.datetime.now(), 'y': temp})

    time.sleep(0.25)
