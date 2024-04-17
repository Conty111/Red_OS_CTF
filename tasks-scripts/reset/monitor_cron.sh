#!/bin/bash

output_script=checkmytask
rm -f "/usr/local/bin/$output_script"
# Удаляем задачу из crontab
(crontab -l -u | grep -v "*/5 * * * * *  >> /home/memory_state" ) | crontab -
