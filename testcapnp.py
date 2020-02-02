import capnp
import addressbook_capnp


f = open("schema/addressbook_capnp.bin", 'rb')
addresses = addressbook_capnp.AddressBook.read(f)

people = addresses.people[0]

print(people)
