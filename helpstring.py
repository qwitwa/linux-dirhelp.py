helpstring = """
$HOME
This is your home directory, it is your user space where you keep your personal files and other settings specific to you. In Unix, a user will be automatically placed into their home directory upon login. The ~user shorthand variable refers to a user's home directory (allowing the user to navigate to it from anywhere else in the filesystem, or use it in other Unix commands). The ~ (tilde character) shorthand command refers to that particular user's home directory.
/
Primary hierarchy root and root directory of the entire file system hierarchy.
/bin
Essential command binaries that need to be available in single user mode; for all users, e.g., cat, ls, cp.
/boot
Boot loader files, e.g., kernels, initrd.
/dev
Essential devices, e.g., /dev/null.
/etc
Host-specific system-wide configuration files. There has been controversy over the meaning of the name itself. In early versions of the UNIX Implementation Document from Bell labs, /etc is referred to as the etcetera directory, as this directory historically held everything that did not belong elsewhere (however, the FHS restricts /etc to static configuration files and may not contain binaries). Since the publication of early documentation, the directory name has been re-designated in various ways. Recent interpretations include backronyms such as "Editable Text Configuration" or "Extended Tool Chest".
/etc/opt
Configuration files for /opt/.
/etc/sgml
Configuration files for SGML.
/etc/skel
When a new user account is created, files from this directory are usually copied into the user's home directory.
/etc/X11
Configuration files for the X Window System, version 11.
/etc/xml
Configuration files for XML.
/home
Users' home directories, containing saved files, personal settings, etc.
/lib
Libraries essential for the binaries in /bin/ and /sbin/. This directory should hold those shared libraries that are necessary to boot the system and to run the commands in the root file system.
/media
Mount points for removable media such as CD-ROMs and USB sticks.
/mnt
Temporarily mounted filesystems.
/opt
Optional application software packages.
/proc
Virtual filesystem providing information about processes and kernel information as files. In Linux, corresponds to a procfs mount.
/root
Home directory for the root user.
/sbin
Essential system binaries, e.g., init, ip, mount. Like /bin, this directory holds commands needed to boot the system, but which are usually not executed by normal users.
/srv
Site-specific data which are served by the system.
/tmp
Temporary files (see also /var/tmp). Often not preserved between system reboots.
/usr
Secondary hierarchy for read-only user data; contains the majority of (multi-)user utilities and applications.
/usr/bin
Non-essential command binaries (not needed in single user mode); for all users.
/usr/bin/X11
The traditional place to look for X11 executables; on Linux, it usually is a symbolic link to /usr/X11R6/bin.
/usr/dict
Replaced by /usr/share/dict.
/usr/doc
Replace by /usr/share/doc.
/usr/etc
Site-wide configuration files to be shared between several machines may be stored in this directory.  However, commands should always reference those files using the /etc directory.  Links from files in /etc should point to the appropriate files in usr/etc.
/usr/include
Standard include files for the C compiler.
/usr/include/X11
Include files for the C compiler and the X-Window system.  This is usually a symbolic link to /usr/X11R6/include/X11.
/usr/include/asm
Include files which declare some assembler functions.  This used to be a symbolic link to /usr/src/linux/include/asm.
/usr/include/linux
This contains information which may change from system release to system release and used to be a symbolic link to /usr/src/linux/include/linux to get at operating system specific information.
/usr/include/g++
Include files to use with the GNU C++ compiler.
/usr/lib
Libraries for the binaries in /usr/bin/ and /usr/sbin/.
/usr/lib/X11
The usual place for data files associated with X programs, and configuration files for the X system itself.  On Linux, it usually is a symbolic link to /usr/X11R6/lib/X11.
/usr/lib/gcc-lib
contains executables and include files for the GNU C compiler, gcc
/usr/lib/groff
Files for the GNU groff document formatting system.
/usr/local
Tertiary hierarchy for local data, specific to this host. Typically has further subdirectories, e.g., bin/, lib/, share/.
/usr/local/bin
Binaries for programs local to the site.
/usr/local/doc
Local documentation.
/usr/local/etc
Configuration files associated with locally installed programs.
/usr/local/games
Binaries for locally installed games.
/usr/local/lib
Files associated with locally installed programs.
/usr/local/include
Header files for the local C compiler.
/usr/local/info
Info pages associated with locally installed programs.
/usr/local/man
Man pages associated with locally installed programs.
/usr/local/sbin
Locally installed programs for system administration.
/usr/local/share
Local application data that can be shared among different architectures of the same OS.
/usr/local/src
Source code for locally installed software.
/usr/man
Replaced by /usr/share/man
/usr/sbin
Non-essential system binaries, e.g., daemons for various network-services.
/usr/share
Architecture-independent (shared) data. This directory contains subdirectories with specific application data, that can be shared among different architectures of the same OS.  Often one finds stuff here  that  used  to live in /usr/doc or /usr/lib or /usr/man.
/usr/share/dict
Contains the word lists used by spell checkers.
/usr/share/doc
Documentation about installed programs.
/usr/share/games
Static data files for game in /usr/games
/usr/share/info
Info pages go here.
/usr/share/locale
Locale information goes here.
/usr/share/man
Manual pages go here in subdirectories according to the man page sections.
/usr/share/misc
Miscellaenous data that can be shared among different architectures of the same OS.
/usr/share/nls
The message catalogs for native language support go here.
/usr/share/sgml
Files for SGML and XML.
/usr/share/terminfo
The database for terminfo
/usr/share/tmac
Troff macros that are not distributed with groff.
/usr/share/zoneinfo
Files for timezone information.
/usr/src
Source code, e.g., the kernel source code with its header files.
/usr/src/linux
This was the traditional place for the kernel source.  Some distributions put here the source for the default kernel they ship.  You should probably use another directory when building your own kernel.
/usr/tmp
Obsolete.   This should be a link to /var/tmp.  This link is present only for compatibility reasons and shouldn't be used.
/usr/X11R6
X Window System, Version 11, Release 6.
/usr/X11R6/bin
Binaries which belong to the X-Window system; often, there is a symbolic link from the more traditional /usr/bin/X11 to here.
/usr/X11R6/lib
Data files associated with the X-Window system.
/usr/X11R6/lib/X11
These contain miscellaneous files needed to run X; Often, there is a symbolic link from /usr/lib/X11 to this directory.
/usr/X11R6/include/X11
Contains include files needed for compiling programs using the X11 window system. Often, there is a symbolic link from /usr/include/X11 to this directory.
/var
Variable files—files whose content is expected to continually change during normal operation of the system—such as logs, spool files, and temporary e-mail files.
/var/cache
Application cache data. Such data are locally generated as a result of time-consuming I/O or calculation. The application must be able to regenerate or restore the data. The cached files can be deleted without loss of data.
/var/lib
State information. Persistent data modified by programs as they run, e.g., databases, packaging system metadata, etc.
/var/lock
Lock files. Files keeping track of resources currently in use.
/var/log
Log files. Various logs.
/var/opt
Variable data for /opt
/var/mail
Users' mailboxes.
/var/run
Information about the running system since last boot, e.g., currently logged-in users and running daemons.
/var/spool
Spool for tasks waiting to be processed, e.g., print queues and unread mail.
/var/spool/at
Spooled jobs for at.
/var/spool/cron
Spooled jobs for cron.
/var/spool/lpd
Spooled filed for printing.
/var/spool/mail
Deprecated location for users' mailboxes.
/var/spool/mqueue
Queued outgoing mail
/var/spool/news
Spool directory for news
/var/spool/uucp
Spooled files for uucp
/var/tmp
Temporary files to be preserved between reboots.
/var/yp
Database files for NIS
"""

