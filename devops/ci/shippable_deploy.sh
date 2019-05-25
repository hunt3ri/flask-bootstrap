#!/usr/bin/env bash
echo Running shippable deploy current branch is $BRANCH

# We don't want to deploy Pull Requests only builds on develop and master
if [ $IS_PULL_REQUEST == true ]
    then
        echo Not Deploying Build $BUILD_NUMBER - Branch is $BRANCH, Is Pull Request is $IS_PULL_REQUEST
        return
fi

# Set Version Number
VERSION=v.1.0.$BUILD_NUMBER-$BRANCH

# Only deploy to Staging if we're on develop
if [ $BRANCH == "develop" ]
    then
        echo Please add necessary deploy scripts here to deploy to staging environment
fi

# Only deploy to Prod if we're on master
if [ $BRANCH == "master" ]
    then
        echo Please add necessary deploy scripts here to deploy to prod environment
fi
