import socket
import time

def login():
    #username request
    conn.send("ubuntu login:".encode())
    username = ""
    while True:
        data = conn.recv(1) #Receive data from the socket.
        if (data.decode()=='\n'):
            break
        else:
            username += data.decode("utf-8")

    
    #password request
    conn.sendall("password:".encode())
    password=""
    while True:
        data = conn.recv(1) #Receive data from the socket.
        if (data.decode()=='\n'):
            break
        else:
            password += data.decode("utf-8")
    return(username, password)

def loginLog(user_info,username,password):
    separator2='--'
    separator = '*'*30
    file=open('./log.txt', 'a')
    file.write('%s\nTime: %s\nUser IP: %s\nUser Port:%s\n%s\n'%(separator,time.ctime(), user_info[0], user_info[1], separator2))
    file.write(f"Username:{username}Password:{password}")

def commandsLog(user_cmd):
	file = open('./log.txt', 'a')
	file.write(f"Command:{user_cmd}")
	file.write('\n')
	file.close()

addr='127.0.0.1'
port=1024
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((addr, port))
s.listen(5)
(conn, client_info)=s.accept()
print("Connection approved, user:", client_info)
data='Ubuntu 18.04.1 LTS ubuntu tty1'
username, password=login()
loginLog(client_info, username, password)
welcome_text='Welcome '+username
conn.send(welcome_text.encode())
conn.sendall("admin@ubuntu:~$ ".encode())
command=""
while True:
    data = conn.recv(1) #Receive data from the socket.
    if (data.decode()=='\n'):
        break
    else:
        command += data.decode("utf-8")
commandsLog(command)

#TO DO 

#if(command.strip()=='ls'):
     






    
