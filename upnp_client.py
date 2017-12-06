from upnp import *

def main():
	client = upnp()
	print "Entering main"	
	myip = '' #should be localhost
	myport = 0
        
	#Have to create a new socket since replies will be sent directly to our IP, not the multicast IP
	server = client.createNewListener(myip,myport)
	if server == False:
		print 'Failed to bind port %d' % myport
		return
	server.settimeout(2)
	type = 0
	types = ["ssdp:all", "upnp:rootdevice"]
	request= \
		"M-SEARCH * HTTP/1.1\r\n"\
		"HOST: %s:%s\r\n"\
		"MAN: \"ssdp:discover\"\r\n"\
		"MX: 1\r\n"\
		"ST: %s\r\n"\
		"\r\n" % (client.DEFAULT_IP,client.DEFAULT_PORT,types[type])

	print "\"" + request + "\""
	client.send(request,server)
	print "Discovery sent"	

	while True:			
		data = client.listen_from(1024,server)
#		data = client.listen(1024,server)
		if data is None:
			break
		print( "\n\r" + str(data[1]) + "\n\r" + str(data[0]))	
#		print( "\n\r" + str(data))

if __name__ == '__main__':
    main()