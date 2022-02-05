%package -n patterns-sailfish-device-adaptation-enchilada
Summary: Jolla HW Adaptation enchilada
Requires: droid-hal-enchilada
Requires: droid-hal-enchilada-img-boot
Requires: droid-hal-enchilada-kernel-modules
Requires: droid-config-enchilada-sailfish
Requires: droid-config-enchilada-pulseaudio-settings
Requires: droid-config-enchilada-policy-settings
Requires: droid-config-enchilada-preinit-plugin
Requires: droid-config-enchilada-flashing
Requires: droid-config-enchilada-bluez5
Requires: droid-hal-version-enchilada

# Hybris packages
Requires: libhybris-libEGL
Requires: libhybris-libGLESv2
Requires: libhybris-libwayland-egl

# Enchilada extras!
# Requires: triambienced
# Requires: onyx-triambience-settings-plugin
# Requires: gestured
# Requires: onyx-gesture-settings-plugin
# Requires: nemo-qml-plugin-systemsettings

# Sensors
Requires: hybris-libsensorfw-qt5

# FP
Requires: droid-biometry-fp
Requires: droid-fake-crypt
Requires: sailfish-fpd-community

# Vibra
Requires: ngfd-plugin-native-vibrator
Requires: libngf-qt5-qtfeedback

# Needed for /dev/touchscreen symlink
Requires: qt5-plugin-generic-evdev

Requires: pulseaudio-modules-droid
Requires: pulseaudio-modules-droid-hidl

# The -dummy-af is needed for newer devices that run the main
# audiosystem-passthrough in qti mode (e.g. >=Android 9 Qualcomm),
# to fix non-responding Camera app and/or voice during a phone call:
#Requires: audiosystem-passthrough-dummy-af

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
Requires: gstreamer1.0-libav

# This is needed for notification LEDs
Requires: mce-plugin-libhybris

# Flashlight
Requires: jolla-settings-system-flashlight

# USB mode controller
Requires: usb-moded

# hammerhead, grouper, and maguro use this in scripts, so include for all
Requires: rfkill

# enable device lock and allow to select untrusted software
Requires: jolla-devicelock-daemon-encsfa

# Enable home encryption
#Requires: sailfish-device-encryption

# For GPS
Requires: geoclue-provider-hybris

# For FM radio on some QCOM devices
Requires: qt5-qtmultimedia-plugin-mediaservice-irisradio
Requires: jolla-mediaplayer-radio

# NFC for devices using Android 8 or newer as base
Requires: nfcd-binder-plugin
Requires: jolla-settings-system-nfc

# Telephony
Requires: ofono-ril-binder-plugin

# Required for mobile data
Requires: dummy_netd

# Bluetooth
Requires: bluebinder

# Camera resolutions
Requires: camera-settings-plugin

# Browser video acceleration
Requires: gmp-droid

%description -n patterns-sailfish-device-adaptation-enchilada
Pattern with packages for enchilada HW Adaptation

%files -n patterns-sailfish-device-adaptation-enchilada
