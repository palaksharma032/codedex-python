''' Challenge: Slot Machine

Objective: Utilize the random module to simulate a three-reel slot machine and implement conditional logic to detect a "Jackpot" result. '''
import random

symbols = ['🍒', '🍇', '🍉', '7️⃣']
results = random.choices(symbols, k=3)
print(' | '.join(results))
if results.count('7️⃣') == 3:
    print("Jackpot! 💰")
else:
    print("Thanks for playing! 🎉")