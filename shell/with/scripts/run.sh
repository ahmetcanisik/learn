#!/bin/bash

# add to your bash file.
runs() {
	chmod +x $1
	./$1
}

runs $file
