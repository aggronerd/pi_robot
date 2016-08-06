#!/bin/bash

PI_ADDRESS=192.168.27.27
PI_USER=pi
LOCATION="$(git rev-parse --show-toplevel)"
rsync --delete -r $LOCATION ${PI_USER}@${PI_ADDRESS}:/home/${PI_USER}