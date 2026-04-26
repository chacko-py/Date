import tkinter as tk
from tkinter import messagebox
import random

class AskOutApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Will you go on a date with me?")
        self.root.geometry("600x300")
        self.root.configure(bg='lightblue')
        
        self.no_count = 0
        self.yes_button_size = 12
        self.no_button_size = 12
        self.tracking_mouse = False
        
        # Main frame
        self.main_frame = tk.Frame(root, bg='lightblue')
        self.main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Title
        self.title_label = tk.Label(
            self.main_frame,
            text="Hey Tvishie! 💕\nWill you go on a date with me?",
            font=("Arial", 20, "bold"),
            bg='lightblue',
            fg='darkred'
        )
        self.title_label.pack(pady=20)
        
        # Buttons frame
        self.buttons_frame = tk.Frame(self.main_frame, bg='lightblue')
        self.buttons_frame.pack(pady=20)
        
        # Yes button
        self.yes_button = tk.Button(
            self.buttons_frame,
            text="Yes! 😊",
            font=("Arial", self.yes_button_size, "bold"),
            bg='green',
            fg='white',
            padx=20,
            pady=10,
            command=self.on_yes,
            cursor="hand2"
        )
        self.yes_button.pack(side=tk.LEFT, padx=10)
        
        # No button
        self.no_button = tk.Button(
            self.buttons_frame,
            text="No 😔",
            font=("Arial", self.no_button_size, "bold"),
            bg='red',
            fg='white',
            padx=20,
            pady=10,
            command=self.on_no,
            cursor="hand2"
        )
        self.no_button.pack(side=tk.LEFT, padx=10)
        
        # Bind mouse movement for tracking
        self.root.bind('<Motion>', self.on_mouse_move)
    
    def on_yes(self):
        """Handle yes button press"""
        self.root.destroy()
        self.show_thank_you()
    
    def on_no(self):
        """Handle no button press"""
        self.no_count += 1
        
        # Shrink no button
        self.no_button_size = max(4, 12 - (self.no_count * 1.5))
        self.no_button.config(font=("Arial", int(self.no_button_size), "bold"))
        
        # Grow yes button
        self.yes_button_size = 12 + (self.no_count * 1.5)
        self.yes_button.config(font=("Arial", int(self.yes_button_size), "bold"))
        
        # After 5 no presses, enable mouse tracking
        if self.no_count >= 5:
            self.tracking_mouse = True
    
    def on_mouse_move(self, event):
        """Track mouse and move no button away"""
        if not self.tracking_mouse or self.no_count < 5:
            return
        
        # Get mouse position
        mouse_x = event.x_root
        mouse_y = event.y_root
        
        # Get button position
        button_x = self.no_button.winfo_rootx() + self.no_button.winfo_width() // 2
        button_y = self.no_button.winfo_rooty() + self.no_button.winfo_height() // 2
        
        # Calculate distance
        dx = button_x - mouse_x
        dy = button_y - mouse_y
        distance = (dx**2 + dy**2) ** 0.5
        
        # If mouse is close, move button away
        if distance < 100:
            # Calculate direction away from cursor
            if distance > 0:
                move_x = int(dx / distance * 50)
                move_y = int(dy / distance * 50)
            else:
                move_x = random.randint(-50, 50)
                move_y = random.randint(-50, 50)
            
            # Move button to new position
            new_x = button_x + move_x
            new_y = button_y + move_y
            
            # Keep button within window
            window_width = self.root.winfo_width()
            window_height = self.root.winfo_height()
            
            new_x = max(10, min(new_x, window_width - 60))
            new_y = max(10, min(new_y, window_height - 60))
            
            # Move button using place geometry manager
            self.no_button.place(x=new_x, y=new_y)
    
    def show_thank_you(self):
        """Show thank you message"""
        thank_you_window = tk.Tk()
        thank_you_window.title("Thank You!")
        thank_you_window.geometry("500x300")
        thank_you_window.configure(bg='lightcoral')
        
        thank_you_frame = tk.Frame(thank_you_window, bg='lightcoral')
        thank_you_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        thank_you_label = tk.Label(
            thank_you_frame,
            text="Thank You, Tvishie! 💕\n\nI'm so excited to spend time with you!\nYou make me smile every day.",
            font=("Arial", 18, "bold"),
            bg='lightcoral',
            fg='white',
            justify=tk.CENTER
        )
        thank_you_label.pack(expand=True)
        
        ok_button = tk.Button(
            thank_you_frame,
            text="Close",
            font=("Arial", 14, "bold"),
            bg='darkred',
            fg='white',
            padx=20,
            pady=10,
            command=thank_you_window.destroy,
            cursor="hand2"
        )
        ok_button.pack(pady=20)
        
        thank_you_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = AskOutApp(root)
    root.mainloop()
