import tkinter as tk
from tkinter import scrolledtext

class UltimateRSVPReader:
    def __init__(self, root):
        self.root = root
        self.root.title("FocusRead RSVP - Pro")
        self.root.geometry("700x650")
        
        # Color Palette
        self.bg_main = "#121212"
        self.bg_input = "#1E1E1E"
        self.bg_display = "#000000"
        self.text_main = "#E0E0E0"
        self.accent_red = "#FF5252"
        self.accent_green = "#2E7D32"
        
        self.root.configure(bg=self.bg_main)
        
        self.words = []
        self.current_index = 0
        self.is_playing = False
        self.after_id = None
        self.search_start_index = "1.0"  # Track position in text widget
        self.advanced_visible = False

        self.setup_ui()

    def setup_ui(self):
        # Header & Instructions
        tk.Label(self.root, text="FOCUSREAD PRO", font=("Impact", 20), 
                 bg=self.bg_main, fg=self.accent_green).pack(pady=(15,0))
        tk.Label(self.root, text="Vowel-Sync RSVP Mode", font=("Arial", 9), 
                 bg=self.bg_main, fg="#888").pack(pady=(0,10))

        # Text Input Area
        self.text_input = scrolledtext.ScrolledText(
            self.root, height=8, width=70, font=("Consolas", 10),
            bg=self.bg_input, fg=self.text_main, borderwidth=0, 
            insertbackground="white", highlightthickness=1, highlightbackground="#333"
        )
        self.text_input.pack(pady=10)
        
        # Text Highlight Configuration
        self.text_input.tag_config("highlight", background="#333333", foreground=self.accent_green, font=("Consolas", 10, "bold"))

        # The Stage
        self.display_container = tk.Frame(self.root, bg=self.bg_display, height=140, width=620)
        self.display_container.pack_propagate(False)
        self.display_container.pack(pady=10)

        self.word_frame = tk.Frame(self.display_container, bg=self.bg_display)
        self.word_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.prefix_label = tk.Label(self.word_frame, text="", font=("Courier", 38), bg=self.bg_display, fg=self.text_main)
        self.prefix_label.grid(row=0, column=0, sticky="e")

        self.pivot_label = tk.Label(self.word_frame, text="READY", font=("Courier", 38, "bold"), bg=self.bg_display, fg=self.accent_red)
        self.pivot_label.grid(row=0, column=1)

        self.suffix_label = tk.Label(self.word_frame, text="", font=("Courier", 38), bg=self.bg_display, fg=self.text_main)
        self.suffix_label.grid(row=0, column=2, sticky="w")

        # Progress Bar Section
        self.progress_label = tk.Label(self.root, text="Progress: 0%", font=("Arial", 8), bg=self.bg_main, fg="#888")
        self.progress_label.pack()
        
        self.progress_canvas = tk.Canvas(self.root, width=600, height=6, bg="#333", highlightthickness=0)
        self.progress_canvas.pack(pady=5)
        self.progress_bar = self.progress_canvas.create_rectangle(0, 0, 0, 6, fill=self.accent_green, width=0)

        # Speed Slider
        tk.Label(self.root, text="WPM", bg=self.bg_main, fg=self.text_main, font=("Arial", 10, "bold")).pack()
        self.speed_slider = tk.Scale(
            self.root, from_=100, to=1200, orient="horizontal", length=400,
            bg=self.bg_main, fg=self.text_main, highlightthickness=0,
            troughcolor="#222", activebackground=self.accent_red
        )
        self.speed_slider.set(400)
        self.speed_slider.pack(pady=5)

        # Advanced Settings Toggle
        self.adv_btn = tk.Button(
            self.root, text="▼ Advanced Settings", command=self.toggle_advanced,
            bg=self.bg_main, fg="#888", font=("Arial", 8), borderwidth=0, cursor="hand2", activebackground=self.bg_main, activeforeground=self.text_main
        )
        self.adv_btn.pack(pady=5)

        # Advanced Settings Frame (Hidden by default)
        self.adv_frame = tk.Frame(self.root, bg=self.bg_main)
        
        # Punctuation Delays
        tk.Label(self.adv_frame, text="Punctuation Delays", bg=self.bg_main, fg=self.text_main, font=("Arial", 9, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 5))
        
        tk.Label(self.adv_frame, text="End Sentence (. ! ?)", bg=self.bg_main, fg="#AAA", font=("Arial", 8)).grid(row=1, column=0, sticky="e", padx=5)
        self.punct_major_scale = tk.Scale(self.adv_frame, from_=1.0, to=5.0, resolution=0.1, orient="horizontal", length=150, bg=self.bg_main, fg=self.text_main, highlightthickness=0, troughcolor="#222", activebackground=self.accent_green)
        self.punct_major_scale.set(2.5)
        self.punct_major_scale.grid(row=1, column=1, sticky="w")

        tk.Label(self.adv_frame, text="Mid Sentence (, ; :)", bg=self.bg_main, fg="#AAA", font=("Arial", 8)).grid(row=2, column=0, sticky="e", padx=5)
        self.punct_minor_scale = tk.Scale(self.adv_frame, from_=1.0, to=3.0, resolution=0.1, orient="horizontal", length=150, bg=self.bg_main, fg=self.text_main, highlightthickness=0, troughcolor="#222", activebackground=self.accent_green)
        self.punct_minor_scale.set(1.5)
        self.punct_minor_scale.grid(row=2, column=1, sticky="w")

        # Long Word Delays
        tk.Label(self.adv_frame, text="Long Word Delays", bg=self.bg_main, fg=self.text_main, font=("Arial", 9, "bold")).grid(row=0, column=2, columnspan=2, pady=(0, 5), padx=(20, 0))

        tk.Label(self.adv_frame, text="> 9 Chars", bg=self.bg_main, fg="#AAA", font=("Arial", 8)).grid(row=1, column=2, sticky="e", padx=5)
        self.long_word_scale = tk.Scale(self.adv_frame, from_=1.0, to=3.0, resolution=0.1, orient="horizontal", length=150, bg=self.bg_main, fg=self.text_main, highlightthickness=0, troughcolor="#222", activebackground=self.accent_green)
        self.long_word_scale.set(1.4)
        self.long_word_scale.grid(row=1, column=3, sticky="w")

        tk.Label(self.adv_frame, text="> 6 Chars", bg=self.bg_main, fg="#AAA", font=("Arial", 8)).grid(row=2, column=2, sticky="e", padx=5)
        self.med_word_scale = tk.Scale(self.adv_frame, from_=1.0, to=2.0, resolution=0.1, orient="horizontal", length=150, bg=self.bg_main, fg=self.text_main, highlightthickness=0, troughcolor="#222", activebackground=self.accent_green)
        self.med_word_scale.set(1.1)
        self.med_word_scale.grid(row=2, column=3, sticky="w")

        # Buttons
        self.btn_frame = tk.Frame(self.root, bg=self.bg_main)
        self.btn_frame.pack(pady=20)

        self.play_btn = tk.Button(
            self.btn_frame, text="START READING", width=20, height=2, command=self.toggle_play,
            bg=self.accent_green, fg="white", font=("Arial", 10, "bold"), borderwidth=0, cursor="hand2"
        )
        self.play_btn.grid(row=0, column=0, padx=10)

        self.reset_btn = tk.Button(
            self.btn_frame, text="RESET", width=15, height=2, command=self.reset_reader,
            bg="#424242", fg="white", font=("Arial", 10), borderwidth=0, cursor="hand2"
        )
        self.reset_btn.grid(row=0, column=1, padx=10)

    def toggle_advanced(self):
        if self.advanced_visible:
            self.adv_frame.pack_forget()
            self.adv_btn.config(text="▼ Advanced Settings")
            self.root.geometry("700x650")
            self.advanced_visible = False
        else:
            self.adv_frame.pack(pady=10)
            self.adv_btn.config(text="▲ Advanced Settings")
            self.root.geometry("700x800")
            self.advanced_visible = True

    def get_orp_parts(self, word):
        if not word: return "", "", ""
        vowels = "aeiouyAEIOUY"
        length = len(word)
        mid = length // 2
        
        vowel_indices = [i for i, char in enumerate(word) if char in vowels]
        if vowel_indices:
            pivot_idx = min(vowel_indices, key=lambda x: abs(x - mid))
        else:
            pivot_idx = mid - 1 if length % 2 == 0 and length > 1 else mid
            
        return word[:pivot_idx], word[pivot_idx], word[pivot_idx+1:]

    def update_progress(self):
        if not self.words: return
        percent = (self.current_index / len(self.words))
        # Update Visual Bar
        self.progress_canvas.coords(self.progress_bar, 0, 0, 600 * percent, 6)
        # Update Text
        self.progress_label.config(text=f"Progress: {int(percent * 100)}%")

    def animate(self):
        if self.is_playing and self.current_index < len(self.words):
            current_word_str = self.words[self.current_index]
            pre, piv, suf = self.get_orp_parts(current_word_str)
            self.prefix_label.config(text=pre)
            self.pivot_label.config(text=piv)
            self.suffix_label.grid() # Ensure visible
            self.suffix_label.config(text=suf)
            
            # Highlight current word in text widget
            self.text_input.tag_remove("highlight", "1.0", tk.END)
            # Search for the specific word instance starting from our tracked position
            pos = self.text_input.search(current_word_str, self.search_start_index, stopindex=tk.END)
            if pos:
                # Calculate end position (pos + length of word)
                end_pos = f"{pos}+{len(current_word_str)}c"
                self.text_input.tag_add("highlight", pos, end_pos)
                self.text_input.see(pos) # Auto-scroll to keep word in view
                self.search_start_index = end_pos # Advance search index for next word
            
            self.current_index += 1
            self.update_progress()
            
            current_word = self.words[self.current_index - 1]
            base_delay = int((60 / self.speed_slider.get()) * 1000)

            # Punctuation pauses
            if current_word.endswith(('.', '!', '?')):
                base_delay = int(base_delay * self.punct_major_scale.get())
            elif current_word.endswith((',', ';', ':')):
                base_delay = int(base_delay * self.punct_minor_scale.get())
            
            # Long word slowdown
            if len(current_word) > 9:
                base_delay = int(base_delay * self.long_word_scale.get())
            elif len(current_word) > 6:
                base_delay = int(base_delay * self.med_word_scale.get())

            self.after_id = self.root.after(base_delay, self.animate)
        elif self.current_index >= len(self.words) and len(self.words) > 0:
            self.is_playing = False
            self.play_btn.config(text="RESTART", bg=self.accent_green)
            self.pivot_label.config(text="DONE")
            self.prefix_label.config(text="")
            self.suffix_label.config(text="")

    def toggle_play(self):
        if not self.is_playing:
            # Re-fetch words if empty or finished
            if not self.words or self.current_index >= len(self.words):
                text = self.text_input.get("1.0", tk.END).strip()
                if not text: return
                self.words = text.split()
                self.current_index = 0
                self.search_start_index = "1.0"
            
            self.is_playing = True
            self.play_btn.config(text="PAUSE", bg="#D32F2F")
            self.animate()
        else:
            self.is_playing = False
            self.play_btn.config(text="RESUME", bg=self.accent_green)
            if self.after_id: self.root.after_cancel(self.after_id)

    def reset_reader(self):
        self.is_playing = False
        if self.after_id: self.root.after_cancel(self.after_id)
        self.current_index = 0
        self.search_start_index = "1.0"
        self.text_input.tag_remove("highlight", "1.0", tk.END)
        self.words = []
        self.prefix_label.config(text="")
        self.pivot_label.config(text="READY")
        self.suffix_label.config(text="")
        self.update_progress()
        self.play_btn.config(text="START READING", bg=self.accent_green)

if __name__ == "__main__":
    root = tk.Tk()
    app = UltimateRSVPReader(root)
    root.mainloop()