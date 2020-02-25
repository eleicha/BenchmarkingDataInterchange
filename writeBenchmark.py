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


times = []
cpu_utilization = []
cpu_util_user = []
cpu_util_system = []
cpu_util_idle = []
disk_info4 = []
disk_info6 = []
memory = []
time_stamp = []
start_value_disk = 0



def create_proto_message(numberOfPeople):

    address_book = addressBook_pb2.AddressBook()
    
    for x in range(0, int(numberOfPeople)):

        person = address_book.people.add()
        person.id = x
        person.name = "Rosa Luxemburg"
        person.email = "rosa.luxemburg@web.de"
        phone = person.phones.add()
        phone.number = "0178525048"

    message = address_book.SerializeToString();

    return(message)


def create_capnp_message(numberOfPeople):
    

    addresses = addressbook_capnp.AddressBook.new_message()
    people = addresses.init("people", int(numberOfPeople))

    for x in range(0, int(numberOfPeople)):
        people[x].name = "Rosa Luxemburg"
        people[x].id = int(x)
        people[x].email = "rosa.luxemburg@web.de"

        rosaPhone = people[x].init("phones", 1)[0]

        rosaPhone.number = "01785250483"

    message = addresses.to_bytes_packed()

    return(message)


def create_avro_message(numberOfPeople):
    
    message = {'id': 1, 'name': 'Rosa Luxemburg', 'email': 'rosa.luxemburg@web.de', 'PhoneNumber': '01785250483'}
    buf = io.BytesIO();
    schema = avro.schema.Parse(open("schema/addressbook.avsc", "r").read())
    writer = avro.datafile.DataFileWriter(buf, avro.io.DatumWriter(), schema)
    for x in range(0,int(numberOfPeople)):   
        writer.append(message)
    writer.flush()
    buf.seek(0)
    data = buf.read()

    return(data)

def create_XML_message(numberOfPeople):

    messages = '<xml version="1.0" encoding="UTF-8"> \n'

    for x in range(0, int(numberOfPeople)):
        message = """<AddressBook><Person><id>"""+str(x)+"""<id/><personName>Rosa Luxemburg<personName/><email>rosa.luxemburg@web.de<email/><PhoneNumber><number>01785250483<number/><PhoneNumber/><Person/><AddressBook/>"""
        messages += message + """ \n"""

    return(message.encode())

def handle_proto_print_to_file(message):

    f = open("schema/addressbook_proto.bin", "w+b")
    f.write(message)
    
    os.fsync(f)
    f.close()

def handle_capnp_print_to_file(message):

    f = open("schema/addressbook_capnp.bin", "w+b")
    f.write(message)
    os.fsync(f)
    f.close()
 
def handle_avro_print_to_file(message):

    schema = avro.schema.Parse(open("schema/addressbook.avsc", "rb").read())

    message_buf = io.BytesIO(message)
    reader = avro.datafile.DataFileReader(message_buf, avro.io.DatumReader())

    dataFile = open("schema/addressbook.avro", "wb")

    writer = DataFileWriter(dataFile, DatumWriter(), schema)

    for thing in reader:
        writer.append(thing)
    reader.close()
    
    writer.close()

def handle_XML_print_to_file(message):

    f = open("schema/addressbook.xml", "wb")

    f.write(message)

    os.fsync(f)
    f.close()

def clear_stats():

    start = time.perf_counter()
    psutil.cpu_percent(None, False)
    psutil.cpu_times_percent(None,False)
    psutil.net_io_counters.cache_clear()
    psutil.disk_io_counters.cache_clear()
    start_value_disk = psutil.disk_io_counters().write_bytes

    return start, start_value_disk

def clear_vars():
    
    del times[:]
    del cpu_utilization[:]
    del cpu_util_user[:]
    del cpu_util_system[:]
    del cpu_util_idle[:]
    del disk_info4[:]
    del disk_info6[:]
    del memory[:]
    del time_stamp[:]

