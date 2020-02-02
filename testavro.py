import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import json

'''
schema = avro.schema.Parse(open("schema/addressbook.avsc", "r").read())

writer = DataFileWriter(open("schema/addressbook.avro", "wb"), DatumWriter(), schema)
writer.append({'id': 1, 'name': 'Rosa Luxemburg', 'email': 'rosa.luxemburg@web.de', 'PhoneNumber': '01785250483'})

writer.close()
'''
reader = DataFileReader(open("schema/addressbook.avro", "rb"), DatumReader())
for user in reader:
    print (user)
reader.close()
