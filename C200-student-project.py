#!/usr/bin/env python
# coding: utf-8

# # GUI APPLICATION

# In[1]:


from ipywidgets import widgets
from IPython.display import display, clear_output
import pandas as pd
from tkinter import Tk, filedialog
import matplotlib.pyplot as plt 
import numpy as np
graph_type = ['Choose one.. ','bubble','bar']
funtionality = ['Choose One','Sort','Filter']
sort_option = ['ascending','descending']
df = ''
new_df = ''
input_box = ''
input_fontsize = ''
input_title = ''
#end of predefine code

def select_files(b):
    clear_output() 
    global df
    root = Tk()
    root.withdraw() 
    file_name = filedialog.askopenfilename() 
    df = pd.read_csv(file_name)
    function_widget = widgets.Dropdown(options=funtionality)
    function_int = widgets.interactive(choose_the_function, function=function_widget)
    display(function_int)
    
def choose_the_function(function):
    global sort_option
    global df
    global input_box
    if(function == 'Sort'):
        sort_col_widget = widgets.Dropdown(options=df.columns)
        sort_option_widget = widgets.Dropdown(options = sort_option)
        range_widget = widgets.Dropdown(options = [20,30,40])
        sort_int = widgets.interactive(sort_dataframe, column=sort_col_widget, type_of_sort= sort_option_widget, head_range=range_widget)
        display(sort_int)
    elif(function == 'Filter'):
        display(df)
        input_box = widgets.Text(description='Value:')
        display(input_box)
        filter_col_widget = widgets.Dropdown(options=df.columns)
        compare_widget = widgets.Dropdown(options = ['Choose the option..','=', '>','<'])
        head=widgets.Dropdown(options = [20,30,40])
        groupby_int = widgets.interactive(filter_dataframe, filter_column=filter_col_widget, comparison= compare_widget,head_df=head)
        display(groupby_int)
    else:
        print('Choose a function')
        
def sort_dataframe(column, type_of_sort,head_range):
    global df
    global new_df
    try:
        print(df[column].dtypes)
        if(df[column].dtypes != 'float' or df[column].dtypes != 'int'):
            df[column] = df[column].astype(float)
        if(type_of_sort == 'ascending'):
            new_df = df.sort_values(column, ascending=True)
            display(new_df)
        else:
            new_df = df.sort_values(column, ascending=False)
            display(new_df)
        new_df = new_df.head(head_range)
        get_widget()
    except:
        print('The data is not structured so cannot perform the selected action')

def filter_dataframe(filter_column, comparison,head_df):
    print("filter_dataframe")

def get_widget():
    print("get_widget")
    

#start of predefine code 
def display_plot(xaxis, yaxis, graph_type):
    global new_df
    global input_title
    global input_fontsize
    if(graph_type == 'bubble'):
        plt.subplots(figsize=(19,8))
        rgb = np.random.rand(3)
        #Write Condition here

        #End of write condition here 
        plt.title(input_title.value, fontsize=input_fontsize.value)
        plt.xlabel(xaxis, fontsize=input_fontsize.value)
        plt.xticks(rotation='vertical')
        plt.ylabel(yaxis, fontsize=input_fontsize.value)
        plt.show()
    elif(graph_type == 'bar'):
        plt.subplots(figsize=(19,8))
        plt.bar(new_df[xaxis], new_df[yaxis], color=['red', 'green','blue','yellow','pink'])
        plt.title(input_title.value, fontsize=input_fontsize.value)
        plt.xlabel(xaxis, fontsize=input_fontsize.value)
        plt.xticks(rotation='vertical')
        plt.ylabel(yaxis, fontsize=input_fontsize.value)
        plt.show()
    else:
        print("Choose valid graph")
fileselect = widgets.Button(description="File select")
fileselect.on_click(select_files)
display(fileselect)


# In[ ]:




