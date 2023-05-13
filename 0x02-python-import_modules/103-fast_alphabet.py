#!/usr/bin/python3
import os, string; list(map(lambda x: os.write(1, x.encode('ascii')), [c.upper() for c in string.ascii_lowercase]))
os.write(1, b'\n')
