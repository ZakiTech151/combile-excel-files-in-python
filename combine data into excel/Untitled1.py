#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import pandas as pd
from tkinter import *
from tkinter import messagebox 

try:
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog
from tkfilebrowser import askopendirname, askopenfilenames, asksaveasfilename


root = tk.Tk()
style = ttk.Style(root)
style.theme_use("clam")
def c_open_dir_old():
    path = filedialog.askdirectory(parent=root, initialdir='/tmp')
    files = [file for file in os.listdir(path) if not file.startswith('.')] # Ignore hidden files

    all_months_data = pd.DataFrame()

    for file in files:
        current_data = pd.read_csv(path+"/"+file)
        all_months_data = pd.concat([all_months_data, current_data])

    all_months_data.to_csv("all_combine_data.csv", index=False)
    messagebox.showinfo("Sucessfully", "Files is Combine") 
    
   
    
ttk.Button(root, text="Open folder", command=c_open_dir_old).grid(row=2, column=0, padx=4, pady=4, sticky='ew')
root.mainloop()


# In[ ]:




