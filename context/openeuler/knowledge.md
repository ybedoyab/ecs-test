# openEuler

## HCIA-openEulerV1.0TrainingMaterials.pdf

Getting Started with openEuler

Huawei Confidential
2
Foreword
This document describes the following:
GNU Free Software Foundation 
Origin of Linux
openEuler operating system (OS) 
How to install and log in to the openEuler OS

Huawei Confidential
3
Objectives
After completing this course, you will understand:
Open source and GNU
Origin of Linux
Linux principles
How to install openEuler
How to log in to openEuler

Huawei Confidential
4
Contents
1.
Introduction to the Linux OS
2.
Installing the Open Source openEuler OS
3.
Using the openEuler OS

Huawei Confidential
5
OS Overview
An OS is a set of programs that controls and manages the hardware and software
resources of an entire computer system, providing a convenient interface and
environment for users and other software. A computer‘s OS is its most basic system
software, and it gradually evolves in line with the development of computer
research and application.

Huawei Confidential
6
Unix Development History

Unix development
In the 1960s, Bell Labs, MIT, and GE jointly developed a multiprogramming information computing system 
named Multics.
In 1970, Ken Thompson developed Unix.
In 1974, Bell Labs released Unix, which became widely used in universities.
After the breakup of AT&T in 1982, Unix began to charge for commercial use.
Some large hardware companies have developed different versions of Unix based on their own computer 
systems.
AIX
HP-UX
Digital Unix
…

Huawei Confidential
7
GNU and Open Source

In 1984, Richard Stallman launched the Free Software Campaign, established the Free Software
Foundation, and achieved the following:
Created an open source version of the Unix utility.
Released the general public license (GPL).
Open source, also known as open source code, laid the foundations for the rapid development of IT 
technologies.

There are many open source licenses, each with different rules. Some common open source licenses are
as follows:
Mulan.
GPL.
Lesser GPL (LGPL).
Berkeley Source Distribution (BSD).

Huawei Confidential
9
Birth of Linux

Birth of Minix
In 1987, Andrew S. Tanenbaum, a professor of Vrije University in Amsterdam, wrote Minix.  Similar to Unix, this 
OS was instead dedicated to teaching.

Birth of Linux
On September 17, 1991, Linus Torvalds released his own Linux OS on the Internet and claimed that it was free 
of charge. In addition, he hoped to improve the Linux OS through the efforts of developers.
In 1994, Linux kernel 1.0 was officially released.
More accurately, the full name of Linux is GNU/Linux.

Today's Linux
Today, Linux has many derivatives, such as Red Hat, openSUSE, Ubuntu, and Deepin.
Linux distribution = Linux kernel + utility software

Huawei Confidential
10
Introduction to Linux Releases

Kernel versions
You can visit kernel.org to view or download all Linux kernel versions.
The Linux kernel version number is composed of three digits:
The first digit indicates the current major release.
An even second digit indicates a stable version, while an odd second digit indicates a version under development.
The third digit indicates the number of revisions.
The kernel version of openEuler 20.03 LTS is 4.19.90.

Linux distributions
Commercial distros: maintained by companies and provides charged services, such as patch upgrades.
Community distros: maintained by the community organization and free of charge.

Huawei Confidential
11
openEuler OS

openEuler is a free, open source OS operated by the openEuler community. The current openEuler
kernel is based on Linux and supports Kunpeng and other processors, fully unleashing the potential of
computing chips. As an efficient, stable, and sustainable open source OS built by global open source
contributors, openEuler applies to database, big data, cloud computing, and artificial intelligence (AI)
scenarios.

openEuler has two kinds of releases:
Innovation release
Supports the technical innovation and content innovation of Linux enthusiasts, such as openEuler 20.09.
Generally, a new version is released every half a year.
Long-term support (LTS) release
A stable version of openEuler, such as openEuler LTS 20.03.
Usually a new version is released every two years.

Huawei Confidential
12
Contents
1.
Introduction to the Linux OS
2.
Installing the Open Source openEuler OS
3.
Using the openEuler OS

Huawei Confidential
13
openEuler OS Installation Process
1
Prepare the installation 
environment.
2
Select an 
installation mode.
3
Configure system 
settings.
4
Installation 
complete.
•
openEuler can be 
installed on the Arm-
and x86-based 
computing platforms. 
The ISO files of the two 
platforms are 
incompatible.
•
You can obtain the ISO 
image from the 
openEuler community .
•
openEuler supports 
various installation 
modes. If only a few 
devices need to be 
installed, use a USB 
flash drive, CD-ROM, or 
virtual CD-ROM drive. 
During batch 
installation, use the PXE
boot mode.
•
When installing 
openEuler, you need to 
set the system 
parameters, such as the 
installation language, 
installation location, 
software version, host 
name, and network 
configuration.

Huawei Confidential
14
openEuler Installation and Configuration - Selecting 
Installation Options
Install openEuler 20.03 LTS
Test this media & install openEuler 20.03 LTS
Troubleshooting -->
Use the ▲and ▼keys to change the selection.
Press 'e' to edit the selected item, or 'c' for a command prompt.
Directly install the system.
Check the software package 
and install the system.
Troubleshooting
Test this media & install openEuler 20.03 LTS

Huawei Confidential
15
openEuler Installation and Configuration - Selecting an 
Installation Language

Huawei Confidential
16
openEuler Installation and Configuration - System Settings

Huawei Confidential
17
openEuler Installation and Configuration - Setting the 
Installation Location

Set the system installation location and system partitions.
Select the disk where the OS is to be installed.
Choose how to partition your disk. 
In manual mode, you can set partitions, including common partitions, logical volumes, and thin-provisioning 
logical volumes.
You are advised to set the following partitions for the openEuler system startup:
−swap: swap partition, which is used to swap dirty data in the memory when space is insufficient. If the memory is small, 
you are advised to set the swap partition size to twice the memory size. If the memory is large, you can reduce the 
swap partition size.
−/boot: booting
−/boot/efi: boot device and application program to be started by the extensible firmware interface (EFI).
−/: root partition. In Linux, everything starts from the root partition.

Huawei Confidential
18
openEuler Installation and Configuration - Selecting 
Software to Be Installed
openEuler 20.03 LTS supports the following software installation options:
Minimum installation
Minimum Linux installation: Most software is not installed. This mode is applicable to scholars 
who have background in Linux and want to further understand the Linux architecture. Other 
software is also available on the right.
Server
Install the software involved in the server scenario. Other software is also available on the right.
Hypervisor
Install the software involved in the virtualization scenario. Other software is also available on 
the right.

Huawei Confidential
19
openEuler Installation and Configuration - Setting the 
Password of the Root User and Creating a User

Huawei Confidential
20
Contents
1.
Introduction to the Linux OS
2.
Installing the Open Source openEuler OS
3.
Using the openEuler OS

Huawei Confidential
21
Linux GUI and CLI
GUI stands for graphical user interface. All elements of this user interface are
graphical. The mouse is used as the input tool, and buttons, menus, and dialog
boxes are used for interaction, enhancing ease of use.
CLI is short for command line interface. All elements of a CLI are character-based.
The keyboard is used as the input tool to enter commands, options, and parameters
to execute programs, achieving high efficiency.
No GUI is available for openEuler 20.03 LTS.

Huawei Confidential
22
How to Log In to the Linux OS
You can log in to the Linux OS through either of the following methods:
Local login
This method is similar to starting up your own computer or directly connecting the server to the 
monitor.
A typical Linux system runs six virtual consoles and one graphical console. Currently, openEuler 
does not support the GUI.
You can press Ctrl+Alt+F[1,6] to switch between the six virtual consoles.
Remote login
The openEuler OS supports remote login by default. You can also change the login mode.
You can use PuTTY or Xshell to remotely log in to the openEuler OS.

Huawei Confidential
23
Introduction to Shell

Shell, a program compiled in C language, serves as a bridge for those who wish to use Linux. Users
control the Linux system through shells, which are also used by the Linux system to display system
information.

Common shells include bash, sh, csh, and ksh. You can specify a login shell when creating a user, or
enter a shell name to open a shell. For example:

The default login shell for openEuler users is bash.

The default system prompt is [Current login user@Host name Current location]$.
Generally, the last prompt of the root user and common users is #.
[root@openEuler ~]# sh
sh: openEuler_history: command not find
sh-5.0# 
# The interaction modes varies with different shells.
sh-5.0# exit
# Enter exit to exit the current shell.
[root@openEuler ~]#

Huawei Confidential
24
Changing Passwords

The password is directly related to the security of the system and its data.

To ensure system security, perform the following operations:
Change the password upon the first login.
Change passwords periodically.
Set a password with high complexity. For example, set a password containing more than eight characters and 
three or more of the following types of characters: uppercase letters, lowercase letters, digits, and special 
characters.

You can run the passwd command to change your password.
[root@openEuler ~]# passwd
Changing password for user root.
New password:  
# Enter the new password.
Retype new password:                                       # Enter the new password again.
passwd: all authentication tokens updated successfully

Huawei Confidential
25
Linux Users
The root user is a special administrator in the Linux OS.
This super administrator is similar to the administrator in the Windows OS.
The root user has the highest permissions, and can cause infinite damage.
Do not use the root user unless necessary.
You can run the su - username command to switch users.
You can check whether the current user is the root user or a common user through
the command prompt. In the Unix or Linux OS, the command prompt of the root
user generally ends with #, while that of a common user generally ends with $.
You can also run the id command to view the current username.

Huawei Confidential
26
Shortcut Operations with the Bash Shell 

tab
You can use the tab key to supplement functions and quickly enter commands or parameters.

history
The history tool records historical commands. You can run the history command to view historical commands, 
or run the history n command to execute the historical command numbered n.

↑and ↓
You can press the ↑ and ↓ arrow keys to quickly view historical commands.

home and end
To move the cursor to the beginning or end of the current line, press home or end, respectively.

clear and Ctrl+L
When the page is full of characters, you can enter clear or press Ctrl+L to quickly clear the screen.

Huawei Confidential
27
Quiz
1.
(True or false)You do not need to specify the password of the root user during the openEuler OS
installation. However, you must specify the password of the root user when logging in to the OS after
the installation.
A.
True
B.
False
2.
(Single-answer)Which of the following keys can be used to quickly supplement commands and
parameters?
A.
Ctrl+L
B.
↑and ↓
C.
tab
D.
Space

Huawei Confidential
28
Summary
This document describes the development of the Linux OS, introduces the
openEuler OS, and describes how to install openEuler and related shortcut
operations.

Huawei Confidential
29
More Information
For
more
information
about
Linux
shortcut
keys,
please
visit
https://linuxtoy.org/archives/bash-shortcuts.html.

Huawei Confidential
30
Acronyms
Acronym
Full Name
Description
POSIX
Portable Operating System Interface
Portable Operating System Interface (POSIX) is the name of a family of related standards 
specified by the IEEE to define the application programming interface (API), along with 
shell and utilities interfaces for software compatible with variants of the Unix operating 
system, although the standard can apply to any operating system.
GNU
GNU's Not Unix
GNU (prononunced GAH-noo with a hard "G") is an ambitious project started by Richard 
Stallman to create a completely free operating system based upon the design of Unix. 
AT&T
American Telephone and Telegraph Co.
It was an American telecommunications company founded in 1877
KDE
K Desktop Environment
One of the popular desktop environments for Linux. Kubuntu uses KDE by default.
ksh
Korn shell
An interactive command interpreter and a command programming language. 2. A 
command interpreter developed for UNIX, which forms the basis for the z/OS shell.
csh
C shell
A command line processor for UNIX that provides interactive features such as job control 
and command history.

Copyright© 2023 Huawei Technologies Co., Ltd.
All Rights Reserved.
The information in this document may contain predictive 
statements including, without limitation, statements regarding 
the future financial and operating results, future product 
portfolio, new technology, etc. There are a number of factors 
that could cause actual results and developments to differ 
materially from those expressed or implied in the predictive 
statements. Therefore, such information is provided for reference 
purpose only and constitutes neither an offer nor an acceptance. 
Huawei may change the information at any time without notice. 
把数字世界带入每个人、每个家庭、
每个组织，构建万物互联的智能世界。
Bring digital to every person, home, and 
organization for a fully connected, 
intelligent world.
Thank you.

CLI Basics

Huawei Confidential
2
Foreword
This document describes the basics of command line operations, including
the command line interfaces (CLIs) and CLI-based file management.

Huawei Confidential
3
Objectives
After completing this course, you will be familiar with:
Basic Linux commands
Linux login commands
Linux system power management commands
Linux file management commands

Huawei Confidential
4
Contents
1.
Basic Knowledge of Linux Commands
2.
Basic Linux Commands

Huawei Confidential
5
Linux GUI and CLI

GUI stands for graphical user interface. All elements of this user interface are graphical. The mouse is
used as the input tool, and buttons, menus, and dialog boxes are used for interaction, enhancing ease
of use.

CLI is short for command line interface. All elements of a CLI are character-based. The keyboard is used
as the input tool to enter commands, options, and parameters to execute programs, achieving high
efficiency.

Huawei Confidential
6
Why We Use the Linux Command Line?

More efficient
The Linux system allows rapid operations using a keyboard, rather than a mouse.
The GUI is fixed, while CLIs in a script can be compiled to complete all required tasks. For example: 
deleting outdated log files.

Low overhead (compared with GUI)
Running a GUI requires a large number of system resources, whereas a CLI is far more efficient. As 
a result, system resources can be allocated to other operations.

CLIs are often the only choice
Most OSs for running servers do not utilize a GUI.
Tools for maintaining and managing connected devices do not provide a GUI.

Huawei Confidential
7
Syntax of Linux Commands
Syntax: command [-option] [parameter]
Example: ls -la /etc
Note:
Some commands do not comply with this format. The [] symbol indicates an option.
If there are multiple options, you can write them together.
Options can be short by following one hyphen (-) or long by following two hyphens (--). 
For example, ls -a equals ls --all.

Huawei Confidential
8
Linux Command Line Keyboard Shortcuts

Tab: automatically supplements commands or file names, saving time and improving accuracy.
If no command is entered, press Tab twice to list all available commands.
If you have entered a part of the command name or file name, pressing Tab will supplement them 
automatically.

Cursor
↑: Press ↑ to display recently executed commands, enabling you to quickly select and run them.
↓: Used together with ↑, facilitating command selection. 
Home: Press Home to move the cursor to the beginning of the current line.
Ctrl+A: Press Ctrl+A to move the cursor to the beginning of the line.
Ctrl+E: Press Ctrl+E to move the cursor to the end of the line.
Ctrl+C: Press Ctrl+C to stop the current program.
Ctrl+L: Press Ctrl+L to clear the screen.

Huawei Confidential
9
Classification of Linux Commands
Category
Example Commands
Login and power 
management
login, shutdown, halt, reboot, install, exit, and last
File processing
file, mkdir, grep, dd, find, mv, ls, diff, cat, and ln
System management
df, top, free, quota, at, ip, kill, and crontab
Network operation
ifconfig, ip, ping, netstat, telnet, ftp, route, rlogin, rcp, finger, mail, 
and nslookup
System security
passwd, su, umask, chgrp, chmod, chown, chattr, sudo ps, and who
Others
tar, unzip, gunzip, unarj, mtools, and man

Huawei Confidential
10
Contents
1.
Basic Knowledge of Linux Commands
2.
Basic Linux Commands
Login Commands
Power Management Commands
File Management Commands
Help Commands

Huawei Confidential
11
Login Command 1 - login (1)

login is used to log in to the system, which is applicable to all users.

If you choose to log in to the Linux OS in command line mode, the first command required is login.
Authorized users only. All activities may be monitored and reported.
Activate the web console with: systemctl enable --now cockpit.socket
Last login: Wed Jul 29 14:15:56 2020 from 172.19.130.204
Welcome to 4.19.90-2003.4.0.0036.oe1.aarch64
System information as of time:  Wed Jul 29 14:25:33 CST 2020
System load:    0.00
Processes:      185
Memory used:    20.0%
Swap used:      0.0%
Usage On:       13%
IP address:     192.168.110.245
Users online:   2
[root@localhost ~]#

Huawei Confidential
12
Login Command 1 - login (2)
Linux is a multi-user OS that allows multiple users to log in at the same time and a
single user to log in multiple times.
This is because Linux, like many versions of Unix, provides a virtual console access
mode that allows users to log in to the console (a monitor and keyboard that are
directly connected to the system) multiple times simultaneously.
Each virtual console can be regarded as an independent workstation and you can
switch between workstations.
You can press Alt and a function key (typically F1 to F6) to switch between virtual
consoles.

Huawei Confidential
13
Login Command 2 - last
last is used to display the recent logins of users or terminals, and is applicable to all
users. Run the last command to view a program's log. The user will know who used,
or attempted to connect to, the system.
Main options:
-n: specifies the number of output records.
-t tty: displays the login status of the specified virtual console.
-y: displays the year, month, and day of the record.
-ID: displays the username.
-x: displays the history of system shutdowns, user logins, and user logouts.

Huawei Confidential
14
Login Command 3 - exit
exit is used to log out of the system, and is applicable to all users.
The exit command has no options. After this command is executed, the system exits
and the login page is displayed.

Huawei Confidential
15
Contents
1.
Basic Knowledge of Linux Commands
2.
Basic Linux Commands
Login Commands
Power Management Commands
File Management Commands
Help Commands

Huawei Confidential
16
Power Management Command 1 - shutdown (1)

shutdown is used to shut down the computer, and is only applicable to the superuser.

Main options:
-h: powers off the server after it is shut down.
-r: powers on the server after it is shut down. (This operation is equivalent to restarting the server.)
-t: indicates the time after which the init program is shut down before changing to another run 
level.
-k: sends a warning signal to each user. It does not shut down the computer.
-F: forcibly performs file system consistency check (fsck) when restarting the computer.
-time: specifies the time before the shutdown.

