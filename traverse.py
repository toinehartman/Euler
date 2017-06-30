#!/usr/bin/env python3

import os, hashlib, sys

hashes = {}

if len(sys.argv) > 1:
	root_dir = sys.argv[1]
else:
	root_dir = os.path.curdir

for root, dirs, files in os.walk(root_dir, topdown = True):
	# print("Checking root", root)

	dirs[:] = [d for d in dirs if not d.startswith('.')]
	files[:] = [f for f in files if not f.startswith('.')]

	for filename in files:
		file = os.path.join(root, filename)

		with open(file) as f:
			try:
				data = f.read().encode('utf-8').strip()
			except(UnicodeDecodeError):
				continue

			h = hashlib.md5(data).hexdigest()

			if h in hashes:
				print("file", file, "is not unique")
				print("duplicate", hashes[h], "exists!")
			else:
				hashes[h] = file

# print(hashes)
