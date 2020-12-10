#This is the given question.

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False

def animal_cracker(text):
    wordlist = text.upper().split()
    #print(wordlist)
    return wordlist[0][0] == wordlist[1][0]

text = input('Please Enter Two Words : ')

print(animal_cracker(text))
