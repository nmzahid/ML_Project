from os import walk
import csv
import os
import shutil

def loadCsv(filename):
    print "hey"
    lines = csv.reader(open(filename, "rb"))
    dataset = list(lines)
    return dataset


def folderseg(dataset,f):
    count=0
    src="C:\\Users\\AadarshSam\\Desktop\\data\\training\\image"
    data_list=list(dataset)
    filenames = []
    male=[]
    #for copying female records

    for i in range(1,len(data_list)):
            print str(data_list[i][1])
            if (float(data_list[i][3])==1):
                    path = "C:\\Users\\AadarshSam\\Desktop\\data\\training\\Female"
                    filename = str(data_list[i][1]) + '.jpg'
                    filenames.append(filename)

    for filename in filenames:
        full_file_name = os.path.join(src, filename)
        shutil.copy(full_file_name, path)

# for copying male records

    for i in range(1,len(data_list)):
            print str(data_list[i][1])
            if (float(data_list[i][3])==0):
                    path = "C:\\Users\\AadarshSam\\Desktop\\data\\training\\Male"
                    filename_male = str(data_list[i][1]) + '.jpg'
                    male.append(filename_male)

    for filename_male in male:
        full_file_name_male = os.path.join(src, filename_male)
        shutil.copy(full_file_name_male, path)

def folderseg_age(dataset,f):
    count=0
    src="C:\\Users\\AadarshSam\\Desktop\\data\\training\\image"
    data_list=list(dataset)
    age1 = []
    age2= []
    age3= []
    age4 = []
    #for copying records less than 24

    for i in range(1,len(data_list)):
            if (float(data_list[i][2])<= 24):
                    path = "C:\\Users\\AadarshSam\\Desktop\\data\\training\\xx-24"
                    filename = str(data_list[i][1]) + '.jpg'
                    age1.append(filename)

    for filename in age1:
        full_file_name = os.path.join(src, filename)
        shutil.copy(full_file_name, path)

# for copying 25-34

    for i in range(1,len(data_list)):
            print str(data_list[i][1])

            if (float(data_list[i][2])> 24 and float(data_list[i][2])<= 34):
                    path2 = "C:\\Users\\AadarshSam\\Desktop\\data\\training\\25-34"
                    filename_age2 = str(data_list[i][1]) + '.jpg'
                    age2.append(filename_age2)

    for filename_age2 in age2:
        full_file_name_age2 = os.path.join(src, filename_age2)
        shutil.copy(full_file_name_age2, path2)

# for copying 35-49

    for i in range(1,len(data_list)):

            if (float(data_list[i][2])> 34 and float(data_list[i][2])<= 49):
                    path3 = "C:\\Users\\AadarshSam\\Desktop\\data\\training\\35-49"
                    filename_age3 = str(data_list[i][1]) + '.jpg'
                    age3.append(filename_age3)

    for filename_age3 in age3:
        full_file_name_age3 = os.path.join(src, filename_age3)
        shutil.copy(full_file_name_age3, path3)

# for copying 50-xx
    for i in range(1,len(data_list)):
            if (float(data_list[i][2])>=50):
                    path = "C:\\Users\\AadarshSam\\Desktop\\data\\training\\50-xx"
                    filename_age4 = str(data_list[i][1]) + '.jpg'
                    age4.append(filename_age4)

    for filename_age4 in age4:
        full_file_name_age4 = os.path.join(src, filename_age4)
        shutil.copy(full_file_name_age4, path)



def main():
    f = []
    filename='C:\Users\AadarshSam\Downloads\profile.csv'
    #  print f[0]
    dataset = loadCsv(filename)
    #folderseg(dataset,f)
    folderseg_age(dataset,f)

main()