Huawei Confidential
17
Power Management Command 1 - shutdown (2)
The shutdown command safely shuts down the system. It is dangerous to shut down
a Linux system by directly powering it off.
Unlike the Windows OS, Linux runs many processes in the background. As such,
forcible shutdown may result in data loss, leading to system instability or even
damaging hardware in some cases.
If
you run
the shutdown
command
to
shut
down
the system,
the
system
administrator notifies all login users that the system will be shut down and the login
command will be frozen. As a result, no further users can log in to the system.

Huawei Confidential
18
Power Management Command 2 - halt

halt is used to shut down the system, and is only applicable to the superuser.

Main options:
-n: prevents synchronization of system calls. It is used after the root partition is repaired using fsck, 
and prevents the kernel from overwriting the repaired superblock with that of an earlier version.
-w: writes the wtmp file in /var/log/wtmp instead of restarting or shutting down the system.
-f: forcibly shuts down or restarts the system without calling the shutdown command.
-i: shuts down all network interfaces before shutting down or restarting the system.
-f: forcibly shuts down the system without calling the shutdown command.
-d: shuts down the system without making a record.

Huawei Confidential
19
Power Management Command 3 - reboot
reboot is used to restart the computer, and is applicable to the system administrator.
Main options:
-n: saves the data and restarts the system.
-w: writes records to the /var/log/wtmp file. It does not restart the system.
-d: does not write records to the /var/log/wtmp file. (The -n option contains -d.)
-i: restarts the system after disabling the network settings.

Huawei Confidential
20
Contents
1.
Basic Knowledge of Linux Commands
2.
Basic Linux Commands
Login Commands
Power Management Commands
File Management Commands
Help Commands

Huawei Confidential
21
/
/bin
/boot
/dev
/etc
/lib
/lib64
/media
/mnt
/opt
Directory of binary 
programs used by all 
users
System library 
directory
Root directory
Linux File Directory Structure (1)

On the Linux OS, everything is a file.

The file directory utilizes a tree structure, with / as the root directory.
[root@localhost ~]# ls /
bin   dev  home  lib64       media  opt   root  sbin sys  usr
boot  etc lib   lost+found mnt
proc  run   srv
tmp var
Directory of the boot 
loader file
Device file directory
64-bit system library 
directory
Removable media 
device directory
Mounting directory
Directory for storing 
application software
Configuration file 
directory

Huawei Confidential
22
Linux File Directory Structure (2)
Dynamic directory for storing 
files that are frequently 
modified, such as logs.
/
/proc
/root
/run
/sbin
/srv
/sys
/tmp
/usr
/var
Home directory, which is used 
by users to store personal 
configurations.
/home
Directory for storing process 
information
Home directory of the root
user
Memory file system directory
Directory of binary programs 
used by the system 
administrator
Service data directory
Kernel device tree directory
Directory for storing 
temporary files
User application and 
configuration directory
Root directory 
[root@localhost ~]# ls /
bin   dev  home  lib64       media  opt   root  sbin sys  usr
boot  etc lib   lost+found mnt
proc  run   srv
tmp var

Huawei Confidential
23
Linux Directory Usage (1)
Directory
Main Files and Their Functions
/bin
bin is short for binary. This directory stores the most frequently used commands.
/boot
Stores core files used for starting the Linux OS, including some connection files and image files.
/dev
dev is short for device, and this directory stores Linux external device files. The method used to 
access devices on Linux is the same as that for accessing files.
/etc
Stores all configuration files and subdirectories required for system management.
/lib
Stores the system's most basic dynamic link libraries (DLLs). The function of this directory is 
similar to the storing of DLL files on Windows. Almost all applications need to use these shared 
libraries.
/mnt
Temporarily mounts other file systems.
/opt
Stores additional software that is installed on the host.
/proc
A virtual directory, which is the mapping of the system memory. You can obtain the system 
information by directly accessing this directory.

Huawei Confidential
24
Linux Directory Usage (2)
Directory
Main Files and Their Functions
/root
This directory is the home directory of the system administrator, who is also called the 
superuser.
/sbin
s indicates the superuser. This directory stores the system management program used by 
the system administrator.
/srv
Stores the data that needs to be extracted after a service is started.
/tmp
Stores temporary files.
/usr
Many user applications and files are stored in this important directory, which is similar to 
the program files directory on Windows. /usr/bin is the application used by system users. 
/usr/sbin is an advanced management program and system daemon used by the 
superuser. /usr/src is the default directory for storing the kernel source code.
/var
Stores content that is constantly expanded, such as log files. You are advised to place 
frequently modified directories here.
/run
A temporary file system that stores the information generated after the system is started. 
The information is cleared or deleted when the system is restarted.

Huawei Confidential
25
Linux File Paths
When using the shell or invoking an application, specify the path of the invoked
program.
The path can be an absolute or relative path.
Absolute path: On Linux, an absolute path starts from / (also called the root directory). If 
a path starts from /, it must be an absolute path.
Relative path: The relative path is relative to the current directory.

Huawei Confidential
26
File Command 1 - pwd

The pwd command is used to print the current working directory.

The pwd command has two options: -L and –P. The functions are similar to those of the cd command.

-L: outputs the connection path when the directory is linked.

-P: outputs the physical path.
[root@localhost ~]# pwd
/root
[root@localhost ~]# cd /var/log
[root@localhost log]# pwd
/var/log
[root@localhost log]#

Huawei Confidential
27
File Command 2 - cd
The cd command is used to change the current working directory.
Syntax: cd [dir]
cd /usr: accesses the /usr directory.
cd ..: accesses the upper-level directory. Two dots indicate the parent directory.
cd .: accesses the current directory.
cd: accesses the home directory by default if no parameter is added.
cd -: accesses the previous directory. This command is used to quickly switch between two 
directories.
cd ~: accesses the home directory.

Huawei Confidential
28
File Command 2 - Example
Change the current working directory.
[root@localhost ~]# pwd
/root
[root@localhost ~]# cd /var/log
[root@localhost log]# pwd
/var/log
[root@localhost log]# cd ..
[root@localhost var]# pwd
/var
[root@localhost var]# cd ~
[root@localhost ~]# pwd
/root

Huawei Confidential
29
File Command 3 - ls

The ls command is one of the most frequently used Linux commands, and lists the content
of a directory or file information. The output of this command is sorted by file name by
default. If no target is specified, the content of the current directory is listed.

Syntax: ls [OPTION]... [FILE]...
-a: displays all files and directories, including hidden files or directories whose names start with a 
dot (.).
-l: lists information such as the file type, permission, owner, and file size, in addition to the file 
name.
-t: lists files by creation time.
-R: lists any files in the current directory in sequence.

Huawei Confidential
30
File Command 3 - Example
Run the following commands to list all files (including hidden files) in the /usr/local
directory, and sort them by creation time.
[root@localhost ~]# ls /usr/local/ -ahlt
total 48K
drwxr-xr-x. 12 root root 4.0K Jul 28 14:00 ..
drwxr-xr-x. 12 root root 4.0K Jul 28 14:00 .
drwxr-xr-x.  5 root root 4.0K Jul 28 14:00 share
drwxr-xr-x.  2 root root 4.0K Mar 24 05:34 bin
drwxr-xr-x.  2 root root 4.0K Mar 24 05:34 etc
drwxr-xr-x.  2 root root 4.0K Mar 24 05:34 games
drwxr-xr-x.  2 root root 4.0K Mar 24 05:34 include
drwxr-xr-x.  2 root root 4.0K Mar 24 05:34 lib
drwxr-xr-x.  2 root root 4.0K Mar 24 05:34 lib64
drwxr-xr-x.  2 root root 4.0K Mar 24 05:34 libexec
drwxr-xr-x.  2 root root 4.0K Mar 24 05:34 sbin
drwxr-xr-x.  2 root root 4.0K Mar 24 05:34 src

Huawei Confidential
31
File Command 4 - mkdir
The mkdir command is used to create a directory or folder.
Syntax: mkdir [OPTION]... DIRECTORY...
[root@localhost ~]# ls
anaconda-ks.cfg
[root@localhost ~]# mkdir my_dir_01
[root@localhost ~]# ls
anaconda-ks.cfg my_dir_01
[root@localhost ~]# mkdir my_dir_02 my_dir_03
[root@localhost ~]# ls
anaconda-ks.cfg my_dir_01  my_dir_02  my_dir_03
[root@localhost ~]# mkdir my_dir_04/sub_dir
mkdir: cannot create directory 'my_dir_04/sub_dir': No such file or directory
[root@localhost ~]# mkdir -p my_dir_04/sub_dir
[root@localhost ~]# ls
anaconda-ks.cfg my_dir_01  my_dir_02  my_dir_03  my_dir_04
[root@localhost ~]#

