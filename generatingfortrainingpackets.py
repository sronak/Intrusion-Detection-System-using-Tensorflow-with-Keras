# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:06:49 2020

@author: ningesh
"""


import csv
from ipwhois import IPWhois


import csv
#myFile = open('outputofforalgorithm.csv', 'w')
outfile = open('outputofforalgorithm1.csv', 'w')
finaldatatowrite=''
alllist=[]
listofdata=[]
with open('flowdata//test.pcap.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        #splittext=row.split(",")
        print("len of row")
        print(len(row))
        
        
        opname=row[0]
        print("opname")
        print(opname)
    
        #listofdata.append(opname)
        #finaldatatowrite=finaldatatowrite+opname+"\n"
        if '192.168.' not in row[0]:
            print("inside if loop")
            try:
                print("inside try")
                obj = IPWhois(row[0])
                res=obj.lookup()
                name=res["nets"][0]["name"]
                print("name")
                print(name)
                finaldatatowrite=str(row[0])+','+str(row[1])+','+str(row[2])+','+str(row[3])+','+str(row[4])+','+str(row[5])+','+str(row[6])+','+str(row[7])+','+str(row[8])+','+str(row[9])+','+str(row[10])+','+str(row[11])+','+name
                print("finaldatatowrite")
                print(finaldatatowrite)
                outfile.write(finaldatatowrite)
                outfile.write("\n")
            except Exception as e:
                print('exception',e)
            #listofdata.append(finaldatatowrite)
            #listofdata.append("\n")
print(finaldatatowrite)
alllist.append(listofdata)



outfile.close()
        #print(row)