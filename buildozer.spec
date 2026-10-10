[app]

title = MAX AI
package.name = maxai
package.domain = org.maxassistant

source.dir = .
source.include_exts = py,json,kv,png,jpg,atlas,txt,json
source.exclude_dirs = .git,.github,bin,.buildozer

version = 1.0.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,CAMERA,RECORD_AUDIO

android.api = 35
android.minapi = 24
android.archs = arm64-v8a

android.accept_sdk_license = True

# Use a stable python-for-android release instead of master
p4a.branch = v2024.01.21

[buildozer]

log_level = 2
warn_on_root = 1
