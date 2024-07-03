from major import tk,ttk,terminate,subprocess

def gui():
    # Run another Python script
    subprocess.run(["python", "gui_copy.py"])

def facedetection():
    # Run another Python script
    subprocess.run(["python", "face_detection.py"])

# class LanguageSelector:
#     def _init_(self, master):
#         self.master = master
#         master.title("Language Selector")

#         # Create a label
#         self.label = tk.Label(master, text="Selected Language: ")
#         self.label.pack(pady=10)

#         # Create a list of language options
#         self.languages = ["English", "Marathi","Hindi"]

#         # Create a Combobox (Selection Box)
#         self.language_var = tk.StringVar()
#         self.language_var.set(self.languages[0])  # Set default language
#         self.language_combobox = ttk.Combobox(master, textvariable=self.language_var, values=self.languages)
#         self.language_combobox.pack(pady=10)

#         # Create a button to trigger language selection
#         self.select_button = tk.Button(master, text="Select Language", command=self.on_select)
#         self.select_button.pack(pady=10)


#     def on_select(self):
#         selected_language = self.language_var.get()
#         self.label.config(text=f"Rerun: {selected_language}")

#         # Run another Python file based on the selected language
#         if selected_language == "English":
#             root.destroy()
#             subprocess.run(["python", "english.py"])
#         elif selected_language == "Marathi":
#             root.destroy()
#             subprocess.run(["python", "marathi.py"])
#         elif selected_language == "Hindi":
#             root.destroy()
#             subprocess.run(["python", "Hindi.py"])
        
#         # Add more conditions for other languages and corresponding scripts
# # Create the main window

# def gui():
#     global root
#     root = tk.Tk()
#     window_width = 250    #Set window height and width
#     window_height = 200
#     screen_width  = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
#     center_x = int(screen_width/2 - window_width/2)
#     center_y = int(screen_height/2 - window_height/2)
#     root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
#     root.resizable(False, False)
#     root.attributes('-topmost', 2)
#     root.attributes('-alpha', 5)     #Adjust transparacy
#     root.title("desktop assitant") 
#     background_color = "#9894FE"
    
#     language_selector = LanguageSelector(root)
  
#     button = ttk.Button(root, text="Terminate and Destroy", command = terminate)
#     button.pack(ipadx=5,ipady=5,expand=True)
    
  
#     root.mainloop()
    
# gui()