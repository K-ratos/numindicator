#!/usr/bin/env python
import subprocess
from gi.repository import Gtk
from pynput.keyboard import Key
from pynput.keyboard import Listener
import time
from threading import Thread
import glib

stri = subprocess.getoutput('xset q | grep LED')[65]
x = "Hello World"
val = int(stri)
if( val >= 2 ):
	x = "numlockon"
else:
	x = "numlockoff"
builder = Gtk.Builder()
builder.add_from_file("num.glade")
label = builder.get_object("label1")

def on_press(key):
	k = '{0}'.format(key)
	sti = subprocess.getoutput('xset q | grep LED')
	st = sti[65]
	global val
	val = int(st)
	if(k == 'Key.num_lock' ):
		time.sleep(.1)
		sti = subprocess.getoutput('xset q | grep LED')
		st = sti[65]
		global val
		val = int(st)
		if( val >= 2 ):
			x = "numlockon"
			label.set_text(x)
		else:
			x = "numlockoff"
			label.set_text(x)
label.set_text(x)
window = builder.get_object("window1")
window.connect("delete-event", Gtk.main_quit)
window.show_all()
def myfunc():
	with Listener(on_press=on_press) as listener:
	    listener.join()

if __name__ == "__main__":
	thread = Thread(target = myfunc)
	thread.start()
	Gtk.main()
	thread.join()




