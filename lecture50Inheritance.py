class  Phone:
    def  call(self):
        print("You  can  call")
    def  message(self):
        print("You  can  message")
class Samsung(Phone):

    def  photo(self):
        print("You  can  photo")

#Here  Samsung  Class  is  a  sub-class  of  Phone  Class. Bcz,  Samsung  Class inherit Phone Class
# Phone  Class  is  Super class  Here

p = Phone()
p.call()
p.message()

s = Samsung()
s.call()
s.message()
s.photo()

print(issubclass(Samsung,Phone))