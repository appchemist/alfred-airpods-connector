#!/usr/bin/env zsh

export PATH=/usr/local/lib:/usr/local/bin:/opt/homebrew/bin/:$PATH
address="${address_or_state1}"
state="${address_or_state2}"

if [[ $state -eq 0 ]]; then
    blueutil --connect "$address"
    echo "Connecting to $address"
elif [[ $state -eq 1 ]]; then
    blueutil --disconnect "$address"
    echo "Disconnecting from $address"
else
    echo "Invalid state: $state (must be 0 or 1)"
    exit 1
fi