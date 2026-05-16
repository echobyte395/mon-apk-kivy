[app]

# =========================
# 🎮 APP INFO
# =========================
title = Morpion

package.name = morpion
package.domain = org.raph

version = 1.0

# =========================
# 📁 FILES
# =========================
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# =========================
# 🐍 PYTHON / KIVY
# =========================
requirements = python3,kivy==2.2.1

# =========================
# 📱 ANDROID FIX (IMPORTANT)
# =========================
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# ⚠️ IMPORTANT: évite Android 37 auto
android.build_tools = 34.0.0

# =========================
# 🔐 PERMISSIONS
# =========================
android.permissions = INTERNET

# =========================
# 📺 DISPLAY
# =========================
orientation = portrait
fullscreen = 1

# =========================
# ⚙️ STABILITY FIX
# =========================
android.allow_backup = True
log_level = 2
warn_on_root = 1


[buildozer]
