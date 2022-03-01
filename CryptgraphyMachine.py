def cryptomachine():
    keys = 'abcdefghijklmnopqrstuvwxyz123456789 !'
    Value = keys[-1] + keys[0:-1]

    encryptionDictionary = dict(zip(keys, Value))
    decryptionDictionary = dict(zip(Value, keys))

    message = input("Please enter a messege to convey: ")
    mode = input("Please select an encryption mode : Encode(E) OR Decode(D)")

    if mode.upper() == 'E':
        newMessage = ''.join([encryptionDictionary[letter]
                             for letter in message.lower()])

    elif mode.upper() == 'D':
        newMessage = ''.join([decryptionDictionary[letter]
                             for letter in message.lower()])
    else:
        print('Please enter an Valid choice, Decrypt(D) OR Encrypt(E)')

    return newMessage.capitalize()


print(cryptomachine())