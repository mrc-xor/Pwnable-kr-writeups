from pwn import *

con = ssh(user="random",host="pwnable.kr",port=2222,password="guest")
proc = con.process("/home/random/random")
proc.sendline(b"2708864985")
proc.recv()
flag = proc.recv().decode()
log.info(f"Flag: {flag}")