Huawei Confidential
32
File Command 5 - touch
The touch command is used to create an empty file.
It can also be used to change the timestamp of a file.
[root@localhost ~]# ls
[root@localhost ~]# touch test01.log test02.log
[root@localhost ~]# ls -lt
total 0
-rw-------. 1 root root 0 Jul 29 15:06 test01.log
-rw-------. 1 root root 0 Jul 29 15:06 test02.log
[root@localhost ~]# touch -t 202001020304.05 test01.log
[root@localhost ~]# ls -lt
total 0
-rw-------. 1 root root 0 Jul 29 15:06 test02.log
-rw-------. 1 root root 0 Jan  2  2020 test01.log
[root@localhost ~]#

Huawei Confidential
33
File Command 6 - cp
The cp command is used to copy files or directories. You can copy a single file or
multiple files at a time. Exercise caution when running this command, as there is a
risk of data loss.
Syntax: cp [OPTION]... SOURCE... DIRECTORY
-a: copies the files of a directory while retaining the links and file attributes.
-p: copies the file content, modification time, and access permissions to the new file.
-r: copies all subdirectories and files in the source directory file.
-l: generates a link file but does not copy the file.

Huawei Confidential
34
File Command 6 - Example
[root@localhost ~]# ls
test01.log  test02.log
[root@localhost ~]# cp /etc/passwd passwd.back
[root@localhost ~]# cp -r /var/log/audit ./
[root@localhost ~]# ls
audit  passwd.back test01.log  test02.log
[root@localhost ~]# cp -s /etc/passwd passwd_link
[root@localhost ~]# ls
audit  passwd.back passwd_link test01.log  test02.log
[root@localhost ~]# ls -l
total 8
drwx------. 2 root root 4096 Jul 29 15:24 audit
-rw-------. 1 root root 2546 Jul 29 15:24 passwd.back
lrwxrwxrwx. 1 root root
11 Jul 29 15:25 passwd_link -> /etc/passwd
-rw-------. 1 root root
0 Jan  2  2020 test01.log
-rw-------. 1 root root
0 Jul 29 15:06 test02.log
[root@localhost ~]#

Huawei Confidential
35
File Command 7 - mv
The mv command is used to move a file or directory. Exercise caution when running
this command, as there is a risk of data loss.
If the source file and target file are in the same parent directory, the mv command
is used to rename the file.
Syntax: mv [option] source file or directory target file or directory
-b: backs up a file before overwriting it.
-f: forcibly overwrites the target file without asking the user.
-i: overwrites the target file at the destination after obtaining the user's consent.
-u: updates the target file only when the source file is newer than the target.

Huawei Confidential
36
File Command 7 - Example
Change the name of the test02.log file to test03.log.
Move the statistics file in the mail directory to the current directory.
[root@localhost ~]# ls
audit  passwd.back passwd_link test01.log  test02.log
[root@localhost ~]# mv test02.log test03.log
[root@localhost ~]# mv audit/audit.log ./
[root@localhost ~]# ls
audit  audit.log  passwd.back passwd_link test01.log  test03.log
[root@localhost ~]# ls audit/
audit.log.1
[root@localhost ~]# mv audit/ audit_back
[root@localhost ~]# ls
audit_back audit.log  passwd.back passwd_link test01.log  test03.log
[root@localhost ~]#

Huawei Confidential
37
File Command 8 - rm

The rm command is used to delete a file or directory.

Exercise caution when running this command, as it is not possible to completely restore files
deleted in this manner. As the rm command does not move files to a place from which they
can be restored, such as a "recycle bin", the deletion operation cannot be revoked.

Syntax: rm [OPTION] file_or_dir
-f or --force: ignores the files that do not exist and does not display any message.
-I or --interactive: performs interactive deletion.
-r, -R, or --recursive: instructs rm to recursively delete all directories and subdirectories listed in the 
parameter.
-v or --verbose: displays the detailed procedure.

Huawei Confidential
38
File Command 8 - Example
Delete the test01.log file after obtaining the user's consent.
Forcibly delete the test03.log file.
Delete the mail.bak directory and all files and directories within.
[root@localhost ~]# ls
audit_back audit.log  passwd.back passwd_link test01.log  test03.log
[root@localhost ~]# rm test01.log
rm: remove regular empty file 'test01.log'? yes
[root@localhost ~]# rm -rf test03.log
[root@localhost ~]# rm -rf audit_back/
[root@localhost ~]# ls
audit.log  passwd.back passwd_link
[root@localhost ~]#

Huawei Confidential
39
File Command 9 - cat
The cat command is used to read the entire content of a file, or to combine multiple
files into one.
Syntax: cat [OPTION] [FILE]
-A or --show-all: equivalent to -vET.
-b or --number-nonblank: numbers a non-blank output line.
-E or --show-ends: displays $ at the end of each line.
-n or --number: numbers all output lines. The value starts from 1.

Huawei Confidential
40
File Command 9 - Example
View the content of the test01.log and test02.log files, and combine the content of
both into the test03.log file.
[root@localhost ~]# ls
audit.log  passwd.back passwd_link test01.log  test02.log
[root@localhost ~]# cat test01.log
This is a test!
[root@localhost ~]# cat -b test02.log
1  This is a test too!
[root@localhost ~]# cat test01.log test02.log > test03.log
[root@localhost ~]# cat test03.log
This is a test!
This is a test too!
[root@localhost ~]#

Huawei Confidential
41
File Command 10 - head
The head command is used to display the beginning of a file (the first 10 lines, by
default).
Syntax: head [OPTION] [FILE]
Main options:
-q: hides the file name.
-v: displays the file name.
-c<byte>: displays the number of bytes.

Huawei Confidential
42
File Command 10 - Example
Display the first three lines of the /etc/passwd file.
Display the content of the /etc/passwd file, excluding the last 20 lines.
[root@localhost ~]# head -n 3 /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
[root@localhost ~]# head -n -40 /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
[root@localhost ~]#

Huawei Confidential
43
File Command 11 - tail
The tail command is used to read the tail of a file.
Syntax: tail [OPTION]... [FILE]...
Main options:
-f: reads data cyclically.
-q: does not display processing information.
-v: displays detailed processing information.
-c<number>: displays the number of bytes.
-n<number>: displays the number of lines.

Huawei Confidential
44
File Command 11 - Example
Read the last three lines of the /etc/passwd file and display the output of a ping
operation in real time.
[root@localhost ~]# tail -n 3 /etc/passwd
tcpdump:x:72:72::/:/sbin/nologin
dbus:x:978:978:System Message Bus:/:/usr/sbin/nologin
openeuler:x:1000:1000:openEuler:/home/openeuler:/bin/bash
[root@localhost ~]# ping 192.168.110.245 > ping.log &
[1] 12865
[root@localhost ~]# tail -f ping.log
PING 192.168.110.245 (192.168.110.245) 56(84) bytes of data.
64 bytes from 192.168.110.245: icmp_seq=1 ttl=64 time=0.099 ms
64 bytes from 192.168.110.245: icmp_seq=2 ttl=64 time=0.113 ms
64 bytes from 192.168.110.245: icmp_seq=3 ttl=64 time=0.113 ms
64 bytes from 192.168.110.245: icmp_seq=4 ttl=64 time=0.114 ms
64 bytes from 192.168.110.245: icmp_seq=5 ttl=64 time=0.107 ms
64 bytes from 192.168.110.245: icmp_seq=6 ttl=64 time=0.117 ms
[root@localhost ~]#

Huawei Confidential
45
File Command 12 - more
The more command displays further information, page by page, for users to read.
Basically, you can press the space bar to go to the next page, press b to go back to
the previous page, and search for strings. As more reads files from the front to the
back, the entire file is loaded from the very start.
Syntax: more [OPTION]... [FILE]...
+n: displays the information from the first n lines.
-n: defines the screen size as n lines.
+/pattern: searches for the character string pattern before the file is displayed, and then 
displays the character string from the first two lines.
-c: clears the screen from the top.

Huawei Confidential
46
File Command 12 - Common Operation Commands

You can perform interactive operations when reading file information by running the more command.
Enter: moves to the next n lines. This operation needs to be defined. By default, n is set to 1.
Ctrl+F: scrolls down to the next screen.
Space bar: scrolls down to the next screen.
Ctrl+B: returns to the previous screen.
=: outputs the number of the current line.
V: invokes the vi editor.
! command: invokes and executes a shell.
q: exits the more command.

Huawei Confidential
47
File Command 13 - less

The less command is used to read content and display it on multiple screens. The less
command is similar to the more command. Unlike more, which only moves downwards, less
can move both upwards and downwards and does not load the entire file before displaying
the its content.

Syntax: less [OPTION]... [FILE]...

Common operations:
/Character string: searches downwards for character strings.
?Character string: searches upwards for character strings.
Q: exits the less command.
Space bar: scrolls to the next page.
Enter: scrolls to the next line.

Huawei Confidential
48
File Command 14 - find
The find command is used to search for files in a specified directory.
You can specify search conditions, such as file name, file type, user, and even
timestamp.
Syntax: find [path...] [expression]
-name: searches for files by file name.
-perm: searches for files by file permission.
-user: searches for files by file owner.
-mtime -n +n: searches for files by modification time.

