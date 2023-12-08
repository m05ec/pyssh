# SSH clinet for windows systems 
from sys import stderr
import paramiko

def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    _, stdout, stderr = client.exec_command(cmd) #we dont care about the stdin so we use _ which tells python to drop this value
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('----Output---')
        for line in output:
            print(line.strip())

if __name__ == "__main__":
   import getpass
   user = input('Username: ')
   password = getpass.getpass() # this module is a more secure way to get the password if someone is sholder surfing you

   ip = input('Enter server IP: ') or '192.168.1.203'
   port = input('Enter port or <CR>: ') or 22
   cmd = input('Enter command or <CR>: ') or 'id'
   ssh_command(ip, port,user, password, cmd)
