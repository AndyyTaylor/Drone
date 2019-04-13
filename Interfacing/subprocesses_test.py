#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
import subprocess, shlex

args_preplanned = shlex.split("python square_flight.py")
preplanned = subprocess.Popen(args_preplanned, stdout=subprocess.PIPE)

#args_linked = shlex.split("python io_test.py")
#link = subprocess.Popen(args_linked, stdin=subprocess.PIPE, stdout=None)

while True:
    output = preplanned.stdout.readline()
    if output == '' and preplanned.poll() is None:
        break
    #link.stdin.write(output)
    print(output)
    if output == 'l':
        break
#args_transmitter = shlex.split("python manual_flight_velocity.py --connect 127.0.0.1:14550")
#cmd_transmitter = subprocess.Popen(args_transmitter, stdin=subprocess.PIPE, stdout=None)
'''

#!/usr/bin/env python3
#
# Written 2017 by Tobias Brink
#
# To the extent possible under law, the author(s) have dedicated
# all copyright and related and neighboring rights to this software
# to the public domain worldwide. This software is distributed
# without any warranty.
#
# You should have received a copy of the CC0 Public Domain
# Dedication along with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.
#
# Modified by Henry Veng for BlueSat Drone Team

import errno
import os
import pty
import select
import signal
import subprocess
import shlex
import time

# Set signal handler for SIGINT.
signal.signal(signal.SIGINT, lambda s,f: print("received SIGINT") )


class OutStream:
    def __init__(self, fileno):
        self._fileno = fileno
        self._buffer = ""

    def read_lines(self):
        try:
            output = os.read(self._fileno, 1000).decode()
        except OSError as e:
            if e.errno != errno.EIO: raise
            output = ""
        lines = output.split("\n")
        lines[0] = self._buffer + lines[0] # prepend previous
                                           # non-finished line.
        if output:
            self._buffer = lines[-1]
            return lines[:-1], True
        else:
            self._buffer = ""
            if len(lines) == 1 and not lines[0]:
                # We did not have buffer left, so no output at all.
                lines = []
            return lines, False

    def fileno(self):
        return self._fileno

args_linked = shlex.split("python manual_flight_velocity.py --connect 127.0.0.1:14550")
link = subprocess.Popen(args_linked, stdin=subprocess.PIPE, stdout=None, universal_newlines=True)

time.sleep(25)

# Start the subprocess.
out_r, out_w = pty.openpty()
args = shlex.split("python square_flight.py")
proc = subprocess.Popen(args, stdout=out_w)
os.close(out_w)

fds = {OutStream(out_r)}
while fds:
    # Call select(), anticipating interruption by signals.
    while True:
        try:
            rlist, _, _ = select.select(fds, [], [])
            break
        except InterruptedError:
            continue
    # Handle all file descriptors that are ready.
    for f in rlist:
        lines, readable = f.read_lines()
        # Example: Just print every line. Add your real code here.
        for line in lines:
            #print(line)
            link.stdin.write(line + '\n')
            link.stdin.flush()
        if not readable:
            # This OutStream is finished.
            fds.remove(f)