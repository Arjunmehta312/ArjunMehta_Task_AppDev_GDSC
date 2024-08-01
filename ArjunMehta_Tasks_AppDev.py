#!/usr/bin/env python
# coding: utf-8

# In[4]:


import datetime
import tkinter as tk
from tkinter import ttk

def is_leap_year(year):
    return year%4==0 and (year%100!=0 or year%400==0)

def date_calculator(day_of_year, year):
    try:
        date=datetime.datetime(year,1,1)+datetime.timedelta(day_of_year-1)
        formatted_date=date.strftime("%d-%m-%Y")
        week_of_year=date.isocalendar()[1]
        leap_year=is_leap_year(year)
        
        return {
            "Date": formatted_date,
            "Week of the year": week_of_year,
            "Leap Year": leap_year
        }
    except ValueError:
        return None

def calculate():
    try:
        day=int(day_entry.get())
        year=int(year_entry.get())
        result=date_calculator(day, year)
        
        if result:
            date_label.config(text=f"Date: {result['Date']}")
            week_label.config(text=f"Week of the year: {result['Week of the year']}")
            leap_label.config(text=f"Leap Year: {result['Leap Year']}")
        else:
            date_label.config(text="Invalid input")
            week_label.config(text="")
            leap_label.config(text="")
    except ValueError:
        date_label.config(text="Invalid input")
        week_label.config(text="")
        leap_label.config(text="")

root=tk.Tk()
root.title("Date Calculator")
root.geometry("300x200")

ttk.Label(root,text="Day of Year:").grid(row=0,column=0,padx=5,pady=5)
day_entry=ttk.Entry(root)
day_entry.grid(row=0,column=1,padx=5,pady=5)

ttk.Label(root,text="Year:").grid(row=1,column=0,padx=5,pady=5)
year_entry=ttk.Entry(root)
year_entry.grid(row=1,column=1,padx=5,pady=5)

calculate_button=ttk.Button(root,text="Calculate",command=calculate)
calculate_button.grid(row=2,column=0,columnspan=2,pady=10)

date_label=ttk.Label(root,text="")
date_label.grid(row=3,column=0,columnspan=2)

week_label=ttk.Label(root, text="")
week_label.grid(row=4,column=0,columnspan=2)

leap_label=ttk.Label(root,text="")
leap_label.grid(row=5,column=0,columnspan=2)

root.mainloop()


# In[ ]:




