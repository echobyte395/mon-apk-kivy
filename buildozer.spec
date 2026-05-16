[app]

# Nom de l'app
title = Morpion

# Identité Android
package.name = morpion
package.domain = org.raph

# Fichiers source
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 1.0

# Dépendances Python
requirements = python3,kivy

# Permissions
android.permissions = INTERNET

# Orientation
orientation = portrait

# Plein écran
fullscreen = 1

# 🔥 IMPORTANT FIX (anti bug GitHub Actions)
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# 🔥 FIX BUILD TOOLS (évite ton erreur 37)
android.build_tools = 34.0.0

# évite certains crashs buildozer
android.allow_backup = True


[buildozer]

log_level = 2
warn_on_root = 1