Huawei Confidential
49
File Command 14 - Example (1)
Search for files by file name.
[root@localhost ~]# find /etc -name passwd
/etc/pam.d/passwd
/etc/raddb/mods-enabled/passwd
/etc/raddb/mods-available/passwd
/etc/passwd
[root@localhost ~]# find . -name "*.log"
./test01.log
./ping.log
./test02.log
./test03.log
./audit.log
[root@localhost ~]#

Huawei Confidential
50
File Command 14 - Example (2)

Search the /var/log/anaconda directory for the common files with a modification time earlier
than the last seven days.
[root@localhost ~]# find /var/log/anaconda/ -type f -mtime +7
/var/log/anaconda/dnf.librepo.log
/var/log/anaconda/syslog
/var/log/anaconda/dbus.log
/var/log/anaconda/ks-script-cdcy5u0e.log
/var/log/anaconda/packaging.log
/var/log/anaconda/ifcfg.log
/var/log/anaconda/lvm.log
/var/log/anaconda/program.log
/var/log/anaconda/journal.log
/var/log/anaconda/hawkey.log
/var/log/anaconda/anaconda.log
/var/log/anaconda/storage.log
/var/log/anaconda/X.log
[root@localhost ~]#

Huawei Confidential
54
File Command 15 - gzip

gzip is a command used to compress and decompress files on Linux.

Specifically, gzip can be used to compress large, rarely-used files to save disk space.

Syntax: gzip [option] [file or directory]
-d, --decompress, or ----uncompress: decompresses a package.
-f or --force: forcibly compresses a file, regardless of whether the file name exists or 
whether the file is a symbolic link.
-l or --list: lists information about compressed files.
-r or --recursive: recursively processes all files and subdirectories in a specified directory.
-v or --verbose: displays the command execution process.

Huawei Confidential
55
File Command 15 - Example
Compress, view, and decompress files.
[root@localhost ~]# ls
audit.log    passwd_link test01.log  test03.log
passwd.back ping.log     test02.log
[root@localhost ~]# gzip *.log
[root@localhost ~]# ls
audit.log.gz  passwd_link test01.log.gz  test03.log.gz
passwd.back
ping.log.gz  test02.log.gz
[root@localhost ~]# gzip -l test01.log.gz
compressed        uncompressed  ratio uncompressed_name
45                  16   0.0% test01.log
[root@localhost ~]# gzip -dv test01.log.gz
test01.log.gz:    0.0% -- replaced with test01.log
[root@localhost ~]# ls
audit.log.gz  passwd_link test01.log     test03.log.gz
passwd.back
ping.log.gz  test02.log.gz
[root@localhost ~]#

Huawei Confidential
56
File Command 16 - tar
The tar command is used to pack files. You can pack multiple files into a package to
facilitate data transfers.
Syntax: tar [OPTION...] [FILE]
-c: creates a compressed file.
-x: extracts files from a compressed file.
-t: displays the content of a compressed file.
-z: supports gzip decompression.
-j: supports bzip2 file decompression.
-v: displays the operation process.

Huawei Confidential
57
File Command 16 - Example

Compress files.

Query the files in a package and decompress the package to the specified directory.
[root@localhost ~]# ls
passwd  test01.log  test02.log
[root@localhost ~]# tar -cf log.tar *.log
[root@localhost ~]# tar -zcf log.tar.gz *.log
[root@localhost ~]# ls
log.tar  log.tar.gz  passwd  test01.log  test02.log
[root@localhost ~]# tar -ztvf log.tar.gz
-rw------- root/root         0 2020-07-29 17:47 test01.log
-rw------- root/root         0 2020-07-29 17:47 test02.log
[root@localhost ~]# mkdir log
[root@localhost ~]# tar -zxf log.tar.gz -C ./log/
[root@localhost ~]# ls
log  log.tar  log.tar.gz  passwd  test01.log  test02.log
[root@localhost ~]# ls log
test01.log  test02.log
[root@localhost ~]#

Huawei Confidential
58
File Command 17 - ln (1)
The ln command is used to create a link file.
There are two types of links on Linux: soft link (also known as symbolic link) and
hard link.
Soft Link
Hard Link
A path, similar to a Windows shortcut
A file copy, which does not occupy the 
actual space
A link, which becomes invalid after the 
source file is deleted
A link, which has no impact on the source 
file after being deleted
Linking to a directory is supported
Linking to a directory is not supported
Cross-file system linking is supported
Cross-file system linking is not supported

Huawei Confidential
59
File Command 17 - ln (2)
If the ln command does not contain any option, a hard link is created by default.
Syntax: ln [-f] [-n] [-s] SourceFile [TargetFile]
-b: deletes and overwrites the existing link.
-d: allows the superuser to create hard links to directories.
-f: forcibly executes the command.
-i: indicates the interactive mode. If the file exists, the system prompts you to overwrite it.
-n: regards symbolic links as common directories.
-s: soft link (symbolic link).

Huawei Confidential
60
File Command 17 - Example

Create a link, delete the source file, and restore the source file. Then, check the link status.
[root@localhost ~]# ls
passwd
[root@localhost ~]# ln passwd link_h_password
[root@localhost ~]# ln -s passwd link_s_password
[root@localhost ~]# ls -l
total 8
-rw-------. 2 root root 2546 Jul 29 15:24 link_h_password
lrwxrwxrwx. 1 root root
6 Jul 29 17:41 link_s_password -> passwd
-rw-------. 2 root root 2546 Jul 29 15:24 passwd
[root@localhost ~]# rm -f passwd
[root@localhost ~]# ls -l
total 4
-rw-------. 1 root root 2546 Jul 29 15:24 link_h_password
lrwxrwxrwx. 1 root root
6 Jul 29 17:41 link_s_password -> passwd
[root@localhost ~]# cp /etc/passwd passwd
[root@localhost ~]# ls -l
total 8
-rw-------. 1 root root 2546 Jul 29 15:24 link_h_password
lrwxrwxrwx. 1 root root
6 Jul 29 17:41 link_s_password -> passwd
-rw-------. 1 root root 2546 Jul 29 17:41 passwd
[root@localhost ~]#

Huawei Confidential
61
Contents
1.
Basic Knowledge of Linux Commands
2.
Basic Linux Commands
Login Commands
Power Management Commands
File Management Commands
Help Commands

Huawei Confidential
62
Help Command - man

man is used to view the manual, which is classified into the following nine types:
No.
Description
1
Commands or programs that can be operated by users in the shell
2
Functions and tools that can be invoked by the system kernel
3
Common functions and function libraries
4
Device document description, which is usually in the /dev directory
5
File format and conventions
6
Games
7
Miscellaneous (including macros and conventions)
8
System management commands (applicable only to the root user)
9
Kernel routines (non-standard)

Huawei Confidential
63
Help Command - Example

Search results by chapter number in the manual. For example, enter man sleep, as shown in the left
figure.

By default, only command manuals are displayed. To view library functions, enter man 3 sleep, as
shown in the right figure.

Huawei Confidential
64
Help Command - help

Due to the vast number of commands in the Linux system, it is almost impossible to remember them all. However,
you can run the help command to obtain detailed information.

Syntax:
help [option] [command]

The options are as follows:
-d: displays the brief description of the command.
-s: displays the brief description of the command syntax.

See the following example:
[root@localhost ~]# help pwd
pwd: pwd [-LP]
Print the name of the current working directory.
Options:
-L        print the value of $PWD if it names the current working directory
-P        print the physical directory, without any symbolic links
By default, `pwd' behaves as if `-L' were specified.
Exit Status:
Returns 0 unless an invalid option is given or the current directory cannot be read.

Huawei Confidential
65
Quiz
1.
（True or false）When a user wants to use mv command to overwrite the target
file at the destination after obtaining the his consent, he should add “-i” option
into the command.
A. True
B. False

Huawei Confidential
66
Summary
This document describes the basic operations of the Linux command line,
and the basic commands for logging in to the Linux system, starting and
shutting down the system, and operating files.

Huawei Confidential
67
Acronyms
Acronym
Full Name
Description
POSIX
Portable Operating System Interface
Portable Operating System Interface (POSIX) is the name of a family of related standards 
specified by the IEEE to define the application programming interface (API), along with 
shell and utilities interfaces for software compatible with variants of the Unix operating 
system, although the standard can apply to any operating system.
GNU
GNU's Not Unix
GNU (prononunced GAH-noo with a hard "G") is an ambitious project started by Richard 
Stallman to create a completely free operating system based upon the design of Unix. 
AT&T
American Telephone and Telegraph Co.
It was an American telecommunications company founded in 1877
KDE
K Desktop Environment
One of the popular desktop environments for Linux. Kubuntu uses KDE by default.
ksh
Korn shell
An interactive command interpreter and a command programming language. 2. A 
command interpreter developed for UNIX, which forms the basis for the z/OS shell.
csh
C shell
A command line processor for UNIX that provides interactive features such as job control 
and command history.
GUI
graphical user interface
A visual computer environment that represents programs, files, and options with 
graphical images, such as icons, menus, and dialog boxes, on the screen.
CLI
command-line interface
A means of communication between a program and its user, based solely on textual 
input and output.

