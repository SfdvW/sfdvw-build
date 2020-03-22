#!/bin/bash
#for i in 90; do $i ... ; done
convert -font FreeSerif-Fett -fill white -pointsize 200 -gravity center -draw "text 0,10 \"SfdvW\"" -draw "text 0,160 \"$1\"" Unbekannt.png sfdvw$1.jpg;

