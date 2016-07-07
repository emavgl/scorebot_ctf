import sys, re
from lxml import html
import requests

def get_flag(host,port,flag_id,token):
    flagURL = "userName="+flag_id+"&userPassword="+token
    viewfile_resp = requests.get('http://'+host+':'+port+'/viewFile.php?'+flagURL)
    return (viewfile_resp.text)

if __name__ == "__main__":
    params = sys.argv[1]
    params = params.split(" ")
    print get_flag(params[0],params[1],params[2],params[3])
