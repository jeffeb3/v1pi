# Advanced Set Up

Changing the Hostname
=====================

The hostname is `v1pi` by default. But if you have more than one on a network, or you just want to
name it something else, you can by editing two files.

!!! info "/etc/hostname"
    Change /etc/hostname. There is only one word inside hostname, and it's whatever you want the
    hostname to be.

!!! info "/etc/hosts"
    `/etc/hosts/` is part of the networking, and it tells Linux what IP address to use for certain
    names. The v1pi's hostname is in there, so that it can always find itself. Find the line that
    says:
    ```
    127.0.1.1	v1pi
    ```
    Change v1pi to your new hostname.

Reboot the pi, and you should be good to go.

Debugging through UART
======================

There's a good guide [here from adafruit](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/overview)

But the key part is to add `enable_uart=1` to the bottom of /boot/config.txt.

Then connect with 115200 baud. My miniterm.py connection looks like this:

```
miniterm.py /dev/ttyUSB0 115200 --eol LF --raw
```

[Buy USB UART Here](https://amzn.to/34eiuSp)

The nice thing about this is, you probably already have a computer you're working with, and you
don't need another keyboard/mouse/monitor. But if the pi isn't connecting to wifi, then you need a
way to kick it. This is one of the easiest ways.

