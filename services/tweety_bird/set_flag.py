from pwn import *
from random import randint
import sys

def set_flag(host, port, flag):
	flag_id = genFlagID()
	password = genPasswd()
	c = remote(host,port)
	c.recvline()
   	c.recvline()
   	c.recvline()
   	c.sendline("W")
	c.recvline()
	c.recvline()
   	c.sendline(str(flag_id) + " " + str(password) + " " + str(flag) + "\n")
   	c.close()
	return {"flag_id": flag_id, "token": password}
	
def genFlagID():
	flag_id = randint(0,999999999)
	return flag_id
	
def genPasswd():
	password = randint(100,10000)
	return password
	
if __name__ == "__main__":
	params = sys.argv[1]
	params = params.split(' ')
	print set_flag(params[0], int(params[1]), params[2])
