import io
import json
import socket
from avro.datafile import DataFileWriter
import avro.schema
from avro.io import DatumWriter
import avro.ipc
import struct
import addressBook_pb2
import capnp
import addressbook_capnp
import psutil
import os
import sys

def send_proto_message(connection, numberOfPeople, i):

    address_book = addressBook_pb2.AddressBook()
    
    for x in range(0, int(numberOfPeople)):

        person = address_book.people.add()
        person.id = x
        person.name = "Rosa Luxemburg"
        person.email = "rosa.luxemburg@web.de"
        phone = person.phones.add()
        phone.number = "0178525048"

    message = address_book.SerializeToString();

    x = struct.pack('>I', len(message))

    connection.sendall(x)
    connection.sendall(message)
    print("Length of send Proto data: " + str(len(message)))
    print("Type of Proto data send: " + str(type(message)))
    print("Iter: " + str(i))


def send_capnp_message(connection, numberOfPeople, i):
    

    addresses = addressbook_capnp.AddressBook.new_message()
    people = addresses.init("people", int(numberOfPeople))

    for x in range(0, int(numberOfPeople)):
        people[x].name = "Rosa Luxemburg"
        people[x].id = int(i)
        people[x].email = "rosa.luxemburg@web.de"

        rosaPhone = people[x].init("phones", 1)[0]

        rosaPhone.number = "01785250483"

    message = addresses.to_bytes_packed()

    x = struct.pack('>I', len(message))

    connection.sendall(x)
    connection.sendall(message)
    print("Length of send Capnp data: " + str(len(message)))
    print("Type of Capnp data send: " + str(type(message)))
    print("Iter: " + str(i))


def send_avro_message(connection, numberOfPeople, i):
    
    message = {'id': i, 'name': 'Rosa Luxemburg', 'email': 'rosa.luxemburg@web.de', 'PhoneNumber': '01785250483'}
    buf = io.BytesIO();
    schema = avro.schema.Parse(open("schema/addressbook.avsc", "r").read())
    writer = avro.datafile.DataFileWriter(buf, avro.io.DatumWriter(), schema)
    for x in range(0,int(numberOfPeople)):   
        writer.append(message)
    writer.flush()
    buf.seek(0)
    data = buf.read()

    x = struct.pack('>I', len(data))

    connection.sendall(x)
    connection.sendall(data)
    print("Length of Avro data: " + str(len(data)))
    print("Type of Avro data send: " + str(type(data)))
    print("Iter: " + str(i))

def send_XML_message(connection, numberOfPeople, i):

    messages = '<xml version="1.0" encoding="UTF-8"> \n'

    for x in range(0, int(numberOfPeople)):
        message = """<AddressBook><Person><id>"""+str(x)+"""<id/><personName>Rosa Luxemburg<personName/><email>rosa.luxemburg@web.de<email/><PhoneNumber><number>01785250483<number/><PhoneNumber/><Person/><AddressBook/>"""
        messages += message + """ \n"""

    #xs = xmlschema.XMLSchema('schema/addressbook.xsd')
    #print(xs.types)
    #correct = xs.is_valid('schema/addressbook.xml')

    x = struct.pack('>I', len(messages))

    connection.sendall(x)
    connection.sendall(messages.encode())
    print("Length of XML data: " + str(len(messages.encode())))
    print("Type of XML data send: " + str(type(messages.encode())))
    print("Iter: " + str(i))

