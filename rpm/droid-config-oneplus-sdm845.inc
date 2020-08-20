%define vendor oneplus
%define vendor_pretty OnePlus

# Community HW adaptations need this
%define community_adaptation 1

# Sailfish OS is considered to-scale, if in app grid you get 4-in-a-row icons
# and 2x2 or 3x3 covers when up-to-4 or 5-or-more apps are open respectively.
# For 4-5.5" device screen sizes of 16:9 ratio, use this formula (hold portrait):
# pixel_ratio = 4.5/DiagonalDisplaySizeInches * HorizontalDisplayResolution/540
# Other screen sizes and ratios will require more trial-and-error.
%define pixel_ratio 1.5

# Device-specific ofono configuration
Provides: ofono-configs
Obsoletes: ofono-configs-mer

# Fix for MTP using sparse usb-moded config
Provides: usb-moded-configs
Obsoletes: usb-moded-defaults