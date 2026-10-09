[app]
title = MAX AI
package.name = maxai
package.domain = org.maxassistant

source.dir = .
source.include_exts = py,json,kv,png,jpg,txt,md

version = 1.0.0

requirements = python3,kivy,pyjnius

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,CAMERA,RECORD_AUDIO

android.api = 35
android.minapi = 23
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
