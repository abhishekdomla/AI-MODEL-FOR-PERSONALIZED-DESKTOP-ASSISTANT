import tkinter as tk
from tkinter import PhotoImage, ttk
from tkinter.messagebox import showinfo
import major
import pyttsx3
import subprocess

def major_destroy():
    root.destroy()
    # Run another Python script
    subprocess.run(["python", "gui_copy.py"])

# Display settings
root = tk.Tk()  #Create application window

# Display settings
window_width = 450    #Set window height and width
window_height = 400
screen_width  = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
root.attributes('-topmost', 2)
root.attributes('-alpha', 5)     #Adjust transparacy
root.title("desktop assitant") 

background_color = "#9894FE"
# background_image = tk.PhotoImage(file="download.png")

# # Create a canvas the same size as the image
# canvas = tk.Canvas(root, width=background_image.width(), height=background_image.height())
# canvas.pack()

# # Place the image at the top left corner (coordinates 0, 0)
# canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

    # Configure the background color of the main window
# root.configure(bg=background_color)

# image_path = ""  # Replace with the path to your image
# background_image = tk.PhotoImage(file= "C:/Users/MY PC/Desktop/ai-assistant-main/move.png")

button = ttk.Button(root, text = "Call" , command = major_destroy)
button.pack(ipadx=5,ipady=5,expand=True)

# entrylabel = ttk.Label(root,text="wakeup")
# entrylabel.pack(ipadx=5,ipady=5,expand=True)
# entry = ttk.Entry(root,textvariable = major.abc)
# entry.pack(ipadx=5,ipady=5,expand=True)

# Exit button
exit_button = ttk.Button(root,text="Exit",command=lambda: root.destroy())
exit_button.pack(ipadx=5,ipady=5,expand=True)

# Keep GUI on display
root.mainloop()

