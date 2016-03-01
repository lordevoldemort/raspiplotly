import plotly.plotly as py
import json
import time
import datetime
import os
import re


while True:
    result=os.popen('vcgencmd measure_temp').readline()
    temp=re.findall('\d\d.\d', result)
    print temp[0]
    time.sleep(0.25)
    
