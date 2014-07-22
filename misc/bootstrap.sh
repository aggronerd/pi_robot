#!/bin/sh

BRANCH=development
VERSION_LOCATION="https://uk.co.gregorydoran.pi.robot.s3-website-eu-west-1.amazonaws.com/pi_robot_$BRANCH.tar.gz"
INSTALL_LOCATION=/opt/usr/lib/pi_robot

rm -rf "$INSTALL_LOCATION"
curl "$VERSION_LOCATION" | tar xzC "$INSTALL_LOCATION"

