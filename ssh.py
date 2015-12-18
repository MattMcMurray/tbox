import paramiko
import base64
import config


class SSH:

    def __init__(self):
        self.ssh_creds = config.getSSH()
        self.ssh_client = None

    def open(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # TODO grab from config file
        self.ssh_client.connect(self.ssh_creds['host'], username=self.ssh_creds['username'],
                                password=self.ssh_creds['password'])

    def exec_cmd(self, command):
        stdin, stdout, stderr = self.ssh_client.exec_command(command, timeout=10)

        for line in stdout:
            print '...' + line.strip('\n')

    def close(self):
        self.ssh_client.close()
