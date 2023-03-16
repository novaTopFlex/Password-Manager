from tkinter import *
import backend as Backend
#Creates the Tkinter application
root = Tk()
root.geometry("700x700")
root.title("Password Manager")
root.configure(bg="#19191a")

#Main function where the gui's code/functions are housed
def main(debug):
    
    #Gives the ability to change the master password
    def changeMasterPasswordScreen():
        #takes you back to the debug screen
        def backToDebugScreenCommand():
            mainText.destroy()
            outputText.destroy()
            newMasterPasswordEntry.destroy()
            changeMasterPasswordButton.destroy()
            backToDebugScreen.destroy()
            debugScreen()
        #Called on a button press
        def changeMasterPasswordCommand():
            commandOutput = Backend.changeMasterPassword(newMasterPasswordEntry.get())
            outputText.configure(text=commandOutput)

            #Deletes the text in the entry
            newMasterPasswordEntry.delete(0, END)
        
        #Creates the Screen Text
        mainText = Label(root, text="Change your masterpassword below!", bg="#19191a", fg="White")
        outputText = Label(root, text=None, bg="#19191a", fg="White")

        #Create Entry
        newMasterPasswordEntry = Entry(root, width=25, bg="grey", fg="#19191a")

        #Creates Buttons
        changeMasterPasswordButton = Button(root, text="Change your Master Password", bg="grey", command=changeMasterPasswordCommand)
        backToDebugScreen = Button(root, text="Back", bg="grey", command=backToDebugScreenCommand)

        #Places everything on the screen
        mainText.place(relx=0.5, rely=0.0, anchor=N)
        outputText.place(relx=0.5, rely=0.6, anchor=CENTER)
        newMasterPasswordEntry.place(relx=0.5, rely=0.5, anchor=CENTER)
        changeMasterPasswordButton.place(relx=0.5, rely=0.55, anchor=CENTER)
        backToDebugScreen.place(relx=0.5, rely=0.8, anchor=CENTER)


    #Function that houses all the code for the debug screen so it can be ran from the debug screen button
    def debugScreen():
        
        #Function that gets the encrpyt function from that backend and passes the csv file through to encrypt.
        #The Function then displays a comfirmation that the file is encrypted
        def encryptDataSheet():
            Backend.encrypt('passwords.csv')
            outputText.configure(text="encrypted")

        #Function that gets the decrpyt function from that backend and passes the csv file through to encrypt.
        #The Function then displays a comfirmation that the file is decrypted
        def decryptDataSheet():
            Backend.decrypt('passwords.csv')
            outputText.configure(text="decrypted")
        #This function is called by a button to go back to the last screen which requires using the destroy button to get rid of the buttons/text
        def backToSecondScreen():
            mainText.destroy()
            outputText.destroy()
            encryptButton.destroy()
            decryptButton.destroy()
            backToSecondScreenButton.destroy()
            changeMasterPasswordButton.destroy()
            choicesScreen()
        
        def changeMasterPasswordCommand():
            mainText.destroy()
            outputText.destroy()
            encryptButton.destroy()
            decryptButton.destroy()
            backToSecondScreenButton.destroy()
            changeMasterPasswordButton.destroy()
            changeMasterPasswordScreen()
        
        #Creates the debug screens Text
        mainText = Label(root, text="Debug options", bg="#19191a", fg="White")
        outputText = Label(root, text=None, bg="#19191a", fg="White")

        #Creates the debug screens Buttons 
        encryptButton = Button(root, text="encrypt data sheet", bg="grey", command=encryptDataSheet)
        decryptButton = Button(root, text="decrypt data sheet", bg="grey", command=decryptDataSheet)
        changeMasterPasswordButton = Button(root, text="Change Master Password", bg="grey", command=changeMasterPasswordCommand)
        backToSecondScreenButton = Button(root, text="Back", bg="grey", command=backToSecondScreen)

        #Places the buttons/text on the screen at the desired places
        mainText.place(relx=0.5, rely=0.0, anchor=N)
        outputText.place(relx=0.5, rely=0.6, anchor=CENTER)
        encryptButton.place(relx=0.4, rely=0.5, anchor=CENTER)
        decryptButton.place(relx=0.6, rely=0.5, anchor=CENTER)
        backToSecondScreenButton.place(relx=0.5, rely=0.8, anchor=CENTER)
        changeMasterPasswordButton.place(relx=0.5, rely=0.55, anchor=CENTER)

    #Creates the screen for the adding password screen.
    def addANewPasswordScreen():
        #This function is called by a button to go back to the last screen which requires using the destroy button to get rid of the buttons/text
        def goBackToSecondScreen():
            mainText.destroy()
            outputText.destroy()
            websiteText.destroy()
            emailText.destroy()
            passwordText.destroy()
            websiteEntry.destroy()
            emailEntry.destroy()
            passwordEntry.destroy()
            addToCsvButton.destroy()
            backToSecondScreenButton.destroy()
            choicesScreen()
        #On a button press this function is called to add the desired info to the encrypted datasheet.
        def addToCsvSheet():
            #Gets the Entrys from the Entry boxes
            website = websiteEntry.get()
            email = emailEntry.get()
            password = passwordEntry.get()

            #Deletes the text that's in the entries
            websiteEntry.delete(0, END)
            emailEntry.delete(0, END)
            passwordEntry.delete(0, END)
            #Checks to see if the strings have a space using the built in function isspace() and tells them to try again
            if website.isspace() or email.isspace() or password.isspace():
                outputText.configure(text="Your entry contains a space! Try again")
            #Checks to see if any of the fields are blank and tells them to try again
            elif website == "" or email == "" or password == "":
                outputText.configure(text="You left a field blank! Try again")
            elif Backend.addaNewPassword(website, email, password) == None:
                outputText.configure(text="This website is already in your password sheet!")
            #Adds the password to the datasheet and displays that the entry was added
            else:
                Backend.addaNewPassword(website, email, password)
                outputText.configure(text="Your entry was successfully added to the datasheet!")
        
        #Create the title
        mainText = Label(root, text="Add a new addition to your dataset by using the text boxes below! (It can't contain spaces)", background="#19191a", foreground="White")
        mainText.place(relx=0.5, rely=0, anchor=N)

        #Create the output
        outputText = Label(root, text=None, background="#19191a", foreground="White")

        #Create the text that is about the Entries
        websiteText = Label(root, text="Enter Website:", bg="#19191a", fg="White")
        emailText = Label(root, text="Enter Email:", bg="#19191a", fg="White")
        passwordText = Label(root, text="Enter Password:", bg="#19191a", fg="White")

        #Create the text Entries 
        websiteEntry = Entry(root, width=25, bg="grey", fg="#19191a")
        emailEntry = Entry(root, width=25, bg="grey", fg="#19191a")
        passwordEntry = Entry(root, width=25, bg="grey", fg="#19191a")

        #Create the add to Csv Button
        addToCsvButton = Button(root, text="Add to Password Sheet", bg="grey", command=addToCsvSheet)
        
        #Create the backButton
        backToSecondScreenButton = Button(root, text="Back", bg="grey", command=goBackToSecondScreen)

        #Place everything on the screen at the proper cordinates by anchoring it at the Center.
        websiteEntry.place(relx=0.5, rely=0.5, anchor=CENTER)
        websiteText.place(relx=0.451, rely=0.47, anchor=CENTER)
        emailEntry.place(relx=0.5, rely=0.57, anchor=CENTER)
        emailText.place(relx=0.435, rely=0.54, anchor=CENTER)
        passwordEntry.place(relx=0.5, rely=0.64, anchor=CENTER)
        passwordText.place(relx=0.451, rely=0.61, anchor=CENTER)
        addToCsvButton.place(relx=0.5, rely=0.7, anchor=CENTER)
        outputText.place(relx=0.5, rely=0.75, anchor=CENTER)
        backToSecondScreenButton.place(relx=0.5, rely=0.9, anchor=CENTER)
    #Creates a screen function for the retrieve password screen
    def retrievePasswordScreen():
        #Command for the back button that takes you back to the second screen and destroys all screen text/buttons
        def choicesScreenHomeButton():
            choicesScreen()
            mainText.destroy()
            websitesDropDown.destroy()
            backButton.destroy()
            outputText.destroy()
        #Command called on the dropdown that gets the email and password by passing through the input of the dropdown and displays it in the output text
        def dropdownChange(self):
            websites = Backend.getEmailandPasswordFromWebsite(clicked.get())
            outputText.configure(background="#19191a", foreground="white", text="The email for " + websites[0] + " is " + websites[1] + " and the password is " + websites[2])
            outputText.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        #Creates the text Labels
        mainText = Label(root, text="Retrieve a password by using the dropdown Below", background="#19191a", foreground="White")
        outputText = Label(root, text=None)

        #Stores every website that in in the data sheet in a variable called websites
        websites = Backend.getWebsites()

        #Stores the value from the selected part of optionmenu
        clicked = StringVar()

        #Creates the dropdown menu and puts all of the websites as the options. When the dropdown changes it calls dropdownChange()
        websitesDropDown = OptionMenu(root, clicked, *(websites), command=dropdownChange)

        #Creates the back button that on click deletes all screen elements and runs the second screen function
        backButton = Button(root, text="Back", bg="grey", command=choicesScreenHomeButton)

        #Configures the drop down by making it the desired color
        websitesDropDown.configure(background="grey", foreground="#19191a", activebackground="grey")
        websitesDropDown["menu"].config(background="#19191a", foreground="grey", activebackground="grey")

        #Displays Choose your website on the dropdown
        clicked.set("Choose your website")

        #Places all the elements on the screen at the desired place
        websitesDropDown.place(relx=0.5, rely=0.4, anchor=CENTER)
        mainText.place(relx=0.5, rely=0.0, anchor=N)
        backButton.place(relx=0.5, rely=0.9, anchor=CENTER)

    #Creates a choices screen function that houses the code for the choices screen
    def choicesScreen():

        #Creates an onclick function that destroys all screen elements and calls the retrievePasswordScreen function
        def retrieveButton():
            mainText.destroy()
            retrieveButton.destroy()
            addANewPasswordButton.destroy()
            debugButton.destroy()
            retrievePasswordScreen()
            backToFirstScreenButton.destroy()
        
        #Creates a function that is called on a button press that destroys all screen elements and calls the addANewPasswordScreen function
        def addANewPasswordButton():
            mainText.destroy()
            retrieveButton.destroy()
            addANewPasswordButton.destroy()
            debugButton.destroy()
            addANewPasswordScreen()
            backToFirstScreenButton.destroy()
        
        #Creates a function that is called on a button press that destroys all screen elements and calls the debugScreen() function
        def debugButton():
            mainText.destroy()
            retrieveButton.destroy() 
            addANewPasswordButton.destroy()
            debugButton.destroy()
            backToFirstScreenButton.destroy()
            debugScreen()
        
        #Creates a function that is called on a button press that destroys the screen elements and goes back to the first screen
        def backToFirstScreenButton():
            mainText.destroy()
            retrieveButton.destroy() 
            addANewPasswordButton.destroy()
            debugButton.destroy()
            backToFirstScreenButton.destroy()
            authenticationScreen()
        
        #Creates the text Labels for the screen 
        mainText = Label(root, text="You have been successfully logged in! Click one of the options to be redirected!")

        #Creates the Buttons for the screen
        retrieveButton = Button(root, text="Retrieve Password", command=retrieveButton)
        addANewPasswordButton = Button(root, text="Add a New Password", command=addANewPasswordButton)
        debugButton = Button(root, text="Debug", command=debugButton)
        backToFirstScreenButton = Button(root, text="Log Out", background="grey", command=backToFirstScreenButton)
        
        #Configures the screen elements to get the desired colors
        mainText.configure(background="#19191a", foreground="White")
        retrieveButton.configure(background="grey")
        debugButton.configure(background="grey")
        addANewPasswordButton.configure(background="grey")

        #Places the screen elements at the desired places
        retrieveButton.place(relx=0.55, rely=0.5, anchor=CENTER)
        addANewPasswordButton.place(relx=0.35, rely=0.5, anchor=CENTER)
        debugButton.place(relx=0.7, rely=0.5, anchor=CENTER)
        backToFirstScreenButton.place(relx=0.5, rely=0.8, anchor=CENTER)
        mainText.place(relx=0.5, rely=0.25, anchor=N)
    
    #Creates the authentication screen function that houses all the screen elements
    def authenticationScreen():

        #Creates the Labels for the screen
        mainText = Label(root, text="Welcome to your password manager. Enter your master password here to access your passwords.")
        errorText = Label(root, text=None)

        #Creates the text Master Password entry for the screen
        masterPasswordEntry = Entry(root, width=50, bg="grey", fg="black")

        #Configures the Master Password entry by changing the colors
        mainText.configure(background="#19191a", foreground="White")

        #Places the elements on the screen
        mainText.place(relx=0.5, rely=0.25, anchor=N)
        masterPasswordEntry.place(relx=0.5, rely=0.5, anchor=CENTER)

        #Creates a button click function that gets the backend function checkMasterPassword and passes through the entry which either returns true or false
        #If True it changes the screen and destroys the elements
        def authenticateButton():
            if Backend.checkMasterPassword(masterPasswordEntry.get()) or debug:
                root.configure(bg="#19191a")
                errorText.destroy()
                masterPasswordEntry.destroy()
                authenticateButton.destroy()
                mainText.destroy()
                choicesScreen()
            #If false it displays an error
            else:
                errorText.configure(text="Incorrect Master Password", background="#19191a", foreground="White")
                errorText.place(relx=0.5, rely=0.57, anchor=CENTER)

        #Creates a Button for that calls authenticateButton() on click
        authenticateButton = Button(root, text="Login",  command=authenticateButton)

        #Configures the button with a grey background
        authenticateButton.configure(background="grey")
        
        #Places the button on the screen
        authenticateButton.place(relx=0.5, rely=0.539, anchor=CENTER)
    
    #Calls the authentication screen function
    authenticationScreen()

    #Runs the tkinter loop that runs periodically
    root.mainloop()


