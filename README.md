# Daily wallpaper changer using Bing's Picture of the Day for GNOME 3

## Warning

Warning: This sends HTTP requests to Bing.com

## Installation

```bash
$ make install
```

This will copy the script to your `~/.local/bin` and install systemd unit files to your user config which will run the script every day.

If you prefer to symlink, run `make link && make init` instead; see `Makefile`.

Check that the systemd unit files were installed correctly:

```bash
$ systemctl --user status gnome-wallpaper-of-the-day.service
$ systemctl --user status gnome-wallpaper-of-the-day.timer
```


## License

(c) 2020 Zelly Snyder <zelly@outlook.com>

Apache-2.0
