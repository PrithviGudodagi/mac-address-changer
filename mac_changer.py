#!/usr/bin/env python3

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an Interface, use --help for info")
    elif not options.new_mac:
        parser.error("[-] Please specify an MAC Address, use --help for info")
    return options


def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print(f" MAC ADDRESS OF {interface} HAS CHANGED TO {new_mac}")


options = get_arguments()
change_mac(options.interface, options.new_mac)
