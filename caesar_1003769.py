import string
import english_quadgrams as quadgram

alphaUpp = list(string.ascii_uppercase)
alphaLow = list(string.ascii_lowercase)

def group_info():
    return [("1003769", "Mike Jansen", "INF1D1")]

def encrypt_caesar(plaintext, shift):
    output = ""
    for i in plaintext:
        if i in alphaUpp:
            index = alphaUpp.index(i)
            crypt = (index + shift) % 26
            newLetter = alphaUpp[crypt]
            output = output + newLetter
        elif i in alphaLow:
            index = alphaLow.index(i)
            crypt = (index + shift) % 26
            newLetter = alphaLow[crypt]
            output = output + newLetter
        else:
            output = output + i
    return output

def decrypt_caesar(ciphertext, shift):
    output = ""
    for i in ciphertext:
        if i in alphaUpp:
            index = alphaUpp.index(i)
            crypt = (index - shift) % 26
            newLetter = alphaUpp[crypt]
            output = output + newLetter
        elif i in alphaLow:
            index = alphaLow.index(i)
            crypt = (index - shift) % 26
            newLetter = alphaLow[crypt]
            output = output + newLetter
        else:
            output = output + i
    return output

def quadgram_fitness(text):
    number = 0
    txtLst = []
    letters = ""
    
    for i in text:
        if i in alphaLow:
            letters += i
        elif i in alphaUpp:
            low = alphaUpp.index(i)
            letters += alphaLow[low]
    
    max = len(letters)-4
    n = 0
    while n <= max:
        txtLst.append(letters[(0+n):(4+n)])
        n += 1

    for w in txtLst:
        if w in quadgram.quadgram_score.keys():
            index = list(quadgram.quadgram_score.keys()).index(w)
            value = list(quadgram.quadgram_score.values())[index]
            number = number + value
        else:
            number = number + 23
    return number

def solve_caesar(plaintext):
    fitList = []

    for i in range(1, 25):
        decrypt = decrypt_caesar(plaintext, i)
        fitness = quadgram_fitness(decrypt)
        fitList.append(fitness)
    
    lowest = fitList.index(min(fitList)) + 1
    return decrypt_caesar(plaintext, lowest)


