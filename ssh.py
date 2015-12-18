import paramiko
import base64
import config

ssh_creds = config.getSSH()

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# TODO grab from config file
ssh_client.connect(ssh_creds['host'], username=ssh_creds['username'],
                   password=ssh_creds['password'])
stdin, stdout, stderr = ssh_client.exec_command('ls /media')

for line in stdout:
    print '...' + line.strip('\n')

ssh_client.close()
