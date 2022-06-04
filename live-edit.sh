#!/usr/bin/env bash

make html
while inotifywait -e modify,close_write,move,delete_self resume.{rst,css} rst2html.py makefile; do
    make html && sleep 0.5
done
