# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: Python Getting Started

#
# Example file for working with os.path module
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
  # Print the name of the OS
  print (os.name)
  
  # Check for item existence and type
  print ("Item exists: " + str(path.exists("file.txt")))
  print ("Item is a file: " + str(path.isfile("file.txt")))
  print ("Item is a directory: " + str(path.isdir("file.txt")))
  
  # Work with file paths
  print ("Item's path: " + str(path.realpath("file.txt")))
  print ("Item's path and name: " + str(path.split(path.realpath("file.txt"))))
  
  # Get the modification time
  t = time.ctime(path.getmtime("file.txt"))
  print (t)
  print (datetime.datetime.fromtimestamp(path.getmtime("file.txt")))
  
  # Calculate how long ago the item was modified
  td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("file.txt"))
  print ("It has been " + str(td) + " since the file was modified")
  print ("Or, " + str(td.total_seconds()) + " seconds")

if __name__ == "__main__":
  main()
