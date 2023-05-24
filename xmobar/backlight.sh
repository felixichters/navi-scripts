#!/bin/sh

backlight=`xbacklight -get`
backlight=${backlight%.*}
echo "$backlight%"
exit 0 
