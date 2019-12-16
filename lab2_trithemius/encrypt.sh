#!/bin/bash
python main.py --process encrypt --key_file results/key.txt --input_file results/input.txt --output_file results/encrypted.txt
python main.py --process encrypt --a 1 --b 2 --c 10 --input_file results/input.txt --output_file results/encrypted.txt
python main.py --process encrypt --a 1 --b 2 --input_file results/input.txt --output_file results/encrypted.txt
python main.py --process encrypt --a 100 --b "-20" --c 2 --input_file results/input.txt --output_file results/encrypted.txt