Copyright© 2023 Huawei Technologies Co., Ltd.
All Rights Reserved.
The information in this document may contain predictive 
statements including, without limitation, statements regarding 
the future financial and operating results, future product 
portfolio, new technology, etc. There are a number of factors 
that could cause actual results and developments to differ 
materially from those expressed or implied in the predictive 
statements. Therefore, such information is provided for reference 
purpose only and constitutes neither an offer nor an acceptance. 
Huawei may change the information at any time without notice. 
把数字世界带入每个人、每个家庭、
每个组织，构建万物互联的智能世界。
Bring digital to every person, home, and 
organization for a fully connected, 
intelligent world.
Thank you.

Text Editors and Text Processing

Huawei Confidential
2
Foreword
Text processing is a basic OS operation used to manage files. A text editor,
a type of computer software, is mainly used to write and view text files.
Different text editors have different auxiliary functions. This document
describes several common text editors and basic text processing operations.

Huawei Confidential
3
Objectives
After completing this course, you will be familiar with:
Common Linux text editors
Vi and Vim text editor modes
Common and quick Vim operations

Huawei Confidential
4
Contents
1.
Introduction to Common Linux Text Editors
2.
Vim Text Editor
3.
Text Processing

Huawei Confidential
5
Introduction to Linux Text Editors
A text editor is one of the basic pieces of software in an operating system. There are
many types of Linux text editors. Some accompany specific environments and others
can be installed as needed.
Some common Linux text editors are:
Emacs
Nano
gedit
KEDIT
Vi
Vim

Huawei Confidential
6
Linux Text Editor - Emacs
Emacs is more like an operating system than an editor. It comes with a built-in web
browser, IRC client, calculator, and even Tetris. Emacs is used on a Linux GUI.
Advantages:
Customizable and extensible
Powerful functions
Can be integrated with many free software programming tools
Disadvantages:
Difficult to get started for common users

Huawei Confidential
7
Linux Text Editor - Nano

Nano is a simple text editor with a command line interface. Developed to replace the closed-
source Pico text editor, the first version was released, licensed under the GNU General Public
License (GPL), in 1999. This free software is also a part of the GNU Project. Nano has many
user-friendly
features
such
as
syntax
highlighting,
regular
expression
searching
and
replacing, smooth scrolling, multiple buffers, custom shortcut keys, undo, and repeat editing.

Advantages:
Easy to use, very suitable for simple text editing

Disadvantages:
Complex text editing is time-consuming, with no powerful commands available for complex 
operations, for example, no support for macros, editing multiple files at a time, window splitting, 
vertical block/rectangle selection and editing, and automatic completion.

Huawei Confidential
8
Linux Text Editor - gedit

gedit is a text editor in the GNOME desktop environment and is compatible with UTF-8.
gedit
is free software which is easy to use and provides syntax highlighting, multiple
character encodings including GB2312 and GBK, and GUI tabs for editing multiple files. It
also supports a full undo and redo system, searching and replacing, and editing remote files
with the GNOME VFS library.

Advantages:
Easy to use on a GUI, featuring a Windows-like experience, for example, the same 
shortcut keys for operations like copy and paste

Disadvantages:
Requires an installed GUI

Huawei Confidential
9
Linux Text Editor - KEDIT
Similar to gedit in the GNOME environment, KEDIT is a text editor in the K desktop
environment (KDE). It is a small editor, especially suitable for browsing text and
configuration files.
Advantages:
Easy to use on a GUI, featuring a Windows-like experience, for example, the same 
shortcut keys for operations like copy and paste
Disadvantages:
Requires an installed GUI

Huawei Confidential
10
Linux Text Editor - Vi

Vi, the oldest text editor, is a standard Unix text editor and one of the most popular text editors. All
Linux and Unix operating systems have the Vi text editor by default. Although Vi operations are
different from those of other text editors (such as gedit), Vi is still used frequently because it only
needs a character interface and can be used in all Unix and Linux environments.

Three command modes of the Vi editor:
Command
Insert
Visual

Advantages: universal. Almost all Unix and Linux OSs have their own Vi editor.

Disadvantages: lack of advanced function and display options.

Huawei Confidential
11
Linux Text Editor - Vim

Vim is a text editor developed from Vi. Equipped with many convenient programming functions such as
code completion, compilation, and error redirection, Vim is frequently used by programmers, and is
also one of Unix-like system users' favorite editors alongside Emacs.

The first version of Vim was released in 1991 by Bram Moolenaar. The initial name was Vi IMitation.
After it developed more functions, the name was changed to Vi IMproved. It is now free and open-
source software.

Vim has multiple modes:
Basic modes: Normal, Insert, Visual, Select, Command-line, and Ex
Derivative modes: Operator-pending, Insert Normal, Insert Visual, Insert Select, Replace
Others: eVim

After installing openEuler 20.03 LTS, you need to manually install Vim.

Huawei Confidential
13
Contents
1.
Introduction to Common Linux Text Editors
2.
Vim Text Editor
3.
Text Processing

Huawei Confidential
14
Command Syntax of the Vim Editor
Syntax:
Common options:
-c runs a specified command before opening a file.
-R opens a file in read-only mode but allows you to forcibly save the file.
-M opens a file in read-only mode and does not allow you to forcibly save the file.
-r recovers a crashed session.
+num starts at line num.
vim  [options]  [file]...  
Edit specified files.
vim  [options]  -
Read text from standard input (stdin).
vim  [options]  -t  tag   
Edit the file where the tag is defined.
vim  [options]  -q [errorfile] 
Edit the file where the first error occurs.

Huawei Confidential
15
Basic Vim Operations - Opening a File
If the filename file exists, it is opened and its content is displayed.
If the filename file does not exist, Vim displays [New File] at the bottom of the
screen and creates the file when saving the file for the first time.
[root@openEuler ~]# vim  filename
[root@openEuler ~]# vim  test.txt
~
~
~
~
~
"test.txt" [New File]

Huawei Confidential
16
Basic Vim Operations - Moving the Cursor

Cursor control

Arrow keys or k, j, h, and l keys move the cursor up, down, left, and right, respectively.

0 moves the cursor to the beginning of the current line.

g0 moves the cursor to the leftmost character of the current line that is on the screen.

:n moves the cursor to line n.

gg moves the cursor to the first line of the file.

G moves the cursor to the last line of the file.

Data operations

yy or Y copies an entire line of text.

y[n]w copies 1 or n words.

d[n]w deletes (cuts) 1 or n words.

[n] dd deletes (cuts) 1 or n lines.

Huawei Confidential
17
Basic Vim Operations - Data Operations 

Copy

yy or Y copies an entire line of text.

y[n]w copies 1 or n words.

Paste

Line-oriented data:

p places data below the current line.

P places data above the current line.

Character-oriented data:

p places data behind the cursor.

P places data before the cursor.

Deletion

d[n]w deletes (cuts) 1 or n words.

[n] dd deletes (cuts) 1 or n lines.

Huawei Confidential
18
Basic Vim Operations - Displaying and Hiding a Line Number
Displaying a line number
:set nu
Hiding a line number
:set nonu
1  hello
2  openEuler
~
~
~
~
~
:set nu

Huawei Confidential
19
Basic Vim Operations - Finding and Replacing
Find
:/word searches forwards for the word string after the cursor. Press n to match the next 
word string and press N to match the previous word string.
:?word searches backwards for the word string before the cursor. Press n to match the 
next word string and press N to match the previous word string.
Replace
:1,5s/word1/word2/g replaces all occurrences of word1 in lines 1 to 5 with word2. If g is 
not specified, only the first occurrence of word1 in each line is replaced.
%s/word1/word2/gi replaces all occurrences of word1 with word2. i indicates case-
insensitive matches.

Huawei Confidential
20
Basic Vim Operations - Highlighting Search Results

Run the following command in Command mode for a temporary setting
:set hlsearch

Add set hlsearch to the /etc/vimrc file and update variables for a permanent setting
hello
openEuler
hello
world 
~
~
:set nu
hello
hello

Huawei Confidential
21
Basic Vim Operations - Modifying a File

After you run the vim filename command to open a file, the system enters Normal mode. To
modify the file, press i to enter Insert mode. The system displays a message at the bottom,
indicating that the current mode is Insert. You can press ecs to exit Insert mode and return
to Normal mode.
[root@openEuler ~]# vim  test.txt
# Press i to enter Insert mode.
~
~
~
~
~
~
~
-- INSERT --

Huawei Confidential
22
Basic Vim Operations - Undoing or Redoing
u undoes the latest change.
U undoes all changes on the current line since the cursor has been positioned on the
line.
Ctrl+R redoes the last undo operation.

Huawei Confidential
23
Basic Vim Operations - Saving a File and Exiting
Exit Insert mode:
Press ecs to exit Insert mode.
The involved commands are as follows:
:w saves a file.
:q exits the editor.
:wq! saves a file and exits the editor.
:q! forcibly exits the editor.
:wq! forcibly saves a file and exits the editor.

