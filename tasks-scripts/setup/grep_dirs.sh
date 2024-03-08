#!/bin/bash

FLAG=$1

mkdir /home/Cave
cd /home/Cave

# Указываем количество файлов, которые нужно создать
num_files=99
file_prefix="bag_"

# Цикл for для создания файлов
for ((i=1; i<=num_files; i++)); do
    mkdir "${file_prefix}${i}"
    touch "${file_prefix}${i}/maybe_answer.txt"
done

echo $FLAG >> "${file_prefix}24/answer.txt"
