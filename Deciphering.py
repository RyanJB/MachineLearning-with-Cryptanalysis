#==============================================================================
# Ryan Brown - Using Machine Learning optimisation techniques to decipher a polyalphabetic cipher.
#==============================================================================
class deciphering(object):

    key = ""
    ascii_uppercase = 65
    decryptedMessage = []
    
    def __init__(self, msg, key):
        
        self.encryptedMessage = msg
        
        if type(key) == str:
            self.key = key
        elif type(key) == list:
            temp = ''.join(key)
            self.key = temp
       # print self.key
        
    def startDecryption(self):
        
        self.decryptedMessage = []
        #Ti = Ci - Ki (mod 26)
        self.key_num = 0
        
        for i in range(0, len(self.encryptedMessage)):
            
            charAtCipher = self.encryptedMessage[i]
            cipher_index = ord(charAtCipher)
            cipher_alphabet_index = cipher_index - self.ascii_uppercase
            
            charAtKey = self.key[self.key_num]
            key_index = ord(charAtKey)
            key_alphabet_index = key_index - self.ascii_uppercase
            
            if cipher_index >= 65 and cipher_index <= 90:
                
                self.shiftLetters(cipher_alphabet_index, key_alphabet_index)
                
                if self.key_num < len(self.key)-1:
                    self.key_num = self.key_num + 1
                else:
                   self.key_num = 0    
            
    def shiftLetters(self, cipher_text, key):
        
        shift = ((cipher_text - key) + 26) % 26
                
        newLetter = (shift + self.ascii_uppercase)
        newCharacter = chr(newLetter)
        
        self.decryptedMessage.append(newCharacter)
        
    def getDecryptedMessage(self):
        new_string = ''.join(self.decryptedMessage)
        return new_string
    
    def change_key(self,newKey):
        temp = ''.join(newKey)
        self.key = temp
        self.startDecryption()


