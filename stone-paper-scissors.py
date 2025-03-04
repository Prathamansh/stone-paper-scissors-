from PIL import Image, ImageTk
import os
import random
import tkinter as tk

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")
root.configure(bg="#1A1A2E")

# Load images
def load_image(name):
    path = os.path.join("images", f"{name}.jpg")  # Updated to .jpg extension
    try:
        img = Image.open(path).resize((100, 100))  # Resize if needed
        return ImageTk.PhotoImage(img)
    except FileNotFoundError:
        print(f"Error: {name}.jpg not found in images/")
        return None

# Initialize images
rock_img = load_image("rock")
paper_img = load_image("paper")
scissors_img = load_image("scissors")

# Ensure all images loaded
if not all([rock_img, paper_img, scissors_img]):
    print("One or more images failed to load. Check file names and locations.")

# Game logic
def play(choice):
    global player_score, high_score
    bot_choice = random.choice(["rock", "paper", "scissors"])
    result_label.config(text=f"Bot chose {bot_choice}")
    
    if choice == bot_choice:
        outcome_label.config(text="It's a Tie!", fg="blue")
    elif (choice == "rock" and bot_choice == "scissors") or \
         (choice == "paper" and bot_choice == "rock") or \
         (choice == "scissors" and bot_choice == "paper"):
        outcome_label.config(text="You Win!", fg="green")
        player_score += 1
    else:
        outcome_label.config(text="You Lose!", fg="red")
        if player_score > high_score:
            high_score = player_score
        player_score = 0
    
    score_label.config(text=f"Score: {player_score}  High Score: {high_score}")

def reset_game():
    global player_score
    player_score = 0
    score_label.config(text=f"Score: {player_score}  High Score: {high_score}")
    result_label.config(text="")
    outcome_label.config(text="")

player_score = 0
high_score = 0

# Labels
score_label = tk.Label(root, text="Score: 0  High Score: 0", font=("Arial", 12), fg="white", bg="#1A1A2E")
score_label.pack()
result_label = tk.Label(root, text="", font=("Arial", 14), fg="white", bg="#1A1A2E")
result_label.pack()
outcome_label = tk.Label(root, text="", font=("Arial", 16), fg="white", bg="#1A1A2E")
outcome_label.pack()

# Buttons
frame = tk.Frame(root, bg="#1A1A2E")
frame.pack()

tk.Button(frame, image=rock_img, command=lambda: play("rock")).grid(row=0, column=0, padx=10, pady=10)
tk.Button(frame, image=paper_img, command=lambda: play("paper")).grid(row=0, column=1, padx=10, pady=10)
tk.Button(frame, image=scissors_img, command=lambda: play("scissors")).grid(row=0, column=2, padx=10, pady=10)

tk.Button(root, text="Reset", command=reset_game, font=("Arial", 12), fg="black", bg="white").pack(pady=10)
tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12), fg="black", bg="white").pack()

root.mainloop()
