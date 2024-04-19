class Number:
    def __init__(self,val):
        self.val = val
        # We should work to have val be either a string or a integer, should I make a second constructor?


    
    def convert(self,base): # assuming if they input one base its  gonna be base 10 to begin with - is that a stupid assumption?
        # CHECK WHAT THE BASE ACTUALLy IS - IS IT POSSIBLE TO DO THAT?
        return self.convert(10,base)
    

    def convert(self,prevBase, newBase):

        #ASIDE TO DO LATER -- add ability to take advantage of when newBase%prevBase==0, could be some time saving
        # def if newBase = prevBase*prevBase, same from prevBase**3

        # prevBase is the previous base lol, newBase is the base of the final number
        if  (prevBase not in range(2,64) or newBase not in range(2,64)):
            raise ValueError("You fuck faces! The functionality for this isn't built yet. Stick with bases 2 to 64 please (*/ω＼*)")
        
        total = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/" # length of 64, should work
        # Okay so this will be done in two parts even though this might be inneffecient
        # First is converting initial number to base 10, for those who arent in it

        amt = 0
        vals = dict()
        temp = str(self.val)
        

        if prevBase == 16:
            temp = str(self.val)[2:]
        if prevBase != 10:
            needed = total[:prevBase]
            for i in range(len(needed)): # initiates vals
                vals[needed[i]]= i


            for i in range(len(temp)):
                amt += vals[temp[i]] * (prevBase **(len(temp)-1-i))
        else: amt = int(temp)
                

        # Okay now that we have number in decimal, we generalize decToHex, which shouldn't be too bad eh
        #amt is the current amount lol
        if newBase == 10: return amt

        if newBase==16: 
            temporary = Number(amt)
            return temporary.decToHex() #cheaky reuse of functionality
        
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




    def decToHex(self):
        assert type(self.val) == int
        base = 16 # base, might customize function further

        vals = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'} # dictionary of hexademical values

        temp = self.val # made a duplicate for some reason

        string = "0X" # output string

        arr = []
        while(temp != 0):
            place = temp % base
            arr.append(vals[place])
            temp -= place
            temp /= base
        
        while(len(arr)!=0):
            string += arr.pop()

        return string # huzaah!

        
        
            

"""arr= []
for i in range(1,150):
    num = Number(i)
    arr.append(num.decToHex())
print(arr)

arr2 = []
for i in range(len(arr)):
    num = Number(arr[i])
    arr2.append(num.convert(16,10))
print(arr2)"""

if __name__ == '__main__':
    value = Number(3**10)
    print(value.convert(10,3)) # huzaah!

    variable = Number('0XBEC2')
    print(variable.convert(16,10)) # okay this works now


