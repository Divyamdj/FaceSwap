# Renaming the files
import os 

for count, filename in enumerate(os.listdir("E:/Kroop AI/horse2zebra/downloads/elon musk/")): 
  dst ="musk" + str(count) + ".jpg"
  src ='E:/Kroop AI/horse2zebra/downloads/elon musk/'+ filename 
  dst ='E:/Kroop AI/horse2zebra/downloads/elon musk/'+ dst 
  
  # rename() function will 
  # rename all the files 
  os.rename(src, dst) 