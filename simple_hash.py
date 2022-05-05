import hashlib

def hashgen():
    # Prompts and accepts a message for encryption
    # Places that message in a variable
    msg = (input ("Enter your message for encryption:\n "))

    encrypt = hashlib.sha256(msg.encode()).hexdigest()

    
    # Applies a hash alogorithm to that message
    # Prints the encrypted version of the message
    print ("Your original message:\n"+msg)
    print ("Your encrypted message:\n",encrypt)
    
hashgen()
    