def create_stats(start, start_value_disk):

    times.append(time.perf_counter() - start)
    memory.append(psutil.virtual_memory().percent)
    time_stamp.append(time.perf_counter())
    cpu_utilization.append(psutil.cpu_percent(None, False))
    cpu_util_user.append(psutil.cpu_times_percent(None, False).user)
    cpu_util_system.append(psutil.cpu_times_percent(None, False).system)
    cpu_util_idle.append(psutil.cpu_times_percent(None, False).idle)

    disk_info4.append(psutil.disk_io_counters().write_bytes)
    disk_info6.append(psutil.disk_io_counters().write_time)

def write_stats(protocol, numberOfPeople, numberOfExperiments, length, task):

    with open('results/'+task+'_'+str(protocol)+'_'+str(numberOfPeople)+'_'+str(numberOfExperiments)+'.txt', 'w') as f:
        f.write('CPU_UTIL:'+str(cpu_utilization)+'\n')
        f.write('CPU_USER:'+str(cpu_util_user)+'\n')
        f.write('CPU_SYSTEM:'+str(cpu_util_system)+'\n')
        f.write('CPU_IDLE:'+str(cpu_util_idle)+'\n')
        f.write('time_stamp:'+str(time_stamp)+'\n')
        f.write('MEMORY:'+ str(memory)+'\n')
        f.write('TIMES:'+str(times)+'\n')
        f.write('write_bytes:'+str(disk_info4)+'\n')
        f.write('write_time:'+str(disk_info6)+'\n')
        f.write('start_value_disk:'+str(start_value_disk)+'\n')
        f.write('length:'+str(length)+'\n')

def main():

    numberOfPeople = sys.argv[1]
    numberOfExperiments = sys.argv[2]

    for x in range(1,int(numberOfExperiments)+1):

        start, start_value_disk = clear_stats()

        proto = create_proto_message(numberOfPeople)

        create_stats(start, start_value_disk)

    write_stats('protobuf', numberOfPeople, numberOfExperiments, len(proto), 'creation')
    clear_vars()
    print('Finish creating proto')

    for x in range(1,int(numberOfExperiments)+1):

        start, start_value_disk = clear_stats()

        capnp = create_capnp_message(numberOfPeople)

        create_stats(start, start_value_disk)

    write_stats('capnp', numberOfPeople, numberOfExperiments, len(capnp), 'creation')
    clear_vars()
    print('Finish creating capnp')

    for x in range(1,int(numberOfExperiments)+1):

        start, start_value_disk = clear_stats()

        avro = create_avro_message(numberOfPeople)

        create_stats(start, start_value_disk)

    write_stats('avro', numberOfPeople, numberOfExperiments, len(avro), 'creation')
    clear_vars()

    print('Finish creating avro')


    for x in range(1,int(numberOfExperiments)+1):

        start, start_value_disk = clear_stats()

        xml = create_XML_message(numberOfPeople)

        create_stats(start, start_value_disk)

    write_stats('xml', numberOfPeople, numberOfExperiments, len(xml), 'creation')
    clear_vars()

    print('Finish creating xml')

    for x in range(1,int(numberOfExperiments)+1):

        start, start_value_disk = clear_stats()

        handle_proto_print_to_file(proto)

        create_stats(start, start_value_disk)

    write_stats('protobuf', numberOfPeople, numberOfExperiments, len(proto), 'writing')
    clear_vars()

    print('Finish writing proto')

    for x in range(1,int(numberOfExperiments)+1):

        start, start_value_disk = clear_stats()

        handle_capnp_print_to_file(capnp)

        create_stats(start, start_value_disk)

    write_stats('capnp', numberOfPeople, numberOfExperiments, len(capnp), 'writing')
    clear_vars()

    print('Finish writing capnp')

    for x in range(1,int(numberOfExperiments)+1):

        start, start_value_disk = clear_stats()

        handle_avro_print_to_file(avro)

        create_stats(start, start_value_disk)

    write_stats('avro', numberOfPeople, numberOfExperiments, len(avro), 'writing')
    clear_vars()

    print('Finish writing avro')

    for x in range(1,int(numberOfExperiments)+1):

        start, start_value_disk = clear_stats()

        handle_XML_print_to_file(xml)

        create_stats(start, start_value_disk)

    write_stats('xml', numberOfPeople, numberOfExperiments, len(xml), 'writing')
    clear_vars()

    print('Finish writing xml')


if __name__ == '__main__':
    main()
