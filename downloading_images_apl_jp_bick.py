#This script was written with python build 3.4.3
#This script uses a plain text file, which should contain in each row one link to an url of an image

import sys
import os
import urllib.request

linksfile = input("Store your file containing URL's (one per row) as plain text file (.txt) in the DIR, where this script is located and enter the name of the file (without extension):") + '.txt'




i=0
with open(linksfile, "r") as linkss:
    
      for line in linkss:
          i=i+1
          filename="image_"  #to store the file with name "image_[number]", if necessary image could be replaced by parts of the character strings from the links (similar to line[x : y] s.b.)
          if "\n" in line[-7:]:                #IF: checks for line breaks (relevant only for the last line), in order to store the file under the original file extension 
             last_chars=line[-7:-1]
             exten=last_chars.split(".")[-1]
             urllib.request.urlretrieve(line, filename+str(i)+"."+ exten)
          else:
             last_chars=line[-7:]
             exten=last_chars.split(".")[-1]
             urllib.request.urlretrieve(line, filename+str(i)+"."+ exten)



print("The images are stored at",os.getcwd()) #Outputs the file location 
input("Press any key to exit")
