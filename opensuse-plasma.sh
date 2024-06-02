#!/usr/bin/env bash

echo -n "Update the system? [y/N]: "

read answer

if [[ "$answer" == "y" ]] || [[ "$answer" == "Y" ]]; then
    sudo zypper dup
fi
