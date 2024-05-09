#!/usr/bin/env bash
# This script backs up the hosts file and restores it

# Check if the script is run as root
if [ "$EUID" -ne 0 ]; then
	echo "Please run as root"
	exit 1
fi

# Checks if hosts.back exists
if [ ! -f /etc/hosts.bak ]; then
	echo "Backup file does not exist"
	exit 1
fi

# Backup the hosts file from /etc/hosts.bak to /etc/hosts
cp /etc/hosts.bak /etc/hosts && rm /etc/hosts.bak
