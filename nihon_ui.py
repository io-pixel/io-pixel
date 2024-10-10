# Prerequisite  Install tkinter
# pip install tkinter
import tkinter as tk
from tkinter import messagebox
import random

# Dictionary with Japanese characters and their Romaji equivalents
japanese_romaji_dict = {
    'vowels': {
        'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
        'ア': 'a', 'イ': 'i', 'ウ': 'u', 'エ': 'e', 'オ': 'o',
    },
    'k_sounds': {
        'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
        'カ': 'ka', 'キ': 'ki', 'ク': 'ku', 'ケ': 'ke', 'コ': 'ko',
    },
    's_sounds': {
        'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
        'サ': 'sa', 'シ': 'shi', 'ス': 'su', 'セ': 'se', 'ソ': 'so',
    },
    # Additional groups can be added here...
}

# Flatten the dictionary into a single list for easier access
all_japanese_romaji_pairs = [(char, romaji) for group in japanese_romaji_dict.values() for char, romaji in group.items()]

# Variables to track correct and wrong answers
correct_count = 0
wrong_count = 0

# Function to get a random character from the dictionary
def get_random_character():
    return random.choice(all_japanese_romaji_pairs)

# Function to check the user input
def check_answer():
    global correct_count, wrong_count
    user_input = entry.get()
    if user_input.lower() == current_romaji:
        correct_count += 1
        update_score()  # Update the score display
        messagebox.showinfo("Correct!", f"Good job! '{current_char}' is '{current_romaji}'.")
        generate_new_character()
    else:
        wrong_count += 1
        update_score()  # Update the score display
        messagebox.showerror("Incorrect!", f"Oops! '{current_char}' is actually '{current_romaji}'. Try again!")

# Function to generate a new character and update the label
def generate_new_character():
    global current_char, current_romaji
    current_char, current_romaji = get_random_character()
    japanese_label.config(text=current_char)
    entry.delete(0, tk.END)

# Function to update the score display
def update_score():
    score_label.config(text=f"Correct: {correct_count}   Wrong: {wrong_count}")

# Initialize the Tkinter window
root = tk.Tk()
root.title("Nadeem の Japanese Character Practice")

# Japanese character label
japanese_label = tk.Label(root, text="", font=("Helvetica", 48))
japanese_label.pack(pady=20)

# Input field for user to type Romaji
entry = tk.Entry(root, font=("Helvetica", 24))
entry.pack(pady=20)

# Button to submit answer
submit_button = tk.Button(root, text="Submit", command=check_answer, font=("Helvetica", 16))
submit_button.pack(pady=10)

# Button to skip and generate a new character
new_button = tk.Button(root, text="Next", command=generate_new_character, font=("Helvetica", 16))
new_button.pack(pady=10)

# Score label to display correct and wrong counts
score_label = tk.Label(root, text="Correct: 0   Wrong: 0", font=("Helvetica", 16))
score_label.pack(pady=10)

# Generate the first character when the app starts
generate_new_character()

# Start the Tkinter event loop
root.mainloop()
