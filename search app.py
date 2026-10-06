#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import Entry, Label, Button, messagebox
import webbrowser
from urllib.parse import quote_plus


# In[ ]:


# Define main window


# In[2]:


root = tk.Tk()

root.title("Multi-Platform Search Assistant")
root.geometry("500x430")
root.configure(bg="steelblue")
root.resizable(False, False)


# In[3]:


# YouTube search
def search_youtube():
    query = entry.get().strip()

    if query == "":
        messagebox.showwarning("Warning", "Please enter something to search.")
        return

    url = f"https://www.youtube.com/results?search_query={quote_plus(query)}"
    webbrowser.open(url)


# In[4]:


# Google search
def search_google():
    query = entry.get().strip()

    if query == "":
        messagebox.showwarning("Warning", "Please enter something to search.")
        return

    url = f"https://www.google.com/search?q={quote_plus(query)}"
    webbrowser.open(url)


# In[5]:


# Instagram search
def search_instagram():
    username = entry.get().replace("@", "").strip()

    if username == "":
        messagebox.showwarning("Warning", "Please enter an Instagram username.")
        return

    url = f"https://www.instagram.com/{username}/"
    webbrowser.open(url)


# In[6]:


# Clear input
def clear_entry():
    entry.delete(0, tk.END)
    entry.focus()


# In[7]:


# Heading
Label(
    root,
    text="Multi-Platform Search Assistant",
    font=("Arial", 20, "bold"),
    bg="steelblue",
    fg="white"
).pack(pady=(30, 5))



# In[8]:


# Subtitle
Label(
    root,
    text="Search Google, YouTube or Instagram",
    font=("Arial", 11),
    bg="steelblue",
    fg="white"
).pack(pady=(0, 20))


# In[9]:


# Input label
Label(
    root,
    text="Enter your search:",
    font=("Arial", 11, "bold"),
    bg="steelblue",
    fg="white"
).pack(pady=5)


# In[10]:


# Input field
entry = Entry(
    root,
    width=40,
    font=("Arial", 12)
)

entry.pack(ipady=6, pady=10)
entry.focus()



# In[11]:


# Buttons
Button(
    root,
    text="Search on YouTube",
    command=search_youtube,
    width=25,
    font=("Arial", 11)
).pack(pady=6)


Button(
    root,
    text="Search on Google",
    command=search_google,
    width=25,
    font=("Arial", 11)
).pack(pady=6)


Button(
    root,
    text="Open Instagram Profile",
    command=search_instagram,
    width=25,
    font=("Arial", 11)
).pack(pady=6)


Button(
    root,
    text="Clear",
    command=clear_entry,
    width=25,
    font=("Arial", 11)
).pack(pady=6)



# In[12]:


# Press Enter to search Google
root.bind("<Return>", lambda event: search_google())



# In[ ]:


# Run GUI
root.mainloop()


# In[ ]:




