#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import tkinter as tk
from tkinter import messagebox

options = ["sang", "kaghz", "ghaichi"]
h_a = 0
h_b = 0
g = 0

def play(a, b):
    global h_a, h_b
    if a == b:
        return "Mosavi"
    elif (a == 'sang' and b == 'ghaichi') or (a == 'ghaichi' and b == 'kaghz') or (a == 'kaghz' and b == 'sang'):
        h_a += 1
        return "Player 1 barandeh"
    else:
        h_b += 1
        return "Player 2 barandeh"

def player_choice(choice):
    global g
    g += 1
    b = random.choice(options)
    result = play(choice, b)
    
    player1_choice_label.config(text=f"{choice}")
    player2_choice_label.config(text=f"{b}")
    
    result_label.config(text=f"{result}")
    score_label.config(text=f"Player1: {h_a} | Player2: {h_b}")
    
    
    if g == 5:
        if h_a > h_b:
            winner = "Player 1 is the winner!"
        elif h_b > h_a:
            winner = "Player 2 is the winner!"
        else:
            winner = "The game is a tie!"
        messagebox.showinfo("Game Over", winner)
        root.quit()


root = tk.Tk()
root.title("Sang Kaghaz Ghaichi")

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="Sang, Kaghz, Ghaichi Game", font=("Arial", 14))
label.pack()

buttons = [
    tk.Button(frame, text=option, font=("Arial", 12), width=10, command=lambda opt=option: player_choice(opt))
    for option in options
]
for btn in buttons:
    btn.pack(pady=5)

player_frame = tk.Frame(root)
player_frame.pack(pady=10)

tk.Label(player_frame, text="Player 1", font=("Arial", 12)).grid(row=0, column=0, padx=10)
tk.Label(player_frame, text="Player 2", font=("Arial", 12)).grid(row=0, column=1, padx=10)

player1_choice_label = tk.Label(player_frame, text="", font=("Arial", 12), width=10, relief="solid")
player1_choice_label.grid(row=1, column=0, padx=10)

player2_choice_label = tk.Label(player_frame, text="", font=("Arial", 12), width=10, relief="solid")
player2_choice_label.grid(row=1, column=1, padx=10)

result_frame = tk.Frame(root, relief="solid", borderwidth=2)
result_frame.pack(pady=10)

result_label = tk.Label(result_frame, text="", font=("Arial", 14), width=20, height=2)
result_label.pack()

score_frame = tk.Frame(root, relief="solid", borderwidth=2)
score_frame.pack(pady=10)

score_label = tk.Label(score_frame, text="Player1: 0 | Player2: 0", font=("Arial", 14), width=20, height=2)
score_label.pack()

winner_label = tk.Label(root)
winner_label.pack()

root.mainloop()


# In[ ]:




