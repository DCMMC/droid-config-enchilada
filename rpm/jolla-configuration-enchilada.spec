%define vendor oneplus
%define device enchilada

Name: jolla-configuration-%{device}
Summary: Jolla Configuration %{device}
Version: 1.0.0
Release: 0
License: BSD-3-Clause
Source: %{name}-%{version}.tar.gz

Requires: droid-hal-enchilada
Requires: droid-hal-enchilada-detritus
Requires: droid-hal-enchilada-img-boot
Requires: droid-hal-enchilada-kernel-modules
Requires: droid-config-enchilada-sailfish
Requires: droid-config-enchilada-pulseaudio-settings
Requires: droid-config-enchilada-policy-settings
Requires: droid-config-enchilada-preinit-plugin
Requires: droid-config-enchilada-flashing
Requires: droid-config-enchilada-bluez5
Requires: droid-hal-version-enchilada

# We also depend on the oneplus sdm845 common metapackage
# It contains packages used by the 6 and 6T
Requires: jolla-configuration-oneplus-sdm845

%description
Meta-package to install packages for %{device} HW adaptation configurations
%files
