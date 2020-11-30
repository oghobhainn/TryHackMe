#!/bin/bash

input=$(<b64.txt)
for i in {1..50}; do
   input=$(<<<"$input" base64 --decode)
done
echo "$input"

#NOTES :
# Backticks are discouraged (``), use $(...) instead
