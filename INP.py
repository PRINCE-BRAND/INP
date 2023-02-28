import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from INP1 import INP1
 
        INP1()
 
 
 
elif bit == "32bit":
 
        from INP32 import INP32
 
 
        INP32()
