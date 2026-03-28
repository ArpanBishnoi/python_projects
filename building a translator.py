def translate(phrase):
 translation = ''
 for letter in phrase:
    if letter in 'AEIOUaeiou':
        translation= translation + 'g'
    else:
        translation=translation + letter
 print( translation)
print(translate(input('Enter your phrase:')))     