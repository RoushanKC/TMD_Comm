import socket
import threading
import struct
import time
from Data_maps import receive_offset_map ,type_dict ,format_map
from Shared_data import Shared_data


class Connection:
    _instance=None
    _lock=threading.Lock()
    
    def __new__(cls ,*args ,**kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance=super().__new__(cls)
            return cls._instance
    
    def __init__(self ,host ,port ,refresh_rate ,packet_size):
        self.s_data=Shared_data.getInstance()
        self.host=host
        self.port=port
        self.refresh_rate=refresh_rate
        self.packet_size=packet_size
        self.client=None
        
    def establish_connection(self):
        if self.client is None:
            self.client=socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
        self.client.connect((self.host ,self.port))
        socket.setdefaulttimeout(5)
        
    def connection_handling(self):
        pass
    
    #decoder decode the data buffer recieved from plc and return decoded data
    def decode(self ,dataP):
        parsed_data={}
        packet=dataP
        parsed_data["dTimestamp"]=time.time()
        for items in receive_offset_map:
            addr=items["address"]
            addr=int(addr/8)
            name=items["name"]
            typeF=items["type"]
            offset_len=type_dict[typeF]
            decode_format=format_map[typeF]
            if addr==0:
                #bit manup impl
                pass
            elif addr==30:
                #bit manup impl
                pass
            elif(addr==694):
                bolt_arr=[]
                for i in range(206):
                    bolt_addr=addr+(i*4)
                    tdata=packet[bolt_addr : bolt_addr+offset_len]
                    if(len(tdata)==offset_len):
                        value=struct.unpack(decode_format ,tdata)
                    bolt_arr.append(value)
                parsed_data[name]=bolt_arr
            elif(addr==1540):
                pos_arr=[]
                for i in range(1050):
                    pos_addr=addr+(i*4)
                    tdata=packet[pos_addr : pos_addr+offset_len]
                    if(len(tdata)==offset_len):
                        value=struct.unpack(decode_format ,tdata)
                    pos_arr.append(value)
                parsed_data[name]=pos_arr
            else:
                tdata=packet[addr : addr+offset_len]
                if(len(tdata)==offset_len):
                    value=struct.unpack(decode_format ,tdata)
                    parsed_data[name]=value
        return parsed_data
    
    def receive(self):
        self.establish_connection()
        self.client.sendall(b'11')
        while True:
            try:
                data=self.client.recv(self.packet_size)
                if not data:
                    print("closing connection")
                    self.client.close()
                else:
                    data_map=self.decode(data)
                    self.s_data.put_data(data_map)
            except socket.timeout:
                print("socket timeout ,closing connection")
                self.client.close()