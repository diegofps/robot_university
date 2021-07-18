#!/usr/bin/sh

if [ -z "$1" ]; then
    TARGET='all'
else
    TARGET="$1"
fi

echo "Target: $TARGET"

for CURRENT in baseimg python3image clangimage monoimage openjdkimage; do
    if [ "$TARGET" = 'all' -o "$TARGET" = "$CURRENT" ]; then
        echo "Building image $CURRENT"
        (cd $CURRENT && docker build -t $CURRENT:v0 .)
    fi
done

