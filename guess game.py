password = 'ARPAN'
guess = ''
guess_count= 0
guess_limit= 3
out_of_guesses = False
while guess!=password:
    if guess_count<=guess_limit and not out_of_guesses:
         guess = input('Enter your guess:')
         guess_count= guess_count+1
    else:
        out_of_guesses = True
print()
if out_of_guesses:
    print('FUCK OFF!! ')
else:
 print('HE HE YEAH BOY !!!')
