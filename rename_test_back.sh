#!/bin/bash

for file in *.test; do
	name=$(basename "$file" .test)
	mv "$file" "$name.py"
	echo "$file renamed to "$name.py"
done
