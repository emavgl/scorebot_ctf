import sys, re
from lxml import html
import requests

def get_flag(host, port, flag_id, token):
    flagURL = "userName=%s&userPassword=%s" % (flag_id, token)
    url = "http://%s:%s/viewFile.php?%s" % (host, port, flagURL)
    viewfile_resp = requests.get(url)
    return viewfile_resp.text

def set_flag(host,port,flag):
    payload = {"text": flag}
    url = "http://%s:%s/uploadFile.php" % (host, port)
    upload_resp = requests.get(url, params=payload)
    fid = re.findall(r'(Username: .*)', upload_resp.content)
    tkn = re.findall(r'(Password: .*)', upload_resp.content)
    flag_id = fid[0][10:]
    token = tkn[0][10:]
    return {"flag_id": flag_id[:-4], "token": token[:-4]}
