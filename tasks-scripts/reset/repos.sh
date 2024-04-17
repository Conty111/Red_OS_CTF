#!/bin/bash

repo_file="/etc/yum.repos.d/custom.repo"
output_script=checkmytask
rm -f $repo_file
rm -f "/usr/local/bin/$output_script"