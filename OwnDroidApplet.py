#!/usr/bin/env python
import sys

import gtk
import pygtk
import gnomeapplet

pygtk.require('2.0')


XML_PATH = "/home/florian/work/code/OwnDroidClient/gtk_ui.glade"

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
    builder = gtk.Builder()
    builder.add_from_file(XML_PATH)
    builder.connect_signals(handlers)
    window = builder.get_object("ownAboutWindow")
    response = window.run()
    window.destroy()


def show_preferences(*arguments):
    builder = gtk.Builder()
    builder.add_from_file(XML_PATH)
    builder.connect_signals(handlers)
    window = builder.get_object("ownSettings")
    response = window.run()
    window.destroy()
    
def toggle_window(*arguments):
    global main_window
    
    
    if main_window != 0 :
        main_window.destroy()
        main_window=0
    else:
        createUI(XML_PATH)
        
        
    
handlers={"show_about":show_about, "show_preferences":show_preferences }
main_window=0;


def createUI(file_name):
    builder = gtk.Builder()
    builder.add_from_file(file_name)
    builder.connect_signals(handlers)
    window = builder.get_object("owndroidMain")
    global main_window
    main_window = window
    window.show_all()
    

def applet_factory(applet, iid):
    create_menu(applet)
   
    image = gtk.Image()
    image.set_from_file("/home/florian/work/code/OwnDroidClient/android_small.png")
    
    eventBox = gtk.EventBox()
    eventBox.add(image)
   
    #eventBox.set_events(gtk.gdk.BUTTON_PRESS_MASK)
    eventBox.connect("button_press_event", toggle_window)
    applet.add(eventBox)
    
    applet.show_all()
    print('Factory started')
    return True
            
            
if __name__ == '__main__':   # testing for execution
    print('Starting factory')
    if len(sys.argv) > 1 and sys.argv[1] == '-d': # debugging
        #mainWindow = gtk.Window()
        #mainWindow.set_title('OwnDroid Debug-Mode')
        #mainWindow.connect('destroy', gtk.main_quit)
        #applet = gnomeapplet.Applet()
        #applet_factory(applet, None)
        #applet.reparent(mainWindow)
        #mainWindow.show_all()
        
        createUI(XML_PATH)
        
        gtk.main()
        sys.exit()
    else:
        gnomeapplet.bonobo_factory('OAFIID:OwnDroid_Factory', 
                              gnomeapplet.Applet.__gtype__, 
                              'Own Droid Client', '0.1', 
                              applet_factory)
   
