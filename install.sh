#!/bin/sh
set -e


##  xdebugtracetree - add trees to xdebug traces.
##  Copyright (C) 2019  BrainFucker <retratserif@gmail.com>
##  
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##  
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.

umask 002

if [ ! "$(id -u)" -eq 0 ]; then
    echo 'This should be run as root.'
    exit 1
fi

DIR="$(dirname "$0")"

if [ ! -d '/opt/xdebugtracetree' ]; then
    mkdir /opt/xdebugtracetree
fi

cp -r "$DIR/"* /opt/xdebugtracetree/

python3 -OO -m compileall -b "/opt/xdebugtracetree/xdebugtracetree.py"

if [ ! -f "/opt/xdebugtracetree/xdebugtracetree.py" ]; then
    echo "Build failed."
    exit 1
else
    chmod 755 /opt/xdebugtracetree/xdebugtracetree.sh
    ln -s /opt/xdebugtracetree/xdebugtracetree.sh /usr/local/bin/xdebugtracetree
    echo "Build complete."
fi
