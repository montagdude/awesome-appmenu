PREFIX=/usr
TARGET=awesome-appmenu

all:
	@echo Run \'make install\' to install awesome-appmenu

install:
	@echo "INSTALLING AWESOME-APPMENU"
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@mkdir -p $(DESTDIR)$(PREFIX)/share/awesome-appmenu
	@echo "DIRECTORIES CREATED, INSTALLING PACKAGES..."
	@cp -p $(TARGET) $(DESTDIR)$(PREFIX)/bin/$(TARGET)
	@cp -p menurc.py $(DESTDIR)$(PREFIX)/share/awesome-appmenu/menurc.py
	
uninstall:
	@echo "UNINSTALLING AWESOME-APPMENU"
	@rm -rf $(DESTDIR)$(PREFIX)/bin/$(TARGET)
	@rm -rf $(DESTDIR)$(PREFIX)/share/awesome-appmenu/menurc.py


