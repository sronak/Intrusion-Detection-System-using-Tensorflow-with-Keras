import socket
#defines properties of a packet
class Packet:
    def __init__(self,fields):
        if fields == None:
            self.source = None
            self.dest = None
            self.timestamp = None
            self.size = 0
            self.key = None
        else:
            if fields[3]=='':
                fields[3]=0
                
            if fields[0]=='':
                fields[0]='0'
            if fields[1]=='':
                fields[1]='0'
            if fields[2]=='':
                fields[2]=0
            self.source = socket.inet_aton(fields[0])
            self.dest = socket.inet_aton(fields[1])
            
            self.timestamp = float(fields[2])
            self.size = int(fields[3])
            if self.source < self.dest:
                self.key = self.source + self.dest
            else:
                self.key = self.dest + self.source
        
