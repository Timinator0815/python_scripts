# This Python file uses the following encoding: utf-8
# 28.12.2020 exercise from Interview:
# URL: https://www.youtube.com/watch?v=PIeiiceWe_w

#multi dimensional dict for converting word into number
numbers = {0:'',1:'',2:['a','b','c'],3:['d','e','f'],
4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],
7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}

#phonenumber to find the word in
phonenumber = "3662277"

words = ['foo','bar','foobar','emo','cap','car','cat']

result = []
tmpresult = []
wordnum = ""
final = []

for word in words: #loop through all words
    x = 0
    while (x <= len(word) - 1): #loop through every char in word
        y = 2

        while (y < len(numbers)): #loop through numbers array
            tmp = str(word[x])
            if tmp in numbers[y]:           #look in every entry of array, if the number is 
                wordnum = wordnum + str(y)  #in the list and add it to the temp-number
            y+=1
        x+=1
    if (wordnum in phonenumber):    #if the temp-number is in the phonenumber, add it to
        result.append(word)         #the result
    wordnum = ""


result.sort() #sort alphabetically
print("Following words are contained in the phone number: \n")
print(result)
