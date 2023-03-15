from cryptography.fernet import Fernet
import csv

#Opens the key file and stores the data in a file called key
with open('encryptionKey.key', 'rb') as mykey:
        key = mykey.read()
#Function that encrypts a file by passing through the file path
def encrypt(path):
    #Converts the key to the proper format to use for encryption
    encryptionKey = Fernet(key)

    #Opens the file and stores all the data in the file originalData
    with open(path, 'rb') as unencryptedData:
        originalData = unencryptedData.read()

    #Encrypts the data using the key and stores it in the variable encrypted
    encrypted = encryptionKey.encrypt(originalData)

    #Writes the same file with the encrypted data and places it in the file
    with open(path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

#Function that decrypts a file by passing through the file path
def decrypt(path):

    #Converts the key to the proper format to be used for decryption
    decryptionKey = Fernet(key)

    #Opens the passed through file and stores the data in a variable called encrypted
    with open(path, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    #Decrypts the data from encrypted and stores the unencrypted data in decrypted  
    decrypted = decryptionKey.decrypt(encrypted)

    #Writes the decrypted data and writes it to the file
    with open(path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

#Boolean function that opens the passwords.csv file and checks if the row called website exists by seeing if row["website"] is equal to something not None
#Since if the data is encrypted the row called website will not exist and it will be a long string of characters
def isEncrypted():
    with open('passwords.csv', 'r') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            if row["website"] is not None:
                return False
            else:
                pass
        return True

#Uses a pass through variable called website that checks all the websites until it find the correct one returning the website the email and the password.
def getEmailandPasswordFromWebsite(website):
    decrypt('passwords.csv')
    with open('passwords.csv', 'r') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            #Compares the website variable to every value in the row "website" until they are equal and returns the needed data
            if website == row["website"]:
                returninformation = [
                row["website"],  
                row["email"],
                row["password"]]
                encrypt('passwords.csv')
                return returninformation

#adds a new password by passing the website, email, and password
def addaNewPassword(website, email, password):
    decrypt('passwords.csv')

    #Checks to see if you are adding a duplicate if you have a duplicate it returns None so it can be checked on the GUI end and so it stops the function.
    with open('passwords.csv', 'r') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            if row["website"] == website:
                print("you already made a password for this website")
                encrypt('passwords.csv')
                return None
            
    #opens the passwords.csv file in append mode and writes a row on a new line with the website, email, and password
    with open('passwords.csv', 'a+', newline="\n") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow([website, email, password])
        print("your email and password is stored safely in the datasheet!")
    encrypt('passwords.csv')

#Boolean function that unencrypts the masterpassword and checks it with the inputtedpassword and returning true or false
def checkMasterPassword(inputtedPassword):
    with open('masterpass.pass', 'r') as masterpass:
        decrypt('masterpass.pass')
        masterpassword = masterpass.read()
        encrypt('masterpass.pass')
    if inputtedPassword == masterpassword:
        return True
    else:
        return False

#returns every website from the website row in a list
def getWebsites():
    decrypt('passwords.csv')
    outputList = []
    with open('passwords.csv', 'r') as file:
        csvreader = csv.DictReader(file)
        for row in csvreader:
            outputList.append(row["website"])
    encrypt('passwords.csv')
    return outputList

#main function that makes sure the passwords file is encrypted
def main():
    if not isEncrypted():
        print("encrypted")
        encrypt('passwords.csv')
main()