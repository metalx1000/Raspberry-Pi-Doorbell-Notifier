#!/bin/sh
echo "Content-type: text/html"
echo ""

cat /sys/class/gpio/gpio23/value