Huawei Confidential
24
Contents
1.
Introduction to Common Linux Text Editors
2.
Vim Text Editor
3.
Text Processing

Huawei Confidential
25
Viewing a File - cat (1)

cat is a tool for viewing and connecting text files. It has the following functions:
cat filename displays file content.
cat > filename edits a file.
cat file1 file2 > file3 combines several files into one.

Main options:
-n numbers all lines starting from 1 and displays the number at the beginning of each line.
-b numbers non-empty lines starting from 1 and displays the number at the beginning of each line.
-s outputs only one blank line when multiple blank lines exist.
-E adds $ at the end of each line.
--help displays the help information.

Huawei Confidential
26
Viewing a File - cat (2)
Example
[root@openEuler ~]# cat /etc/profile
# View the /etc/profile file content.
[root@openEuler ~]# cat -b /etc/profile
# View the /etc/profile file content and number non-blank lines 
starting from 1.
[root@openEuler ~]# cat -n /etc/profile
# View the /etc/profile file content and display the line number 
at the beginning of each line.
[root@openEuler ~]# cat -E /etc/profile
# View the /etc/profile file content and add $ at the end of 
each line.
[root@openEuler ~]# cat -s /etc/profile
# View the /etc/profile file content. If multiple blank lines exist, 
only one is displayed.

Huawei Confidential
27
Viewing a File - more (1)
more can be used to view one file at a time or a standard input page. Unlike cat,
more can be used to view the file content by page or to directly jump to another
line.
Command syntax: more [options] <file>...
Common options:
+n displays from the nth line.
-n defines the screen size to n lines.
-c clears a screen from the top and displays information.
-s displays multiple consecutive blank lines in one line.

Huawei Confidential
28
Viewing a File - more (2)
Common operations:
Enter scrolls down one line by default.
Ctrl+F scrolls down to the next page.
Space key scrolls down to the next page.
Ctrl+B scrolls up one page.
b scrolls up one page.
=outputs the current line number.
:f outputs file name and current line number.
q exits more.

Huawei Confidential
29
Viewing a File - less (1)

less can be used to view one file at a time or a standard input page, and is a more flexible command
than more.

Command syntax: less [option] file

Common options:
-f forcibly opens a special file, such as peripheral device code, directory, or binary file.
-g specifies only the last found keyword.
-i ignores case sensitivity during search.
-N displays the line number of each line.
-s outputs only one blank line when multiple blank lines exist.
-o <file name> saves the less output to a specified file.

Huawei Confidential
30
Viewing a File - less (2)

Main operations:
b turns to the previous page.
d turns to the next half page.
h displays the help information.
q exits less.
u turns to the previous half page.
y turns to the previous line.
Space key turns to the next line.
Enter turns to the next page.
Up or down arrow key: turns to the previous or next line, respectively.

Huawei Confidential
31
Extracting a File - head
head is used to display the beginning of a file to the standard output. By default, the
first 10 lines of a file are displayed.
Command syntax: head [option]... [file]...
Common options:
-q hides a file name during output. By default, the file name is not displayed.
-v displays a file name during output.
-c num displays the first num bytes.
-n num displays the first num lines.

Huawei Confidential
32
Extracting a File - tail
tail is used to display the end of a file to the standard output. By default, the last 10
lines of a file are displayed.
Command syntax: tail [option]... [file]...
Common options:
-f reads log files cyclically for log management
-q hides a file name. File names are not displayed by default.
-v displays a file name.
-c num displays the last num bytes of a file.
-n num displays the last num lines of a file.

Huawei Confidential
33
Extracting a Column or Field - cut
cut is used to display a specific column of a file or standard input. For example:
Command syntax: cut [option]... [file]
Common options:
-b [range] displays only the content within the specified range in a line.
-c [range] displays only characters within the specified range in a line.
-d specifies a field separator. The default field separator is TAB.
-f [range] displays the content of the specified numth field. Multiple fields can be 
separated by commas (,).
[root@openEuler ~]# cut  -d: -f1 /etc/passwd
# Display the first column of the /etc/passwd file separated 
by colons (:).

Huawei Confidential
34
Extracting a Column or Field - awk
awk is a powerful text analysis tool. It reads files or standard input by line, uses
spaces as the default separator to slice each line, and performs analysis on each
slice.
Command syntax: awk action filename, for example, awk '{print $0}' test.txt
[root@openEuler ~]# last -n 5 | awk '{print $1}' # Display the last five accounts that have logged in to the 
system.

Huawei Confidential
35
Extracting Keywords - grep

grep is a powerful text search tool that uses regular expressions to search for text in one or more files, and then
print matched lines. To find a pattern more than one word long, enclose the text string with single or double
quotation marks, otherwise search terms after the first word will be misinterpreted as file names to search in. The
search result is sent to standard output, leaving the original file(s) unaltered.

Command syntax: grep [option] [file]...

Common options:
-c prints a count of matching lines.
-i ignores case sensitivity.
-w prints whole word matches.
-x prints only results matching the whole line.

Huawei Confidential
36
Text Statistics - wc

wc is used to calculate the number of words, bytes, or columns of a file. If the file name is
not specified or the given file name is -, wc reads data from the standard input device.

Command syntax: wc [option]... [file]...

Common options:
-c, --bytes, or --chars displays only the number of bytes.
-l or --lines displays only the number of lines.
-w or --words displays only the number of words.

Huawei Confidential
37
Text Sorting - sort

sort is used to sort files and output the sorting result in standard mode. You can use sort to obtain input from a
specific file or standard input (stdin).

Command syntax: sort [option]... [file]...

Common options:
-b ignores the space character at the beginning of each line.
-c checks whether files are sorted in sequence.
-d processes only letters, digits, and spaces during sorting.
-f regards lowercase letters as uppercase letters during sorting.
-n sorts by value.
-r sorts in reverse order.
-o <file> saves the sorted result to a specified file.
-u ignores repeated lines.

Huawei Confidential
38
Text Comparison - diff

diff compares the similarities and differences between text files line by line. If a directory is
specified, diff compares files with the same file name in the directory but does not compare
subdirectories.

Command syntax: diff [option]... file

Common options:
-B does not check blank lines.
-c displays all content and marks the differences.
-i ignores case differences.
-r compares files in subdirectories.
-w ignores all space characters.

Huawei Confidential
39
Text Operating Tool - tr

tr reads data from a standard input device, converts character strings, and outputs the result to the standard output
device. It is used to convert or delete characters in a file.

Command syntax: tr [option]... set1 [set2]

Main options:
-c inverts the selection of characters. That is, characters that meet set1 are not processed, and the remaining 
characters are converted.
-d deletes characters.
-s reduces consecutive repeated characters to a specified single character.
-t reduces the specified range of set1 to the length of set2.
[root@openEuler ~]# cat text.txt | tr a-z A-Z
# Convert lowercase letters to uppercase letters.

Huawei Confidential
40
Text Operating Tool - sed

sed, a streamlined, noninteractive editor, can edit standard input and text from files. Compared with tr (which performs character-
based transformation), sed can modify character strings. When a command is executed, sed reads a line from the file or standard
input and copies it to buffers. sed continues to read each next line until all lines have been edited. As such, sed only changes the
copied text stored in buffers. To edit the original file directly, use the -i option. You can also redirect results to a new file.

Command syntax: sed [option]... [option] {script-only-if-no-other-script} [input-file]...

Common options:

-n cancels the default output.

-e specifies multipoint editing. Multiple subcommands can be executed.

-f reads commands from a script file.

-i directly edits the original file.

-l specifies the line length.

-r uses an extended expression in a script.

Huawei Confidential
41
Quiz
1.
(Single-answer)How many lines of a file are displayed by default when using the
head command ?
A. 5
B. 10
C. 15
D. 20

Huawei Confidential
42
Summary
This document describes the development of the Linux OS and introduces
the openEuler OS, as well as its installation methods and shortcut
operations.

Huawei Confidential
43
More Information
For more information about Linux shortcut keys, visit
https://linuxtoy.org/archives/bash-shortcuts.html.

Huawei Confidential
44
Acronyms
Acronym
Full Name
Description
POSIX
Portable Operating System Interface
Portable Operating System Interface (POSIX) is the name of a family of related standards 
specified by the IEEE to define the application programming interface (API), along with 
shell and utilities interfaces for software compatible with variants of the Unix operating 
system, although the standard can apply to any operating system.
GNU
GNU's Not Unix
GNU (prononunced GAH-noo with a hard "G") is an ambitious project started by Richard 
Stallman to create a completely free operating system based upon the design of Unix. 
AT&T
American Telephone and Telegraph Co.
It was an American telecommunications company founded in 1877
KDE
K Desktop Environment
One of the popular desktop environments for Linux. Kubuntu uses KDE by default.
ksh
Korn shell
An interactive command interpreter and a command programming language. 2. A 
command interpreter developed for UNIX, which forms the basis for the z/OS shell.
csh
C shell
A command line processor for UNIX that provides interactive features such as job control 
and command history.
GUI
graphical user interface
A visual computer environment that represents programs, files, and options with 
graphical images, such as icons, menus, and dialog boxes, on the screen.
CLI
command-line interface
A means of communication between a program and its user, based solely on textual 
input and output.

