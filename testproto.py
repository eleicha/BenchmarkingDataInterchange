import addressBook_pb2


address_book = addressBook_pb2.AddressBook()

f = open("schema/addressbook_proto.bin", "rb")
address_book.ParseFromString(f.read())
f.close()

print(address_book)
