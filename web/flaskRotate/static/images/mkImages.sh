#!/usr/bin/env sh

for i in {1..12}; do
    I=$(printf %02d $i)
    echo $I
    convert -size 1000x600 -background white -fill grey -font URWGothic-Demi -pointsize 256 label:$I image$I.png
done
