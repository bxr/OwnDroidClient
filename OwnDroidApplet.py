#!/usr/bin/env python
import sys

import gtk
import pygtk
import gnomeapplet

pygtk.require('2.0')

def create_menu(applet):
    xml="""<popup name="button3"> <menuitem name="ItemPreferences" 
verb="Preferences" 
label="_Preferences" 
pixtype="stock" 
pixname="gtk-preferences"/>
<separator/>
<menuitem name="ItemAbout" 
verb="About" 
label="_About" 
pixtype="stock" 
pixname="gtk-about"/>
</popup>"""

    verbs = [('About', show_about), ('Preferences', show_preferences)]
    applet.setup_menu(xml, verbs, None)
    

def show_about(*arguments):
    print(arguments)

def show_preferences(*arguments):
    print(arguments)

def applet_factory(applet, iid):
    create_menu(applet)
   
    image = gtk.Image();
    image.set_from_file("/home/florian/work/code/OwnDroidClient/robot.png")
    
    button = gtk.Button();
    button.set_image(image);
    label = gtk.Label("Own-Me \/")
    label.set
    #applet.add(gtk.Window("Test"))
    applet.add(button)
    applet.add(label)
    applet.show_all()
    
    print('Factory started')
    return True
            
            
if __name__ == '__main__':   # testing for execution
    print('Starting factory')
    if len(sys.argv) > 1 and sys.argv[1] == '-d': # debugging
        mainWindow = gtk.Window()
        mainWindow.set_title('OwnDroid Debug-Mode')
        mainWindow.connect('destroy', gtk.main_quit)
        applet = gnomeapplet.Applet()
        applet_factory(applet, None)
        applet.reparent(mainWindow)
        mainWindow.show_all()
        gtk.main()
        sys.exit()
    else:
        gnomeapplet.bonobo_factory('OAFIID:OwnDroid_Factory', 
                              gnomeapplet.Applet.__gtype__, 
                              'Own Droid Client', '0.1', 
                              applet_factory)
   
