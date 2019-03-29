'''
---LOGISTICS---
- Make a discord bot
- Make a test dictionary (apple, please, lease, fetch, chap)
- Make the timer 10 seconds (make timer visible)
- 2 lives

---LOGIC---
- Generate and display a 2-3 letter string
    - String must exist within a word in dictionary
- Input = user input
- 2 checks:
    - Check if user input contains String
    - If yes check if user input matches word in dictionary
- If both checks = true, move to next person and reset timer.
- If any checks = false, refuse word.
- If timer = 0, remove life from player, move to next player. Repeat same string.
    - If all players fail same string, reveal word with answer. Generate new string.

---EXTRA---
- When all letters are used, get +1 life. 3 max.
- Add settings page to edit:
    - Words used (categories such as drug names)
    - Timer duration
'''