# Classical ciphers

### Course: Cryptography & Security
### Author: Cernei Ion

----
## Objectives:

* Implement dedicated functions for 4 cyphers.
* Use SOLID and OOP principles to improve the code.


## Implementation description
* ### Caesar cypher
Caesar cypher is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. To do this we use a for loop in which we assign the encrypted letter the value of the actual letter in the alphabet.
```
for letter in message:
    encrypted_letter = secret_alpha[alpha.find(letter)]
    encrypted_message.append(encrypted_letter)
```
In order to create the secret alphabet we use a value named key, by which we shift the alphabet
```
secret_alpha = self.alpha[self.key:] + self.alpha[:self.key]
```
The decryption procces is similar, we just use a negative key for the alphabet.

* ### Caesar cypher with keyword
For this cypher we add a keyword at the beggining of the alphabeth, and the we shift it by the value of the key. In order to avoid letter repetitions in the alphabet after we add the keyword, one way to do it is by creating dictionary keys from the letters
```
self.alpha_with_keyword = "".join(dict.fromkeys(keyword + alpha))

secret_alpha = self.alpha_with_keyword[self.key:] + self.alpha_with_keyword[:self.key]
```
The encryption and decryption methods are the same as in Caesar cypher.

* ### Polybius cypher with keyword
For the Polybius cypher we use a simple alphabeth at the beggining of which we add a keyword. Then we put it in a 5x5 matrix. In order to encrypt the message we substitute the letter with it's indices in the matrix
```
def encrypt(self, message):
        message = message.replace('j', 'i')
        encrypted_message = []
        for letter in message:
            letter_new_index = self.secret_alpha.find(letter) + 1
            row, col = divmod(letter_new_index,5)
            if  (letter_new_index%5 == 0):
                encrypted_message.append(str(row)+str(col+5))
            else:
                encrypted_message.append(str(row+1)+str(col))
        return "".join(encrypted_message)
```
We divide the letter index in the alphabeth to 5 and also find the remainder, then by concatenating this values as a string we obtain the encrypted letter.

In order to decrypt the message we do the opposite. We multiply the first number by 5 and add the remainder, to obtain the index of the letter from the alphabeth.
```
def decrypt(self, encrypted_message):
        decrypted_message = []
        for i in range(0, len(encrypted_message), 2):
            row = int(encrypted_message[i])
            col = int(encrypted_message[i+1])
            letter = self.secret_alpha[(row-1)*5 + col-1]
            decrypted_message.append(letter)
        return "".join(decrypted_message)
```

* ### Vigenere cypher
For the Vigenere cypher encryption we use the formula. In this way, the encrypted letter index will be equal to the summ of the actual index and the index of the letter from the keyword, all this modulo 26
```
encrypted_letter = self.alpha[(letter_alpha_index + keyword_alpha_index) % 26]
```
and for decryption, we substract instead of sum
```
decrypted_letter = self.alpha[(letter_alpha_index - keyword_alpha_index) % 26]
```

## Conclusions, Results
In this laboratory work I implemented 4 chyphers and used SOLID and OOP principles.

To demonstrate the implementation I created several test
```
def test_caesar(self):
    cypher = Caesar(5)
    assert cypher.encrypt("anothersecretmessage") == "fstymjwxjhwjyrjxxflj"
    assert cypher.decrypt("fstymjwxjhwjyrjxxflj") == "anothersecretmessage"

def test_caesar_with_keyword(self):
    cypher = CaesarWithKeyword(5, 'lemon')
    assert cypher.encrypt("letmein") == "abycbrf"
    assert cypher.decrypt("abycbrf") == "letmein"

def test_polybius_with_keyword(self):
    cypher = PolybiusWithKeyword('lemon')
    assert cypher.encrypt("whyareyourunning") == "52325421421254144542451515331531"
    assert cypher.decrypt("52325421421254144542451515331531") == "whyareyourunning"

def test_vigenere(self):
    cypher = Vigenere('super')
    assert cypher.encrypt("perasperaadastra") == "hygejhygervuhxis"
    assert cypher.decrypt("hygejhygervuhxis") == "perasperaadastra"
```
The results were as follows:

![test_results](./screenshots/classic_cyphers_test_results.png)