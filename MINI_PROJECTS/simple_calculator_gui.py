import tkinter as tk #here tk is the alias

#creating window
root  = tk.Tk()
root.title("Simple calculator")
root.geometry("300x400") #widthxhight
root.configure(bg = "#2E2E2E")

expression = "" #global string to store math function

def press(num):
    global expression
    expression +=str(num)
    entry_text.set(expression)#updates the text inside display (entry box)

def equal_press():
    global expression
    try:
        result = str(eval(expression)) #evaluated the string expression into code 
        entry_text.set(result)
        expression = result
    except: 
        entry_text.set("Error")
        expression =""

def clear():
    global expression
    expression = "" #Clears the internal variable
    entry_text.set("")#Also clears the entry display



entry_text = tk.StringVar()
entry = tk.Entry(root , # put this entry on the main window.
                 textvariable =entry_text , 
                 font=("Arial", 20), 
                 bd=10, 
                 relief='ridge', 
                 justify='right',
                  bg="#1E1E1E",        # dark background for entry
                fg="white",          # white text
                insertbackground="white")
entry.grid(row=0,
            column=0, 
            columnspan =4 ,
              ipadx=8, 
              ipady=25)


buttons= [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for i in range(4):
    for j in range(4):
        btn_text = buttons[i][j]
        btn_command = lambda x = btn_text:press(x) if x not in ['C',  '='] else equal_press() if x == '=' else clear()

        tk.Button(
          root, 
          text=btn_text,
          font=('Arial', 18),
          width=5,
          height=2,
          command=btn_command,
          bg="#3E3E3E",     # dark button background
          fg="white",       # white text
          activebackground="#5E5E5E",  # hover background
          activeforeground="white"    # hover text color
          ).grid(row=i+1, column=j, padx=5, pady=5)
  

# run
# root.mainloop()