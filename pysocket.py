
import socket
import time
import sys
 
HOST_IP = "192.168.12.1"    #�ҵ���ݮ����ΪAP�ȵ��ip��ַ
HOST_PORT = 7654            #�˿ں�
 
print("Starting socket: TCP...")
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #����socket
 
print("TCP server listen @ %s:%d!" %(HOST_IP, HOST_PORT) )
host_addr = (HOST_IP, HOST_PORT)
socket_tcp.bind(host_addr)    #���ҵ���ݮ�ɵ�ip��ַ�Ͷ˿ں�
socket_tcp.listen(1)	#listen�����Ĳ����Ǽ����ͻ��˵ĸ���������ֻ����һ������ֻ������һ���ͻ��˴�������
 
while True:
	print ('waiting for connection...')
	socket_con, (client_ip, client_port) = socket_tcp.accept()    #���տͻ��˵�����
	print("Connection accepted from %s." %client_ip)
 
	socket_con.send("Welcome to RPi TCP server!")    #��������
 
	while True:
		data=socket_con.recv(1024)    #��������
		
		if data:    #������ݲ�Ϊ�գ����ӡ���ݣ���������ת�����ͻ���
			print(data)
			socket_con.send(data)
 
socket_tcp.close()