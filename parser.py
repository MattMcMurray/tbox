import argparse

parser = argparse.ArgumentParser(description='Run a command on the Pi')
subparsers = parser.add_subparsers(help='sub-command help')

parser.add_argument('--deluged', type=str,
                    help='Issue a command to the deluge daemon')
parser_deluged = subparsers.add_parser('deluged', help='deluged help')
parser_deluged.add_argument(
    'restart', type=str, help='restart the deluge daemon')
parser_deluged.add_argument('stop', type=str, help='stop the deluge daemon')
parser_deluged.add_argument('start', type=str, help='start the deluge daemon')

parser.add_argument('--samba', type=str,
                    help='Issue a command to the samba service')
parser_samba = subparsers.add_parser('samba', help='samba help')
parser_samba.add_argument(
    'restart', type=str, help='restart the samba service')
parser_samba.add_argument('stop', type=str, help='stop the samba service')
parser_samba.add_argument('start', type=str, help='start the samba service')

parser.add_argument('--system', type=str,
                    help='Issue a command to the operating system')
parser_system = subparsers.add_parser('system', help='system help')
parser_system.add_argument('halt', type=str, help='stop the system and halt')
parser_system.add_argument('reboot', type=str, help='reboot the pi')

args = parser.parse_args()
