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


####################################################
####################   API   #######################
####################################################
@app.route('/api/start/<service>', methods=['POST'])
def api_start(service):
	status = 500
	data = {
	}

	print service
	if service == 'samba':
		cmd = 'sudo service samba start'
		data['cmd'] = cmd
		data['stdout'] = run_command(cmd)
		status = 200
	elif service == 'deluge':
		cmd = 'deluged'
		data['cmd'] = cmd
		data['stdout'] = run_command(cmd)
		status = 200
	else:
		data['error'] = "No service {0}".format(service)

	js = json.dumps(data)
	resp = Response(js, status=status, mimetype='application/json')

	return resp

@app.route('/api/stop/<service>', methods=['POST'])
def api_stop(service):
	status = 500
	data = {
	}

	print service
	if service == 'samba':
		cmd = 'sudo service samba stop'
		data['cmd'] = cmd
		data['stdout'] = run_command(cmd)
		status = 200
	elif service == 'deluge':
		cmd = 'pkill deluged'
		data['cmd'] = cmd
		data['stdout'] = run_command(cmd)
		status = 200
	else:
		data['error'] = "No service {0}".format(service)

	js = json.dumps(data)
	resp = Response(js, status=status, mimetype='application/json')

	return resp

@app.route('/api/restart/<service>', methods=['POST'])
def api_restart(service):
	print ''

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')