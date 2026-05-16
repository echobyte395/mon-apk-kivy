[app]

title = Morpion
package.name = morpion
package.domain = org.raph

version = 1.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 1

android.permissions = INTERNET

# 🔥 FORCÉ STABLE ANDROID 34
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.build_tools = 34.0.0

android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
