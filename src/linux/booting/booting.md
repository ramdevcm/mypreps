# Booting Process of Linux System

![Booting Process](booting.drawio.svg)



***GRUB***
    - loads configurations form /boot/grub2/grub.cfg
    - displays a menu to select kernel to boot
    - loads vmlinuz
        - extract initramfs

***KERNEL***
    - Kernal intitalize all hardware that are found as driver in initramfs

***/sbin.init***
    - PID = 1
    - systemd PID = 0
    