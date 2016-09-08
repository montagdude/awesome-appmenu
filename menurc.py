#!/usr/bin/env python

import os

home = os.environ["HOME"]

""" List of paths to find launchers and icons, given in order of priority. They
    are searched recursively, so there's no need to enter subpaths. """
launcherpaths=["/usr/share/applications", home + "/.local/share/applications"]
iconpaths=["/usr/share/icons/Adwaita", "/usr/share/icons/oxygen", "/usr/share/icons/hicolor"]

""" List of categories """
"""             Name in .desktop file   Display name    Icon """
categories = [ ["Utility",              "Accessories",  "applications-utilities"],
               ["Development",          "Development",  "applications-development"],
               ["Education",            "Education",    "applications-science"],
               ["Game",                 "Games",        "applications-games"],
               ["Graphics",             "Graphics",     "applications-graphics"],
               ["Network",              "Internet",     "applications-internet"],
               ["Office",               "Office",       "applications-office"],
               ["AudioVideo",           "Multimedia",   "applications-multimedia"],
               ["Settings",             "Settings",     "applications-accessories"],
               ["System",               "System",       "applications-system"],
               ["Wine",                 "Wine",         "wine"] ]
