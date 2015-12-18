import json
from pprint import pprint

filename='config.json'

config = None

try:
	with open(filename, 'r') as f:
		config = json.load(f)
except:
	print '[ERROR] Couldn\'t load config file: {0}'.format(filename)

def getSSH():
	return config['ssh']
	if config is not None and 'ssh' in config:
		return config['ssh']
