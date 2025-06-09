import tkinter as tk
import time
import winsound #works only for windows

root = tk.Tk() #Think of root like your app’s blank page or main window.
root.title("⏰Countdown timer")
root.geometry("500x300")
root.configure(bg="#2E2E2E")

# tk.Label(root , text="⏳ Timer(in seconds)",
#          fg="white", 
#          bg="#2e2e2e",
#          font=("Lucida Console", 14)).pack(pady=10) #pack is used to stack it up


tk.Label(root , text="⏳Hours",
         fg="white", 
         bg="#2e2e2e",
         font=("Lucida Console", 14)).pack(pady=10) #pack is used to stack it up
hours_entry = tk.Entry(root,
                       font=("Lucida Console", 16),
                       justify="center")
hours_entry.pack(pady =5)


tk.Label(root , text="Minutes",
         fg="white", 
         bg="#2e2e2e",
         font=("Lucida Console", 14)).pack(pady=10) #pack is used to stack it up
minutes_entry = tk.Entry(root,
                       font=("Lucida Console", 16),
                       justify="center")
minutes_entry.pack(pady =5)


tk.Label(root , text="Seconds",
         fg="white", 
         bg="#2e2e2e",
         font=("Lucida Console", 14)).pack(pady=10) #pack is used to stack it up
sec_entry = tk.Entry(root,
                       font=("Lucida Console", 16),
                       justify="center")
sec_entry.pack(pady =5)



# entry =tk.Entry(root , font=("Lucida Console", 20), justify='center')
# entry.pack(pady=10)

count_label = tk.Label(root, text="", font=("Lucida Console", 24), fg="white", bg="#2e2e2e")
count_label.pack(pady=20)

def countdown(t):
    if t>=0:
        # count_label.config(text=f"{t} sec")
        # root.after(1000,countdown, t-1)

        mins, secs = divmod(t, 60)
        hrs, mins = divmod(mins, 60)
        time_format = f"{hrs:02d}:{mins:02d}:{secs:02d}"
        count_label.config(text=time_format)
        root.after(1000, countdown, t - 1)
    else:
        count_label.config(text ="Time's up!")
        winsound.Beep(1000, 2000) # freq and duration
        # winsound.PlaySound("SystemExit", winsound.SND_ALIAS)


def start_timer():
    try:
        # total_time = int(entry.get())
        # countdown(total_time)

        h = int(hours_entry.get()) if hours_entry.get().strip() else 0
        m = int(minutes_entry.get()) if minutes_entry.get() else 0
        s = int(sec_entry.get()) if sec_entry.get() else 0
        total_time = h * 3600 + m * 60 + s
        countdown(total_time)
    except:
        count_label.config(text="Invalid input!")

tk.Button(root,
          text="Start Timer...",
          command=start_timer,
          font=("Lucida Console", 14),
          bg="#4e4e4e",
          fg="white").pack(pady=10)

# run
root.mainloop()