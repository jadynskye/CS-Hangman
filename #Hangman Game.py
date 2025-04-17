#Hangman Game 
#Have to import random to chose word from the list
import random 

#using raw strings so the program doesn't treat my blackslashes as escape characters
#hangman bodies 
hangman = [
    r"""            _____    
           |     |      
           |     |      
           |            
           |            
           |            
           |_____________       
           |            |       
         / | \          |       
 _______/  |  \_________|____   """,
    
    r"""            _____     
           |     |      
           |     |      
           |     0      
           |            
           |            
           |_____________       
           |            |       
         / | \          |       
 _______/  |  \_________|____   """,
    
    r"""            _____     
           |     |      
           |     |      
           |     0      
           |     |      
           |            
           |_____________       
           |            |       
         / | \          |       
 _______/  |  \_________|____   """,

    r"""            _____     
           |     |      
           |     |      
           |     0      
           |    /|      
           |            
           |_____________       
           |            |       
         / | \          |       
 _______/  |  \_________|____   """,

    r"""            _____     
           |     |      
           |     |      
           |     0      
           |    /|\     
           |            
           |_____________       
           |            |       
         / | \          |       
 _______/  |  \_________|____   """,

    r"""            _____     
           |     |      
           |     |      
           |     0      
           |    /|\     
           |    /       
           |_____________       
           |            |       
         / | \          |       
 _______/  |  \_________|____   """,

    r"""            _____     
           |     |      
           |     |      
           |     0      
           |    /|\     
           |    / \     
           |_____________       
           |            |       
         / | \          |       
 _______/  |  \_________|____   """
]

#Centering the intro text 
#Creating a function so I can work on calling it all from the main 

def intro():
    title_text = "Hello, and welcome to Hangman for Coders!"
    intro_text = """   In this version of Hangman the answers are 
all coding related words. Good luck and lets begin!"""
    created_by = "Created By Jadyn Reid"


    print("-" * 50)
    print(title_text.center(50, " "))
    print("-" * 50)
    print(intro_text.center(60, " "))
    print("-" * 50)
    print(created_by.center(50, " "))
    print("-" * 50)
    print()
    print(hangman[0])
    print()

#This function is where all of the code for this game will be  
def body_of_game():

    #First I had to make a list of python words that the computer will be able to choose from 
    hangman_words = [ "algorithm", "array", "binary", "bit", "boolean", "bug", "byte", "cache", "class", "compiler",
    "computing", "condition", "constant", "constructor", "data", "debug", "dictionary", "encryption",
    "exception", "float", "function", "hardware", "inheritance", "input", "integer", "interface",
    "iteration", "java", "javascript", "kernel", "linux", "loop", "memory", "method", "module",
    "network", "object", "operator", "output", "pointer", "process", "program", "python", "queue",
    "recursion", "runtime", "software", "stack", "syntax", "variable", "virtual", "while", "windows",
    "argument", "assembler", "backend", "buffer", "command", "compile", "cyber", "database",
    "firewall", "frontend", "git", "hash", "html", "index", "ipaddress", "json", "machine", "null",
    "packet", "script", "secure", "server", "thread", "token", "upload"]
       
    #randomized choice 
    computers_word = random.choice(hangman_words)

    #to keep track of the length of word
    length_of_word = len(computers_word)

    #For loop to get the length of the word in "_", starting placeholder
    print(f"\nThe length of the word is : {length_of_word}")
    for letter in computers_word:
        print("_", end = "")
        
    #This print statment is for visual spacing and my OCD :p
    print()
    
    #lives variable to keep count of the lives of the player 
    lives = 6

    game_over = False
    
    correct_letters = []
    incorrect_letters = []

    while not game_over:
    
        user_input = str(input("\nType your first letter here: ").lower())
        #string to keep users guess
        users_guess = ''

        #If the user already guessed the letter for each case
        if user_input in correct_letters:
            print(f"\nYou've already guessed {user_input}!")
        if user_input in incorrect_letters:
            print(f"\nYou've already guessed {user_input}!")

        for letter in computers_word:
            #if letter is the same as user_input, add the letter to the string and list
            if letter == user_input:
                users_guess += letter
                correct_letters.append(user_input)
            #else if letter is not the guess but is in the correct_letters it will also be in the display
            elif letter in correct_letters:
                users_guess += letter
            else:
                users_guess += "_"
        
        
        print(users_guess)

        #if statment to make sure if the letter is not in the chosen word, then the lives - 1
        #also if the lives are equal to 0 then the game is over.
        if user_input not in correct_letters :
            lives -= 1
            incorrect_letters.append(user_input)
        else:
            pass
        #if statments to print the right hangman based on the number of lives left
        if lives == 0:
                print(hangman[6])
                print("\nSorry, you ran out of lives. Game over")
                break
        if lives == 1:
                print(hangman[5])
        if lives == 2:
                print(hangman[4])
        if lives == 3:
                print(hangman[3])
        if lives == 4:
                print(hangman[2])
        if lives == 5:
                print(hangman[1])
        if lives == 6:
                print(hangman[0])

        print(f"\nPlayers lives left = {lives}")
        print(f"\nCorrect letters = {correct_letters}")
        print(f"\nIncorrect letters tried = {incorrect_letters}")
        #ending the game for user to win if they guessed it all without using up number of tries 
        if "_" not in users_guess:
            game_over = True 
            print("\nYou win")
            break

    print(f"\nThe word was {computers_word}!\n")
        


def main():
    intro()
    body_of_game()

main()
