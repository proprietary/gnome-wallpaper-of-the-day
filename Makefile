XDG_DATA_HOME ?= ${HOME}/.config
makefile_path := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

install: copy init

init:
	systemctl --user start gnome-wallpaper-of-the-day{.service,.timer}
	systemctl --user enable gnome-wallpaper-of-the-day{.service,.timer}

copy:
	cp -ar $(makefile_path)gnome-wallpaper-of-the-day.py ${HOME}/.local/bin/
	mkdir -p $(XDG_DATA_HOME)/systemd/user
	cp -ar $(makefile_path)/gnome-wallpaper-of-the-day{.service,.timer} \
		$(XDG_DATA_HOME)/systemd/user/

# If you do this, don't move this directory
link:
	ln -sf $(makefile_path)gnome-wallpaper-of-the-day.py ${HOME}/.local/bin/
	mkdir -p $(XDG_DATA_HOME)/systemd/user
	ln -sf $(makefile_path)/gnome-wallpaper-of-the-day{.service,.timer} \
		$(XDG_DATA_HOME)/systemd/user/
