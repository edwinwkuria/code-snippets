import pathlib

import hashlib

import logging



file1 = open('./checksums.txt', 'r')

Lines = file1.readlines()



hashes = set()

textcount = 0

# Strips the newline character

for line in Lines:

    values = line.split("  ")

    filename = values[1].replace("student",".")

    #f = open(filename, "r")

    hashes.add(values[0])

print(textcount)



filecount = 0

desktop = pathlib.Path("/home/cs6035/binexp/03_hunt_then_rop")

for item in desktop.iterdir():

   if item.is_file():

      f = open(item, "r")

      filecount += 1

      try:

      	localLines = f.read()

      	result = hashlib.sha1(localLines.encode())

      	if result.hexdigest() not in hashes:

      	   print(item)

      except Exception as Argument:

      	bf = open(item , 'rb')

      	bl = bf.read()

      	result = hashlib.sha1(bl)

      	if result.hexdigest() not in hashes:

      	   print(item)

print(filecount)

 

