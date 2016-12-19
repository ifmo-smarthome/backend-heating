#!/usr/bin/python
import os, sys

fd = os.open("/dev/rfcomm1", os.O_RDWR);
cmd = sys.stdin.readlines()[0]
os.write(fd, cmd.encode())

s = "";
while True:
    a = os.read(fd, 1)[0];
    if a == ord('\n'):
        print(s);
        sys.exit(0);
    s = s + chr(a);
