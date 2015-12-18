import argparse

parser = argparse.ArgumentParser(description='Run a command on the Pi')

parser.add_argument('--deluged', type=str,
                    help='Issue a command to the deluge daemon')

parser.add_argument('--samba', type=str,
                    help='Issue a command to the samba service')

parser.add_argument('--system', type=str,
                    help='Issue a command to the operating system')
