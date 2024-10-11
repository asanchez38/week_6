# Names: Diego P, Abel S, Lorenzo G, Logan L, Andrew P, Tony O

#This makes the user input a paragrapgh and 3 random letters 
text1 = input("Provide a paragraph: ").lower () #asks the user to put a paragraph and puts the paragraph in lower case
text2 = input("write one random letters: ").lower () #asks user for 3 letters that we are going to find in the paragraph
text3 = input("write another random letters: ").lower ()
text4 = input("write another random letters: ").lower ()
tuple1 = tuple(text1) #This makes the text into a variable and seperates each letter
print(tuple1) #this prints the seperated letters

#Amount of each letter
print("searching for",text2, text3, text4) #This prints the 3 seperated letters
letter_find = tuple1.count (text2)
letter_find2 = tuple1.count (text3)
letter_find3 = tuple1.count (text4)
print(f"you have {letter_find} {text2}'s, {letter_find2} {text3}'s, and {letter_find3} {text4}'s") #this tells the user how much they have of their letters

#Find how many words the text has
print("you have", len(text1.split()), "words") #find all words in the text

#Tell the user the first and last letter of the text
letter1=(text1[0]) #this finds the first letter of the text
letter2=(text1[-1]) #this findd the last letter of the text
print(f"The first letter is {letter1} and the final letter is {letter2}")

#reverse the order of the text
print("the reverse of your text is", text1[::-1]) #reverses the text

#check if python is in the text
print("do you have python in your text:", "python" in text1) # This checks whether or not pyhton is in the sentence and says either false or true
