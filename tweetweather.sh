#!/bin/sh

# Autorun for tweetweather.py
# copy this file into /etc/init.d/ directory and 
# make the run at start up:

#    % cp tweetweather.sh /etc/init.d/.
#    % cd /etc/init.d/
#    % update-rc.d tweetweather.sh defaults

# Make sure dmesgs dont print to console
echo 4 > /proc/sys/kernel/printk

# Let everything start up
sleep 80

echo "-!- Beginning tweetweather tasks" > /dev/kmsg

# Run background tasks
cd /home/root/EdiTweet
python tweetweather.py
