# awesome-appmenu
awesome-appmenu is a tool to create a menu of installed applications for the awesome window manager. It searches for and parses .desktop files to find the name, execution command, and icon of installed applications. These are then grouped into categories, sorted, and written to a lua script ($HOME/.config/awesome/appmenu.lua) that can be used in your awesome WM configuration script. 

To modify the default settings, edit the variables launcherpaths, iconpaths, and categories in $HOME/.config/awesome-appmenu/menurc.py. launcherpaths and iconpaths are searched in the order listed in this file, so list them in order of your preference. Categories will appear in the menu in the order they are listed in the config file. A sample configuration is supplied and installed by default at /usr/share/awesome-appmenu/menurc.py when you run make install.

Features of awesome-appmenu:
* Supports icons
* Fully configurable search paths for launchers and icons
* Fully configurable categories
* Searches recursively for launchers in specified search paths
* Properly ignores .desktop files with NoDisplay=true, and does not write empty categories
* Ungrouped launchers are automatically put into a Miscellaneous category

================================================================================

Intallation:

Type make install or make install DESTDIR=/target/install/directory (the latter to install in a custom directory).

================================================================================

Running:

Just type awesome-appmenu. The file appmenu.lua will be placed in $HOME/.config/awesome. You can also run awesome-appmenu --no-icons or awesome-appmenu -n to not include icons in the menu.

================================================================================

Using the menu:

Put in your rc.lua: 

local appmenu = require("appmenu")

...

mymainmenu = awful.menu({ items = { { "applications", appmenu.Appmenu }, ...

You can also use the menus for categories individually, e.g., by referencing appmenu.Applications, appmenu.Office, etc.

================================================================================

Screenshot of the menu's appearance:

![alt tag](https://raw.githubusercontent.com/montagdude/awesome-appmenu/master/awesome-appmenu.png)
