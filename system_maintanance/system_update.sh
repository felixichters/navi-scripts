#!/bin/sh

echo $'\n\e[34m'"Create a list of all explicitly installed packages..."$'\e[0m\n'
pacman -Qqe > ~/.config/pkglist.txt
echo $'\e[32m'"Created a list of all explicitly installed packages."$'\e[0m'

echo $'\n\e[34m'"Check if any systemd services have failed..."$'\e[0m\n'
systemctl --failed
echo $'\n\e[32m'"Checked if any systemd services have failed."$'\e[0m'

echo $'\n\e[34m'"Look for errors in the log files..."$'\e[0m\n'
journalctl -p 3 -b
echo $'\n\e[32m'"Lokked for errors in the log files."$'\e[0m'

echo $'\n\e[34m'"Update packages..."$'\e[0m\n'
yay -Syu
echo $'\n\e[32m'"System updated."$'\e[0m'

echo $'\n\e[32m'"DONE"$'\e[0m\n'
exit 
exit 0
