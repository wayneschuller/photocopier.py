#!/usr/bin/python
'''photocopier.py  
GUI interface for scanimage for simple copying of scanner documents

Copyright: Wayne Schuller (wayne@schuller.id.au) 2005-2012
Requires: 
	pnmtops (netpbm package in ubuntu)
	scanimage (sane-utils package in ubuntu)

This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import gtk
import os

class Photocopier(gtk.Window):

    def clicked_cb(self, widget, data):
	if self.button.get_active():
		resolution = 500  # 500 dpi is a nice high quality resolution
	else:
		resolution = 100  # 100 dpi a nice quick and nasty resolution 

        scanimage = "scanimage --mode Gray --resolution %i -l 0 -t 0 -x 210mm -y 297mm | pnmtops -width 8.27 -height 11.69 | lpr -# %i" % (resolution, self.spinbutton.get_value_as_int())
	print scanimage
	os.system(scanimage)

    def __init__(self, parent=None):
        # Create the toplevel window
        gtk.Window.__init__(self)
        try:
            self.set_screen(parent.get_screen())
        except AttributeError:
            self.connect('destroy', lambda *w: gtk.main_quit())

        self.set_title(self.__class__.__name__)
        self.set_border_width(5)

        main_vbox = gtk.VBox()
        self.add(main_vbox)

	main_vbox.pack_start(gtk.Label("How Many Copies?"))

	adj = gtk.Adjustment(1.0, 1.0, 50.0, 1.0, 5.0, 0.0)
	self.spinbutton = gtk.SpinButton(adj, 1, 0)
        main_vbox.pack_start(self.spinbutton)

        main_hbox = gtk.HBox()
	self.button = gtk.RadioButton(None, "Fast Speed")
        main_hbox.pack_start(self.button)
	self.button = gtk.RadioButton(self.button, "High Quality")
	self.button.set_active(True)
        main_hbox.pack_start(self.button)
        main_vbox.pack_start(main_hbox)

	execute = gtk.Button(label="Copy!", stock=gtk.STOCK_OK)
	execute.connect("clicked", self.clicked_cb, "")

        main_vbox.pack_end(execute)

        self.show_all()

def main():
    Photocopier()
    gtk.main()

if __name__ == '__main__':
    main()
