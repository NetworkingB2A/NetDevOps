
# Create virtual environment and activate environment
```
python3 -m venv venv
source ./venv/bin/activate
```
# pip install requirements
`pip install -r requirements.txt`
OR
`pip install requests`



# Below is the script that will authenticate to DNAC and get a device list.

```python
#import all modules required into script
from requests.auth import HTTPBasicAuth
import requests
import urllib3

""" 
ignore insecure warnings. 
This is purely to make the output to screen look nicer. (probably shouldn't do in production.)
Also in my code I said verify=False. This means I will not check the certs in being used. Again, I shouldn't be doing this in production.
"""
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

""" 
Function to make post request and get Auth token. 
The output of this code will be used many times in your script. 
Putting as a function will allow me to reuse whenever I want to.
"""
def get_auth_token(base_url, dnac_user, dnac_password, ssl_verify=False):
    url = f'{base_url}/dna/system/api/v1/auth/token'
    resp = requests.post(url, auth=HTTPBasicAuth(dnac_user, dnac_password), verify=ssl_verify)
    token = resp.json()['Token']
    return token

"""
Basic get API to get a list of devices in DNAC.
"""
def get_device_list(base_url, auth_token, ssl_verify=False):
    url = f'{base_url}/dna/intent/api/v1/network-device'
    response = requests.get(url, headers={'X-Auth-Token':auth_token}, verify=ssl_verify)
    print(response)
    if response.status_code == 200:
        return response.json()

"""
This is where I bring all the functions together to create the actual script. 
"""
def main():   
    dnac_url = 'https://sandboxdnac.cisco.com'
    user = 'devnetuser'
    super_cool_password = 'Cisco123!'
    token_getter = get_auth_token(dnac_url, user, super_cool_password)
    device_list = get_device_list(dnac_url, token_getter)
    print(device_list)

"""

This is the part that runs the actual script. It's a nice to have. This gives me the ability (if I wanted to) to grab the above functions and use in a different script, without running the main function.

"""
if __name__ == '__main__':
    main()

```