from tkinter import ttk
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox

mydb = sqlite3.connect(r'data.sqlite')

mycursor = mydb.cursor()



class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (StartPage, AdminPage,UserPage,ViewEvents1,AddEvent, ViewVenues1, AddVenue, ViewEvents2,AddStudent,ViewStudents,AddClub,ViewClubs,Register,ViewPayments,ViewRegistration,ViewTransactions):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def report_callback_exception(self, exc, val, tb):
         messagebox.showerror("Exception", message="Something Went Wrong \n" + str(val))

    def show_frame(self, cont):

        for frame in self.frames.values():
            frame.grid_remove()

        frame = self.frames[cont]
        frame.grid()
        frame.winfo_toplevel().geometry("")

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        welcLabel = tk.Label(self, text = "Welcome! Please select one option from below.")
        welcLabel.grid(row = 0, column = 0,columnspan = 3,padx = 5, pady = 5)

        frame1 = tk.LabelFrame(self, padx = 70, pady = 5)
        frame1.grid(row = 1, column = 1,padx = 5, pady = 5)
        buttonAdmin = ttk.Button(frame1,text = "Admin",command = lambda: controller.show_frame(AdminPage))
        buttonAdmin.grid(row = 0, column = 1,ipadx = 5, ipady = 5,padx = 5, pady = 5)

        buttonUser = ttk.Button(frame1,text = "User",command = lambda: controller.show_frame(UserPage))
        buttonUser.grid(row = 1, column = 1,padx = 5, pady = 5,ipadx = 5, ipady = 5)

def showMessage():
    messagebox.showinfo("success",message = "Entery Successfull!")

class AdminPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        buttonStart = ttk.Button(self,text = "Back",command = lambda: controller.show_frame(StartPage))
        buttonStart.grid(row = 0, column = 0,sticky = "w")


        frame2 = tk.LabelFrame(self, padx = 5, pady = 5)
        frame2.grid(row = 1, column = 0,columnspan = 3,padx = 5, pady = 5,sticky = "nsew")


        buttonAddVenue = ttk.Button(frame2, text = "Add Venues", command = lambda: controller.show_frame(AddVenue))
        buttonAddVenue.grid(row = 0, column = 0,padx = 5, pady = 5,ipadx = 15, ipady = 5,sticky = "nsew")

        buttonAddVenue = ttk.Button(frame2, text = "Add Club", command = lambda: controller.show_frame(AddClub))
        buttonAddVenue.grid(row = 1, column = 0,padx = 5, pady = 5,ipadx = 15, ipady = 5,sticky = "nsew")

        buttonAddEvent = ttk.Button(frame2, text = "Add Event", command = lambda: controller.show_frame(AddEvent))
        buttonAddEvent.grid(row = 2, column = 0,padx = 5, pady = 5,ipadx = 15, ipady = 5,sticky = "nsew")

        buttonViewVenues = ttk.Button(frame2,text = "View Venues",command = lambda: controller.show_frame(ViewVenues1))
        buttonViewVenues.grid(row = 0, column = 1,padx = 5, pady = 5,ipadx = 15, ipady = 5,sticky = "nsew")

        buttonViewVenues = ttk.Button(frame2,text = "View Clubs",command = lambda: controller.show_frame(ViewClubs))
        buttonViewVenues.grid(row = 1, column = 1,padx = 5, pady = 5,ipadx = 15, ipady = 5,sticky = "nsew")

        buttonViewEvents = ttk.Button(frame2,text = "View Events",command = lambda: controller.show_frame(ViewEvents1))
        buttonViewEvents.grid(row = 3, column = 0,padx = 5, pady = 5,ipadx = 15, ipady = 5,sticky = "nsew")

        buttonViewVenues = ttk.Button(frame2,text = "View Students",command = lambda: controller.show_frame(ViewStudents))
        buttonViewVenues.grid(row = 2, column = 1,padx = 5, pady = 5,ipadx = 15, ipady = 5,sticky = "nsew")

        buttonViewVenues = ttk.Button(frame2,text = "View Registrations",command = lambda: controller.show_frame(ViewRegistration))
        buttonViewVenues.grid(row = 3, column = 1,padx = 5, pady = 5,ipadx = 15, ipady = 5,sticky = "nsew")

        buttonViewEvents = ttk.Button(frame2,text = "View Payments",command = lambda: controller.show_frame(ViewPayments))
        buttonViewEvents.grid(row = 4, column = 0,padx = 5, pady = 5,ipadx = 15, ipady = 5,sticky = "nsew")

        buttonViewVenues = ttk.Button(frame2,text = "View Transaction Details",command = lambda: controller.show_frame(ViewTransactions))
        buttonViewVenues.grid(row = 4, column = 1,padx = 5, pady = 5,ipadx = 15, ipady = 5,sticky = "nsew")

