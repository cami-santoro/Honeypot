import socket
import time

def login():
    #username request
    conn.send("ubuntu login:".encode())
    username = ""
    while True:
        data = conn.recv(1) #Receive username from the socket
        if (data.decode()=='\n'):
            break
        else:
            username += data.decode("utf-8")

    
    #password request
    conn.sendall("password:".encode())
    password=""
    while True:
        data = conn.recv(1) #Receive password from the socket
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
conn.sendall("Welcome ".encode())
conn.sendall(username.encode())
conn.send('\r\n'.encode())
exit=False
current_dir="home"
while (not exit):
    if(current_dir=="home"):
        conn.sendall("admin@ubuntu:~$ ".encode())
    elif(current_dir=="Desktop"):
        conn.sendall("admin@ubuntu:~/Desktop$ ".encode())
    elif(current_dir=="Documents"):
        conn.sendall("admin@ubuntu:~/Documents$ ".encode())
    elif(current_dir=="Downloads"):
        conn.sendall("admin@ubuntu:~/Downloads$ ".encode())
    elif(current_dir=="Pictures"):
        conn.sendall("admin@ubuntu:~/Pictures$ ".encode())
    elif(current_dir=="Public"):
        conn.sendall("admin@ubuntu:~/Public$ ".encode())
    elif(current_dir=="Videos"):
        conn.sendall("admin@ubuntu:~/Videos$ ".encode())
    
    command=""
    # --
    while True:
        data = conn.recv(1) #Receive command from the socket
        if (data.decode()=='\n'):
            break
        else:
            command += data.decode("utf-8")
    # --
    print(command.strip())
    commandsLog(command) #save the command
    if (command.strip()=='exit'):
        exit=True
    elif(current_dir=='home' and command.strip()=='ls'):
        fakeDirectory='Desktop\r\nDocuments\r\nDownloads\r\nPictures\r\nPublic\r\nVideos'
        conn.send(fakeDirectory.encode())
    elif (command.strip()=="cat /etc/*-release"):
        fake_distro="DISTRIB_ID=Ubuntu\r\nDISTRIB_RELEASE=22.04\r\nDISTRIB_CODENAME=jammy\r\nDISTRIB_DESCRIPTION=\"Ubuntu 22.04.2 LTS\"\r\nPRETTY_NAME=\"Ubuntu 22.04.2 LTS\"\r\nNAME=\"Ubuntu\"\r\nVERSION_ID=\"22.04\"\r\nVERSION=\"22.04.2 LTS (Jammy Jellyfish)\r\n\"VERSION_CODENAME=jammy\r\nID=ubuntu\r\nID_LIKE=debian\r\nHOME_URL=\"https://www.ubuntu.com/\"\r\nSUPPORT_URL=\"https://help.ubuntu.com/\"\r\nBUG_REPORT_URL=\"https://bugs.launchpad.net/ubuntu/\"\r\nPRIVACY_POLICY_URL=\"https://www.ubuntu.com/legal/terms-and-policies/privacy-policy\"\r\nUBUNTU_CODENAME=jammy\r\n"
        conn.send(fake_distro.encode())
    elif(command.strip()=="uname -r"):
        fake_version="5.19.0-42-generic\r\n"
        conn.send(fake_version.encode())
    elif (command.strip()=="cd Desktop"):
        current_dir="Desktop"
    elif (command.strip()=="cd Documents"):
        current_dir="Documents"
    elif (command.strip()=="cd Downloads"):
        current_dir="Downloads"
    elif (command.strip()=="cd Pictures"):
        current_dir="Pictures"
    elif (command.strip()=="cd Public"):
        current_dir="Public"
    elif (command.strip()=="cd Videos"):
        current_dir="Videos"
    elif(command.strip()=="cd .."):
        current_dir="home"
    else:
        conn.send("Command not found\r\nTry '--help' for more information\r\n".encode())




     






    
