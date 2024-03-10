#!/bin/bash

FLAG=$1

mkdir /home/Matreshka
chmod 777 /home/Matreshka
cd /home/Matreshka

echo $FLAG > answer.txt

# Указываем количество файлов, которые нужно создать
num=99
file_prefix="matreshka"

chmod 755 "answer.txt"
tar -czf "${file_prefix}1.tar.gz" "answer.txt"
rm "answer.txt"

# Устанавливаем начальные права доступа
chmod 755 "${file_prefix}1.tar.gz"

# Цикл for для создания файлов
for ((i=2; i<=num; i++)); do
    tar -czf "${file_prefix}${i}.tar.gz" "${file_prefix}$((i-1)).tar.gz"
    chmod 755 "${file_prefix}${i}.tar.gz"
    rm "${file_prefix}$((i-1)).tar.gz"
done
