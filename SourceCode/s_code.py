#!/bin/python3

import urllib
print('''            ---------------------------------------------------------------
                        Finding the Source code of the Websites
            ---------------------------------------------------------------''')
url=raw_input("Enter the url for Ex:http://192.168.43.24/login.php :")
print(url)
f = urllib.urlopen(url)
s=f.read()
print(s)

#except:
 #   print("Exception Occured")
 #  print("Kindly Use python not Python3 ")
 #  exit()
