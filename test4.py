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

def get_left (key):
	t=None
	if key == 'u':
		t=threading.Thread(target=left, args = (0.2, True))
		t.start()
	elif key == 'j':
		t=threading.Thread(target=left, args = (0.2, False))
		t.start()

def get_right (key):
	t=None
	if key == 'i':
		t=threading.Thread(target=right, args = (0.2, True))
		t.start()
	elif key == 'k':
		t=threading.Thread(target=right, args = (0.2, False))
		t.start()
	return t

init ()

key=0

print 'Press "q" to quit'
print 'Press "u,j" for left'
print 'Press "i,k" for right'

while key != 'q':
	key = _getch()

	t1=get_left(key)
	time.sleep(0.05)
	t2=get_right(key)
	time.sleep(0.05)

	print key

	if t1 != None:
		t1.join ()
	if t2 != None:
		t2.join ()

cleanup ()
