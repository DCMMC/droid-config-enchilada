#!/bin/bash

sleep 1
cat << EOF > /persist/wlan_mac.bin
Intf0MacAddress=583653F9A264
Intf1MacAddress=00AA00BB00C2
Intf2MacAddress=00AA00BB00C3
Intf3MacAddress=00AA00BB00C4
EOF