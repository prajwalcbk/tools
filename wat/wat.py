#/bin/python3

from argparse import *
from termcolor import colored


def arguments():
	parser=ArgumentParser(colored('Usage of the Program ','green')+(colored(' pyhton3 wat.py -u <url> \n','red')))
	parser.add_argument('-u',dest='url',help='URL of the target')
	return parser.parse_args()
arg=arguments()
print(arg.url)
