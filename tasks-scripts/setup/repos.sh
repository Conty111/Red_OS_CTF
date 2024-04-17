#!/bin/bash

FLAG=$1

output_script=checkmytask
script_content="#!/bin/bash
# Выполняем команду yum update -y
if yum update -y &> /dev/null; then
    echo "$FLAG"
else
    echo "Ошибка: Команда yum update -y завершилась с ошибкой."
fi"
echo -e "$script_content" > "$output_script"

# Установка прав на выполнение для созданного скрипта
chmod +x "$output_script"
mv $output_script "/usr/local/bin/$output_script"

repo_file="/etc/yum.repos.d/custom.repo"
echo -e "[custom]\nname=Custom Repository\nbaseurl=http://example.com/repo\nenabled=1\ngpgcheck=0" > $repo_file
    