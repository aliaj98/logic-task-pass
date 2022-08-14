# Q3/write a function that count how many the given character repeated in a given string?

def myCharacterCounter(str, char):
    count = 0
    for s in str:
        if s == char:
            count += 1
    return count

def characterCounter(str, char):
    return str.count(char)

def main():
    #myString = input('Enter a string: ')
    #tobeCountedCharacter = input('Enter a character to be counted: ')
    
    myString = 'Hello World!'
    tobeCountedCharacter = 'l'

    #countedCharacter = myCharacterCounter(myString, tobeCountedCharacter)
    countedCharacter = characterCounter(myString, tobeCountedCharacter)

    print('The character [', tobeCountedCharacter, '] occurs', countedCharacter, 'times in [', myString, '] string')    

if __name__ == '__main__':
    main()
