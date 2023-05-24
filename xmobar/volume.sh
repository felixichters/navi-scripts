#!/bin/sh

master_volume=`amixer get Master | sed s/%.*$// | sed 's/^.*\[//' | tail -n 1`
echo "$master_volume%"
exit 0
