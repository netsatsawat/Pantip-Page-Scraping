# -*- coding: utf-8 -*-
####################################################################################
# Name: PT_getTag
# Description: Get pantip tags from API
# Version:
#   2016/11/11 RS: Initial version
#   2016/12/08 SN: Organize the code, add functions to standardize the program
####################################################################################

from urllib.request import urlopen
import json
import pandas as pd
import urllib.request
import datetime
import time

# Utility to read the URL - out as full str
def read_url(url):
    req = urllib.request.Request(url)
    req_ind = False
    attempt = 0
    while req_ind is False:
        attempt+=1
        try:
            resp = urlopen(req)
            if resp.getcode() == 200: #HTTP success code - doesn't mean the page is empty though
                req_ind = True
                html_resp = resp.read().decode('utf-8')
                print("{}: Successfully connecting and reading the assigned URL".format(datetime.datetime.now()))
        except Exception:
            print("{}: Error connecting to the URL {}".format(datetime.datetime.now(), url))
            if attempt == 10: # End
                break
            time.sleep(5) #Wait 5 seconds for retry
        return html_resp

# Utility to read json convert to panda dataframe
def json_to_df(txt):
    data = json.loads(txt)
    data_df = pd.DataFrame(data)
    return data_df


pt_url = "https://service.pantip.com/api/get_all_tags?access_token=<INSERT TOKEN HERE>"
tmp = read_url(pt_url)
data = json_to_df(tmp)
print(data.head(2))

#data.to_csv('tag_mapping.csv', encoding='utf-8', index=False)
