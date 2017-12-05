from upnp import *

def main():
    client = upnp(None,None,None)
    print "Entering main"	
    myip = '' #should be localhost
        
    #Have to create a new socket since replies will be sent directly to our IP, not the multicast IP
    server = client.createNewListener(myip,client.port)
    if server == False:
        print 'Failed to bind port %d' % client.port
        return
    server.settimeout(2)
    request= \
        "M-SEARCH * HTTP/1.1\r\n"\
		"HOST: 239.255.255.250:1900\r\n"\
		"MAN: \"ssdp:discover\"\r\n"\
		"MX: 1\r\n"\
		"ST: ssdp:all\r\n"\
        "\r\n"
    
    print "\"" + request + "\""
    client.send(request,server)
    print "Discovery sent"	
    
    while True:			
		data = client.listen(1024,server)
		print( data)
#		if data != False:
#			print "\"" + data[0] + "\""
#			print "\"" + str(data[1]) + "\"" + "\"" + data[0] + "\""
    
if __name__ == '__main__':
    main()