#!/usr/bin/env python

import os

home = os.environ["HOME"]

""" List of paths to find launchers and icons, given in order of priority. They
    are searched recursively, so there's no need to enter subpaths. """
launcherpaths=["/usr/share/applications", home + "/.local/share/applications"]
iconpaths=["/usr/share/icons/Adwaita", "/usr/share/icons/oxygen", "/usr/share/icons/hicolor"]

""" List of categories """
"""             Name in .desktop file   Display name    Icon    SubcategoryOf"""
categories = [ ["Utility",     "Accessories", "applications-utilities",   ""],
               ["Development", "Development", "applications-development", ""],
               ["Education",   "Education",   "applications-science",     ""],
               ["Game",        "Games",       "applications-games",       ""],
               ["Graphics",    "Graphics",    "applications-graphics",    ""],
               ["Network",     "Internet",    "applications-internet",    ""],
               ["Office",      "Office",      "applications-office",      ""],
               ["AudioVideo",  "MultiMedia",  "applications-multimedia",  ""],
               ["Settings",    "Settings",    "applications-accessories", ""],
               ["System",      "System",      "applications-system",      ""],
               ["Wine",        "Wine",        "wine",                     ""] ]

""" Favorite applications by name of .desktop file. 
    e.g., favorites = ["mozilla-firefox.desktop", "gimp.desktop"], etc. """
favorites = []

""" For launching terminal apps (Terminal=true in launcher). Will be launched
    with 'terminal -e Exec'."""
terminal = "xterm"

""" By default, entries with OnlyShowIn= (! awesome) will not be added. You can
    override this here. """
ignore_OnlyShowIn = False
