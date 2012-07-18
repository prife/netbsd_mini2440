#!/bin/bash
rm -rf netbsd

cp /usr/src/sys/arch/evbarm/compile/MY_2440/netbsd netbsd

/usr/src/obj/tooldir.Linux-3.2.0-26-generic-pae-i686/bin/arm--netbsdelf-mdsetimage -v -s netbsd disk

/usr/src/obj/tooldir.Linux-3.2.0-26-generic-pae-i686/bin/arm--netbsdelf-objcopy -S -O binary netbsd netbsd.bin

rm -rf ~/tftp/netbsd
cp netbsd.bin ~/tftp/netbsd
rm -rf netbsd.bin netbsd
