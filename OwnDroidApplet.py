import sys

import gtk
import pygtk
import gnomeapplet

pygtk.require('2.0')


def applet_factory(applet, iid):   
   label = gtk.Label("Own-Me \/")
   #applet.add(gtk.Window("Test"))
   applet.add(label)
   applet.show_all()
   print('Factory started')
   return True
            
if __name__ == '__main__':   # testing for execution
   print('Starting factory')
   gnomeapplet.bonobo_factory('OAFIID:OwnDroid_Factory', 
                              gnomeapplet.Applet.__gtype__, 
                              'Own Droid Client', '0.1', 
                              applet_factory)
   
