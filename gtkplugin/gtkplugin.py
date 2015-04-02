#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Rafael Carlos Cordano Ottati <rafael.cordano@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import os
import sys

from gettext import gettext as _

from plugins.plugin import Plugin
from TurtleArt.tapalette import make_palette
from TurtleArt.tatype import TYPE_STRING
from TurtleArt.taprimitive import Primitive, ArgSlot, ConstantArg
import logging
LOGGER = logging.getLogger('turtleart-activity x11 events plugin')

sys.path.append(os.path.abspath('./plugins/gtkplugin'))


import gtk


class Gtkplugin(Plugin):
    def __init__(self, parent):
        Plugin.__init__(self)
        self._parent = parent
        self.running_sugar = self._parent.running_sugar
        self._status = True
        self.pause = 0
        self.widgets = {}

    def setPause(self, arg):
        self.pause = arg

    def getPause(self):
        print 1
        return self.pause
        
    def setup(self):
        palette1 = make_palette('gtk-basic-widgets', ["#00FF00","#008000"], _('Gtk plugin'), translation=_('Gtk plugin'))
        palette2 = make_palette('gtk-basic-methods', ["#00FF00","#008000"], _('Gtk plugin2'), translation=_('Gtk plugin2'))
        
        palette1.add_block('MakeWindow',
                    style='basic-style-1arg',
                    label=_('Window'),
                    default=["name"],
                    prim_name='makeWindow',
                    help_string= _('Makes a window with a name'))
                    
        self._parent.lc.def_prim(
            'makeWindow', 1,
            Primitive(self.make_window, arg_descs=[ArgSlot(TYPE_STRING)]))
        
        palette1.add_block('MakeButton',
                    style='basic-style-2arg',
                    label=_('Button'),
                    default=["name", "label"],
                    prim_name='makeButton',
                    help_string= _('Makes a button'))
                    
        self._parent.lc.def_prim(
            'makeButton', 2,
            Primitive(self.make_button, arg_descs=[ArgSlot(TYPE_STRING), ArgSlot(TYPE_STRING)]))
            
        palette1.add_block('MakeVBox',
                    style='basic-style-1arg',
                    label=_('VBox'),
                    default=["name"],
                    prim_name='makeVBox',
                    help_string= _('Makes a vbox'))
                    
        self._parent.lc.def_prim(
            'makeVBox', 1,
            Primitive(self.make_vbox, arg_descs=[ArgSlot(TYPE_STRING)]))
            
        palette1.add_block('MakeHBox',
                    style='basic-style-1arg',
                    label=_('HBox'),
                    default=["name"],
                    prim_name='makeHBox',
                    help_string= _('Makes a hbox'))
                    
        self._parent.lc.def_prim(
            'makeHBox', 1,
            Primitive(self.make_hbox, arg_descs=[ArgSlot(TYPE_STRING)]))
            
        palette2.add_block('hideWidget',
                    style='basic-style-1arg',
                    label=_('Hide Widgets'),
                    default=["name"],
                    prim_name='hideWidget',
                    help_string= _('Hides any gtk widget'))
                    
        self._parent.lc.def_prim(
            'hideWidget', 1,
            Primitive(self.hide_widget, arg_descs=[ArgSlot(TYPE_STRING)]))
            
        palette2.add_block('addWidget',
                    style='basic-style-2arg',
                    label=[_('Add Widgets'), _('dest'), _('src')],
                    default=["dest", "src"],
                    prim_name='addWidget',
                    help_string= _('Adds any gtk widget'))
                    
        #palette2.add_block('connect',
         #           style='basic-style-3arg',
          #          label=[_('Connect'), _('dest'), _('on'), _('to')],
           #         default=["dest", "clicked", "func"],
            #        prim_name='connectWidget',
             #       help_string= _('Connect'))
             
                    
        palette2.add_block('gtkMain',
                    style='basic-style',
                    label=_('Gtk Main'),
                    prim_name='gtkMain',
                    help_string= _('Runs gtk main loop'))
                    
        self._parent.lc.def_prim(
            'addWidget', 2,
            Primitive(self.add_widget, arg_descs=[ArgSlot(TYPE_STRING),
                                                  ArgSlot(TYPE_STRING)]))
            
        self._parent.lc.def_prim(
            'gtkMain', 0,
            Primitive(lambda x : gtk.main()))
            
        #self._parent.lc.def_prim(
         #   'connectWidget', 3,
          #  Primitive(self.add_widget, arg_descs=[ArgSlot(TYPE_STRING),
           #                                       ArgSlot(TYPE_STRING)]))
        
                                                     
    def make_window(self, name):
        print name
        self.widgets[name] = gtk.Window()
        self.widgets[name].show()
    
    def make_button(self, name, label):
        print name
        self.widgets[name] = gtk.Button(label)
        self.widgets[name].show()
        
    def make_vbox(self, name):
        self.widgets[name] = gtk.VBox()
        self.widgets[name].show()
        
    def make_hbox(self, name):
        self.widgets[name] = gtk.HBox()
        self.widgets[name].show()
        
    def hide_widget(self, name):
        print name
        self.widgets[name].hide()
        
    def add_widget(self, dest, src):
        self.widgets[dest].add(self.widgets[src])
        self.widgets[src].show_all()
