import subprocess
import re
import os
from datetime import datetime

# current date and time
now = datetime.now().replace(microsecond=0)
timestamp = datetime.timestamp(now)

# current fan speed
result = subprocess.run(['hplog', '-f'], stdout=subprocess.PIPE)
fan_speed_regex = re.findall("\([ \d]+\)", result.stdout.decode('utf-8'))

# write to influxdb
os.system("curl -s -XPOST 'http://localhost:8086/write?db=fan_speed' --data-binary 'percent,fan=fan1 value=" + str(int(fan_speed_regex[0].replace("(","").replace(")",""))) + " " + str(int(timestamp)) + "000000000'")
os.system("curl -s -XPOST 'http://localhost:8086/write?db=fan_speed' --data-binary 'percent,fan=fan2 value=" + str(int(fan_speed_regex[1].replace("(","").replace(")",""))) + " " + str(int(timestamp)) + "000000000'")
