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
```sh
root@kali:~/Downloads# ./Anaconda3-2020.02-Linux-x86_64.sh
```

Importing and unzipping files
-----------------------------

### Packetto.zip

Import this zip file into the VM (Desktop). Unzip it as shown below.
```sh
root@kali:~/Desktop# unzip Packetto.zip
```

If everything was extracted correctly, this should be the output when the command shown below is entered.
```sh
root@kali:~/Desktop/Packetto# ./packetto.py
```

packetAnalytics.tar.bz2
-----------------------

A file with this name will be found in the Packetto directory. We will have to unzip that with anaconda. To do that lets open a terminal in the same directory.
```sh
root@kali:~/Desktop/Packetto# anaconda-project unarchive packetAnalytics.tar.bz2
```

After unzipping we need to change directory into it and run the anaconda project and let it setup.
```sh
root@kali:~/Desktop/Packetto/packetAnalytics# anaconda-project run
```
After that 15 minute process has completed and succeeded, we are all setup to use the product!!

Usage of Packetto
=================

Packet sniffing with Packetto
-----------------------------

There are various different kinds of packets that you can sniff with packetto. To get started, you can visit the help page following the commands shown below. (Open the shell in the Packetto directory first)
```sh
root@kali:~/Desktop/Packetto# ./packetto.py -H
```
In each option in our program, you are able to choose which adapter you would like to sniff incase you have more than one main adapter on your machine. Moreover, you are even able to choose if u would like to output it to a pcap file for further analysis with other software or our AI/ML driven packet analysis solution!

For e.g

To select the network adapter that you would like to use for the sniffing process, do the following.
```sh
root@kali:~/Desktop/Packetto# ip a
```
As you can see above there are 2 adapters available to us to use for sniffing. When u launch our program with the correct argument stated in the help page, you will see this question asked to you. You can enter the adapter that you would like to use and then hit enter!

If you want to filter for HTTP packets but do not want to save the output to a pcap file, you can do the following
```sh
root@kali:~/Desktop/Packetto# ./packetto.py -h**n**
```
If you want to filter for HTTP packets and want to save the output to a pcap file, you can do the following
```sh
root@kali:~/Desktop/Packetto# ./packetto.py -h**o**
```
As you can see the only difference is the value passed together with the main argument. O or N.

O = output to pcap file

N = no output to pcap file

Here's how things should look if everything goes through properly.

There should be a new file named capture.pcap

Packet Analysis (AI/ML)
=======================

Start the tool
--------------

We first need to change directory into the packetAnalytics directory. In there is a file named `initialise.sh` This will make it much easier for the end user to import the pcap capture file into the directory and setup the anaconda environment. First enter this command the command below and then Run that file similar to how we would run any shell script.
```sh
root@kali:~/# conda activate /root/Desktop/Packetto/packetAnalytics/envs/default

root@kali:~/Desktop/Packetto/packetAnalytics# ./initialise.sh
```
The script and the command does 4 important things.

- Removes any pcap files that exist in the directory(incase the previous user forgot to remove it)

- Brings the newly created pcap file by Packetto into this directory and preps it for data analytics

- Activates the anaconda environment with python 3 and all the dependencies that we need for this project

- Initiates jupyter lab with root permissions

Disclaimer: You will only be able to access the jupyter lab environment on the web browser using the link provided in the terminal due to the token auth being switched on. This is to prevent some attack vectors.

This is what you will be greeted with when u access the jupyter lab web environment using the web browser. Our main working file will be **Packet-Analytics.ipynb.** You can see a bunch of controls at the top of the screen. This is to run/stop/modify/delete code on the file.

Now that we have initialised the environment, let's get to using it! The codes on the file will run in snippets so that you can follow through and see the output as the pcap file is being analysed. You just have to keep pressing play [>RUN] up top and you will be able to see the output on the screen!

Stop the tool
-------------

Head to the command prompt where the jupyter lab notebook is running and do the following.

Control + c;   yes.
