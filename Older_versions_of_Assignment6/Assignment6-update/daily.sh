#!/usr/bin/env bash
#python frontend.py <<< 'login' 'agent' 'createacct' '1111111' 'heller' 'no'

#runs the program using inputs in text file
python3 frontend.py < $1
python3 frontend.py < $2
python3 frontend.py < $3

#runs the program to merge the transactionSummaryFile
python3 daily.py

#runs backend
python3 backend.py
