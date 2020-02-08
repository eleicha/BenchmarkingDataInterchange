import avro.datafile
import avro.io
import io
import socket
import time
import numpy as np
from avro.datafile import DataFileWriter
import avro.schema
from avro.io import DatumWriter
import struct
import capnp
import addressbook_capnp
import addressBook_pb2
import psutil
import sys
import os

def handle_proto_client(connection, address):

    data = connection.recv(4)
    print(len(data))
    message_length, = struct.unpack('>I', data)

    #print(message_length)

    message = connection.recv(message_length)

    addresses = addressBook_pb2.AddressBook()
    addresses.ParseFromString(message)

    print (addresses)
    return(len(message))

def handle_proto_client_print_to_file(connection, address):

    data = connection.recv(4)
    message_length, = struct.unpack('>I', data)

    #print(message_length)

    message = connection.recv(message_length)

    #addresses = addressBook_pb2.AddressBook()
    #addresses.ParseFromString(message)

    f = open("schema/addressbook_proto.bin", "w+b")
    f.write(message)
    
    os.fsync(f)
    f.close()
    return(len(message))

def handle_capnp_client(connection, address):

    data = connection.recv(4)
    message_length, = struct.unpack('>I', data)

    #print(message_length)

    message = connection.recv(message_length)

    addresses = addressbook_capnp.AddressBook.new_message()
    addresses = addressbook_capnp.AddressBook.from_bytes_packed(message)

    print (addresses)
    return(len(message))

def handle_capnp_client_print_to_file(connection, address):
    
    data = connection.recv(4)
    message_length, = struct.unpack('>I', data)

    #print(message_length)

    message = connection.recv(message_length)

    #addresses = addressbook_capnp.AddressBook.new_message()
    #addresses = addressbook_capnp.AddressBook.from_bytes(message)

    f = open("schema/addressbook_capnp.bin", "w+b")
    f.write(message)
    os.fsync(f)
    f.close()
    return(len(message))

def handle_avro_client(connection, address):

    #data = connection.recv(1024*1024)
    data = connection.recv(4)

    message_length, = struct.unpack('>I', data)

    message = connection.recv(message_length)

    message_buf = io.BytesIO(message)
    reader = avro.datafile.DataFileReader(message_buf, avro.io.DatumReader())

    for thing in reader:
        print(thing)
    reader.close()
    return(len(message))
    
def handle_avro_client_print_to_file(connection, address):

    schema = avro.schema.Parse(open("schema/addressbook.avsc", "rb").read())

    data = connection.recv(4)

    message_length, = struct.unpack('>I', data)
    
    message = connection.recv(message_length)

    message_buf = io.BytesIO(message)
    reader = avro.datafile.DataFileReader(message_buf, avro.io.DatumReader())

    # Create a data file using DataFileWriter

    dataFile = open("schema/addressbook.avro", "wb")

    writer = DataFileWriter(dataFile, DatumWriter(), schema)

    for thing in reader:
        writer.append(thing)
    reader.close()
    
    writer.close()
    return(len(message))

def handle_XML_client(conn, addr):
    
    data = conn.recv(4)
    message_length, = struct.unpack('>I', data)

    message_buf = conn.recv(message_length)

    print(message_buf.decode())
    return(len(message_buf))

def handle_XML_client_print_to_file(conn, addr):
    
    data = conn.recv(4)
    message_length, = struct.unpack('>I', data)

    message_buf = conn.recv(message_length)

    f = open("schema/addressbook.xml", "wb")

    f.write(message_buf)

    os.fsync(f)
    f.close()
    return(len(message_buf))

def main():

    #0 for just command line printing, 1 for file printing
    printToFile = sys.argv[1]
    #0 for protobuf, 1 for cap'n proto, 2 for Apache Avro, and 3 for XML
    messageType = sys.argv[2]
    numberOfPeople = sys.argv[3]
    numberOfMessages = sys.argv[4]
    numberOfExperiments = sys.argv[5]
    machinesUsed = sys.argv[6]

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #sock.bind(('172.16.150.67', 12345))
    #sock.bind(('127.0.0.1', 12345))
<<<<<<< HEAD
    sock.bind(('192.168.43.156',12345))
=======
    sock.bind('172.17.0.1', 12345))
