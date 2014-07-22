#!/bin/sh

BRANCH="development"
FILENAME="pi_robot_$BRANCH.tar.gz"
TEMP_LOCATION="/tmp/$FILENAME"

if ! hash git 2>/dev/null; then
    echo "git is not installed, please install before running this script"
    exit 1
fi

if ! hash git 2>/dev/null; then
    echo "aws is not installed, please install awscli before running this script"
    exit 1
fi

git archive --format tar $BRANCH | gzip - > "$TEMP_LOCATION"
aws s3 cp --acl public-read "$TEMP_LOCATION" "s3://uk.co.gregorydoran.pi.robot/$FILENAME"