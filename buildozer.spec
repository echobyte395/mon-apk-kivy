[app]

# Nom de ton app
title = Morpion

# Identité Android
package.name = morpion
package.domain = org.raph

# Fichiers
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 1.0

# Dépendances Python
requirements = python3,kivy==2.2.1

# Permissions
android.permissions = INTERNET

# Orientation
orientation = portrait

# Plein écran
fullscreen = 1

# =========================
# 🔥 FIX IMPORTANT ANDROID
# =========================

android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# 🔥 BLOQUE LES BUILD-TOOLS (IMPORTANT POUR TON BUG 37)
android.build_tools = 34.0.0

# évite certains crashs inutiles
android.allow_backup = True


[buildozer]

log_level = 2
warn_on_root = 1
