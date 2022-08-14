# Q1/Write a method that will remove any given character from a String?

def removeCharacter(str, char):
    return str.replace(char, '')

def main():
    #originalString = input('Enter a string: ')
    #tobeRemovedCharacter = input('Enter a character to be removed: ')

    originalString = 'Hello World!'
    tobeRemovedCharacter = 'l'

    modifiedString = removeCharacter(originalString, tobeRemovedCharacter)

    print('Original: ', originalString)
    print('Modified: ', modifiedString)

if __name__ == '__main__':
    main()
