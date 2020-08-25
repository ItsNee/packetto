Installation
============

This guide, will teach you how to install our product onto a fresh kali VM (or any other Linux based machine that supports python and anaconda)

Prerequisites
-------------

### Python

Make sure the machine has Python installed (higher than v2.6)

### Anaconda 64-bit (x86)

Next we have to install the anaconda framework on the VM to be able to leverage off of the ML/AI improvements of packetto

First off, get the latest anaconda individual installation from [here](https://www.anaconda.com/products/individual). Then proceed to download the **64-Bit (x86) Installer** at the bottom of the webpage.

Next up, download and save it onto the kali VM (in our case) and open a shell in the same location the file is saved. Use command `ls` to verify.

Now we need to give this file permissions so that it is able to install Anaconda successfully

Now to install it, enter the following command.

root@kali:~/Downloads# ./Anaconda3-2020.02-Linux-x86_64.sh

Importing and unzipping files
-----------------------------

### Packetto.zip
