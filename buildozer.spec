[app]
title = GameVanila
package.name = gamevanila
package.domain = org.gamevanila
source.dir = .
source.include_exts = py,png,jpg
version = 1.0
requirements = python3,kivy,telethon,PySocks
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# ВАЖНО: Фиксируем стабильные версии SDK и Build-Tools
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
