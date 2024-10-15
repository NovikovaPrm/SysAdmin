#!/bin/bash

du --max-depth=1 -a -h $HOME | sort -rh

echo "Hello, $USER"
