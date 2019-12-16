#!/bin/bash
python main.py --process decrypt --key_file results/key.txt --input_file results/encrypted.txt --output_file results/decrypted.txt
python main.py --process decrypt --a 1 --b 2 --c 10 --input_file results/encrypted.txt --output_file results/decrypted.txt
python main.py --process decrypt --a 1 --b 2 --input_file results/encrypted.txt --output_file results/decrypted.txt
python main.py --process decrypt --a 100 --b "-20" --c 2 --input_file results/encrypted.txt --output_file results/decrypted.txt
