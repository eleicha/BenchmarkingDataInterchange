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
        people[x].id = x
        people[x].email = "rosa.luxemburg@web.de"

        rosaPhone = people[x].init("phones", 1)[0]

        rosaPhone.number = "01785250483"

    message = addresses.to_bytes()

    x = struct.pack('>I', len(message))

    connection.sendall(x)
    connection.sendall(message)
    print("Length of send Capnp data: " + str(len(message)))
    print("Type of Capnp data send: " + str(type(message)))
    print("Iter: " + str(i))


def send_avro_message(connection, numberOfPeople, i):
    
    message = {'id': 1, 'name': 'Rosa Luxemburg', 'email': 'rosa.luxemburg@web.de', 'PhoneNumber': '01785250483'}
    buf = io.BytesIO();
    schema = avro.schema.Parse(open("schema/addressbook.avsc", "r").read())
    writer = avro.datafile.DataFileWriter(buf, avro.io.DatumWriter(), schema)
    for x in range(0,int(numberOfPeople)):   
        writer.append(message)
    writer.flush()
    buf.seek(0)
    data = buf.read()

    connection.sendall(data)
    print("Length of Avro data: " + str(len(data)))
    print("Type of Avro data send: " + str(type(data)))
    print("Iter: " + str(i))

def main():

    #0 for protobuf, 1 for cap'n proto, and 2 for Apache Avro
    printToFile = sys.argv[1]
    messageType = sys.argv[2]
    numberOfPeople = sys.argv[3]
    numberOfMessages = sys.argv[4]
    numberOfExperiments = sys.argv[5]

    p = psutil.Process(os.getpid())
    psutil.cpu_percent(None, False)
    cpu_util = []
    memory = []
    net_io_counters1 = []
    net_io_counters2 = []

    for i in range(0,int(numberOfExperiments)):
        

        if int(messageType) == 0 :
            for x in range(0,int(numberOfMessages)):
                #psutil.cpu_times_percent(None, False)
                connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                connection.connect(('127.0.0.1', 12345))
                send_proto_message(connection, numberOfPeople, i)
                #print(psutil.cpu_times_percent(0.0, False))
                #print(psutil.cpu_times())
            memory.append(psutil.virtual_memory().percent)
            cpu_util.append(psutil.cpu_percent(None, False))
            net_io_counters1.append(psutil.net_io_counters().bytes_recv)
            net_io_counters2.append(psutil.net_io_counters().packets_recv)
        elif int(messageType) == 1 :
            for x in range(0,int(numberOfMessages)):
                psutil.cpu_times_percent(1, False)
                connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                connection.connect(('127.0.0.1', 12345))
                send_capnp_message(connection, numberOfPeople,i)
            memory.append(psutil.virtual_memory().percent)
            cpu_util.append(psutil.cpu_percent(None, False))
            net_io_counters1.append(psutil.net_io_counters().bytes_recv)
            net_io_counters2.append(psutil.net_io_counters().packets_recv)
        elif int(messageType) == 2 :
            for x in range(0,int(numberOfMessages)):
                psutil.cpu_times_percent(1, False)
                connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                connection.connect(('127.0.0.1', 12345))
                send_avro_message(connection, numberOfPeople,i)
            memory.append(psutil.virtual_memory().percent)
            cpu_util.append(psutil.cpu_percent(None, False))
            net_io_counters1.append(psutil.net_io_counters().bytes_recv)
            net_io_counters2.append(psutil.net_io_counters().packets_recv)

        with open('results/serverResult_'+str(messageType)+'_'+str(numberOfPeople)+'_'+str(numberOfMessages)+'_'+str(printToFile)+'.txt', 'w') as f:
            f.write('CPU: '+ str(cpu_util)+'\n')
            f.write('MEMORY: '+ str(memory)+'\n')
            f.write('bytes_sent: '+str(net_io_counters1)+'\n')
            f.write('packets_sent: '+str(net_io_counters2)+'\n')
    print('finished')

if __name__ == '__main__':
    main()
