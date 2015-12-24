## MAKE SURE TO CHANGE TO PROPER VIRTUALENV
#!/bin/python

from subprocess import check_output
import json
from flask import Flask, render_template, Response

app = Flask(__name__)

def run_command(cmd):
	return check_output([cmd])

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/api/start/<service>', methods=['POST'])
def api_start(service):
	data = {
		'cmd': '',
		'stdout': ''
	}

	print service
	if service == 'samba':
		data['cmd'] = 'ls'
		data['stdout'] = run_command('ls')
	elif service == 'deluge':
		data['stdout'] = data['cmd'] = 'ls'
		run_command('ls')

	js = json.dumps(data)
	resp = Response(js, status=200, mimetype='application/json')

	return resp

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')