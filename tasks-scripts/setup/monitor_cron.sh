#!/bin/bash

FLAG="FLAG=$1"

output_script=checkmytask
check_script="$(dirname "$0")/monitor_check.sh"

cp $check_script "/usr/local/bin/$output_script"
chmod 777 "/usr/local/bin/$output_script"
sed -i "3s;^;$FLAG\n;" "/usr/local/bin/$output_script"
