'''
---LOGISTICS---
- Make a discord bot
- Make a test dictionary (apple, please, lease, fetch, chap)
- Make the timer 10 seconds (make timer visible)
- 2 lives

---LOGIC---
- Generate and display a 2 or 3 letter string
    - RNG generate a number between 0 and 1
        - If number <0.5, make string 2 letters
        - If number >= 0.5, make string 3 letters
    - Pick a random word in the dictionary
    - Select a random 2-3 letter sequence in that dictionary
- Start a 10 second timer
    - Ideal: make displayed time decrease in 0.1 second intervals. 10.0 -> 9.9 -> 9.8 -> etc.
- Input = user input

- 3 checks:
    - Check if user input contains String
        - If yes, return true
    - Does user input match word in words_used list
        - If no, return true
    - Does user input match word in dictionary
        - If yes, return true

- If all checks = true:
    - Move to next person
    - Reset timer
    - Add user input to words_used list

- If any checks = false:
    - Refuse word

- If timer = 0:
    - Reset timer
    - Remove life from active player
        - If number of lives = 0
            - Display msg saying 'X has blown up' (make some funny death lines)
    - Move to next player
        - If next player has 0 lives:
            - Move to next player
    - If all players failed same string:
        - Reveal word with answer
        - Generate new string
    - Else:
        - Repeat same string

- If number of active players = 1
    - Display msg saying 'X has won game'
    - END GAME

---EXTRA---
- When all letters are used, get +1 life. 3 max.
- Add settings page to edit:
    - Words used (categories such as drug names)
    - Timer duration
'''