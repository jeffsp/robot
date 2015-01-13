#!/bin/bash

# view stream at
#
# 	http://192.168.1.64:8080/stream.html
#
# or
#
# 	http://192.168.1.64:8080/stream_simple.html

cd /usr/src/mjpg-streamer/mjpg-streamer-experimental
export LD_LIBRARY_PATH=.
./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -x 640 -y 480 -fps 20 -ex night -rot 180"
