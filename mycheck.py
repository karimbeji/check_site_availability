import ConfigParser
import os
config = ConfigParser.ConfigParser()
config.read ("./sites.ini")
#print config.sections()
print config.get('checks', 'google')
for site in config.items('checks'):
     host_name = site[1]
     response = os.system("ping -c 1 " + host_name)
     print response
     if response == 1:
         print host_name + " is down\n"
     else:
         print host_name + " \033[92m] is up\n"


