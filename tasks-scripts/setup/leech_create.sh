#!/bin/bash
# prepare_file_explorer.sh

FLAG=$1
process_name=leech
content="#!/bin/bash
while true; do
    sleep 1
done"
echo -e "$content" > "leech"
chmod +x "leech"


output_script=checkmytask
parent_pid=$BASHPID

# Создание указанного количества процессов с одинаковым именем
for ((i=1; i<=10; i++)); do
    "./$process_name" &  # Создаем пустой процесс с указанным именем
done


script_content="#!/bin/bash\n\nprocess_name=\"$process_name\"\ncount=\$(pgrep \"\$process_name\" | wc -l)\n\nif [ \"\$count\" -gt 0 ]; then\n    echo \"Процессы с именем '\$process_name' найдены. Количество: \$count.\"\nelse\n    echo \"Процессы с именем '\$process_name' отсутствуют. Флаг: $FLAG\"\nfi"
# Запись содержимого в файл
echo -e "$script_content" > "$output_script"

# Установка прав на выполнение для созданного скрипта
chmod +x "$output_script"

mv $output_script "/usr/local/bin/$output_script"
