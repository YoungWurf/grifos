class Rotor:
    def __init__(self,wiring,position,notches):
        self.wiring = wiring
        self.position = position
        self.notches=notches

    def rotate(self,flag):
        if flag:
            self.position = (self.position + 1) % 26
            for notch in self.notches:
                if self.position==notch:
                    return True
            return False
    
    def return_rotor_position(self):
        return self.position
        
    def encode(self, letter):
        encoded_letter = self.wiring[(ord(letter)-65+self.position)%26]
        return encoded_letter

    def decode(self, letter):
        index = (self.wiring.index(letter) - self.position) % 26
        decoded_letter = chr(index + 65)
        return decoded_letter
    
class Plugboard:
    def __init__(self, wiring):
        self.wiring = wiring
        
    def swap(self, letter):
        return self.wiring.get(letter, letter)
    
    def set_wiring(self, wiring):
        self.wiring = wiring

class EnigmaMachine:
    def __init__(self,rotor_1,rotor_2,rotor_3,plugboard):
        self.rotor_1=rotor_1
        self.rotor_2=rotor_2
        self.rotor_3=rotor_3
        self.plugboard=plugboard

    def encode_message(self,message):
        encrypted_message=""
        for letter in message:
            self.rotor_3.rotate(self.rotor_2.rotate(self.rotor_1.rotate(True)))
            encrypted_message=encrypted_message+(self.rotor_3.encode(self.rotor_2.encode(self.rotor_1.encode(self.plugboard.swap(letter)))))
        return encrypted_message
            
    def decode_message(self,message):
        decrypted_message=""
        for letter in message:
            self.rotor_3.rotate(self.rotor_2.rotate(self.rotor_1.rotate(True)))
            decrypted_message=decrypted_message+(self.plugboard.swap(self.rotor_1.decode(self.rotor_2.decode(self.rotor_3.decode(letter)))))
        return decrypted_message

rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ",0,[2])
rotor2 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ",0,[4])
rotor3 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ",0,[5])
plugboard = Plugboard({"A": "B", "C": "D", "E": "F","B":"A","D":"C","F":"E"})

enigma=EnigmaMachine(rotor1,rotor2,rotor3,plugboard)
message="FOTIS"

