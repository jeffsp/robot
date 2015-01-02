#!/usr/bin/python

import RPi.GPIO as GPIO
import time

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

def both (t, f):
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
	time.sleep(0.2)

def init():
	GPIO.setmode(GPIO.BOARD)

	GPIO.setup(7,GPIO.OUT)
	GPIO.setup(11,GPIO.OUT)
	GPIO.setup(13,GPIO.OUT)
	GPIO.setup(15,GPIO.OUT)
	GPIO.setup(16,GPIO.OUT)
	GPIO.setup(18,GPIO.OUT)

	GPIO.output(16,True)
	GPIO.output(18,True)

def cleanup():
	GPIO.output(16,False)
	GPIO.output(18,False)

	GPIO.cleanup()

init ()

both (0.5, True)
both (0.5, False)
left (0.1, True)
left (0.1, False)
left (0.1, False)
both (0.5, True)
both (0.5, False)
right (0.1, True)
both (0.5, True)
both (0.5, False)
right (0.1, True)
right (0.1, True)
right (0.1, True)
both (0.5, True)
both (0.5, False)
right (0.1, False)
right (0.1, False)
right (0.1, False)
both (0.5, True)
both (0.5, False)

cleanup ()
