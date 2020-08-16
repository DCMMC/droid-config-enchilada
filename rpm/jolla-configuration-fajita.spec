%define vendor oneplus
%define device fajita

Name: jolla-configuration-%{device}
Summary: Jolla Configuration %{device}
Version: 1.0.0
Release: 0
License: BSD-3-Clause
Source: %{name}-%{version}.tar.gz

Requires: droid-hal-fajita
Requires: droid-hal-fajita-detritus
Requires: droid-hal-fajita-img-boot
Requires: droid-hal-fajita-kernel-modules
Requires: droid-config-fajita-sailfish
Requires: droid-config-fajita-pulseaudio-settings
Requires: droid-config-fajita-policy-settings
Requires: droid-config-fajita-preinit-plugin
Requires: droid-config-fajita-flashing
Requires: droid-config-fajita-bluez5
Requires: droid-hal-version-fajita

# We also depend on the oneplus sdm845 common metapackage
# It contains packages used by the 6 and 6T
Requires: jolla-configuration-oneplus-sdm845

%description
Meta-package to install packages for %{device} HW adaptation configurations
%files