def main():

    #0 for protobuf, 1 for cap'n proto, 2 for Apache Avro, and 3 for XML
    printToFile = sys.argv[1]
    messageType = sys.argv[2]
    numberOfPeople = sys.argv[3]
    numberOfMessages = sys.argv[4]
    numberOfExperiments = sys.argv[5]
    machinesUsed = sys.argv[6]

    p = psutil.Process(os.getpid())
    cpu_util = []
    cpu_util_user = []
    cpu_util_system = []
    cpu_util_idle = []
    memory = []
    net_io_counters1 = []
    net_io_counters2 = []
        

    if int(messageType) == 0 :
        for i in range(0,int(numberOfExperiments)):
            #psutil.cpu_times_percent(None, False)
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #connection.connect(('172.16.150.67', 12345))
            #connection.connect(('127.0.0.1', 12345))
            connection.connect(('172.16.150.165', 12345))
            psutil.cpu_times_percent(None,False)
            psutil.cpu_percent(None, False)
            psutil.net_io_counters.cache_clear()
            for x in range(0,int(numberOfMessages)):
                send_proto_message(connection, numberOfPeople, i)
            #print(psutil.cpu_times_percent(0.0, False))
            #print(psutil.cpu_times())
            memory.append(psutil.virtual_memory().percent)
            cpu_util.append(psutil.cpu_percent(None, False))
            net_io_counters1.append(psutil.net_io_counters().bytes_sent)
            cpu_util_user.append(psutil.cpu_times_percent(None, False).user)
            cpu_util_system.append(psutil.cpu_times_percent(None, False).system)
            cpu_util_idle.append(psutil.cpu_times_percent(None, False).idle)

        with open('results/client_'+str(messageType)+'_'+str(numberOfPeople)+'_'+str(numberOfMessages)+'_'+str(printToFile)+'_'+str(machinesUsed)+'.txt', 'w') as f:
            f.write('CPU:'+ str(cpu_util)+'\n')
            f.write('CPU_USER:'+str(cpu_util_user)+'\n')
            f.write('CPU_SYSTEM:'+str(cpu_util_system)+'\n')
            f.write('CPU_IDLE:'+str(cpu_util_idle)+'\n')
            f.write('MEMORY:'+ str(memory)+'\n')
            f.write('bytes_sent:'+str(net_io_counters1)+'\n')
            f.write('packets_sent:'+str(net_io_counters2)+'\n')
            print('finished')
    elif int(messageType) == 1 :
        for i in range(0,int(numberOfExperiments)):
            #psutil.cpu_times_percent(1, False)
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #connection.connect(('172.16.150.67', 12345))
            #connection.connect(('127.0.0.1', 12345))
            connection.connect(('172.16.150.165',12345))
            psutil.cpu_times_percent(None,False)
            psutil.cpu_percent(None, False)
            psutil.net_io_counters.cache_clear()
            for x in range(0,int(numberOfMessages)):
                send_capnp_message(connection, numberOfPeople,i)
            memory.append(psutil.virtual_memory().percent)
            cpu_util.append(psutil.cpu_percent(None, False))
            net_io_counters1.append(psutil.net_io_counters().bytes_sent)
            cpu_util_user.append(psutil.cpu_times_percent(None, False).user)
            cpu_util_system.append(psutil.cpu_times_percent(None, False).system)
            cpu_util_idle.append(psutil.cpu_times_percent(None, False).idle)

        with open('results/client_'+str(messageType)+'_'+str(numberOfPeople)+'_'+str(numberOfMessages)+'_'+str(printToFile)+'_'+str(machinesUsed)+'.txt', 'w') as f:
            f.write('CPU:'+ str(cpu_util)+'\n')
            f.write('CPU_USER:'+str(cpu_util_user)+'\n')
            f.write('CPU_SYSTEM:'+str(cpu_util_system)+'\n')
            f.write('CPU_IDLE:'+str(cpu_util_idle)+'\n')
            f.write('MEMORY:'+ str(memory)+'\n')
            f.write('bytes_sent:'+str(net_io_counters1)+'\n')
            f.write('packets_sent:'+str(net_io_counters2)+'\n')
            print('finished')
    elif int(messageType) == 2 :
        for i in range(0,int(numberOfExperiments)):
            #psutil.cpu_times_percent(1, False)
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #connection.connect(('172.16.150.67', 12345))
            #connection.connect(('127.0.0.1', 12345))
            connection.connect(('172.16.150.165', 12345))
            psutil.cpu_times_percent(None,False)
            psutil.cpu_percent(None, False)
            psutil.net_io_counters.cache_clear()
            for x in range(0,int(numberOfMessages)):
                send_avro_message(connection, numberOfPeople,i)
            memory.append(psutil.virtual_memory().percent)
            cpu_util.append(psutil.cpu_percent(None, False))
            net_io_counters1.append(psutil.net_io_counters().bytes_sent)
            cpu_util_user.append(psutil.cpu_times_percent(None, False).user)
            cpu_util_system.append(psutil.cpu_times_percent(None, False).system)
            cpu_util_idle.append(psutil.cpu_times_percent(None, False).idle)

        with open('results/client_'+str(messageType)+'_'+str(numberOfPeople)+'_'+str(numberOfMessages)+'_'+str(printToFile)+'_'+str(machinesUsed)+'.txt', 'w') as f:
            f.write('CPU:'+ str(cpu_util)+'\n')
            f.write('CPU_USER:'+str(cpu_util_user)+'\n')
            f.write('CPU_SYSTEM:'+str(cpu_util_system)+'\n')
            f.write('CPU_IDLE:'+str(cpu_util_idle)+'\n')
            f.write('MEMORY:'+ str(memory)+'\n')
            f.write('bytes_sent:'+str(net_io_counters1)+'\n')
            f.write('packets_sent:'+str(net_io_counters2)+'\n')
            print('finished')
    elif int(messageType) == 3 :
        for i in range(0,int(numberOfExperiments)):
            #psutil.cpu_times_percent(1, False)
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #connection.connect(('172.16.150.67', 12345))
            #connection.connect(('127.0.0.1', 12345))
            connection.connect(('172.16.150.165',12345))
            psutil.cpu_times_percent(None,False)
            psutil.cpu_percent(None, False)
            psutil.net_io_counters.cache_clear()
            for x in range(0,int(numberOfMessages)):
                send_XML_message(connection, numberOfPeople,i)
            memory.append(psutil.virtual_memory().percent)
            cpu_util.append(psutil.cpu_percent(None, False))
            net_io_counters1.append(psutil.net_io_counters().bytes_sent)
            cpu_util_user.append(psutil.cpu_times_percent(None, False).user)
            cpu_util_system.append(psutil.cpu_times_percent(None, False).system)
            cpu_util_idle.append(psutil.cpu_times_percent(None, False).idle)

        with open('results/client_'+str(messageType)+'_'+str(numberOfPeople)+'_'+str(numberOfMessages)+'_'+str(printToFile)+'_'+str(machinesUsed)+'.txt', 'w') as f:
            f.write('CPU:'+ str(cpu_util)+'\n')
            f.write('CPU_USER:'+str(cpu_util_user)+'\n')
            f.write('CPU_SYSTEM:'+str(cpu_util_system)+'\n')
            f.write('CPU_IDLE:'+str(cpu_util_idle)+'\n')
            f.write('MEMORY:'+ str(memory)+'\n')
            f.write('bytes_sent:'+str(net_io_counters1)+'\n')
        print('finished')

if __name__ == '__main__':
    main()
