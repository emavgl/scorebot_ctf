from pwn import *
from random import randint
import sys

context.log_level = 'error'

def get_flag(host, port, flag_id, token):
	c = remote(host,port)
	c.recvline()
   	c.recvline()
   	c.recvline()
   	c.sendline("R")
	c.recvline()
   	c.sendline(str(flag_id) + " " + str(token) + "\n")
	data = c.recvline()
   	data = data[14:].strip()
	c.close()
	return data

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

