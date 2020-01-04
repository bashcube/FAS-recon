from fedora.client.fas2 import AccountSystem
from fedora.client import AuthError
import sys

USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]

class colors:
	GREEN = '\033[92m'
	STOP = '\033[0m'
	BLUE = '\33[94m'
	RED = '\033[31m'
	BOLD = '\033[93m'

def get_email(id):
	print ()
	fas = AccountSystem(username=USERNAME, password=PASSWORD)
	value = fas.people_by_key(key='email', search=id, fields=['email'])
	mail = value.keys()
	if str(mail)[12:][:-3] == '':
		print (colors.RED+"[-]NO EMAIL FOUND!!! \n[-]QUITTING NOW..."+colors.STOP+"\n")
	else:
		print (colors.GREEN+"[+]EMAIL:    "+str(mail)[12:][:-3]+colors.STOP+"\n")
	sys.exit(0)

def main():
	print (colors.BLUE+' _____ _    ____       ___ ____    ____  _____ ____ ___  _   _')
	print ('|  ___/ \  / ___|     |_ _|  _ \  |  _ \| ____/ ___/ _ \| \ | |')
	print ('| |_ / _ \ \___ \ _____| || | | | | |_) |  _|| |  | | | |  \| |')
	print ('|  _/ ___ \ ___) |_____| || |_| | |  _ <| |__| |__| |_| | |\  |')
	print ('|_|/_/   \_\____/     |___|____/  |_| \_\_____\____\___/|_| \_|'+"\n"+colors.STOP)
	FAS_ID = input(colors.BOLD+"USERNAME>>"+colors.STOP)
	get_email(FAS_ID)

main()
