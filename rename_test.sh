#!/bin/bash

#This renames all the files in a location

for file in *.py; do
	name=$(basename "$file" .py)
	mv "$file" "$name.test"
	echo "$file renamed to "$name.test"
done
