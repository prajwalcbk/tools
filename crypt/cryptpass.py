import crypt
from termcolor import colored


file_name=input(colored("Enter the path of the file :>",'yellow'))
file1=open(file_name,'r')
for word in file1.readlines():
	word=word.strip("\n")
	pas=(crypt.crypt(word,'$6$QzDubckmlDK6uclc'))
	if(pas=='$6$QzDubckmlDK6uclc$unRkwFD7EFYpDMdOrpIeiPJNs2NxN4vhHbber3KkUGpB/9bI88QM7EdhNqCci6jU/I4/HcwtfcRrWzr2Ru02F1'):
		print(colored("Password found : > "+word,'green'))
		exit()
	else:
		print(colored("Trying "+word,'red'))
