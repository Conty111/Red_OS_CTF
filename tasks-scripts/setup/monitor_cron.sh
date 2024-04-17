#!/bin/bash

FLAG=$1

output_script=checkmytask
script_content="#!/bin/bash

users=$(cut -d: -f1 /etc/passwd)

# Флаг, указывающий, был ли найден пользователь с нужной задачей
found=false

# Проверяем каждого пользователя
for user in \$users; do
    # Проверяем, есть ли у пользователя задачи в crontab
    if ! crontab -u "\$user" -l &>/dev/null; then
        continue
    fi

    # Проверяем, есть ли у пользователя в crontab задача, которая выполняется каждые 5 минут и что-то записывает в /home/memory_state
    if crontab -u "\$user" -l | grep -q "*/5 * * * *  >> /home/memory_state"; then
        found=true
        break
    fi
done

# Если пользователь не был найден
if ! \$found; then
    echo "Нет задач в crontab для записи информации в /home/memory_state каждые 5 минут"
    exit 0
fi
echo $FLAG"

echo -e "$script_content" > "$output_script"
# Установка прав на выполнение для созданного скрипта
chmod +x "$output_script"
mv $output_script "/usr/local/bin/$output_script"

