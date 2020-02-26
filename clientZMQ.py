import io
import json
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
import time
import zmq
from zmq import ssh

def send_proto_message(connection, numberOfPeople, i):

    address_book = addressBook_pb2.AddressBook()
    
    for x in range(1, int(numberOfPeople)+1):

        person = address_book.people.add()
        person.id = x
        person.name = "Rosa Luxemburg"
        person.email = "rosa.luxemburg@web.de"
        phone = person.phones.add()
        phone.number = "0178525048"

    message = address_book.SerializeToString()

    connection.send(message)
    print("Length of send Proto data: " + str(len(message)))
    print("Type of Proto data send: " + str(type(message)))
    print("Iter: " + str(i))

    return(len(message))


def send_capnp_message(connection, numberOfPeople, i):
    

    addresses = addressbook_capnp.AddressBook.new_message()
    people = addresses.init("people", int(numberOfPeople)+1)

    for x in range(1, int(numberOfPeople)+1):
        people[x].name = "Rosa Luxemburg"
        people[x].id = int(i)
        people[x].email = "rosa.luxemburg@web.de"

        rosaPhone = people[x].init("phones", 1)[0]

        rosaPhone.number = "01785250483"

    message = addresses.to_bytes_packed()

    connection.send(message)
    print("Length of send Capnp data: " + str(len(message)))
    print("Type of Capnp data send: " + str(type(message)))
    print("Iter: " + str(i))

    return(len(message))


def send_avro_message(connection, numberOfPeople, i):
    
    message = {'id': i, 'name': 'Rosa Luxemburg', 'email': 'rosa.luxemburg@web.de', 'PhoneNumber': '01785250483'}
    buf = io.BytesIO()
    schema = avro.schema.Parse(open("schema/addressbook.avsc", "r").read())
    writer = avro.datafile.DataFileWriter(buf, avro.io.DatumWriter(), schema)
    for x in range(1, int(numberOfPeople)+1):
        writer.append(message)
    writer.flush()
    buf.seek(0)
    data = buf.read()

    connection.send(data)
    print("Length of Avro data: " + str(len(data)))
    print("Type of Avro data send: " + str(type(data)))
    print("Iter: " + str(i))

    return(len(data))

