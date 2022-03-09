## Module to obtain packet data from a pcap/dump file
## and save it in csv format using tshark.
## Filenames of input pcap files are taken from InputFiles.txt
## Tshark options are present in TsharkOptions.txt
## TsharkOptions.txt should not contain the -r option.

## usage: python FilterPackets.py

#import global constants
from P2P_CONSTANTS import *
from FilterPacketsHelper import *
import multiprocessing as MP
import subprocess

#execute a shell command as a child process
def executeCommand(command,outfilename,sem):
    print('hi2')
    sem.acquire()

    subprocess.call(command, shell = True)
    print('hi3')
    infile = open(outfilename, 'r')
    data = [eachline.strip() for eachline in infile]
    infile.close()
    
    data = preprocess(data)
    
    outfile = open(outfilename,'w')
    for eachcomponent in data:
        outfile.write(eachcomponent)
    outfile.close()
    
    print ('done processing : ' + outfilename)
    sem.release()

#obtain input parameters and pcapfilenames
    
def filterpacketsall():    
    inputfiles = getPCapFileNames()
    tsharkOptions = getTsharkOptions()

#create a semaphore so as not to exceed threadlimit
    sem = MP.Semaphore(THREADLIMIT)

#get tshark commands to be executed
    for filename in inputfiles:
        print( filename)
        print('hi1')
        (command,outfilename) = contructTsharkCommand(filename,tsharkOptions)
        print('hi11')
        executeCommand(command, outfilename,sem)
        #task = MP.Process(target = executeCommand, args = (command, outfilename,))
        print('hi12')
    #task.start()
        print('hi13')
        
#filterpacketsall()