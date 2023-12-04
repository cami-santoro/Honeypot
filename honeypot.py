import socket
import time

def login():
    #username request
    conn.send("ubuntu login:".encode())
    username = ""
    while True:
        data = conn.recv(1) #Receive username from the socket.
        if (data.decode()=='\n'):
            break
        else:
            username += data.decode("utf-8")

    
    #password request
    conn.sendall("password:".encode())
    password=""
    while True:
        data = conn.recv(1) #Receive password from the socket.
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
port=1024 #use a non-reserved port
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((addr, port))
s.listen(5)
(conn, client_info)=s.accept()
print("Connection approved, user:", client_info)
conn.send('Ubuntu 22.04.2 LTS \r\n'.encode())
username, password=login()
loginLog(client_info, username, password)
welcome_text='Welcome '+username
conn.send(welcome_text.encode())
conn.sendall("admin@ubuntu:~$ ".encode())
while True:
    command=""
    while True:
        data = conn.recv(1) #Receive command from the socket.
        if (data.decode()=='\n'):
            break
        else:
            command += data.decode("utf-8")
    if (command.strip()=='exit'):
        break
    commandsLog(command)
    #TO DO 
    '''if(command.strip()=='ls'):
        fakeDirectory=''
    elif (command.strip()=='cat /etc/*-release'):
        fake_distro="DISTRIB_ID=Ubuntu\r\nDISTRIB_RELEASE=22.04\r\nDISTRIB_CODENAME=jammy\r\nDISTRIB_DESCRIPTION=\"Ubuntu 22.04.2 LTS\"\r\nPRETTY_NAME=\"Ubuntu 22.04.2 LTS\"\r\nNAME=\"Ubuntu\"\r\nVERSION_ID=\"22.04\"\r\nVERSION=\"22.04.2 LTS (Jammy Jellyfish)\r\n\"VERSION_CODENAME=jammy\r\nID=ubuntu\r\nID_LIKE=debian\r\nHOME_URL=\"https://www.ubuntu.com/\"\r\nSUPPORT_URL=\"https://help.ubuntu.com/\"\r\nBUG_REPORT_URL=\"https://bugs.launchpad.net/ubuntu/\"\r\nPRIVACY_POLICY_URL=\"https://www.ubuntu.com/legal/terms-and-policies/privacy-policy\"\r\nUBUNTU_CODENAME=jammy"
    elif(command.strip()=='uname -r'):
'''

     






    
