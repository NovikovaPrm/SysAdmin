#!/usr/bin/python3

import os
path = '/home/kisstep'
def get_size(path)
	total_size = 0
	if os.path.isfile(path):
		total_size = os.path.getsize(path)
	else:
		for dir, subdir, files in os.walk(path):
			