def send_XML_message(connection, numberOfPeople, i):

    messages = '<xml version="1.0" encoding="UTF-8"> \n'

    for x in range(1, int(numberOfPeople)+1):
        message = """<AddressBook><Person><id>"""+str(x)+"""<id/><personName>Rosa Luxemburg<personName/><email>rosa.luxemburg@web.de<email/><PhoneNumber><number>01785250483<number/><PhoneNumber/><Person/><AddressBook/>"""
        messages += message + """ \n"""

    #xs = xmlschema.XMLSchema('schema/addressbook.xsd')
    #print(xs.types)
    #correct = xs.is_valid('schema/addressbook.xml')

    connection.send_string(messages)
    print("Length of XML data: " + str(len(messages.encode())))
    print("Type of XML data send: " + str(type(messages.encode())))
    print("Iter: " + str(i))

    return(len(messages))

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
    start_value_bytes_sent = psutil.net_io_counters().bytes_sent
    times = []
    message_length = []
    context = zmq.Context()
            
    #for numberOfPeople in range(1,int(numberOfPeopleOrigin)+1):

    #psutil.cpu_times_percent(None, False)
    socket = context.socket(zmq.REQ)
    #connection.connect(('172.16.150.67', 12345))
    socket.connect("tcp://192.168.43.156:5555")
    #ssh.tunnel_connection(socket, "tcp://192.168.2.105:5555")
    #connection.connect(('192.168.2.104', 5555))

    if int(messageType) == 0:
        for i in range(1,int(numberOfExperiments)+1):

            #psutil.cpu_times_percent(None,False)
            #psutil.cpu_percent(None, False)
            psutil.net_io_counters.cache_clear()
            

            for x in range(1,int(numberOfMessages)+1):
                start = time.perf_counter()
                mem = send_proto_message(socket, numberOfPeople, i)

                message_length.append(mem)
                times.append(time.perf_counter() - start)
                #memory.append(psutil.virtual_memory().percent)
                #cpu_util.append(psutil.cpu_percent(None, False))
                net_io_counters1.append(psutil.net_io_counters().bytes_sent)
                #cpu_util_user.append(psutil.cpu_times_percent(None, False).user)
                #cpu_util_system.append(psutil.cpu_times_percent(None, False).system)
                #cpu_util_idle.append(psutil.cpu_times_percent(None, False).idle)

                answer = socket.recv()
                print("Received reply %s: %s" % (i, answer))

        with open('results/client_'+str(messageType)+'_'+str(numberOfPeople)+'_'+str(numberOfMessages)+'_'+str(printToFile)+'_'+str(machinesUsed)+'.txt', 'w') as f:
            #f.write('CPU:'+ str(cpu_util)+'\n')
            #f.write('CPU_USER:'+str(cpu_util_user)+'\n')
            #f.write('CPU_SYSTEM:'+str(cpu_util_system)+'\n')
            #f.write('CPU_IDLE:'+str(cpu_util_idle)+'\n')
            #f.write('MEMORY:'+ str(memory)+'\n')
            f.write('TIME:'+str(times)+'\n')
            f.write('message_length:'+str(message_length)+'\n')
            f.write('bytes_sent:'+str(net_io_counters1)+'\n')
            f.write('start_value_bytes_sent:'+str(start_value_bytes_sent)+'\n')
        print('finished')

    elif int(messageType) == 1 :
        for i in range(1,int(numberOfExperiments)+1):

            #psutil.cpu_times_percent(None,False)
            #psutil.cpu_percent(None, False)
            psutil.net_io_counters.cache_clear()

            for x in range(0,int(numberOfMessages)):
                start = time.perf_counter()
                mem = send_capnp_message(socket, numberOfPeople,i)
                message_length.append(mem)
                times.append(time.perf_counter() - start)
                #memory.append(psutil.virtual_memory().percent)
                #cpu_util.append(psutil.cpu_percent(None, False))
                net_io_counters1.append(psutil.net_io_counters().bytes_sent)
                #cpu_util_user.append(psutil.cpu_times_percent(None, False).user)
                #cpu_util_system.append(psutil.cpu_times_percent(None, False).system)
                #cpu_util_idle.append(psutil.cpu_times_percent(None, False).idle)

                answer = socket.recv()
                print("Received reply %s: %s" % (i, answer))

        with open('results/client_'+str(messageType)+'_'+str(numberOfPeople)+'_'+str(numberOfMessages)+'_'+str(printToFile)+'_'+str(machinesUsed)+'.txt', 'w') as f:
            #f.write('CPU:'+ str(cpu_util)+'\n')
            #f.write('CPU_USER:'+str(cpu_util_user)+'\n')
            #f.write('CPU_SYSTEM:'+str(cpu_util_system)+'\n')
            #f.write('CPU_IDLE:'+str(cpu_util_idle)+'\n')
            #f.write('MEMORY:'+ str(memory)+'\n')
            f.write('TIME:'+str(times)+'\n')
            f.write('message_length:'+str(message_length)+'\n')
            f.write('bytes_sent:'+str(net_io_counters1)+'\n')
            f.write('start_value_bytes_sent:'+str(start_value_bytes_sent)+'\n')
        print('finished')
    elif int(messageType) == 2 :
        for i in range(1,int(numberOfExperiments)+1):

            #psutil.cpu_times_percent(None,False)
            #psutil.cpu_percent(None, False)
            psutil.net_io_counters.cache_clear()
            
            for x in range(0,int(numberOfMessages)):
                start = time.perf_counter()
                mem = send_avro_message(socket, numberOfPeople,i)
                message_length.append(mem)
                times.append(time.perf_counter() - start)
                #memory.append(psutil.virtual_memory().percent)
                #cpu_util.append(psutil.cpu_percent(None, False))
                net_io_counters1.append(psutil.net_io_counters().bytes_sent)
                #cpu_util_user.append(psutil.cpu_times_percent(None, False).user)
                #cpu_util_system.append(psutil.cpu_times_percent(None, False).system)
                #cpu_util_idle.append(psutil.cpu_times_percent(None, False).idle)

                answer = socket.recv()
                print("Received reply %s: %s" % (i, answer))

        with open('results/client_'+str(messageType)+'_'+str(numberOfPeople)+'_'+str(numberOfMessages)+'_'+str(printToFile)+'_'+str(machinesUsed)+'.txt', 'w') as f:
            #f.write('CPU:'+ str(cpu_util)+'\n')
            #f.write('CPU_USER:'+str(cpu_util_user)+'\n')
            #f.write('CPU_SYSTEM:'+str(cpu_util_system)+'\n')
            #f.write('CPU_IDLE:'+str(cpu_util_idle)+'\n')
            #f.write('MEMORY:'+ str(memory)+'\n')
            f.write('TIME:'+str(times)+'\n')
            f.write('message_length:'+str(message_length)+'\n')
            f.write('bytes_sent:'+str(net_io_counters1)+'\n')
            f.write('start_value_bytes_sent:'+str(start_value_bytes_sent)+'\n')
        print('finished')
    elif int(messageType) == 3 :
        for i in range(1,int(numberOfExperiments)+1):

            #psutil.cpu_times_percent(None,False)
            #psutil.cpu_percent(None, False)
            psutil.net_io_counters.cache_clear()
            
            for x in range(0,int(numberOfMessages)):
                start = time.perf_counter()
                mem=send_XML_message(socket, numberOfPeople,i)
                message_length.append(mem)
                times.append(time.perf_counter() - start)
                #memory.append(psutil.virtual_memory().percent)
                #cpu_util.append(psutil.cpu_percent(None, False))
                net_io_counters1.append(psutil.net_io_counters().bytes_sent)
                #cpu_util_user.append(psutil.cpu_times_percent(None, False).user)
                #cpu_util_system.append(psutil.cpu_times_percent(None, False).system)
                #cpu_util_idle.append(psutil.cpu_times_percent(None, False).idle)

                answer = socket.recv()
                print("Received reply %s: %s" % (i, answer))

        with open('results/client_'+str(messageType)+'_'+str(numberOfPeople)+'_'+str(numberOfMessages)+'_'+str(printToFile)+'_'+str(machinesUsed)+'.txt', 'w') as f:
            #f.write('CPU:'+ str(cpu_util)+'\n')
            #f.write('CPU_USER:'+str(cpu_util_user)+'\n')
            #f.write('CPU_SYSTEM:'+str(cpu_util_system)+'\n')
            #f.write('CPU_IDLE:'+str(cpu_util_idle)+'\n')
            #f.write('MEMORY:'+ str(memory)+'\n')
            f.write('TIME:'+str(times)+'\n')
            f.write('message_length:'+str(message_length)+'\n')
            f.write('bytes_sent:'+str(net_io_counters1)+'\n')
            f.write('start_value_bytes_sent:'+str(start_value_bytes_sent)+'\n')
        print('finished')

if __name__ == '__main__':
    main()
