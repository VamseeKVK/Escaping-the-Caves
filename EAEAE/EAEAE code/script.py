import paramiko
import time

h = "172.27.26.188"
p = 22
u = "student"
passw = "cs641"

ssh_server = paramiko.client.SSHClient()
ssh_server.load_system_host_keys()
ssh_server.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_server.connect(h,p, u, passw, allow_agent=False, look_for_keys=False)

chan = ssh_server.invoke_shell()

chan.send("Cryptosenpai\n")
time.sleep(1)
chan.recv(5000)
time.sleep(1)
chan.send("cryptosenpai99\n")
time.sleep(1)
chan.recv(5000)
time.sleep(1)
chan.send("5\n")
time.sleep(1)
chan.recv(5000)
time.sleep(1)
chan.send("go\n")
time.sleep(1)
chan.recv(5000)
time.sleep(1)
chan.send("wave\n")
time.sleep(1)
chan.recv(5000)
time.sleep(1)
chan.send("dive\n")
time.sleep(1)
chan.recv(5000)
time.sleep(1)
chan.send("go\n")
time.sleep(1)
chan.recv(5000)
time.sleep(1)
chan.send("read\n")
time.sleep(1)
chan.recv(5000)

to_ciphers = {'0':'f', '1':'g', '2':'h', '3':'i', '4':'j', '5':'k', '6':'l', '7':'m', '8':'n', '9':'o', 'a':'p', 'b':'q', 'c':'r', 'd':'s', 'e':'t', 'f':'u'}
to_hexa = {'f':'0', 'g':'1', 'h':'2', 'i':'3', 'j':'4', 'k':'5', 'l':'6', 'm':'7', 'n':'8', 'o':'9', 'p':'a', 'q':'b', 'r':'c', 's':'d', 't':'e', 'u':'f'}

def cipher_to_hex(word):
    new=''
    for i in word:
        new+=to_hexa[i]
    return new

def hex_to_cipher(word):
    new=''
    for i in word:
        new+=to_ciphers[i]
    return new

chan.send("c\n")
time.sleep(1)
chan.recv(5000)

chan.send("ffffffffffffffmu"+"\n")
time.sleep(1)
A = chan.recv(5000)
print(A)
A = A[-43:-27]
print(A.decode("UTF-8"))
chan.send("c\n")
time.sleep(1)
chan.recv(5000)

file1 = open("C:/Users/RUMITGORE/Downloads/m_plain_text.txt", 'r')
file2 = open("C:/Users/RUMITGORE/Downloads/ciphertexts.txt",'w')

for lines in file1.readlines():
    lin = lines.split()
    for l in lin:
        chan.send(l+"\n")
        time.sleep(1)
        A = chan.recv(5000)
        A = A[-43:-27]
        str = A.decode("UTF-8")        
        print(str)
        chan.send("c\n")
        time.sleep(1)
        chan.recv(5000)

        file2.write(str)
        file2.write(" ")
    file2.write("\n")

file1.close()
file2.close()

