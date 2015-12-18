import time
import socket

from parser import parser

import ssh

help = set(['help', 'h', 'he', 'hel', '-h', '-help', '--help'])
args = parser.parse_args()


def get_ssh_conn():
    ssh_manager = ssh.SSH()
    ssh_manager.open()
    return ssh_manager

if __name__ == '__main__':
    try:
        ssh_conn = get_ssh_conn()

        if args.deluged is not None:
            if args.deluged in help:
                print 'Run a command on the deluge daemon\n'
                print 'arguments:'
                print '\t start   -- start the deluge daemon'
                print '\t stop    -- stop the deluge daemon'
                print '\t restart -- restart the deluge daemon\n'

            elif args.deluged == 'start':
                ssh_conn.exec_cmd('deluged')
                print('Checking if deluged is running...')
                ssh_conn.exec_cmd('ps -e | grep deluge')
                ssh_conn.close()

            elif args.deluged == 'stop':
                ssh_conn.exec_cmd('sudo pkill deluged')
                print('Checking if deluged is still running...')
                time.sleep(0.5)
                ssh_conn.exec_cmd('ps -e | grep deluge')
                ssh_conn.close()

            elif args.deluged == 'restart':
                ssh_conn.exec_cmd('sudo pkill deluged')
                ssh_conn.exec_cmd('deluged')
                print('Checking if deluged is running...')
                ssh_conn.exec_cmd('ps -e | grep deluge')
                ssh_conn.close()

        elif args.samba is not None:
            if args.samba in help:
                print 'Run a command on the samba service\n'
                print 'arguments:'
                print '\t start   -- start the samba service'
                print '\t stop    -- stop the samba service'
                print '\t restart -- restart the samba service\n'

            elif args.samba == 'start':
            	ssh_conn.exec_cmd('sudo service samba start')
            	ssh_conn.close()

            elif args.samba == 'stop':
            	ssh_conn.exec_cmd('sudo service samba stop')
            	ssh_conn.close()

            elif args.samba == 'restart':
            	ssh_conn.exec_cmd('sudo service samba restart')
            	ssh_conn.close()


        elif args.system is not None:
            if args.system in help:
                print 'Run a command on the system\n'
                print 'arguments:'
                print '\t shutdown -- halt and shutdown the pi'
                print '\t reboot   -- reboot the system\n'

            elif args.samba == 'shutdown':
            	ssh_conn.exec_cmd('sudo shutdown -h now')
            	ssh_conn.close()

            elif args.samba == 'restart':
            	ssh_conn.exec_cmd('sudo reboot')
            	ssh_conn.close()

    except socket.timeout:
        print 'Socket timed out; try again'
