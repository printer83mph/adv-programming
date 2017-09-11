# Installing Linux

**DISCLAIMER** - if you want unix commands (and git) there is [something else](#supa-secret-hack) you can do without installing linux. 

## Choose a distro

First of all you have a lot of choices when it comes to distros (linux distributions, like free donuts but you have to choose one type), but if you don't want to spend hours
troubleshooting with the terminal or you aren't that familiar with the commandline, there are some
distros that are better documented and will give you a much smoother overall experience.

* **[Ubuntu](https://www.ubuntu.com/desktop)** - Popular distro built on Debian with great documentation and solid looks, but some Amazon/"Ubuntu One" product placement. Uses the "Unity" desktop environment (which is dying rn)

* **[Ubuntu Flavors](https://www.ubuntu.com/download/ubuntu-flavours)** - Ubuntu but with different "desktop environments," providing different looking and speedier/slower experiences (and maybe different default apps). These include:

  Ubuntu GNOME - quick and polished with a modern look, maybe too modern
	
  Kubuntu - KDE gives you a powerful experience with a more zany look
	
  Ubuntu Mate - Supa quick but uses an older UI that you probably won't like unless you know you already know it.
	
  Probably more - but those are the popular ones.

* **[Linux Mint](https://www.linuxmint.com/download.php)** - Distro built on Ubuntu without the product placement, fast and rather nice looking UI - very smooth user experience

* **[Elementary OS](https://elementary.io/)** - Fairly new distro built on Ubuntu with a sleek and very fast UI, not as customizable but very refined: think open source Mac OS X. Life hack: they say pay what you want but you can just download it for free (Custom > $0).

* **[Zorin OS](https://zorinos.com/)** - Windows-like distro built on Ubuntu (I think) focusing on ease of use and good looking UI. Quick and solid according to the internet

I'm sure you can find more distros that are just as good, but these are the popular ones I think are good for beginners and I would stick to one of these (don't distro hop PLEASE)

If you're not sure which distro to use I would use Ubuntu (a flavor if you want) or Linux Mint since they have the best documentation, and if you're willing to give up some customizability Elementary OS looks and runs fantastic.

## Flash the OS

You're going to need a flash drive, CD, or any removable storage that you're willing to format in order to install another OS on your computer.

Make sure to download the 64 bit version if you have a 64 bit computer and 32 bit otherwise, and if there are multiple versions go with the newest LTS or stable release.
Use a torrenting program like uTorrent if you can, it should be quicker. You should have a .iso file downloaded. Then you need to burn it to a flash drive or CD.

I would use [Etcher](https://etcher.io/) to burn it, but any software works. I've just found Etcher to be straightforward and reliable. Choose your donwloaded ISO file and the drive you want to use, then burn it.
*It will eject the drive so you'll have to pull it out and reconnect it.*

## Boot from the drive

You could go through Windows or the BIOS, either way works but Windows is probably easier.

### Windows:

1. Open the start menu and search "boot"
2. You should see "Change advanced startup options," click it
3. Under "Advanced startup" choose "Restart now"
4. Your PC will restart and when it comes back on choose "Boot from device"
5. There should be an option that's the name of your drive and/or "UEFI". Choose that.

### BIOS:

1. Reboot your PC and while it's booting up hold the f key that opens the bios - this is probably f2 but on different computers it could be something else.
2. Using the arrow keys, go to "boot" and boot from the drive, probably your drive name and/or "UEFI"

## Setting it up finally

Most of these OS's will ask you whether to try the OS first or install it. Either one works, but if you select try you'll have to open up the install program after it boots into the OS.
Don't remove the drive until the install is complete. It might ask you if you want to install 3rd party drivers, definitely do.

When it comes to partitioning, it will ask what to do. Choose install alongside Windows, and choose how much space you want it to have. I would recommend at least 16 gigs, but more is great.
If there is no option to install alongside Windows, you will have to manually resize the Windows partition (C:) and set up a new partition in the blank space yourself. This can be risky
and I would change the partition size in Windows if possible.

The other setup steps should be simple enough. You can put your full name in for "Name" and your username can just be your first name, lowercase. Make sure you choose a solid password!

Ta daaa! Once the setup is done you should be asked to reboot, and eventually pull the drive out. Now every time you boot up your PC it will ask which OS to boot into.

I would look up some starters online if you want to get to know the OS. Definitely learn terminal commands.

## Supa Secret Hack

1. Install git on Windows. Not github, git.
2. Open up system environment variables > environment variables (at the bottom)
3. Edit the variable "Path" (on the top)
4. Add a path to `Program Files\usr\bin` and save
5. Now you can use most unix commands in a Windows terminal! EZ game EZ life