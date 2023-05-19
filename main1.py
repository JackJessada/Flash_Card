import tkinter as tk

#base 
root = tk.Tk()
root.title("Flash Card")
bg_color = "#E3FFD1"
#root.eval("tk::PlaceWindow . center")
root.geometry("1440x1024")
root.resizable(False, False)
#root.configure(bg = bg_color)

#frame
frame0 = tk.Frame(root,width=1440,height=1024,bg=bg_color)
frame1 = tk.Frame(root,width=1440,height=1024,bg=bg_color)

def load_frame1():
    frame1.tkraise()
    frame1.pack_propagate(False)
    # Store deck_photo as an attribute of frame1 because the gabage collector always clean data.
    frame1.deck_photo = tk.PhotoImage(file = r"assets\frame1\button_2.png")
    deck_button = tk.Button(
        frame1,
        image = frame1.deck_photo,
        borderwidth=0,
        highlightthickness=0,
        cursor="hand2",
        command=lambda: print("deck_button_has_click"),
        relief="flat"
    )
    deck_button.place(
        x=516.0,
        y=60.0,
        width=189.0,
        height=90.0
    )
   


for frame in (frame1,frame0):
    frame.grid(row=0,column=0,sticky="nesw")


load_frame1()

root.mainloop()
