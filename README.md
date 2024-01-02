# Shared App Menu
##Installation
##Features of Shared App Menu
##Instalation
##Flags and configuration

Shared App Menu is a tool forked from the unmantained  https://github.com/montagdude/awesome-appmenu. 

This application is a python script that extraxt the icons on your ssystem, and creates a sorted categories menu on $HOME/.config/awesome-appmenu/appmenu.lua


To modify the default settings, edit the variables launcherpaths, iconpaths, and categories in $HOME/.config/awesome-appmenu/menurc.py. launcherpaths and iconpaths are searched in the order listed in this file, so list them in order of your preference. Categories will appear in the menu in the order they are listed in the config file. A sample configuration is supplied and installed by default at /usr/share/awesome-appmenu/menurc.py when you run make install.

##Features of Shared App Menu:
* Supports icons
* Fully configurable search paths for launchers and icons
* Fully configurable categories
* Can create a custom Favorites menu
* Searches recursively for launchers in specified search paths
* Properly ignores .desktop files with NoDisplay=true, and does not write empty categories
* Ungrouped launchers are automatically put into a Miscellaneous category


##Intallation:

Clone the package

```
git clone https://github.com/sharedordaz/Shared-AppMenu
```

1.Make the package

```
sudo make install
```

2.Run the initial script

```
awesome-appmenu
```

3.Write the configuration on `~/.config/awesome/rc.lua` or where is your `rc.lua` awesome config file. Write this code at the begginig of the file


```lua
~/.config/awesome/rc.lua
------------------------
--Importing appmenu module
local appmenu = require("appmenu")

```

4. Copy and paste `{ "applications", appmenu.Appmenu }` to this fragment of the code, so it looks like that
```lua
mymainmenu = awful.menu({ items = { { "awesome", myawesomemenu, beautiful.awesome_icon },
                                    { "open terminal", terminal },
                                    { "applications", appmenu.Appmenu}

                                  }
                        })

```
4.OPTIONAL: Write a command to keep updating the apps you install each session. You can write the flags you want.

```
~/.config/awesome/rc.lua
------------------------
--Importing appmenu module

awful.spawn.with_shell("awesome-appmenu")

``` 


##Flags and configuration

|    Flag       |              Action               |
|---------------|-----------------------------------|
| --no-icons    | Do no include icons on the menu   |
| --verbose, -v | Print verbose output for debugging|
| --help, -h    | Show usage information            |


You can also config the menurc.py file to add favorites and other preferences e.g., by referencing appmenu.Applications, appmenu.Office, etc. If you put any .desktop files in the favorites list (favorites = [ ... ] in menurc.py), a favorites menu will also be created, which can be accessed via appmenu.Favorites.

================================================================================

Screenshot of the menu's appearance:

![alt tag](https://raw.githubusercontent.com/montagdude/awesome-appmenu/master/awesome-appmenu.png)
