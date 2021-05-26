import subprocess
from influxdb import InfluxDBClient
client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('heizung')

prvl = float(subprocess.check_output("cat /sys/bus/w1/devices/28-000000018c1b/temperature", shell=True).decode("utf-8"))/1000
sevl = float(subprocess.check_output("cat /sys/bus/w1/devices/28-00000001b7d7/temperature", shell=True).decode("utf-8"))/1000
prrl = float(subprocess.check_output("cat /sys/bus/w1/devices/28-00000001d4b8/temperature", shell=True).decode("utf-8"))/1000

json_body = [
	{
		"measurement": "heizung",
		"fields": {
			"primaer_vorlauf": prvl,
			"sekundaer_vorlauf": sevl,
			"primaer_ruecklauf": prrl
		}
	},
]

client.write_points(json_body)
