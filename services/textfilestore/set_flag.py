import sys, re
from lxml import html
import requests

def set_flag(host,port,flag):
    payload = {"text": flag}
    url = 'http://'+host+':'+port+'/uploadFile.php'
    upload_resp = requests.get(url, params=payload)
    fid=re.findall(r'(Username: .*)', upload_resp.content)
    tkn=re.findall(r'(Password: .*)', upload_resp.content)
    flag_id = fid[0][10:]
    token = tkn[0][10:]
    return {"flag_id": flag_id[:-4],"token": token[:-4]}

if __name__ == "__main__":
	params = sys.argv[1]
	params = params.split(" ")
	print set_flag(params[0],params[1],params[2])
