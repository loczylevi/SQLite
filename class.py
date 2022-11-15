class Allatok:
    def eszik(self):
        print("ez az állat eszik")
    def alszik(self):
        print("ez az állat alszik")
        
class Elefant(Allatok):
    def szarazfoldi(self):
        print("ez az állat százazföldi")
            
            
class Ponty(Allatok):
    def vizi(self):
        print("ez az állat vizi")
        
class Nimfa_papagaj(Allatok):
    def repulo_allat(self):
        print("ez az állat repül")
        
elefant = Elefant()

ponty = Ponty()

nimfa = Nimfa_papagaj()

print(nimfa.eszik())
