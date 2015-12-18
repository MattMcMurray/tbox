import json
import os
from pprint import pprint

filename= os.path.dirname(os.path.realpath(__file__)) + 'config.json'

config = None

try:
	with open(filename, 'r') as f:
		config = json.load(f)
		
except Exception as e:
	print '[ERROR] Couldn\'t load config file: {0}'.format(filename)
	print e

def getSSH():
	return config['ssh']
	if config is not None and 'ssh' in config:
		return config['ssh']