>>>>>>> ecc96c7d53ee574b77f7c74658b777f5218f2cdf
    sock.listen(10)

    print("Listening")

    times = []
    message_length_total = []
    cpu_utilization = []
    cpu_util_user = []
    cpu_util_system = []
    cpu_util_idle = []
    disk_info1 = []
    disk_info2 = []
    disk_info3 = []
    disk_info4 = []
    disk_info5 = []
    disk_info6 = []
    memory = []
    net_io_counters1 = []
    net_io_counters2 = []
    time_stamp = []
    message_length = []
    start_value_disk = psutil.disk_io_counters().write_bytes
    start_value_bytes_rec = psutil.net_io_counters().bytes_recv
            
    while True:
        
        conn, addr = sock.accept()

        if int(printToFile) == 0:
            if int(messageType) == 0:
                start = time.perf_counter()
                psutil.cpu_percent(None, False)
                psutil.cpu_times_percent(None,False)
                psutil.net_io_counters.cache_clear()
                psutil.disk_io_counters.cache_clear()
                message_length.append(handle_proto_client(conn, addr))
            elif int(messageType) == 1:
                start = time.perf_counter()
                psutil.cpu_percent(None, False)
                psutil.net_io_counters.cache_clear()
                psutil.disk_io_counters.cache_clear()
                message_length.append(handle_capnp_client(conn, addr))
            elif int(messageType) == 2:
                start = time.perf_counter()
                psutil.cpu_percent(None, False)
                psutil.net_io_counters.cache_clear()
                psutil.disk_io_counters.cache_clear()
                message_length.append(handle_avro_client(conn, addr))
            elif int(messageType) == 3:
                start = time.perf_counter()
                psutil.cpu_percent(None, False)
                psutil.net_io_counters.cache_clear()
                psutil.disk_io_counters.cache_clear()
                message_length.append(handle_XML_client(conn, addr))
        elif int(printToFile) == 1:
            if int(messageType) == 0:
                start = time.perf_counter()
                psutil.cpu_percent(None, False)
                psutil.net_io_counters.cache_clear()
                psutil.disk_io_counters.cache_clear()
                message_length.append(handle_proto_client_print_to_file(conn, addr))
            elif int(messageType) == 1:
                start = time.perf_counter()
                psutil.cpu_percent(None, False)
                psutil.net_io_counters.cache_clear()
                psutil.disk_io_counters.cache_clear()
                message_length.append(handle_capnp_client_print_to_file(conn, addr))
            elif int(messageType) == 2:
                start = time.perf_counter()
                psutil.cpu_percent(None, False)
                psutil.net_io_counters.cache_clear()
                psutil.disk_io_counters.cache_clear()
                message_length.append(handle_avro_client_print_to_file(conn, addr))
            elif int(messageType) == 3:
                start = time.perf_counter()
                psutil.cpu_percent(None, False)
                psutil.net_io_counters.cache_clear()
                psutil.disk_io_counters.cache_clear()
                message_length.append(handle_XML_client_print_to_file(conn, addr))

        times.append(time.perf_counter() - start)
        message_length_total.append(message_length)
        memory.append(psutil.virtual_memory().percent)
        time_stamp.append(time.perf_counter())
        cpu_utilization.append(psutil.cpu_percent(None, False))
        cpu_util_user.append(psutil.cpu_times_percent(None, False).user)
        cpu_util_system.append(psutil.cpu_times_percent(None, False).system)
        cpu_util_idle.append(psutil.cpu_times_percent(None, False).idle)

        disk_info1.append(psutil.disk_io_counters().read_count)
        disk_info2.append(psutil.disk_io_counters().write_count)
        disk_info3.append(psutil.disk_io_counters().read_bytes)
        disk_info4.append(psutil.disk_io_counters().write_bytes)
        disk_info5.append(psutil.disk_io_counters().read_time)
        disk_info6.append(psutil.disk_io_counters().write_time)
        net_io_counters1.append(psutil.net_io_counters().bytes_recv)

        with open('results/server_'+str(messageType)+'_'+str(numberOfPeople)+'_'+str(numberOfMessages)+'_'+str(printToFile)+'_'+str(machinesUsed)+'.txt', 'w') as f:
            f.write('CPU_UTIL:'+str(cpu_utilization)+'\n')
            f.write('CPU_USER:'+str(cpu_util_user)+'\n')
            f.write('CPU_SYSTEM:'+str(cpu_util_system)+'\n')
            f.write('CPU_IDLE:'+str(cpu_util_idle)+'\n')
            f.write('message_length:'+str(message_length_total)+'\n')
            f.write('time_stamp:'+str(time_stamp)+'\n')
            f.write('MEMORY:'+ str(memory)+'\n')
            f.write('TIMES:'+str(times)+'\n')
            f.write('read_bytes:'+str(disk_info3)+'\n')
            f.write('write_bytes:'+str(disk_info4)+'\n')
            f.write('read_time:'+str(disk_info5)+'\n')
            f.write('write_time:'+str(disk_info6)+'\n')
            f.write('bytes_recv:'+str(net_io_counters1)+'\n')
            f.write('start_value_disk:'+str(start_value_disk)+'\n')
            f.write('start_value_bytes_rec:'+str(start_value_bytes_rec)+'\n')


        #conn.close()

if __name__ == '__main__':
    main()
