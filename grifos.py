class rotter:
    def __init__(self,rotter_alfabet,starting_position) -> None:
        self.total_rotations=starting_position
        self.rotter_alfabet=rotter_alfabet
        self.alfabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def return_rotations(self):
        return self.total_rotations

    def rotate(self,key,flag):
        if self.total_rotations<=24 and flag==True:
            self.total_rotations+=1
        elif self.total_rotations>25 and flag==True:
            self.total_rotations=0
        try:
            return self.rotter_alfabet[(self.alfabet.index(key.upper())+self.total_rotations-1)%26].upper()
        except:
            self.total_rotations-=1
            return key

    def de_rotate(self,key,flag):
        if self.total_rotations<=24 and flag==True:
            self.total_rotations+=1
        elif self.total_rotations>25 and flag==True:
            self.total_rotations=0
        try:
            return self.alfabet[(self.rotter_alfabet.index(key.upper())-self.total_rotations+1)%26].upper()
        except:
            self.total_rotations-=1
            return key

class rotter_engine:
    def __init__(self,rotter_a,rotter_b,rotter_c) -> None:
        self.rotter_a=rotter_a
        self.rotter_b=rotter_b
        self.rotter_c=rotter_c
        self.rotter_a_rotations=self.rotter_a.return_rotations()
        self.rotter_b_rotations=self.rotter_b.return_rotations()
        self.rotter_c_rotations=self.rotter_c.return_rotations()
        self.alfabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def execute_encryption(self,key):

        if self.rotter_a_rotations<25:
            if key.upper() in self.alfabet:
                self.rotter_a_rotations+=1
            output=self.rotter_a.rotate(key,True)
            output=self.rotter_b.rotate(output,False)
            output=self.rotter_c.rotate(output,False)
            output=self.rotter_c.rotate(output,False)
            output=self.rotter_b.rotate(output,False)
            output=self.rotter_a.rotate(output,False)
            
        elif self.rotter_a_rotations>=25 and self.rotter_b_rotations<25:
            if key.upper() in self.alfabet:
                self.rotter_a_rotations=0
                self.rotter_b_rotations+=1
            output=self.rotter_a.rotate(key,True)
            output=self.rotter_b.rotate(output,True)
            output=self.rotter_c.rotate(output,False)
            output=self.rotter_c.rotate(output,False)
            output=self.rotter_b.rotate(output,False)
            output=self.rotter_a.rotate(output,False)

        elif self.rotter_a_rotations>=25 and self.rotter_b_rotations>=25 and self.rotter_c_rotations<25:
            if key.upper() in self.alfabet:
                self.rotter_a_rotations=0
                self.rotter_b_rotations=0
                self.rotter_c_rotations+=1
            output=self.rotter_a.rotate(key,True)
            output=self.rotter_b.rotate(output,True)
            output=self.rotter_c.rotate(output,True)
            output=self.rotter_c.rotate(output,False)
            output=self.rotter_b.rotate(output,False)
            output=self.rotter_a.rotate(output,False)

        elif self.rotter_a_rotations>=25 and self.rotter_b_rotations>=25 and self.rotter_c_rotations>=25:
            if key.upper() in self.alfabet:
                self.rotter_a_rotations=0
                self.rotter_b_rotations=0
                self.rotter_c_rotations=0
            output=self.rotter_a.rotate(key,True)
            output=self.rotter_b.rotate(output,True)
            output=self.rotter_c.rotate(output,True)
            output=self.rotter_c.rotate(output,False)
            output=self.rotter_b.rotate(output,False)
            output=self.rotter_a.rotate(output,False)
        return output

    def execute_decryption(self,key):

        if self.rotter_a_rotations<25:
            if key.upper() in self.alfabet:
                self.rotter_a_rotations+=1
            output=self.rotter_a.de_rotate(key,True)
            output=self.rotter_b.de_rotate(output,False)
            output=self.rotter_c.de_rotate(output,False)
            output=self.rotter_c.de_rotate(output,False)
            output=self.rotter_b.de_rotate(output,False)
            output=self.rotter_a.de_rotate(output,False)

        elif self.rotter_a_rotations>=25 and self.rotter_b_rotations<25:
            if key.upper() in self.alfabet:
                self.rotter_a_rotations=0
                self.rotter_b_rotations+=1
            output=self.rotter_a.de_rotate(key,True)
            output=self.rotter_b.de_rotate(output,True)
            output=self.rotter_c.de_rotate(output,False)
            output=self.rotter_c.de_rotate(output,False)
            output=self.rotter_b.de_rotate(output,False)
            output=self.rotter_a.de_rotate(output,False)

        elif self.rotter_a_rotations>=25 and self.rotter_b_rotations>=25 and self.rotter_c_rotations<25:
            if key.upper() in self.alfabet:
                self.rotter_a_rotations=0
                self.rotter_b_rotations=0
                self.rotter_c_rotations+=1
            output=self.rotter_a.de_rotate(key,True)
            output=self.rotter_b.de_rotate(output,True)
            output=self.rotter_c.de_rotate(output,True)
            output=self.rotter_c.de_rotate(output,False)
            output=self.rotter_b.de_rotate(output,False)
            output=self.rotter_a.de_rotate(output,False)

        elif self.rotter_a_rotations>=25 and self.rotter_b_rotations>=25 and self.rotter_c_rotations>=25:
            if key.upper() in self.alfabet:
                self.rotter_a_rotations=0
                self.rotter_b_rotations=0
                self.rotter_c_rotations=0
            output=self.rotter_a.de_rotate(key,True)
            output=self.rotter_b.de_rotate(output,True)
            output=self.rotter_c.de_rotate(output,True)
            output=self.rotter_c.de_rotate(output,False)
            output=self.rotter_b.de_rotate(output,False)
            output=self.rotter_a.de_rotate(output,False)
        return output

