#Author:-18BCE077

#part3 ad part4 of the question are dealt here
from tkinter import *
from tkinter import simpledialog
import uuid 
import csv
import random
import pandas as pd
import datetime
import tkinter as tk    

std_marks=0  #to track total correct marks of  the student.
std_totalMarks=0   #to track the total marks student has attempted for.
class QuizMCQ:#to display MCQ type question on the window.
    q = []#list containg only questions.
    options = []#list containing list of options for particular question.
    a = []#list containing correct answer for quetions
    marks=[]#list containing marks to questions.
    qid=[]
    def __init__(self, master,quiz_id,std_id):
        self.readFile(master)  #to read the mcq type questions
        #print(self.q,self.options,self.a)
        self.opt_selected = tk.IntVar()
        self.quiz_id=quiz_id
        #print(self.quiz_id)
        self.std_id=std_id
        self.l=len(self.q)
        self.q_no=[]
        for i in range(0,self.l):
            self.q_no.append(i)
        #print(self.q_no)
        random.shuffle(self.q_no)#to randomly select a question
        #print(self.q_no)
        self.qn = self.q_no[0]
        self.correct = 0#to track the total marks student got in this section
        self.total_marks=0#to track the weightage of this section
        self.label=Label(master,text="MCQ Question")
        self.label.place(relx=0,rely=0)
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        self.button = Button(master, text="Next", command=self.next_btn)
        self.button.place(relx=0,rely=0.6)
    def readFile(self,master):#to read the Questioon file and store them
        with open('F:/nirma/Sem4/PSC/mcq_question.csv') as csv_file:
            reader=csv.reader(csv_file,delimiter=',');
            
            self.line_count=0;
            self.rows=[]
            for row in reader: 
                #print(row)
                self.qid.append(row[0])
                self.q.append(row[1])
                temp=[]
                temp.append(row[2])
                temp.append(row[3])
                temp.append(row[4])
                temp.append(row[5])
                self.options.append(temp)
                self.a.append(row[6])
                self.marks.append(row[7])
                #print(self.q,self.options,self.a)
    
    def create_q(self, master, qn):#to create the question field
        w = Label(master, text=self.q[qn])
        w.place(relx=0.1,rely=0.1)#to place the label on top left corner.
        return w

    def create_options(self, master, n):#to create option field
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="foo", variable=self.opt_selected, value=b_val+1)
            b.append(btn)
            btn.place(relx=0,rely=b_val/10+0.2)
            b_val = b_val + 1
        return b

    def display_q(self, qn):#to display question
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = self.q[qn]
        for op in self.options[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def check_q(self, qn):#to check whether the answer is correct or not
        if self.opt_selected.get() == int(self.a[qn]):
            return True
        return False

    def print_results(self):#to print result on cmd window.
        print("Score in MCQ: ", self.correct, "/", self.total_marks)
        global std_marks
        global std_totalMarks
        std_marks+=self.correct
        std_totalMarks+=self.total_marks
        print("your total: ",std_marks,"/",std_totalMarks)


    def next_btn(self):#code for next button.
        if self.check_q(self.qn):
            print("Correct")
            self.correct += int(self.marks[self.qn])
        else:
            print("Wrong")
            
        self.total_marks+=int(self.marks[self.qn])
        x=datetime.datetime.now()
        dict={"sid":[self.std_id],"qid":[self.qid[self.qn]],"ans":[self.opt_selected.get()],"quiz_id":[self.quiz_id],"date":[x]}
        df=pd.DataFrame.from_dict(dict)
        df.to_csv('F:/nirma/Sem4/PSC/quiz.csv',mode='a',index=False,header=False)
        
        if self.q_no.index(self.qn)+1 >= len(self.q):
            self.print_results()
        else:
            self.qn = self.q_no[self.q_no.index(self.qn) + 1]
            self.display_q(self.qn)
            

class QuizOneWord:#for one word type question
    q = []
    options = []
    a = []
    marks=[]
    qid=[]
    def __init__(self, master,quiz_id,std_id):
        self.readFile(master)  
        #print(self.q,self.options,self.a)
        self.quiz_id=quiz_id
        #print(self.quiz_id)
        self.std_id=std_id
        self.l=len(self.q)
        self.q_no=[]
        for i in range(0,self.l):
            self.q_no.append(i)
        #print(self.q_no)
        random.shuffle(self.q_no)
        #print(self.q_no)
        self.qn = self.q_no[0]
        self.correct = 0
        self.total_marks=0
        self.label=Label(master,text="One Word Question")
        self.label.place(relx=0.5,rely=0)
        self.ques = self.create_q(master, self.qn)
        self.display_q(self.qn)
        self.e= Entry()
        self.e.place(relx=0.5,rely=0.2)
        self.button = Button(master, text="Next", command=self.next_btn)
        self.button.place(relx=0.5,rely=0.3)
    def readFile(self,master):
        with open('F:/nirma/Sem4/PSC/oneword_question.csv') as csv_file:
            reader=csv.reader(csv_file,delimiter=',');
            
            self.line_count=0;
            self.rows=[]
            for row in reader: 
                #print(row)
                self.qid.append(row[0])
                self.q.append(row[1])
                self.a.append(row[2])
                self.marks.append(row[3])
                
    def create_q(self, master, qn):
        w = Label(master, text=self.q[qn])
        w.place(relx=0.5,rely=0.1)#to place the label in top right corner.
        return w

    def display_q(self, qn):
        self.ques['text'] = self.q[qn]
        

    def check_q(self, qn):
        if self.e.get() == self.a[qn]:
            return True
        return False

    def print_results(self):
        print("Score in One Word Answer: ", self.correct, "/", self.total_marks)
        global std_marks
        global std_totalMarks
        std_marks+=self.correct
        std_totalMarks+=self.total_marks
        print("your total: ",std_marks,"/",std_totalMarks)

    def next_btn(self):
        if self.check_q(self.qn):
            print("Correct")
            self.correct += int(self.marks[self.qn])
        else:
            print("Wrong")
            
        self.total_marks+=int(self.marks[self.qn])
        x=datetime.datetime.now()
        dict={"sid":[self.std_id],"qid":[self.qid[self.qn]],"ans":[self.e.get()],"quiz_id":[self.quiz_id],"date":[x]}
        df=pd.DataFrame.from_dict(dict)
        df.to_csv('F:/nirma/Sem4/PSC/quiz.csv',mode='a',index=False,header=False)
        if self.q_no.index(self.qn)+1 >= len(self.q):
            self.print_results()
        else:
            self.qn = self.q_no[self.q_no.index(self.qn) + 1]
            self.display_q(self.qn)


class QuizShortAns:#for short answer type questions
    q = []
    options = []
    a = []
    marks=[]
    qid=[]
    def __init__(self, master,quiz_id,std_id):
        self.readFile(master)  
        #print(self.q,self.options,self.a)
        self.quiz_id=quiz_id
        #print(self.quiz_id)
        self.std_id=std_id
        self.l=len(self.q)
        self.q_no=[]
        for i in range(0,self.l):
            self.q_no.append(i)
        #print(self.q_no)
        random.shuffle(self.q_no)
        #print(self.q_no)
        self.qn = self.q_no[0]
        self.correct = 0
        self.total_marks=0
        self.label=Label(master,text="Short Answer Question")
        self.label.place(relx=0,rely=0.7)
        self.ques = self.create_q(master, self.qn)
        self.display_q(self.qn)
        self.e= Entry()
        self.e.place(relx=0,rely=0.83)
        self.button = Button(master, text="Next", command=self.next_btn)
        self.button.place(relx=0,rely=0.9)
    def readFile(self,master):
        with open('F:/nirma/Sem4/PSC/short_question.csv') as csv_file:
            reader=csv.reader(csv_file,delimiter=',');
            
            self.line_count=0;
            self.rows=[]
            for row in reader: 
                #print(row)
                self.qid.append(row[0])
                self.q.append(row[1])
                self.a.append(row[2])
                self.marks.append(row[3])
                
    def create_q(self, master, qn):
        w = Label(master, text=self.q[qn])
        w.place(relx=0,rely=0.75)#to place the corner in bottom left corner.
        return w

    def display_q(self, qn):
        self.ques['text'] = self.q[qn]
        

    def print_results(self):
        print("Score in Short Question: ", self.correct, "/", self.total_marks)
        global std_marks
        global std_totalMarks
        std_marks+=self.correct
        std_totalMarks+=self.total_marks
        print("your total: ",std_marks,"/",std_totalMarks)

    def next_btn(self):
        #print(self.e.get().split(" "))
        #print(self.a[self.qn])
        m=[]
        w=''
        for x in self.a[self.qn]:
            if x=="[" or x=="]" or x=="'" or x==" ":
                continue
            elif x==',':
                m.append(w)
                w=''
            else:
                w+=x
        m.append(w)
        #print(m)
        t=int(self.marks[self.qn])
        l=len(m)
        corr_marks=t/l
        flag=0
        for x in (self.e.get().split(" ")):
            for y in m:
                #print(x," ",y)
                if x==y:
                    self.correct+=corr_marks
                    flag=1
        if flag:
            print("Good attempt")
        else:
            print("Wrong")
            
        self.total_marks+=int(self.marks[self.qn])
        x=datetime.datetime.now()
        dict={"sid":[self.std_id],"qid":[self.qid[self.qn]],"ans":[self.e.get()],"quiz_id":[self.quiz_id],"date":[x]}
        df=pd.DataFrame.from_dict(dict)
        df.to_csv('F:/nirma/Sem4/PSC/quiz.csv',mode='a',index=False,header=False)
        if self.q_no.index(self.qn)+1 >= len(self.q):
            self.print_results()
        else:
            self.qn = self.q_no[self.q_no.index(self.qn) + 1]
            self.display_q(self.qn)

class QuizLongAns:#for long answer type questions.
    q = []
    options = []
    a = []
    marks=[]
    qid=[]
    def __init__(self, master,quiz_id,std_id):
        self.readFile(master)  
        #print(self.q,self.options,self.a)
        self.quiz_id=quiz_id
        #print(self.quiz_id)
        self.std_id=std_id
        self.l=len(self.q)
        self.q_no=[]
        for i in range(0,self.l):
            self.q_no.append(i)
        #print(self.q_no)
        random.shuffle(self.q_no)
        #print(self.q_no)
        self.qn = self.q_no[0]
        self.correct = 0
        self.total_marks=0
        self.label=Label(master,text="Long Answer Question")
        self.label.place(relx=0.5,rely=0.5)
        self.ques = self.create_q(master, self.qn)
        self.display_q(self.qn)
        self.e= Entry()
        self.e.place(relx=0.5,rely=0.7)
        self.button = Button(master, text="Next", command=self.next_btn)
        self.button.place(relx=0.5,rely=0.8)
    def readFile(self,master):
        with open('F:/nirma/Sem4/PSC/long_question.csv') as csv_file:
            reader=csv.reader(csv_file,delimiter=',');
            
            self.line_count=0;
            self.rows=[]
            for row in reader: 
                #print(row)
                self.qid.append(row[0])
                self.q.append(row[1])
                self.a.append(row[2])
                self.marks.append(row[3])
                
    def create_q(self, master, qn):
        w = Label(master, text=self.q[qn])
        w.place(relx=0.5,rely=0.6)#to place the label in bottom right corner.
        return w

    def display_q(self, qn):
        self.ques['text'] = self.q[qn]
        

    def print_results(self):
        print("Score in Long Question: ", self.correct, "/", self.total_marks)
        global std_marks
        global std_totalMarks
        std_marks+=self.correct
        std_totalMarks+=self.total_marks
        print("your total: ",std_marks,"/",std_totalMarks)

    def next_btn(self):
        #print(self.e.get().split(" "))
        #print(self.a[self.qn])
        m=[]
        w=''
        for x in self.a[self.qn]:
            #print(x)
            if x=="[" or x=="]" or x=="'" or x==" ":
                continue
            elif x==',':
                m.append(w)
                w=''
            else:
                w+=x
            
        m.append(w)
        #print(m)
        t=int(self.marks[self.qn])
        l=len(m)
        corr_marks=t/l
        print(corr_marks)
        flag=0
        for x in (self.e.get().split(" ")):
            for y in m:
                #print(x," ",y)
                if x==y:
                    self.correct+=corr_marks
                    flag=1
        if flag:
            print("Good attempt")
        else:
            print("Wrong")
            
        self.total_marks+=int(self.marks[self.qn])
        x=datetime.datetime.now()
        dict={"sid":[self.std_id],"qid":[self.qid[self.qn]],"ans":[self.e.get()],"quiz_id":[self.quiz_id],"date":[x]}
        df=pd.DataFrame.from_dict(dict)
        df.to_csv('F:/nirma/Sem4/PSC/quiz.csv',mode='a',index=False,header=False)
        if self.q_no.index(self.qn)+1 >= len(self.q):
            self.print_results()
        else:
            self.qn = self.q_no[self.q_no.index(self.qn) + 1]
            self.display_q(self.qn)
    
class Quiz():
    def __init__(self,master):
        self.id = uuid.uuid1()#generates a 128 bit unique id for Quiz
        self.id=self.id.int&(1<<8)-1#to convert the 128 bit id to 8 bit
        #print(self.id)
        self.sid=simpledialog.askstring(title="Studentid",prompt="Enter Student ID: or end to exit")#asking the student for his/her id
        self.q_list=[1,2,3,4]
        
        for q in self.q_list:
            if q==1:
                app=QuizMCQ(master,self.id,self.sid)
            elif q==2:
                app=QuizOneWord(master,self.id,self.sid)
            elif q==3:
                app=QuizShortAns(master,self.id,self.sid)
            else:
                app=QuizLongAns(master,self.id,self.sid)
                

root=Tk()
root.geometry("500x300")
app=Quiz(root)
root.mainloop()