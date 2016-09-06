PREFIX=/usr
TARGET=awesome-appmenu

install:
	install -d -m 0755 $(DESTDIR)$(PREFIX)/bin
	install -d -m 0755 $(DESTDIR)$(PREFIX)/share/awesome-appmenu
	install -m 0755 $(TARGET) $(DESTDIR)$(PREFIX)/bin/$(TARGET)
	install -m 0644 menurc.py $(DESTDIR)$(PREFIX)/share/awesome-appmenu/menurc.py

uninstall:
	rm $(DESTDIR)$(PREFIX)/bin/$(TARGET)
	rm $(DESTDIR)$(PREFIX)/share/awesome-appmenu/menurc.py
