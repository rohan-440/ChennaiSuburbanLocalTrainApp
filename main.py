import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def display_ticket():
    # Connect to the database
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    # Fetch the last booked ticket from the database
    cursor.execute("SELECT * FROM TICKET ORDER BY ROWID DESC LIMIT 1")
    ticket_data = cursor.fetchone()

    if ticket_data:
        # Create a new window to display the ticket
        ticket_window = tkinter.Toplevel()
        ticket_window.title("Ticket")
         
        frame = tkinter.Frame(ticket_window)
        frame.pack()
        
        user_info_frame = tkinter.LabelFrame(frame,text = "Ticket Info")
        user_info_frame.grid(row = 0, column=0, padx=20,pady=10)
        
        title_label = tkinter.Label(user_info_frame,text = "Title")
        title_label.grid(row = 0 , column=0)
        
        title_output = tkinter.Label(user_info_frame,text = f"{ticket_data[0]}\n")
        title_output.grid(row = 1 , column=0)


        
        first_name_label = tkinter.Label(user_info_frame,text = "First Name")
        first_name_label.grid(row = 0 , column=1)
        
        first_name_output = tkinter.Label(user_info_frame,text = f"{ticket_data[1]}\n")
        first_name_output.grid(row = 1 , column=1)

        
        last_name_label = tkinter.Label(user_info_frame, text = "Last Name")
        last_name_label.grid(row = 0 , column= 2)
        
        last_name_output = tkinter.Label(user_info_frame,text = f"{ticket_data[2]}\n")
        last_name_output.grid(row = 1 , column=2)
         
        age_label = tkinter.Label(user_info_frame,text="Age")
        age_label.grid(row=2,column=0)
        
        age_output = tkinter.Label(user_info_frame,text = f"{ticket_data[3]}\n")
        age_output.grid(row = 3 , column=0)
        
        nationality_label = tkinter.Label(user_info_frame,text="Nationality")
        nationality_label.grid(row=2,column=1)
        
        nationality_output = tkinter.Label(user_info_frame,text=f"{ticket_data[4]}")
        nationality_output.grid(row=3,column=1)
        
        contact_number_label = tkinter.Label(user_info_frame,text="Contact Number")
        contact_number_label.grid(row=2,column=2)
        
        contact_output = tkinter.Label(user_info_frame,text = f"{ticket_data[5]}")
        contact_output.grid(row=3,column=2)
                
        source_label = tkinter.Label(user_info_frame,text="Source")
        source_label.grid(row=4,column=0) 
        
        src_output = tkinter.Label(user_info_frame,text=f"{ticket_data[6]}")
        src_output.grid(row=5,column=0)
        
        destination_label = tkinter.Label(user_info_frame,text="Destination")
        destination_label.grid(row=4,column=1)
        
        dest_output = tkinter.Label(user_info_frame,text=f"{ticket_data[7]}")
        dest_output.grid(row=5,column=1)
        
        route_label = tkinter.Label(user_info_frame,text="Route")
        route_label.grid(row=4,column=2)
        
        route_output = tkinter.Label(user_info_frame,text=f"{ticket_data[8]}")
        route_output.grid(row=5,column=2)
        
        price_label = tkinter.Label(user_info_frame,text="Price")
        price_label.grid(row=6,column=1)
        
        route_output = tkinter.Label(user_info_frame,text="10 Rs")
        route_output.grid(row=7,column=1)
        
     
    else:
        tkinter.messagebox.showwarning(title="Error", message="No booked tickets found.")

def Book_Ticket():
    accept = accept_var.get()
    
    if accept == "Booked": 
        #user info get 
        title = title_combobox.get()
        firstName = first_name_entry.get()
        lastName = last_name_entry.get()
        if firstName and lastName :
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            contact = contact_number_Entry.get()
            
            #journey info get
            source = source_combobox.get()
            destination = destination_combobox.get()
            route = route_combobox.get()
            
            #terms and condition info get
            reg_var = accept_var.get() 
            
            print("title : ",title,"firstName : ",firstName , "Last Name : ",lastName)
            print("age : ",age,"Nationality : ",nationality ,"Contact Number : ",contact)
            print("source : ",source,"destination : ",destination,"Route: ",route)
            print("Status : ",reg_var)
            
            #create Table
            conn = sqlite3.connect('test.db')
            table_creation = '''CREATE TABLE IF NOT EXISTS TICKET(title TEXT,
            firstName TEXT, lastName TEXT,age INT,nationality TEXT,
            contact TEXT,source TEXT,destination TEXT,way TEXT)'''
            conn.execute(table_creation)
            
            #insert the data
            insert_data = '''INSERT INTO TICKET(title,firstName,lastName,age,nationality,
                             contact,source,destination,way) VALUES(?,?,?,?,?,?,?,?,?)'''
            insert_data_tuple = (title,firstName,lastName,age,nationality,contact,source,destination,route)                 
            cursor = conn.cursor()
            cursor.execute(insert_data,insert_data_tuple)
            conn.commit()
            conn.close()
            
            tkinter.messagebox.showinfo(title = " Successfully booked" , message = "Your ticket is successfully booked")
            display_ticket()
        else :
            tkinter.messagebox.showwarning(title= "Error",message = "First Name and Last Name are required")    
    else :
       tkinter.messagebox.showwarning(title = "Error",message="You have not accepted the terms and conditions")
        