class plugboard:
        def __init__(self,plug_alfabet) -> None:
            self.alfabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            self.plug_alfabet=plug_alfabet
            
        def swap_letter(self,key):
            if key.upper() in self.alfabet:
                return self.plug_alfabet[self.alfabet.index(key.upper())]
            else:
                return key
    
        def original_letter(self,key):
            if key.upper() in self.alfabet:
                return self.alfabet[self.plug_alfabet.index(key.upper())]
            else:
                return key

class jumper:
    def __init__(self) -> None:
        self.counter=0
        self.rotters=[['P','E','F','B','H','J','M','U','Y','V','X','S','D','L','K','A','Z','G','I','W','C','N','T','R','Q','O'],
                    ['J','F','L','H','B','M','O','D','E','S','U','T','R','Z','G','W','P','I','V','C','Q','Y','X','K','A','N'],
                    ['K','J','M','U','L','F','T','D','Z','X','I','E','W','B','A','N','G','Q','H','P','S','C','Y','O','V','R'],
                    ['O','U','H','D','F','Z','E','A','P','J','X','M','L','S','N','G','T','V','B','C','R','I','Q','W','Y','K'],
                    ['D','Y','O','N','V','R','J','P','G','F','T','H','C','S','M','Z','B','K','L','E','A','U','I','X','W','Q'],
                    ['Y','K','T','M','V','S','R','C','A','I','D','N','F','X','J','G','L','U','Q','W','E','O','H','P','B','Z'],
                    ['Z','D','N','M','X','Q','T','O','H','R','K','Y','S','I','W','U','V','G','E','F','L','P','J','C','B','A'],
                    ['G','R','Z','U','L','D','J','S','M','Y','E','V','W','B','Q','I','X','A','N','O','K','T','F','C','P','H'],
                    ['H','E','A','R','L','K','X','Q','Y','I','J','S','P','B','T','D','F','Z','U','C','W','G','M','O','V','N'],
                    ['L','W','S','T','V','Q','D','E','I','U','A','M','C','K','F','Z','N','G','O','H','J','B','X','R','P','Y'],
                    ['A','M','N','R','O','G','B','V','I','D','Q','K','C','L','H','E','Z','P','J','T','W','S','X','F','Y','U'],
                    ['X','D','I','O','W','A','V','E','Y','T','J','M','U','N','F','S','C','Q','K','B','H','R','P','L','G','Z'],
                    ['B','V','N','P','G','J','W','E','I','C','Y','S','X','M','O','U','A','Z','Q','D','K','H','F','R','L','T'],
                    ['N','R','K','S','U','L','D','Z','T','G','P','B','W','H','A','V','I','M','Q','Y','O','J','E','X','F','C'],
                    ['M','U','A','H','K','E','S','N','G','Y','T','F','R','Q','D','W','V','P','I','C','B','Z','X','L','J','O'],
                    ['P','R','C','M','S','G','Y','A','U','E','K','W','T','Q','B','O','Z','N','I','L','D','X','V','J','F','H'],
                    ['Y','N','T','X','C','G','M','O','V','K','U','Q','F','I','H','Z','R','E','S','B','A','J','P','D','W','L'],
                    ['C','Y','G','P','S','T','I','H','M','U','W','Z','A','J','B','R','L','V','E','D','Q','F','X','K','O','N'],
                    ['K','C','V','F','J','M','G','H','D','I','X','A','R','P','S','Y','L','Q','N','Z','T','E','U','O','B','W'],
                    ['E','K','M','V','Y','Z','N','I','T','U','C','J','W','X','R','F','P','B','L','S','G','D','A','Q','H','O'],
                    ['X','V','B','R','H','L','I','K','W','F','P','Q','N','M','C','Z','E','J','T','S','O','D','U','Y','G','A'],
                    ['D','G','M','Z','E','H','B','S','K','P','N','Q','J','X','O','U','R','Y','A','F','I','W','T','C','L','V'],
                    ['N','L','G','J','O','M','C','R','K','F','X','I','Z','A','Y','D','W','H','S','U','P','T','B','E','V','Q'],
                    ['N','L','R','K','V','Y','T','I','O','S','H','E','M','C','X','J','W','G','U','B','Q','F','D','Z','P','A'],
                    ['Y','T','U','A','G','J','S','Z','B','W','X','F','L','K','R','D','V','H','P','O','C','N','E','I','Q','M'],
                    ['A','L','B','S','G','O','D','N','C','J','M','P','V','F','I','K','Z','R','U','W','H','T','Q','E','X','Y'],
                    ['P','Z','I','U','C','X','H','T','Q','G','B','M','J','K','W','Y','R','E','F','D','S','O','L','N','V','A'],
                    ['P','J','G','L','I','A','M','Y','F','V','N','S','B','D','T','R','Q','E','W','K','X','H','C','U','O','Z'],
                    ['W','O','B','V','X','P','A','Q','J','C','K','G','F','Z','U','M','T','N','Y','H','S','L','E','D','I','R'],
                    ['Q','V','M','T','D','W','E','Y','S','P','R','F','L','J','H','I','A','G','B','N','K','U','O','C','Z','X'],
                    ['Z','O','C','L','R','W','N','X','G','K','H','U','M','P','A','D','I','Q','F','Y','J','B','V','E','S','T']]
        self.counter_a=0
        self.counter_b=0
        self.counter_c=0
        self.counter_a_r=0
        self.counter_b_r=0
        self.counter_c_r=0
        self.flag=False

    def change_rotters(self,key):
        if self.flag==False:
            res = [int(x) for x in str(key)]
            if len(res)<12:
                while len(res)<=12:
                    res.append(0)

            elif len(res)>12:
                while len(res)>=12:
                    res.pop(len(res)-1)

            rotter_a=res[0]*10+res[1]
            rotter_a_r=res[2]*10+res[3]
            if rotter_a>30:
                rotter_a=30
            if rotter_a_r>25:
                rotter_a_r=0

            rotter_b=res[4]*10+res[5]+self.counter
            rotter_b_r=res[6]*10+res[7]+self.counter
            if rotter_b>30:
                rotter_b=30
            if rotter_b_r>25:
                rotter_b_r=0

            rotter_c=res[8]*10+res[9]+self.counter
            rotter_c_r=res[10]*10+res[11]+self.counter
            if rotter_c>30:
                rotter_c=30
            if rotter_c_r>25:
                rotter_c_r=0
            self.counter_a_r=rotter_a_r
            self.counter_b_r=rotter_b_r
            self.counter_c_r=rotter_c_r  
            self.flag==True
            return rotter_engine(rotter(self.rotters[rotter_a],rotter_a_r),rotter(self.rotters[rotter_b],rotter_b_r),rotter(self.rotters[rotter_c],rotter_c_r))
        
        elif self.flag==True:
            if self.counter_a>30:
                self.counter_a=0
            if self.counter_b>30:
                self.counter_b=0
            if self.counter_c>30:
                self.counter_c=0
            self.counter_a+=1
            self.counter_b+=1
            self.counter_c+=1
            return rotter_engine(rotter(self.rotters[rotter_a+self.counter_a],rotter_a_r),rotter(self.rotters[rotter_b+self.counter_b],rotter_b_r),rotter(self.rotters[rotter_c+self.counter_c],rotter_c_r))

