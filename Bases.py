

class Number:
    def __init__(self,val, base = 10):
        
        self.negative = False
        if str(val) and str(val)[0]=='-': 
            val = str(val)[1:]
            self.negative = True
        self.val = str(val)
        # We should work to have val be either a string or a integer, should I make a second constructor?
        self.base = base
        
        
    def __repr__(self):
        sign = '-' if self.negative else ''
        return f"Number({sign+self.val}, base={self.base})"


    def convert(self,newBase): # note default param
        """
        Converts self from prevBase (default decimal) to radix newBase"""

        #ASIDE TO DO LATER -- add ability to take advantage of when newBase%prevBase==0, could be some time saving
        # def if newBase = prevBase**2, generalized to prevBase**n

        if  (self.base not in range(2,64) or newBase not in range(2,64)):
            raise ValueError("You goobers! The functionality for this isn't built yet. Stick with bases 2 to 64 please (*/ω＼*)")
        
        total = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/" # length of 64, should work
        # Okay so this will be done in two parts even though this might be inneffecient
        # First is converting initial number to base 10, for those who arent in it

        amt = 0
        vals = dict()
        temp = str(self.val)
        

        if self.base == 16:
            temp = str(self.val)[2:]
        if self.base != 10:
            needed = total[:self.base]
            for i in range(len(needed)): # initiates vals
                vals[needed[i]]= i


            for i in range(len(temp)):
                amt += vals[temp[i]] * (self.base **(len(temp)-1-i))
                
        else:  #base is 10
            amt = 0 if temp is None else int(temp)
                

        # Okay now that we have number in decimal, we generalize decToHex, which shouldn't be too bad eh
        #amt is the current amount lol
        if newBase == 10: return amt

        if newBase==16: 
            temporary = Number(amt)
            return temporary.decToHex() #cheaky reuse of functionality, not the best but whatev
        
        #Establish vals dictionary
        vals2 = dict()
        need = total[:newBase]
        for i in range(len(need)): # initiates vals
            vals2[i]= need[i]


        string = "" # output string

        arr = []
        while(amt != 0):
            place = amt % newBase
            arr.append(vals2[place])
            amt -= place
            amt /= newBase
        
        while(len(arr)!=0):
            string += arr.pop()

        return string # finally!
    
    def change_base(self, newBase):
        """Changes self.val and self.base according to radix newBase"""
        self.val = self.convert(newBase)
        self.base = newBase




    def decToHex(self): #first iteration of this function
        assert type(self.val) == int
        base = 16 # base, might customize function further

        vals = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'} # dictionary of hexademical values

        temp = self.val # made a duplicate for some reason

        string = "0x" # output string

        arr = []
        while(temp != 0):
            place = temp % base
            arr.append(vals[place])
            temp -= place
            temp /= base
        
        while(len(arr)!=0):
            string += arr.pop()

        return string 
    
    def to_binary(self):
        """Special function to help find the (signed/unsigned) binary equivalent of Number objects"""
        bit = '1' if self.negative else '0'
        return bit + self.convert(2)
    
    
    def complement(self):
        """Returns complement of self.val in number system w/ radix self.base"""
        pass
    #TODO: do this, then add, sub, etc

        
    def to_ones_complement(self):
        """Returns bitstring in form of ones complement; assumes input in base 10"""
        if not self.negative: return self.to_binary()
        binary = Number(abs(int(self.val))).to_binary()
        ones_complement = ""
        for bit in binary:
            ones_complement += '1' if bit=='0' else '0'
        return ones_complement
        
        
    def to_twos_complement(self):
        """Returns bitstring in form of twos complement; assumes input in base 10"""
        if not self.negative: return self.to_binary()
        twos = list(self.to_ones_complement())
        if all(bit=='1' for bit in twos): return '1' + ('0' * len(twos)) # for overflow
        for i in range(len(twos)-1,-1 ,-1):
            if twos[i]=='0':
                twos[i] = '1'
                break
        return ''.join(twos)
            
        
    
            


if __name__ == '__main__':
    # value = Number(3**10)
    # print(value.convert(3)) # huzaah!

    # variable = Number('0xBEC2',16)
    # print(variable.convert(10)) # okay this works now
    
    # num = Number(92)
    # print(num.val)
    # print(num.convert(2))
    # print(num.convert(8))
    # print(num.convert(16))
    
    #num = Number("77")
    #print(num.convert(2))
    
    v1 = Number(3)
    v2 = Number(1)
    v3 = Number(-1)
    v4 = Number(8)
    v5 = Number(-8)
    for v in [v1,v2,v3,v4,v5]:
        print(f'{v} becomes {v.to_ones_complement()} ones complement')
        print(f'{v} becomes {v.to_twos_complement()} ones complement')

    


