#!/bin/bash

# This script checks for the latest Android Studio version and updates the spec file.

set -e

# Get the latest version from the AUR PKGBUILD
LATEST_VERSION=$(curl -s "https://aur.archlinux.org/cgit/aur.git/plain/PKGBUILD?h=android-studio" | grep "pkgver=" | cut -d'=' -f2)
CURRENT_VERSION=$(grep "Version:" android-studio.spec | awk '{print $2}')

if [ "$LATEST_VERSION" != "$CURRENT_VERSION" ]; then
    echo "New version found: $LATEST_VERSION"
    # Update the spec file with the new version
    sed -i "s/^Version:.*/Version:        $LATEST_VERSION/" android-studio.spec
    # The _service file will handle the source download
else
    echo "Android Studio is up to date."
fi
