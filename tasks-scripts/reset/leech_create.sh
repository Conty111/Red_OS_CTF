#!/bin/bash

# Параметр - имя созданного скрипта
script_name="checkmytask"

# Удаление созданного скрипта
rm "/usr/local/bin/$script_name"
rm "leech"

# Остановка процессов с указанным именем
pkill -f "leech"

