[app]
title = GameVanila
package.name = gamevanila
package.domain = org.gamevanila
source.dir = .
source.include_exts = py,png,jpg
version = 1.0
requirements = python3,kivy,telethon,PySocks
orientation = portrait
icon.filename = %(source.dir)s/icon.png
fullscreen = 0
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
