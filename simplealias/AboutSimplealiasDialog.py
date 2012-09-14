# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('simplealias')

import logging
logger = logging.getLogger('simplealias')

from simplealias_lib.AboutDialog import AboutDialog

# See simplealias_lib.AboutDialog.py for more details about how this class works.
class AboutSimplealiasDialog(AboutDialog):
    __gtype_name__ = "AboutSimplealiasDialog"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the about dialog"""
        super(AboutSimplealiasDialog, self).finish_initializing(builder)

        # Code for other initialization actions should be added here.

