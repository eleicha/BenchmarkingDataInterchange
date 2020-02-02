@0xbaa291b123bfd08b;

struct Person {
  id @0 :UInt32;
  name @1 :Text;
  email @2 :Text;
  phones @3 :List(PhoneNumber);

  struct PhoneNumber {
    number @0 :Text;
  }

}

struct AddressBook {
  people @0 :List(Person);
}
