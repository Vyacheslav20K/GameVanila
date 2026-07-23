[app]
title = GameVanila
package.name = gamevanila
package.domain = org.gamevanila
source.dir = .
source.include_exts = py,png,jpg,kv
version = 1.0

requirements = python3,kivy,telethon,pysocks,openssl,requests,urllib3,idna,certifi

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Гарантированно рабочая связка Android SDK / NDK:
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
