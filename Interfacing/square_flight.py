#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys

for i in range(10):
    sys.stdout.write("1,0,0\n")
    time.sleep(1)

for i in range(10):
    sys.stdout.write("0,1,0\n")
    time.sleep(1)

for i in range(10):
    sys.stdout.write("-1,0,0\n")
    time.sleep(1)

for i in range(10):
    sys.stdout.write("0,-1,0\n")
    time.sleep(1)

print("l")