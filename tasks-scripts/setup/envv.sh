#!/bin/bash

FLAG=$1
# Параметры - имя переменной окружения и имя выходного файла
env_variable_name="YOUR_NEW_PET_NAME"
output_script_name="checkmytask"

# Генерация содержимого скрипта
script_content="#!/bin/bash\n\n# Проверка наличия переменной окружения\nif [ -z \"\$$env_variable_name\" ]; then\n    echo \"Ошибка: Переменная окружения '$env_variable_name' отсутствует.\"\nelse\n    echo \"Флаг: $FLAG\"\nfi"

# Запись содержимого в файл
echo -e "$script_content" > "$output_script_name"

# Установка прав на выполнение для созданного скрипта
chmod +x "$output_script_name"

# Перемещение скрипта в /usr/local/bin
sudo mv "$output_script_name" /usr/local/bin/