class engine:
    def __init__(self,*inp) -> None:
        if len(inp) == 1:
            self.engine_plugboard=plugboard(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
            self.engine_jumper=jumper()
            self.engine_rotter_engine=self.engine_jumper.change_rotters(inp[0])
            self.characters=0
            self.key=inp[0]
        elif len(inp)==2:
            self.engine_plugboard=plugboard(inp[1])
            self.engine_jumper=jumper()
            self.engine_rotter_engine=self.engine_jumper.change_rotters(inp[0])
            self.characters=0
            self.key=inp[0]
        else:
            print("Error:Too many arguments\n")

    def encrypt(self,key):
        if self.characters==50:
            self.engine_rotter_engine=self.engine_jumper.change_rotters(self.key)
            self.characters=0
        self.characters+=1
        key=self.engine_plugboard.swap_letter(key)
        return self.engine_rotter_engine.execute_encryption(key)
    
    def decrypt(self,key):
        if self.characters==50:
            self.engine_rotter_engine=self.engine_jumper.change_rotters(self.key)
            self.characters=0
        self.characters+=1
        key=self.engine_rotter_engine.execute_decryption(key)
        return self.engine_plugboard.original_letter(key)
        return key

    def encrypt_file(self,file):
        out_f= open("output.txt","w")
        with open(file) as f:
         for line in f :
             for letter in line.lower():
                 out_f.write(self.encrypt(letter))

    def decrypt_file(self,file):
        out_f=open("reverse.txt","w")
        with open(file) as f:
         for line in f :
             for letter in line.lower():
                 out_f.write(self.decrypt(letter))

def main():                  
    eng1=engine(290029002900)
    eng1.encrypt_file("original.txt")
    
if __name__ == "__main__":
    main()

