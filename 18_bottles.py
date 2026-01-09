''' Challenge: 99 Bottles

Objective: Practice iteration and string formatting by printing the lyrics to a traditional song using a loop. '''
for i in range(99, 0, -1):
    # Determine the correct plural/singular for the current number
    current_bottles = "bottles" if i > 1 else "bottle"

    # Determine the correct plural/singular for the next number (i-1)
    next_bottles = "bottles" if (i - 1) != 1 else "bottle"
    next_number = i - 1

    # Line 1 & 2: Current number of bottles
    print(f'{i} {current_bottles} of beer on the wall,')
    print(f'{i} {current_bottles} of beer.')

    # Line 3: Action
    print('Take one down, pass it around,')

    # Line 4: Next number of bottles
    if i > 1:
        print(f'{next_number} {next_bottles} of beer on the wall.')
    else:
        # Special ending when only 0 bottles are left
        print('No more bottles of beer on the wall!')
    
    print() # Add a blank line for separation between verses

# Final verse after the loop finishes (for 0 bottles)
print('No more bottles of beer on the wall,')
print('No more bottles of beer.')
print('Go to the store and buy some more,')
print('99 bottles of beer on the wall.')