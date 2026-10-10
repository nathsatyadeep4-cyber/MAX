[app]

title = MAX AI
package.name = maxai
package.domain = org.maxassistant

source.dir = .
source.include_exts = py,json,kv,png,jpg,atlas
source.exclude_dirs = .git,.github,bin,.buildozer

version = 1.0.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,CAMERA

android.api = 35
android.minapi = 24
android.archs = arm64-v8a

android.accept_sdk_license = True

p4a.branch = master

[buildozer]

log_level = 2
warn_on_root = 1
