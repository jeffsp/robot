#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import threading

def right (t, f):
    if f:
        GPIO.output(7,True)
        time.sleep(t)
        GPIO.output(7,False)
    else:
        GPIO.output(11,True)
        time.sleep(t)
        GPIO.output(11,False)
    time.sleep(0.2)

def center (t, f):
    if f:
        GPIO.output(7,True)
        GPIO.output(13,True)
        time.sleep(t)
        GPIO.output(7,False)
        GPIO.output(13,False)
    else:
        GPIO.output(11,True)
        GPIO.output(15,True)
        time.sleep(t)
        GPIO.output(11,False)
        GPIO.output(15,False)

def left (t, f):
    if f:
        GPIO.output(13,True)
        time.sleep(t)
        GPIO.output(13,False)
    else:
        GPIO.output(15,True)
        time.sleep(t)
        GPIO.output(15,False)
    time.sleep(0.2)

def _getch ():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def init ():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(7,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(15,GPIO.OUT)
    GPIO.setup(16,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)

    GPIO.output(16,True)
    GPIO.output(18,True)

def cleanup ():
    GPIO.output(16,False)
    GPIO.output(18,False)

    GPIO.cleanup()

init ()

key=0

print 'Press "q" to quit'
print 'Press "u,j" for left'
print 'Press "i,k" for center'
print 'Press "o,l" for right'

while key != 'q':
    key = _getch()

    print key

    t1=None
    t2=None
    t3=None

    if key == 'u':
        t1=threading.Thread(target=left, args = (0.2, True))
        t1.start()
    elif key == 'j':
        t1=threading.Thread(target=left, args = (0.2, False))
        t1.start()
    elif key == 'i':
        t2=threading.Thread(target=center, args = (0.2, True))
        t2.start()
    elif key == 'k':
        t2=threading.Thread(target=center, args = (0.2, False))
        t2.start()
    elif key == 'o':
        t3=threading.Thread(target=right, args = (0.2, True))
        t3.start()
    elif key == 'l':
        t3=threading.Thread(target=right, args = (0.2, False))
        t3.start()

    if t1 != None:
        t1.join ()
    if t2 != None:
        t2.join ()
    if t3 != None:
        t3.join ()

cleanup ()
