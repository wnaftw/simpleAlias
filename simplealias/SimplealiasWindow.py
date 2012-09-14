# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('simplealias')

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('simplealias')

from simplealias_lib import Window
from simplealias.AboutSimplealiasDialog import AboutSimplealiasDialog
from simplealias.PreferencesSimplealiasDialog import PreferencesSimplealiasDialog

# See simplealias_lib.Window.py for more details about how this class works
class SimplealiasWindow(Window):
    __gtype_name__ = "SimplealiasWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(SimplealiasWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutSimplealiasDialog
        self.PreferencesDialog = PreferencesSimplealiasDialog

        # Code for other initialization actions should be added here.

