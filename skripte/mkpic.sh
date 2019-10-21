#!/bin/bash
for i in 86; do convert -font FreeSerif-Fett -fill white -pointsize 200 -gravity center -draw "text 0,10 \"SfdvW\"" -draw "text 0,160 \"$i\"" Unbekannt.png sfdvw$i.jpg; done
