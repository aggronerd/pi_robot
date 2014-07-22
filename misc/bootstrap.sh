#!/bin/sh

SSH_HOST="$1"

scp misc/init.d/pirobot "pi@$SSH_HOST:~/"
ssh "pi@$SSH_HOST" "sudo cp ~/pirobot /etc/init.d/"
ssh "pi@$SSH_HOST" "sudo chmod 755 /etc/init.d/pirobot"
ssh "pi@$SSH_HOST" "sudo update-rc.d pirobot defaults"



