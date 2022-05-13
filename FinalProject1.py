from tkinter import *
import csv


class GUI:
    def __init__(self, window) -> None:
        '''
        This section of code will create the name textbox
        '''
        self.window = window
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Name')
        self.entry_name = Entry(self.frame_name)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', pady=10)  # anchor='w' helps to change the frame position from center to west.

        '''
        This code will create the reset button
        '''

        self.button_reset = Button(self.window, text='RESET', command=self.reset)
        self.button_reset.pack(side='bottom', pady=10)

        '''
        This code will create the save button
        '''
        self.button_save = Button(self.window, text='SAVE', command=self.infoCheck)
        self.button_save.pack(side='bottom', pady=10)

        '''
        This button will exit the program
        '''

        self.button_exit = Button(self.window, text='EXIT', command=window.destroy)
        self.button_exit.pack(side='bottom', pady=10)

        '''
        This code will create the age textbox
        '''
        self.frame_age = Frame(self.window)
        self.label_age = Label(self.frame_age, text='Age')
        self.entry_age = Entry(self.frame_age)
        self.label_age.pack(padx=5, side='left')
        self.entry_age.pack(padx=15, side='left')
        self.frame_age.pack(anchor='w', pady=10)

        '''
        This code will create the class textbox
        '''

        self.frame_class = Frame(self.window)
        self.label_class = Label(self.frame_class, text='Class')
        self.entry_class = Entry(self.frame_class)
        self.label_class.pack(padx=5, side='left')
        self.entry_class.pack(padx=15, side='left')
        self.frame_class.pack(anchor='w', pady=10)

        '''
        This code will create the teacher textbox
        '''

        self.frame_teacher = Frame(self.window)
        self.label_teacher = Label(self.frame_teacher, text='Teacher')
        self.entry_teacher = Entry(self.frame_teacher)
        self.label_teacher.pack(padx=5, side='left')
        self.entry_teacher.pack(padx=15, side='left')
        self.frame_teacher.pack(anchor='w', pady=10)

        '''
        This section of code will create the Status radio buttons
        '''
        self.frame_status = Frame(self.window)
        self.label_status = Label(self.frame_status, text='Status')
        self.label_status.pack(padx=5, side='left')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.status_student = Radiobutton(self.frame_status, text='Student', variable=self.radio_1, value=0)
        self.status_staff = Radiobutton(self.frame_status, text='Staff', variable=self.radio_1, value=1)
        self.status_both = Radiobutton(self.frame_status, text='Both', variable=self.radio_1, value=2)
        self.status_student.pack(side='left')
        self.status_staff.pack(side='left')
        self.status_both.pack(side='left')
        self.label_status.pack(side='left')
        self.frame_status.pack(side='left')

        self.frame_error = Frame(self.window)
        self.label_error = Label(self.frame_error, text='Error: Give all required info')
        self.label_error.pack(side='bottom')



    '''
    This function will check to see if there are is any missing information in your entry before saving the data
    '''


    def infoCheck(self) -> None:
        if self.entry_name.get() == '' or self.entry_age.get() == '' or self.entry_class.get() == '' or self.entry_teacher.get() == '' or self.radio_1.get() == -1:
            self.frame_error.pack(padx=5, anchor='w', side='bottom')
        else:
            self.clicked()
    '''
    If there are no errors, the data is computed. 
    '''
    def clicked(self) -> None:
        '''
        Get all the values from the GUI inputs
        '''
        nameText: str = self.entry_name.get()
        ageText = int(self.entry_age.get())
        ageText: int = (ageText) * 2
        classText: str = self.entry_class.get()
        teacherText: str = self.entry_teacher.get()
        radioText = self.radio_1.get()

        '''
        Change the radio values to the status of the person
        '''
        if radioText == 0:
            radioText = 'Student'
        elif radioText == 1:
            radioText = 'Staff'
        else:
            radioText = 'Both'

        '''
        Copy this information to a CSV file
        '''

        with open('records.csv', 'a', newline='') as records:
            content = csv.writer(records)
            content.writerow([nameText, ageText, radioText, classText, teacherText])

        '''
        Delete The text and values on the GUI window
        '''
        self.entry_name.delete(0, END)
        self.entry_age.delete(0, END)
        self.radio_1.set(-1)
        self.entry_class.delete(0, END)
        self.entry_teacher.delete(0, END)

    '''
    This function will reset the text
    '''
    def reset(self) -> None:
        self.entry_name.delete(0, END)
        self.entry_age.delete(0, END)
        self.radio_1.set(-1)
        self.entry_class.delete(0, END)
        self.entry_teacher.delete(0, END)