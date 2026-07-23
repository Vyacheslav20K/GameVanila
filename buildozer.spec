[app]
title = GameVanila
package.name = gamevanila
package.domain = org.gamevanila
source.dir = .
source.include_exts = py,png,jpg,kv
version = 1.0

# Минимально необходимые пакеты для работы
requirements = python3,kivy,telethon,pysocks,asyncio

orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Настройки SDK / NDK
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
