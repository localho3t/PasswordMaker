#Password maker
from os import system
import re
import sys
import random 
from time import sleep
def banner():
	print """
 _ _ _                              _ _ _
| | | | [!] Exploit TM         [!] | | | | 
| | | | [!] LocalHo3t          [!] | | | |
\_/_\_/ [!] Passwors Maker     [!] \_/_\_/ 
\ | | /	[!] 8 SEP 2020         [!] \ | | /
 \| |/ 	[!] 00:51 TH           [!]  \| |/ 
  \_/   [!] Next Update : NONE [!]   \_/  
"""

	

def passed():
        z = 0
        
        while(z < 12):
                a = ""
                for i in range(0,10):
                    a += random.choice(["a", "b", "c","d", "e", "f","g", "h", "i","j", "k", "l","m", "n", "o","p", "q", "r","s", "t", "u","v", "w", "x","y", "z", "A",
                                     "B", "C", "D","E", "F", "G","H", "I", "J","K", "L", "M","N", "O", "P","Q", "R", "S","T", "U", "V","W", "X", "Y","Z","_","-","1"
                                     "2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","~","`","/","."])
                 
                print a
                sleep(2)
                z+=1
  




if(__name__ == "__main__"):
    try:
        system('cls')
        banner()
        passed()
    except KeyboardInterrupt as e:
        print("\nGood By :)")
        