Copyright© 2023 Huawei Technologies Co., Ltd.
All Rights Reserved.
The information in this document may contain predictive 
statements including, without limitation, statements regarding 
the future financial and operating results, future product 
portfolio, new technology, etc. There are a number of factors 
that could cause actual results and developments to differ 
materially from those expressed or implied in the predictive 
statements. Therefore, such information is provided for reference 
purpose only and constitutes neither an offer nor an acceptance. 
Huawei may change the information at any time without notice. 
把数字世界带入每个人、每个家庭、
每个组织，构建万物互联的智能世界。
Bring digital to every person, home, and 
organization for a fully connected, 
intelligent world.
Thank you.

User and Permission Management

Huawei Confidential
2
Foreword
This document describes user and permission management on openEuler.
After learning this document, you will understand the basic concepts of users
and user groups on openEuler, and be familiar with commands for creating,
deleting, and modifying files and directories. You will also learn about file
permission configuration and specific operation commands.

Huawei Confidential
3
Objectives

After completing this course, you will understand:
Basic concepts about users and user groups
Command line operations related to files and directories
File permission configuration and related command operations
Special control methods for file access

Huawei Confidential
4
Contents
1.
User and User Group Management

Basic Concepts About Users

User Management Commands

Basic Concepts About User Groups

User Group Management Commands

Files Associated with Users and User Groups
2.
File Permission Management
3.
Other Permission Management

Huawei Confidential
5
Basic Concepts About Users
Linux is a multi-user operating system.
All users who wish to use system resources must apply for an account from a system administrator, and then 
use it to log in. 
Multiple users can be created on the system, and can log in to the same system at the same time to perform 
different tasks without affecting each other.
User
A user can be viewed as a set of permissions to obtain system resources.
Each user is assigned a unique user ID (UID).

Huawei Confidential
6
UID
UID is a unique user identification that can also identify the user type. When a user
logs in to a system, the UID (not the user name) is used to identify the user type.

Superuser: also called a root user whose UID is 0. A superuser has full control over a system, and can modify
and delete files, as well as running commands. As such, exercise caution when delegating the root user.

Common user: also called a normal or regular user whose UID ranges from 1000 to 60000. Common users can
access and modify files in their own directories, and access authorized files.

Virtual user: also called a system user whose UID ranges from 1 to 999. Virtual users can log in to a system
without passwords, facilitating system management.

Huawei Confidential
7
Distinguishing User Types
You can determine whether a user is the superuser, a common user, or a virtual user
by viewing the UID.

Run the id [option] [user_name] command to view a UID.

Main options:

-u, -user: displays only a valid UID.

-n, -name: displays a name instead of a number for -ugG.

-r, -real: displays a real ID instead of a valid ID for -ugG.
UID 0 indicates the superuser (root user). UIDs from 1000 to 60000 indicate common users.
UIDs from 1 to 999 indicate virtual users (system users).

Huawei Confidential
8
Contents
1.
User and User Group Management

Basic Concepts About Users

User Management Commands

Basic Concepts About User Groups

User Group Management Commands

Files Associated with Users and User Groups
2.
File Permission Management
3.
Other Permission Management

Huawei Confidential
9
Managing Users
On Linux, each common user has an account containing information such as a user
name, password, and home directory. In addition, there are some special users
created by the system. The most important user has the administrator account, and
is the superuser root by default.
Users can run commands to create, modify, and delete user files, as well as
changing passwords.

Huawei Confidential
10
Creating a User - useradd
The useradd command is used to create a user account and save it in the
/etc/passwd file.
Syntax: useradd [options] user_name
Main options:
-u specifies the user's UID.
-o is used together with -u to allow duplicate UIDs.
-g specifies a basic group to which the user belongs. It can be a user group name or a group ID (GID) if the
group exists.
-d specifies the home directory for the user and automatically creates the home directory.
-s specifies the default shell program of a user.
-D displays or changes the default configuration.

Huawei Confidential
11
Creating a User - Example
Create a user named user.

The command is useradd user.

Run the cat /etc/passwd command to check whether a user has been successfully created. The
command output shows that the user has been created.
[root@localhost ~]# useradd user
[root@localhost ~]# cat /etc/passwd
dbus:x:980:980:System Message Bus:/:/usr/sbin/nologin
test:x:1000:1000::/home/test:/bin/bash
test02:x:1001:1001::/home/test02:/bin/bash
user:x:1002:1004::/home/user:/bin/bash

Huawei Confidential
12
Modifying a User - usermod
The usermod command is used to modify the information about a user account.
Syntax: usermod [options] user_name
Main options:
-u modifies the user's UID.
-g modifies the user group to which the user belongs.
-I modifies the user account name.
-d modifies the user's home directory.
-s modifies the user's default shell program.

Huawei Confidential
13
Modifying a User - Example
Modify a user named user:

Run the id user command to view the user's UID before modification.

Run the usermod -u 1003 user command to modify the UID to 1003. The command output shows that the UID
has been modified.
[root@localhost ~]# id user
uid=1002(user) gid=1004(user) groups=1004(user)
[root@localhost ~]# usermod -u 1003 user
[root@localhost ~]# id user
uid=1003(user) gid=1004(user) groups=1004(user)

Huawei Confidential
14
Deleting a User - userdel
The userdel command is used to delete a specified user and related files.
Syntax: userdel [options] user_name
Main options:
-f forcibly deletes a user account even if the user is logged in.
-r deletes a user and all related files.
-h displays the help information about a command.
(Using the userdel command to delete a specified user and user-related files modifies the user account system
files.)

Huawei Confidential
15
Deleting a User - Example
Delete a test user:

Run the cat /etc/passwd command to view a user before deletion.

Run the userdel user command to delete a test user. The command output shows that the user has been
deleted.
[root@localhost ~]# cat /etc/passwd
dbus:x:980:980:System Message Bus:/:/usr/sbin/nologin
test:x:1000:1000::/home/test:/bin/bash
test02:x:1001:1001::/home/test02:/bin/bash
user:x:1002:1004::/home/user:/bin/bash
[root@localhost ~]# userdel user
[root@localhost ~]# cat /etc/passwd
dbus:x:980:980:System Message Bus:/:/usr/sbin/nologin
test:x:1000:1000::/home/test:/bin/bash
test02:x:1001:1001::/home/test02:/bin/bash

Huawei Confidential
16
Changing a User Password - passwd
The passwd command is used to change a user password.
Syntax: passwd [OPTION...] user_name
Main options:
-n sets the minimum number of days between password change.
-x sets the maximum number of days between password change.
-w sets the number of days of warning before password expires.
-i sets the number of days before an account is disabled once a password expires.
-d deletes the user password.
-S displays the user password information.
(The root user can change any user's password. Common users can change only their own passwords.)

Huawei Confidential
17
Changing a User Password - Example

Change the password of a test user:

Run the /etc/shadow command to check the user password before the change. The output shows that the password has not set
and is displayed as !.

Run the passwd user command to change the user password.

Run the /etc/shadow command again to check whether the password has been changed successfully. The command output
shows that the password has been changed successfully.
[root@localhost ~]# cat /etc/shadow
user:!:18421:0:99999:7:::
[root@localhost ~]# passwd user
Changing password for user user.
New password:
Retype new password:
passwd: all authentication tokens updated successfully.
[root@localhost ~]# cat /etc/shadow
user:$6$KOrFTTStwbMS0eIG$3peFd8yIgxPyaSYi8TG8XFNUdYUdeMd60lR2hvRC6zx3dAdbEqQcnQuDoWT7ocu3Ss.zzWSrEb6
cZ6Ae6b2EN/:18421:0:99999:7:::

Huawei Confidential
18
Contents
1.
User and User Group Management

Basic Concepts About Users

User Management Commands

Basic Concepts About User Groups

User Group Management Commands

Files Associated with Users and User Groups
2.
File Permission Management
3.
Other Permission Management

Huawei Confidential
19
Basic Concepts About User Groups
User group:
A user group is a logical set of users with the same features. These users in one group can have the same 
permissions, which facilitates management.
Each user has a private group.
All users in the same group can share files in the group.
Each user group is assigned a unique group ID (GID).

Huawei Confidential
20
GID
A GID is similar to a UID, and is a unique identifier of a user group in a system.

When an account is added, a group with the same name as the user is created by default. The UID and GID are
the same.

UID 0 is assigned to the superuser and GID 0 is assigned to a user group that has the superuser (that is, the
root user group).

The system reserves some small GIDs for virtual users (also called system users).
You can run the id [option] [user_name] command to view the GID and the number
of users in a group.

Huawei Confidential
21
User Group Classification

Common user group: Multiple users can be added to a common us