window = tkinter.Tk()
window.title("Local Train Counter")

frame = tkinter.Frame(window)
frame.pack()


#Saving User Info
user_info_frame = tkinter.LabelFrame(frame,text = "Passenger Info")
user_info_frame.grid(row = 0, column=0, padx=20,pady=10)

title_label = tkinter.Label(user_info_frame,text = "Title")
title_combobox = ttk.Combobox(user_info_frame, values=["Mr.","Mrs.","Dr."])
title_label.grid(row = 0 , column=0)
title_combobox.grid(row = 1 , column=0)

first_name_label = tkinter.Label(user_info_frame,text = "First Name*")
first_name_label.grid(row = 0 , column=1)

last_name_label = tkinter.Label(user_info_frame, text = "Last Name*")
last_name_label.grid(row = 0 , column= 2)



first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row = 1, column=1)

last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row = 1 ,column=2)

age_label = tkinter.Label(user_info_frame,text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame,from_= 5 ,to=100)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

nationality_label = tkinter.Label(user_info_frame,text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame,values=["Africa","America","Asia","Indian","Europe"])
nationality_label.grid(row=2,column=1)
nationality_combobox.grid(row=3,column=1)

contact_number_label = tkinter.Label(user_info_frame,text="Contact Number")
contact_number_label.grid(row=2,column=2)
contact_number_Entry = tkinter.Entry(user_info_frame)
contact_number_Entry.grid(row=3,column=2)

#padding to all widgets 

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#***********************END OF SECTION USER INFO***************



#JOURNEY INFO

journey_frame = tkinter.LabelFrame(frame,text="Journey Info")
journey_frame.grid(row=1,column=0,sticky="news",padx=20,pady=10)

source_label = tkinter.Label(journey_frame,text="Source")
source_label.grid(row=0,column=0)

source_combobox = ttk.Combobox(journey_frame,values=["Chennai Park","Tirusulam","Chennai Beach","Potheri","Tambaram","Tambaram Santorium","Chengalpattu","Guindy","Chromepet","Chetpet","Chennai Egmore"])
source_combobox.grid(row=1,column=0)

destination_label = tkinter.Label(journey_frame,text="Destination")
destination_label.grid(row=0,column=1)

destination_combobox = ttk.Combobox(journey_frame,values=["Chennai Park","Tirusulam","Chennai Beach","Potheri","Tambaram","Tambaram Santorium","Chengalpattu","Guindy","Chromepet","Chetpet","Chennai Egmore"])
destination_combobox.grid(row=1,column=1)

route_label = tkinter.Label(journey_frame,text="Route")
route_label.grid(row=0,column=3)

route_combobox = ttk.Combobox(journey_frame,values=["Single","Return"])
route_combobox.grid(row=1,column=3)

for widget in journey_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)
    
#********END OF JOURNEY INFO *************************

#CONFIRMATION

confirmation_frame = tkinter.LabelFrame(frame,text="Terms and Conditions")
confirmation_frame.grid(row=2,column=0,sticky="news",padx=20,pady=10)

confirmation_label = tkinter.Label(confirmation_frame,text="Once The Ticket Is Booked, Will not be Cancelled")
confirmation_label.grid(row=0,column=0)

accept_var = tkinter.StringVar(value="Not Booked")

confirmation_check = tkinter.Checkbutton(confirmation_frame,text="I accept the terms and conditions*",variable=accept_var,onvalue="Booked",offvalue="Not Booked")
confirmation_check.grid(row=1,column=0)

for widget in confirmation_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5) 
     
#*************END OF CONFIRMATION*****************
   
   
        
#BOOK TICKET BUTTON

button = tkinter.Button(frame,text = "Book Ticket",bg = "green",foreground="white",font="bold",command=Book_Ticket)
button.grid(row=3,column=0,sticky="news",padx=20,pady=10)





window.mainloop()