%define device oneplus-sdm845

Name: jolla-configuration-oneplus-sdm845
Summary: Jolla Configuration OnePlus SDM845 Generic
Version: 1.0.0
Release: 0
License: BSD-3-Clause
Source: %{name}-%{version}.tar.gz

Requires: patterns-sailfish-applications
Requires: patterns-sailfish-ui
# For devices with cellular modem. Those without one, please comment out:
Requires: patterns-sailfish-cellular-apps

Requires: sailfish-content-graphics-z1.5

# For multi-SIM devices
Requires: jolla-settings-networking-multisim

# Introduced starting Sailfish OS 2.0.4.x:
# 3rd party accounts like Twitter, VK, cloud services, etc
Requires: jolla-settings-accounts-extensions-3rd-party-all

# Introduced starting Sailfish OS 2.1.1.26
# Required for Jolla Store Access
Requires: patterns-sailfish-consumer-generic

# For Mozilla location services (online)
Requires: geoclue-provider-mlsdb

# Sailfish OS CSD tool for hardware testing
# needs some configuration to get all features working
Requires: csd

# Devices with 2G or more memory should also include this booster
# to improve camera startup times and the like
Requires: mapplauncherd-booster-silica-qt5-media

# Early stages of porting benefit from these:
# On the basis of sailfish-porter-tools
Requires: jolla-developer-mode
Requires: sailfishsilica-qt5-demos
Requires: busybox-static
Requires: net-tools
Requires: openssh-clients
Requires: openssh-server
Requires: vim-enhanced
Requires: zypper
Requires: jolla-rnd-device
# End sailfish-porter-tools

# FP daemon
Requires: droid-biometry-fp
Requires: sailfish-fpd-community

# No more flingerglue
Requires: audiosystem-passthrough-dummy-af

# Hybris packages
Requires: libhybris-libEGL
Requires: libhybris-libGLESv2
Requires: libhybris-libwayland-egl

# Telephony
Requires: ofono-ril-binder-plugin

# Flashlight
Requires: jolla-settings-system-flashlight

# Sensors
Requires: hybris-libsensorfw-qt5

# Vibra
Requires: ngfd-plugin-native-vibrator
Requires: qt5-feedback-haptics-native-vibrator

# Needed for /dev/touchscreen symlink
Requires: qt5-plugin-generic-evdev

Requires: pulseaudio-modules-droid
# for call audio
Requires: pulseaudio-modules-droid-hidl
# for audio recording to work:
Requires: qt5-qtmultimedia-plugin-mediaservice-gstmediacapture

# These need to be per-device due to differing backends (fbdev, eglfs, hwc, ..?)
Requires: qt5-qtwayland-wayland_egl
Requires: qt5-qpa-hwcomposer-plugin
Requires: qtscenegraph-adaptation

# Add GStreamer v1.0 as standard
Requires: gstreamer1.0
Requires: gstreamer1.0-plugins-good
Requires: gstreamer1.0-plugins-base
Requires: gstreamer1.0-plugins-bad
Requires: nemo-gstreamer1.0-interfaces
# For devices with droidmedia and gst-droid built, see HADK pdf for more information
Requires: gstreamer1.0-droid

# This is needed for notification LEDs
Requires: mce-plugin-libhybris

## USB mode controller
# Enables mode selector upon plugging USB cable:
Requires: usb-moded
Requires: usb-moded-defaults-android
Requires: usb-moded-developer-mode-android
Requires: usb-moded-connection-sharing-android-config

# Extra useful modes not officially supported:
# might need some configuration to get working
#Requires: usb-moded-mass-storage-android-config
# working but careful with roaming!
#Requires: usb-moded-connection-sharing-android-config
# android diag mode only usable for certain android tools
#Requires: usb-moded-diag-mode-android

# hammerhead, grouper, and maguro use this in scripts, so include for all
Requires: rfkill

# enable device lock (and FP)
Requires: sailfish-devicelock-fpd

# For GPS
Requires: geoclue-provider-hybris

# For Bluetooth
Requires: bluebinder

# For FM radio on some QCOM devices
#Requires: qt5-qtmultimedia-plugin-mediaservice-irisradio
#Requires: jolla-mediaplayer-radio

# NFC for devices using Android 8 or newer as base
Requires: nfcd-binder-plugin
Requires: jolla-settings-system-nfc

# OnePlus stuff
Requires: triambienced
Requires: onyx-triambience-settings-plugin
Requires: gestured
Requires: onyx-gesture-settings-plugin
Requires: nemo-qml-plugin-systemsettings



%description
Meta-package to install packages for %{device} HW adaptation configurations
%files
