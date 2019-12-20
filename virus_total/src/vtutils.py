import os
import sys
import requests

def is_valid_apikey(apikey):
    """
    Check an api key is whether valid or not.

    -----
    Note: this function simply returns False for an api key that is invalid or reached limit on Virus Total.

    -----------
    Parameters:
        apikey (str): Virus Total api key.

    --------
    Returns:
        boolean: True if apikey is valid. Otherwise, returns False.

    """
    
    # Url of Virus Total.
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    # MD5 checksum of procexp64.exe (a tool of sysinternal suit of Microsoft).
    md5 = '119339E9229720B6E9294D1B52A6BCD8'
    params = { 'apikey': apikey, 'resource': md5 }
    
    # Submit MD5 checksum to Virus Total.
    response = requests.get(url, params=params)

    # If received code is 200 (OK), return True.
    if response.status_code == requests.codes.ok:
        return True
    
    return False