class ViewRegistration(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        buttonStart = ttk.Button(self,text = "Back",command = lambda: controller.show_frame(AdminPage))
        buttonStart.grid(row = 0, column = 0,sticky = "w")


        frame4 = tk.LabelFrame(self, padx = 5, pady = 5)
        frame4.grid(row = 1, column = 0,columnspan = 3,padx = 5, pady = 5,sticky = "nsew")

        my_canvas = Canvas(frame4)
        my_canvas.pack(side = LEFT, fill =BOTH, expand = 1)
        my_scrollbar = ttk.Scrollbar(frame4, orient = VERTICAL, command = my_canvas.yview)
        my_scrollbar.pack(side = RIGHT, fill = Y)
        my_canvas.configure(yscrollcommand = my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
        secondFrame = Frame(my_canvas)
        my_canvas.create_window((0,0), window = secondFrame, anchor = "nw")

        eventLabel = tk.Label(secondFrame,width = 50, anchor = "nw",justify = LEFT)
        eventLabel.grid(row = 0, column = 0, sticky = "nsew")

        def labelValues():
            mycursor.execute("SELECT * FROM registered_for;")
            myresult = mycursor.fetchall()

            eventLabel.configure(text = "")

            if(len(myresult) == 0):
                eventLabel.configure(text = "No registrations found")

            for x in myresult:
                eventLabel.configure(text = eventLabel.cget('text') + "Registration Number = " + str(x[0]))
                eventLabel.configure(text = eventLabel.cget('text') + "\nEvent No = " + str(x[1]))
                eventLabel.configure(text = eventLabel.cget('text') + "\n\n")

            eventLabel.after(2000,labelValues)

        labelValues()


class ViewPayments(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        buttonStart = ttk.Button(self,text = "Back",command = lambda: controller.show_frame(AdminPage))
        buttonStart.grid(row = 0, column = 0,sticky = "w")


        frame4 = tk.LabelFrame(self, padx = 5, pady = 5)
        frame4.grid(row = 1, column = 0,columnspan = 3,padx = 5, pady = 5,sticky = "nsew")

        my_canvas = Canvas(frame4)
        my_canvas.pack(side = LEFT, fill =BOTH, expand = 1)
        my_scrollbar = ttk.Scrollbar(frame4, orient = VERTICAL, command = my_canvas.yview)
        my_scrollbar.pack(side = RIGHT, fill = Y)
        my_canvas.configure(yscrollcommand = my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
        secondFrame = Frame(my_canvas)
        my_canvas.create_window((0,0), window = secondFrame, anchor = "nw")

        eventLabel = tk.Label(secondFrame,width = 50, anchor = "nw",justify = LEFT)
        eventLabel.grid(row = 0, column = 0, sticky = "nsew")

        def labelValues():
            mycursor.execute("SELECT * FROM Payment;")
            myresult = mycursor.fetchall()

            eventLabel.configure(text = "")

            if(len(myresult) == 0):
                eventLabel.configure(text = "No payments found")

            for x in myresult:
                eventLabel.configure(text = eventLabel.cget('text') + "Transaction ID = " + str(x[0]))
                eventLabel.configure(text = eventLabel.cget('text') + "\nCard No = " + str(x[1]))
                eventLabel.configure(text = eventLabel.cget('text') + "\nRegistration No = " + str(x[2]))
                eventLabel.configure(text = eventLabel.cget('text') + "\nEvent No = " + str(x[3]))
                eventLabel.configure(text = eventLabel.cget('text') + "\n\n")

            eventLabel.after(2000,labelValues)

        labelValues()

class ViewTransactions(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        buttonStart = ttk.Button(self,text = "Back",command = lambda: controller.show_frame(AdminPage))
        buttonStart.grid(row = 0, column = 0,sticky = "w")


        frame4 = tk.LabelFrame(self, padx = 5, pady = 5)
        frame4.grid(row = 1, column = 0,columnspan = 3,padx = 5, pady = 5,sticky = "nsew")

        my_canvas = Canvas(frame4)
        my_canvas.pack(side = LEFT, fill =BOTH, expand = 1)
        my_scrollbar = ttk.Scrollbar(frame4, orient = VERTICAL, command = my_canvas.yview)
        my_scrollbar.pack(side = RIGHT, fill = Y)
        my_canvas.configure(yscrollcommand = my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
        secondFrame = Frame(my_canvas)
        my_canvas.create_window((0,0), window = secondFrame, anchor = "nw")

        eventLabel = tk.Label(secondFrame,width = 50, anchor = "nw",justify = LEFT)
        eventLabel.grid(row = 0, column = 0, sticky = "nsew")

        def labelValues():
            mycursor.execute("SELECT * FROM Student_Transactions_history;")
            myresult = mycursor.fetchall()

            eventLabel.configure(text = "")

            if(len(myresult) == 0):
                eventLabel.configure(text = "No Transactions found")

            for x in myresult:
                eventLabel.configure(text = eventLabel.cget('text') + "Transaction Details = " + str(x[0]))
                eventLabel.configure(text = eventLabel.cget('text') + "\nRegistration No = " + str(x[1]))
                eventLabel.configure(text = eventLabel.cget('text') + "\n\n")

            eventLabel.after(2000,labelValues)

        labelValues()


class ViewEvents1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        buttonStart = ttk.Button(self,text = "Back",command = lambda: controller.show_frame(AdminPage))
        buttonStart.grid(row = 0, column = 0,sticky = "w")

        frame4 = tk.LabelFrame(self, padx = 5, pady = 5)
        frame4.grid(row = 1, column = 0,columnspan = 3,padx = 5, pady = 5,sticky = "nsew")

        my_canvas = Canvas(frame4)
        my_canvas.pack(side = LEFT, fill =BOTH, expand = 1)
        my_scrollbar = ttk.Scrollbar(frame4, orient = VERTICAL, command = my_canvas.yview)
        my_scrollbar.pack(side = RIGHT, fill = Y)
        my_canvas.configure(yscrollcommand = my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
        secondFrame = Frame(my_canvas)
        my_canvas.create_window((0,0), window = secondFrame, anchor = "nw")

        eventLabel = tk.Label(secondFrame,width = 50, anchor = "nw", justify = LEFT)
        eventLabel.grid(row = 0, column = 0, sticky = "nsew")

        def labelEvents():
            mycursor.execute("SELECT * FROM Event;")
            myresult = mycursor.fetchall()

            eventLabel.configure(text = "")

            if(len(myresult) == 0):
                eventLabel.configure(text = "No Events found")

            for x in myresult:
                eventLabel.configure(text = eventLabel.cget('text') + "Event Number = " + str(x[0]))
                eventLabel.configure(text = eventLabel.cget('text') + "\nCo-ordinator Name = " + str(x[1]))
                eventLabel.configure(text = eventLabel.cget('text') + "\nCo-ordinator Number = " + str(x[2]))
                eventLabel.configure(text = eventLabel.cget('text') + "\nEvent Name = " + str(x[3]))
                eventLabel.configure(text = eventLabel.cget('text') + "\nBuilding = " + str(x[4]))
                eventLabel.configure(text = eventLabel.cget('text') + "\nClub Name = " + str(x[5]))
                eventLabel.configure(text = eventLabel.cget('text') + "\n")

                sqlstuff = "SELECT * FROM Details WHERE Event_No = " + str(x[0]) + ";"
                mycursor.execute(sqlstuff)
                myresult2 = mycursor.fetchall()

                for y in myresult2:
                    eventLabel.configure(text = eventLabel.cget('text') + "Date = " + str(y[0]))
                    eventLabel.configure(text = eventLabel.cget('text') + "\nTime = " + str(y[1]))
                    eventLabel.configure(text = eventLabel.cget('text') + "\nSpeaker Name = " + str(y[2]))
                    eventLabel.configure(text = eventLabel.cget('text') + "\nSpeaker Number = " + str(y[3]))
                    eventLabel.configure(text = eventLabel.cget('text') + "\nDescription = " + str(y[4]))
                    eventLabel.configure(text = eventLabel.cget('text') + "\nNo. of seats = " + str(y[5]))
                    eventLabel.configure(text = eventLabel.cget('text') + "\nDuration = " + str(y[6]))
                    eventLabel.configure(text = eventLabel.cget('text') + "\nFees = " + str(y[7]))
                    eventLabel.configure(text = eventLabel.cget('text') + "\n\n")

            eventLabel.after(2000,labelEvents)

        labelEvents()

def createEvent(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14):
    sqlAddEvent = "INSERT intO Event VALUES(?,?,?,?,?,?);"
    valAddEvent = (int(str(e1)), str(e2), int(str(e3)),str(e4),str(e5),str(e6))
    mycursor.execute(sqlAddEvent,valAddEvent)
    #mydb.commit()
    sqlAddEvent = "INSERT intO Details VALUES(?,?,?,?,?,?,?,?,?);"
    valAddEvent = (str(e7),str(e8),str(e9),int(str(e10)),str(e11),int(str(e12)),int(str(e13)),int(str(e14)),int(str(e1)))
    mycursor.execute(sqlAddEvent,valAddEvent)
    mydb.commit()
    showMessage()


class AddEvent(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        buttonStart = ttk.Button(self,text = "Back",command = lambda: controller.show_frame(AdminPage))
        buttonStart.grid(row = 0, column = 0,sticky = "w")

        frame7 = tk.LabelFrame(self, padx = 78, pady = 5)
        frame7.grid(row = 1, column = 0,columnspan = 3,padx = 5, pady = 5,sticky = "nsew")

        l1 = tk.Label(frame7, text = "Event No- ")
        l1.grid(row = 0, column = 0,padx = 5, pady = 5,sticky = "w")

        e1 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e1.grid(row = 0, column = 1, padx = 5, pady = 5,sticky = "e")

        l2 = tk.Label(frame7, text = "Coordinator name- ")
        l2.grid(row = 1, column = 0,padx = 5, pady = 5,sticky = "w")

        e2 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e2.grid(row = 1, column = 1, padx = 5, pady = 5,sticky = "e")

        l3 = tk.Label(frame7, text = "Coordinator number- ")
        l3.grid(row = 2, column = 0,padx = 5, pady = 5,sticky = "w")

        e3 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e3.grid(row = 2, column = 1, padx = 5, pady = 5,sticky = "e")

        l4 = tk.Label(frame7, text = "Event Name- ")
        l4.grid(row = 3, column = 0,padx = 5, pady = 5,sticky = "w")

        e4 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e4.grid(row = 3, column = 1, padx = 5, pady = 5,sticky = "e")

        l5 = tk.Label(frame7, text = "Building- ")
        l5.grid(row = 4, column = 0,padx = 5, pady = 5,sticky = "w")

        e5 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e5.grid(row = 4, column = 1, padx = 5, pady = 5,sticky = "e")

        l6 = tk.Label(frame7, text = "Club Name- ")
        l6.grid(row = 5, column = 0,padx = 5, pady = 5,sticky = "w")

        e6 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e6.grid(row = 5, column = 1, padx = 5, pady = 5,sticky = "e")

        l7 = tk.Label(frame7, text = "Date (yyyy-mm-dd)- ")
        l7.grid(row = 6, column = 0,padx = 5, pady = 5,sticky = "w")

        e7 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e7.grid(row = 6, column = 1, padx = 5, pady = 5,sticky = "e")

        l8 = tk.Label(frame7, text = "Time (hh:mm:ss)- ")
        l8.grid(row = 7, column = 0,padx = 5, pady = 5,sticky = "w")

        e8 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e8.grid(row = 7, column = 1, padx = 5, pady = 5,sticky = "e")

        l9 = tk.Label(frame7, text = "Speaker Name- ")
        l9.grid(row = 8, column = 0,padx = 5, pady = 5,sticky = "w")

        e9 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e9.grid(row = 8, column = 1, padx = 5, pady = 5,sticky = "e")

        l10 = tk.Label(frame7, text = "Speaker Number- ")
        l10.grid(row = 9, column = 0,padx = 5, pady = 5,sticky = "w")

        e10 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e10.grid(row = 9, column = 1, padx = 5, pady = 5,sticky = "e")

        l11 = tk.Label(frame7, text = "Description- ")
        l11.grid(row = 10, column = 0,padx = 5, pady = 5,sticky = "w")

        e11 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e11.grid(row = 10, column = 1, padx = 5, pady = 5,sticky = "e")

        l12 = tk.Label(frame7, text = "No. of Seats- ")
        l12.grid(row = 11, column = 0,padx = 5, pady = 5,sticky = "w")

        e12 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e12.grid(row = 11, column = 1, padx = 5, pady = 5,sticky = "e")

        l13 = tk.Label(frame7, text = "Duration- ")
        l13.grid(row = 12, column = 0,padx = 5, pady = 5,sticky = "w")

        e13 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e13.grid(row = 12, column = 1, padx = 5, pady = 5,sticky = "e")

        l14 = tk.Label(frame7, text = "Fees- ")
        l14.grid(row = 13, column = 0,padx = 5, pady = 5,sticky = "w")

        e14 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e14.grid(row = 13, column = 1, padx = 5, pady = 5,sticky = "e")



        buttonStart = ttk.Button(self,text = "Create Event",command = lambda: createEvent(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),e14.get()))
        buttonStart.grid(row = 14, column = 0,sticky = "nsew")




class ViewVenues1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        buttonStart = ttk.Button(self,text = "Back",command = lambda: controller.show_frame(AdminPage))
        buttonStart.grid(row = 0, column = 0,sticky = "w")


        frame4 = tk.LabelFrame(self, padx = 5, pady = 5)
        frame4.grid(row = 1, column = 0,columnspan = 3,padx = 5, pady = 5,sticky = "nsew")

        my_canvas = Canvas(frame4)
        my_canvas.pack(side = LEFT, fill =BOTH, expand = 1)
        my_scrollbar = ttk.Scrollbar(frame4, orient = VERTICAL, command = my_canvas.yview)
        my_scrollbar.pack(side = RIGHT, fill = Y)
        my_canvas.configure(yscrollcommand = my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
        secondFrame = Frame(my_canvas)
        my_canvas.create_window((0,0), window = secondFrame, anchor = "nw")

        eventLabel = tk.Label(secondFrame,width = 50, anchor = "nw",justify = LEFT)
        eventLabel.grid(row = 0, column = 0, sticky = "nsew")

        def labelValues():
            mycursor.execute("SELECT * FROM Venue;")
            myresult = mycursor.fetchall()

            eventLabel.configure(text = "")

            if(len(myresult) == 0):
                eventLabel.configure(text = "No venues found")

            for x in myresult:
                eventLabel.configure(text = eventLabel.cget('text') + "Building Name = " + str(x[0]))
                eventLabel.configure(text = eventLabel.cget('text') + "\nRoom Number = " + str(x[1]))
                eventLabel.configure(text = eventLabel.cget('text') + "\n\n")

            eventLabel.after(2000,labelValues)

        labelValues()



def createVenue(buildingName, roomNumber):
    sqlAddVenue = "INSERT INTO Venue VALUES(?,?);"
    valAddVenue = (str(buildingName), int(str(roomNumber)))
    mycursor.execute(sqlAddVenue,valAddVenue)
    mydb.commit()
    showMessage()

class AddVenue(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        buttonStart = ttk.Button(self,text = "Back",command = lambda: controller.show_frame(AdminPage))
        buttonStart.grid(row = 0, column = 0,sticky = "w")

        frame7 = tk.LabelFrame(self, padx = 5, pady = 5)
        frame7.grid(row = 1, column = 0,columnspan = 3,padx = 5, pady = 5,sticky = "nsew")

        buildingLabel = tk.Label(frame7, text = "Building Name- ")
        buildingLabel.grid(row = 0, column = 0,padx = 5, pady = 5,sticky = "w")

        buildingEntry = tk.Entry(frame7, width = 45, borderwidth = 1)
        buildingEntry.grid(row = 0, column = 1, padx = 5, pady = 5,sticky = "e")

        roomNumberLabel = tk.Label(frame7, text = "Room Number- ")
        roomNumberLabel.grid(row = 1, column = 0,padx = 5, pady = 5,sticky = "w")

        roomNumberEntry = tk.Entry(frame7, width = 45, borderwidth = 1)
        roomNumberEntry.grid(row = 1, column = 1, padx = 5, pady = 5,sticky = "e")

        buttonStart = ttk.Button(self,text = "Create Venue",command = lambda: createVenue(buildingEntry.get(),roomNumberEntry.get()))
        buttonStart.grid(row = 2, column = 0,sticky = "nsew")


class ViewStudents(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        buttonStart = ttk.Button(self,text = "Back",command = lambda: controller.show_frame(AdminPage))
        buttonStart.grid(row = 0, column = 0,sticky = "w")

        frame4 = tk.LabelFrame(self, padx = 5, pady = 5)
        frame4.grid(row = 1, column = 0,columnspan = 3,padx = 5, pady = 5,sticky = "nsew")

        my_canvas = Canvas(frame4)
        my_canvas.pack(side = LEFT, fill =BOTH, expand = 1)
        my_scrollbar = ttk.Scrollbar(frame4, orient = VERTICAL, command = my_canvas.yview)
        my_scrollbar.pack(side = RIGHT, fill = Y)
        my_canvas.configure(yscrollcommand = my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
        secondFrame = Frame(my_canvas)
        my_canvas.create_window((0,0), window = secondFrame, anchor = "nw")

        studentLabel = tk.Label(secondFrame,width = 50, anchor = "nw",justify = LEFT)
        studentLabel.grid(row = 0, column = 0, sticky = "nsew")

        def labelStudents():
            mycursor.execute("SELECT * FROM Student;")
            myresult = mycursor.fetchall()

            studentLabel.configure(text = "")

            if(len(myresult) == 0):
                studentLabel.configure(text = "No Students found")

            for x in myresult:
                studentLabel.configure(text = studentLabel.cget('text') + "Registration Number = " + str(x[0]))
                studentLabel.configure(text = studentLabel.cget('text') + "\nFirst Name = " + str(x[1]))
                studentLabel.configure(text = studentLabel.cget('text') + "\nMiddle Number = " + str(x[2]))
                studentLabel.configure(text = studentLabel.cget('text') + "\nLast Name = " + str(x[3]))
                studentLabel.configure(text = studentLabel.cget('text') + "\nContact Number = " + str(x[4]))
                studentLabel.configure(text = studentLabel.cget('text') + "\n")

                sqlstuff = "SELECT * FROM Card WHERE Registration_number = '" + str(x[0]) + "';"
                mycursor.execute(sqlstuff)
                myresult2 = mycursor.fetchall()

                for y in myresult2:
                    studentLabel.configure(text = studentLabel.cget('text') + "Card Number = " + str(y[0]))
                    studentLabel.configure(text = studentLabel.cget('text') + "\nExpiry Date = " + str(y[1]))
                    studentLabel.configure(text = studentLabel.cget('text') + "\nName on Card = " + str(y[2]))
                    studentLabel.configure(text = studentLabel.cget('text') + "\nRegistered Phone Number = " + str(y[3]))
                    studentLabel.configure(text = studentLabel.cget('text') + "\n\n")

            studentLabel.after(2000,labelStudents)

        labelStudents()


def createClub(a,b,c,d,e):
    sqlAddClub = "INSERT intO Club VALUES(?,?,?,?,?);"
    valAddClub = (str(a), int(b),str(c),str(d),str(e))
    mycursor.execute(sqlAddClub,valAddClub)
    mydb.commit()
    showMessage()

class AddClub(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        buttonStart = ttk.Button(self,text = "Back",command = lambda: controller.show_frame(AdminPage))
        buttonStart.grid(row = 0, column = 0,sticky = "w")

        frame7 = tk.LabelFrame(self, padx = 5, pady = 5)
        frame7.grid(row = 1, column = 0,columnspan = 3,padx = 5, pady = 5,sticky = "nsew")

        CNLabel = tk.Label(frame7, text = "Club Name- ")
        CNLabel.grid(row = 0, column = 0,padx = 5, pady = 5,sticky = "w")

        CNEntry = tk.Entry(frame7, width = 45, borderwidth = 1)
        CNEntry.grid(row = 0, column = 1, padx = 5, pady = 5,sticky = "e")

        CNameLabel = tk.Label(frame7, text = "Club Coordinator Number- ")
        CNameLabel.grid(row = 1, column = 0,padx = 5, pady = 5,sticky = "w")

        CNameEntry = tk.Entry(frame7, width = 45, borderwidth = 1)
        CNameEntry.grid(row = 1, column = 1, padx = 5, pady = 5,sticky = "e")

        CNoLabel = tk.Label(frame7, text = "Club Coordinator Name- ")
        CNoLabel.grid(row = 2, column = 0,padx = 5, pady = 5,sticky = "w")

        CNoEntry = tk.Entry(frame7, width = 45, borderwidth = 1)
        CNoEntry.grid(row = 2, column = 1, padx = 5, pady = 5,sticky = "e")

        FcLabel = tk.Label(frame7, text = "Faculty Coordinator- ")
        FcLabel.grid(row = 3, column = 0,padx = 5, pady = 5,sticky = "w")

        FcEntry = tk.Entry(frame7, width = 45, borderwidth = 1)
        FcEntry.grid(row = 3, column = 1, padx = 5, pady = 5,sticky = "e")

        DescLabel = tk.Label(frame7, text = "Club Description- ")
        DescLabel.grid(row = 4, column = 0,padx = 5, pady = 5,sticky = "w")

        DescEntry = tk.Entry(frame7, width = 45, borderwidth = 1)
        DescEntry.grid(row = 4, column = 1, padx = 5, pady = 5,sticky = "e")

        buttonStart = ttk.Button(self,text = "Create Club",command = lambda: createClub(CNEntry.get(),CNameEntry.get(),CNoEntry.get(),FcEntry.get(),DescEntry.get()))
        buttonStart.grid(row = 2, column = 0,sticky = "nsew")

class ViewClubs(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        buttonStart = ttk.Button(self,text = "Back",command = lambda: controller.show_frame(AdminPage))
        buttonStart.grid(row = 0, column = 0,sticky = "w")

        frame4 = tk.LabelFrame(self, padx = 5, pady = 5)
        frame4.grid(row = 1, column = 0,columnspan = 3,padx = 5, pady = 5,sticky = "nsew")

        my_canvas = Canvas(frame4)
        my_canvas.pack(side = LEFT, fill =BOTH, expand = 1)
        my_scrollbar = ttk.Scrollbar(frame4, orient = VERTICAL, command = my_canvas.yview)
        my_scrollbar.pack(side = RIGHT, fill = Y)
        my_canvas.configure(yscrollcommand = my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
        secondFrame = Frame(my_canvas)
        my_canvas.create_window((0,0), window = secondFrame, anchor = "nw")

        clubLabel = tk.Label(secondFrame,width = 50, anchor = "nw",justify = LEFT)
        clubLabel.grid(row = 0, column = 0, sticky = "nsew")

        def labelClubs():
            mycursor.execute("SELECT * FROM Club;")
            myresult = mycursor.fetchall()

            clubLabel.configure(text = "")

            if(len(myresult) == 0):
                clubLabel.configure(text = "No Clubs found")

            for x in myresult:
                clubLabel.configure(text = clubLabel.cget('text') + "Club Name = " + str(x[0]))
                clubLabel.configure(text = clubLabel.cget('text') + "\nClub Coordinator Number = " + str(x[1]))
                clubLabel.configure(text = clubLabel.cget('text') + "\nClub Coordinator Name = " + str(x[2]))
                clubLabel.configure(text = clubLabel.cget('text') + "\nFaculty Coordinator = " + str(x[3]))
                clubLabel.configure(text = clubLabel.cget('text') + "\nClub Description = " + str(x[4]))
                clubLabel.configure(text = clubLabel.cget('text') + "\n\n")

            clubLabel.after(2000,labelClubs)

        labelClubs()

class UserPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        buttonStart = ttk.Button(self,text = "Back",command = lambda: controller.show_frame(StartPage))
        buttonStart.grid(row = 0, column = 0,sticky = "w")

        frame3 = tk.LabelFrame(self, padx = 78, pady = 5)
        frame3.grid(row = 1, column = 0,columnspan = 3,padx = 5, pady = 5,sticky = "nsew")

        buttonViewEvents = ttk.Button(frame3,text = "View Events",command = lambda: controller.show_frame(ViewEvents2))
        buttonViewEvents.grid(row = 0, column = 0,padx = 5, pady = 5,ipadx = 15, ipady = 5)

        buttonNewStudent = ttk.Button(frame3,text = "Add Student",command = lambda: controller.show_frame(AddStudent))
        buttonNewStudent.grid(row = 1, column = 0,padx = 5, pady = 5,ipadx = 15, ipady = 5)

        buttonRegister = ttk.Button(frame3,text = "Register",command = lambda: controller.show_frame(Register))
        buttonRegister.grid(row = 2, column = 0,padx = 5, pady = 5,ipadx = 15, ipady = 5)



class ViewEvents2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        buttonStart = ttk.Button(self,text = "Back",command = lambda: controller.show_frame(UserPage))
        buttonStart.grid(row = 0, column = 0,sticky = "w")

        frame4 = tk.LabelFrame(self, padx = 5, pady = 5)
        frame4.grid(row = 1, column = 0,columnspan = 3,padx = 5, pady = 5,sticky = "nsew")

        my_canvas = Canvas(frame4)
        my_canvas.pack(side = LEFT, fill =BOTH, expand = 1)
        my_scrollbar = ttk.Scrollbar(frame4, orient = VERTICAL, command = my_canvas.yview)
        my_scrollbar.pack(side = RIGHT, fill = Y)
        my_canvas.configure(yscrollcommand = my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
        secondFrame = Frame(my_canvas)
        my_canvas.create_window((0,0), window = secondFrame, anchor = "nw")

        eventLabel = tk.Label(secondFrame,width = 50, anchor = "nw",justify = LEFT)
        eventLabel.grid(row = 0, column = 0, sticky = "nsew")

        def labelEvents():
            mycursor.execute("SELECT * FROM Event;")
            myresult = mycursor.fetchall()

            eventLabel.configure(text = "")

            if(len(myresult) == 0):
                eventLabel.configure(text = "No Events found")

            for x in myresult:
                eventLabel.configure(text = eventLabel.cget('text') + "Event Number = " + str(x[0]))
                eventLabel.configure(text = eventLabel.cget('text') + "\nCo-ordinator Name = " + str(x[1]))
                eventLabel.configure(text = eventLabel.cget('text') + "\nCo-ordinator Number = " + str(x[2]))
                eventLabel.configure(text = eventLabel.cget('text') + "\nEvent Name = " + str(x[3]))
                eventLabel.configure(text = eventLabel.cget('text') + "\nBuilding = " + str(x[4]))
                eventLabel.configure(text = eventLabel.cget('text') + "\nClub Name = " + str(x[5]))
                eventLabel.configure(text = eventLabel.cget('text') + "\n")

                sqlstuff = "SELECT * FROM Details WHERE Event_No = '" + str(x[0]) + "';"
                mycursor.execute(sqlstuff)
                myresult2 = mycursor.fetchall()

                for y in myresult2:
                    eventLabel.configure(text = eventLabel.cget('text') + "Date = " + str(y[0]))
                    eventLabel.configure(text = eventLabel.cget('text') + "\nTime = " + str(y[1]))
                    eventLabel.configure(text = eventLabel.cget('text') + "\nSpeaker Name = " + str(y[2]))
                    eventLabel.configure(text = eventLabel.cget('text') + "\nSpeaker Number = " + str(y[3]))
                    eventLabel.configure(text = eventLabel.cget('text') + "\nDescription = " + str(y[4]))
                    eventLabel.configure(text = eventLabel.cget('text') + "\nNo. of seats = " + str(y[5]))
                    eventLabel.configure(text = eventLabel.cget('text') + "\nDuration = " + str(y[6]))
                    eventLabel.configure(text = eventLabel.cget('text') + "\nFees = " + str(y[7]))
                    eventLabel.configure(text = eventLabel.cget('text') + "\n\n")

            eventLabel.after(2000,labelEvents)

        labelEvents()

def createStudent(rno,fn, mn, ln, cn, e6,e7,e8,e9):
    sqlAddStud = "INSERT intO Student VALUES(?,?,?,?,?);"
    valAddStud = (str(rno), str(fn),str(mn),str(ln),int(cn))
    mycursor.execute(sqlAddStud,valAddStud)
    mydb.commit()

    sqlAddStud = "INSERT intO Card VALUES(?,?,?,?,?);"
    valAddStud = (int(str(e6)), str(e7),str(e8),int(str(e9)),str(rno))
    mycursor.execute(sqlAddStud,valAddStud)
    mydb.commit()
    showMessage()


class AddStudent(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        buttonStart = ttk.Button(self,text = "Back",command = lambda: controller.show_frame(UserPage))
        buttonStart.grid(row = 0, column = 0,sticky = "w")

        frame7 = tk.LabelFrame(self, padx = 5, pady = 5)
        frame7.grid(row = 1, column = 0,columnspan = 3,padx = 5, pady = 5,sticky = "nsew")

        R_NoLabel = tk.Label(frame7, text = "Registration Number- ")
        R_NoLabel.grid(row = 0, column = 0,padx = 5, pady = 5,sticky = "w")

        R_NoEntry = tk.Entry(frame7, width = 45, borderwidth = 1)
        R_NoEntry.grid(row = 0, column = 1, padx = 5, pady = 5,sticky = "e")

        FirstNLabel = tk.Label(frame7, text = "First Name- ")
        FirstNLabel.grid(row = 1, column = 0,padx = 5, pady = 5,sticky = "w")

        FirstNEntry = tk.Entry(frame7, width = 45, borderwidth = 1)
        FirstNEntry.grid(row = 1, column = 1, padx = 5, pady = 5,sticky = "e")

        MNLabel = tk.Label(frame7, text = "Middle Name- ")
        MNLabel.grid(row = 2, column = 0,padx = 5, pady = 5,sticky = "w")

        MNEntry = tk.Entry(frame7, width = 45, borderwidth = 1)
        MNEntry.grid(row = 2, column = 1, padx = 5, pady = 5,sticky = "e")

        LNLabel = tk.Label(frame7, text = "Last Name- ")
        LNLabel.grid(row = 3, column = 0,padx = 5, pady = 5,sticky = "w")

        LNEntry = tk.Entry(frame7, width = 45, borderwidth = 1)
        LNEntry.grid(row = 3, column = 1, padx = 5, pady = 5,sticky = "e")

        ContactLabel = tk.Label(frame7, text = "Contact Number- ")
        ContactLabel.grid(row = 4, column = 0,padx = 5, pady = 5,sticky = "w")

        ContactEntry = tk.Entry(frame7, width = 45, borderwidth = 1)
        ContactEntry.grid(row = 4, column = 1, padx = 5, pady = 5,sticky = "e")

        l6 = tk.Label(frame7, text = "Card Number- ")
        l6.grid(row = 5, column = 0,padx = 5, pady = 5,sticky = "w")

        e6 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e6.grid(row = 5, column = 1, padx = 5, pady = 5,sticky = "e")

        l7 = tk.Label(frame7, text = "Expiry Date (yyyy-mm-dd)- ")
        l7.grid(row = 6, column = 0,padx = 5, pady = 5,sticky = "w")

        e7 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e7.grid(row = 6, column = 1, padx = 5, pady = 5,sticky = "e")

        l8 = tk.Label(frame7, text = "Name on Card- ")
        l8.grid(row = 7, column = 0,padx = 5, pady = 5,sticky = "w")

        e8 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e8.grid(row = 7, column = 1, padx = 5, pady = 5,sticky = "e")

        l9 = tk.Label(frame7, text = "Registered Phone Number- ")
        l9.grid(row = 8, column = 0,padx = 5, pady = 5,sticky = "w")

        e9 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e9.grid(row = 8, column = 1, padx = 5, pady = 5,sticky = "e")


        buttonStart = ttk.Button(self,text = "Add Student",command = lambda: createStudent(R_NoEntry.get(),FirstNEntry.get(),MNEntry.get(),LNEntry.get(),ContactEntry.get(),e6.get(),e7.get(),e8.get(),e9.get()))
        buttonStart.grid(row = 2, column = 0,sticky = "nsew")

def registerStudent(e1,e2,e3,e5):
    sqlAddEvent = "INSERT intO registered_for VALUES(?,?);"
    valAddEvent = (str(e1), int(str(e2)))
    mycursor.execute(sqlAddEvent,valAddEvent)
    mydb.commit()

    mycursor.execute("SELECT Card_number FROM Card WHERE Registration_number = '"+ str(e1) + "'")
    e = mycursor.fetchall()
    for x in e:
        e4 = x[0]

    sqlAddEvent = "INSERT intO Payment VALUES(?,?,?,?);"
    valAddEvent = (int(str(e3)),int(str(e4)),str(e1),int(str(e2)))
    mycursor.execute(sqlAddEvent,valAddEvent)
    mydb.commit()

    sqlAddEvent = "INSERT intO Student_Transactions_history VALUES(?,?);"
    valAddEvent = (str(e5),str(e1))
    mycursor.execute(sqlAddEvent,valAddEvent)
    mydb.commit()
    showMessage()


class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        buttonStart = ttk.Button(self,text = "Back",command = lambda: controller.show_frame(UserPage))
        buttonStart.grid(row = 0, column = 0,sticky = "w")

        frame7 = tk.LabelFrame(self, padx = 5, pady = 5)
        frame7.grid(row = 1, column = 0,columnspan = 3,padx = 5, pady = 5,sticky = "nsew")

        buildingLabel = tk.Label(frame7, text = "Registration number- ")
        buildingLabel.grid(row = 0, column = 0,padx = 5, pady = 5,sticky = "w")

        e1 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e1.grid(row = 0, column = 1, padx = 5, pady = 5,sticky = "e")

        roomNumberLabel = tk.Label(frame7, text = "Event Number- ")
        roomNumberLabel.grid(row = 1, column = 0,padx = 5, pady = 5,sticky = "w")

        e2 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e2.grid(row = 1, column = 1, padx = 5, pady = 5,sticky = "e")

        tranid = tk.Label(frame7, text = "Transaction ID- ")
        tranid.grid(row = 2, column = 0,padx = 5, pady = 5,sticky = "w")

        e3 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e3.grid(row = 2, column = 1, padx = 5, pady = 5,sticky = "e")

        thist = tk.Label(frame7, text = "Transaction Details- ")
        thist.grid(row = 4, column = 0,padx = 5, pady = 5,sticky = "w")

        e5 = tk.Entry(frame7, width = 45, borderwidth = 1)
        e5.grid(row = 4, column = 1, padx = 5, pady = 5,sticky = "e")



        buttonStart = ttk.Button(self,text = "Register",command = lambda: registerStudent(e1.get(),e2.get(),e3.get(),e5.get()))
        buttonStart.grid(row = 2, column = 0,sticky = "nsew")


app = MainApp()
app.title("Event Registration")
app.minsize(250,20)
app.resizable(width=False, height=False)

app.mainloop()
