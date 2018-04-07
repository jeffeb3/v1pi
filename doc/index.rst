
#############
V1PI
#############

What is it?
===========

It's an image for a raspberry pi, where I've configured as much as possible to help you get started
quickly making things with your v1engineering.com machines.

Safety Notice
=============

Please be safe. CNC routers, even small ones, with tiny bits can make mistakes, and quickly end up
in a dangerous situation, causing a fire that can quickly grow to serious damage. Don't leave your
machine unattended. I am not responsible for anything you do, but I really don't want to hear about
any tragedies from someone using my software.

Let's Do It
===========

Great, let's flash an SD card with the image and get to making dust in the shop!

Step 1: Download the image
==========================

Download the most recent stable release from github: https://github.com/jeffeb3/v1pi/releases

Step 2: Copy the data to the SD card
====================================

The most general option is Etcher: `Get Etcher <https://etcher.io/>`_

More details: `Burn SD cards with Etcher <https://www.raspberrypi.org/magpi/pi-sd-etcher/>`_

Step 3: Configure WiFi (Optional)
=================================

If you don't want to connect this pi to your home WiFi network, then continue to the next step. If
you're not sure, or you want to connect to your home WiFi, look at :doc:`wifi-setup`. Then come right back.


Step 4: Start it for the first time
===================================

Safely remove your SD card, or call umount/sync on Linux, and put the card in the pi. Connect the
printer and power it up.

The first time the pi boots, it will do some work to expand the filesystem to the full SD card size,
and generally setting things up. This takes a few minutes.

If you are using the pi as a hotspot (it's not connected to your WiFi) then the WiFi network may not
show up on the first boot (I'm not sure why, but in my tests, it wasn't coming up the first time).
Wait a few minutes (literally 5 minutes is fine) and cycle power. Then wait a few more minutes
and it should show up.

Step 5: Connecting
==================

Connect to Hot Spot
-------------------

* The Hot Spot will show up with an ssid of ``v1pi`` and a connection password of ``raspberry``.
* Your computer might complain that you don't have an Internet connection. That's normal. The pi
  doesn't have Internet.
* If you connect with this method, the pi's ip address is ``192.168.50.1``
* Open `http://192.168.50.1 <http://192.168.50.1>`_

Connect Through Your WiFi
-------------------------

* The pi will get it's IP address from your router. If you know how to find the IP address from your
  router, then you can do that, and put ``http://<the ip address>`` in your browser's address bar.
* The pi will also advertise it's address via `http://v1pi.local <http://v1pi.local>`_

  * Macs: Just to there.
  * Linux (including other pi's): Install avahi-daemon, and then go there.
  * Windows: Check out Adafruit's guide `Here <https://learn.adafruit.com/bonjour-zeroconf-networking-for-windows-and-linux/overview>`_
  * Android: I haven't got a good way to do this from android, so I would ``ping v1pi.local`` from a
    computer, and see what address it's pinging, and put that in my android address bar.

* As a last resort, you can connect a monitor and keyboard. The pi will boot up to a login prompt.
  The prompt will print the different addresses that will let you connect to the pi.

Step 6: Use it
==============

The landing page will give you a few sparse links to information about this image, and two options:

* Octoprint: Very mature server for 3D printers. There are a lot of great features, and plugins, but
  it's use case is 99% 3D printing.
* CNC.js: Simple, CNC interface. The Marlin support is especially new, but I've been using it with
  grbl for a long time, and I love how simple and effective it is.

Step 7: Change the Passwords
============================

The default login password is raspberry, which the whole world knows. Even if you don't know how to
use the command line, other people do, and they can do nasty things to you. There are many many
things to do to improve security, but number one is to change the passwords.

Changing the SSH password
-------------------------

You'll need to log into the pi to change the password.

* Connecting with an ssh client is the easiest way, after you know the ip address.

  * Windows: putty.exe is an oldie and a goodie.
  * Mac/Linux: ``ssh pi@v1pi.local``

* If you can't get ssh to work, you can also log in using a keyboard and monitor.
* The default username is ``pi`` and the default password is ``raspberry``
* Change the password by running the ``passwd`` command.
* There is no root password set, so you don't have to change it. Any super user actions can be done
  as pi with the ``sudo`` command.

Changing the Hot Spot Password
------------------------------

The hot spot *default* password is ``raspberry``. Any device within range can connect, and find your
pi, or the web interface, and control your pi, and your CNC machine. It gets worse if you think
about an infected device being in range, and not just a panel van with an antenna on it.

Changing the password is easy, and will help you sleep at night. OK, maybe not, but writing this
will help me sleep at night.

The password is stored on the root file system in ``/etc/hostapd/hostapd.conf``. Log into the pi
through ssh, or you can edit the file on the sd card from your computer (but not in notepad, use
notepad++)

    ``sudo nano /etc/hostapd/hostapd.conf``

Go down to where it says: ``wpa_passphrase=raspberry`` and change the word raspberry to something
you want. Save the file (in nano, it's [Ctrl+x], y, enter).

That's it
=========

Enjoy! Check out some of octoprint's plugins, load up some gcode from your desktop computer, attach
a webcam, etc.

Be sure to look at the (much more detailed) documentation from OctoPi, OctoPrint, and CNC.js:

 * OctoPi: https://octopi.octoprint.org/
 * OctoPrint: https://octoprint.org/
 * CNC.js: https://cnc.js.org/

