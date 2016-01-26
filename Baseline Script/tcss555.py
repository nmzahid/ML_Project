#!/usr/bin/python
import sys, getopt
import os
import pandas as pd
import xml.etree.cElementTree as ET

def XmlConverter(ipFileName,opDirName):
    gender=1
    ope=3.908691
    con=3.445617
    ext=3.486858
    agr=3.583904
    neu=2.732424
    age="25-34"
    count=0

    data=pd.read_csv(ipFileName)
    number_of_pts = data.as_matrix([data.columns])
    number_of_pts[:,1]

    if not os.path.exists(opDirName):
          os.makedirs(opDirName)
    os.chdir(opDirName)

    for row in number_of_pts:
       xmlel = ET.Element("user-id="+"\""+str(row[1])+"\""+"\n"
                       +"age_group="+"\""+str(age)+"\""+"\n"
                       +"gender="+"\""+str(gender)+"\""+"\n"
                       +"extrovert="+"\""+str(ext)+"\""+"\n"
                       +"neurotic="+"\""+str(neu)+"\""+"\n"
                       +"agreeable="+"\""+str(agr)+"\""+"\n"
                       +"conscientious="+"\""+str(con)+"\""+"\n"
                       +"open="+"\""+str(ope)+"\""+"\n")
       tree = ET.ElementTree(xmlel)
       tree.write(str(row[1])+".xml")
       if count>9499:
           break
           count+=1

def main(argv):
   ipDir = ''
   opDir = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         ipDir = arg
      elif opt in ("-o", "--ofile"):
         opDir = arg
#   print 'Input directory is "', ipDir
#   print 'Output file is "', opDir
   ipFilePath=ipDir+"/profile/profile.csv"
#   print 'Input File is"',ipFilePath
   XmlConverter(ipFilePath,opDir)

if __name__ == "__main__":
    main(sys.argv[1:])