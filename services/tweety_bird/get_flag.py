from pwn import *
from random import randint
import sys

def get_flag(host,port,flag_id,token):
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

if __name__ == '__main__':
	params = sys.argv[1]
	params = params.split(' ')
	print get_flag(params[0], int(params[1]), params[2], params[3])
