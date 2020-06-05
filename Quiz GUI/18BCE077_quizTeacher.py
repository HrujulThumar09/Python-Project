from tkinter import simpledialog
import uuid 
import csv
import random
import pandas as pd
import datetime
import tkinter as tk
    
#Part1 and Part2 of thq Question are handled here    
class teacher():
    def __init__(self):
        self.inp()
        
    def inp(self):
        self.root=tk.Tk()
        self.root.withdraw()
        while(True):
            self.type=simpledialog.askstring(title="Type",prompt="Enter Question type: \n1. MCQ\n2. One word\n3. short answer\n4. long answer : ")#Asking the teacher for type of question
            self.qid=simpledialog.askstring(title="Qid",prompt="Enter Question ID: ")#Asking teacher for quiestion id
            self.marks=simpledialog.askstring(title="Marks",prompt="Enter Marks of the Question: ")#asking teacher for mark
            self.ques=simpledialog.askstring(title="Question",prompt="Enter Question : ")#asking teacher to enter the question
            if (self.type=="1"):#for MCQ type Questions
                self.op1=simpledialog.askstring(title="option",prompt="Enter Option 1: ")#Asking for options
                self.op2=simpledialog.askstring(title="option",prompt="Enter Option 2: ")
                self.op3=simpledialog.askstring(title="option",prompt="Enter Option 3: ")
                self.op4=simpledialog.askstring(title="option",prompt="Enter Option 4: ")
                self.qid='M'+self.qid#generating a proper Question id
                self.correct=simpledialog.askstring(title="Correct option",prompt="Enter option number which is correct: ")#asking for the correct option.
                dict={"qid":[self.qid],"q":[self.ques],"op1":[self.op1],"op2":[self.op2],"op3":[self.op3],"op4":[self.op4],"correct":[self.correct],"marks":[self.marks]}
                df=pd.DataFrame.from_dict(dict)
                df.to_csv('F:/nirma/Sem4/PSC/mcq_question.csv',mode='a',index=False,header=False)#storing the question in CSV file
                
            elif (self.type=="2"):#for One word type question
                self.correct=simpledialog.askstring(title="Correct word",prompt="Enter the word: ")#asking the correct word
                self.qid='O'+self.qid
                dict={"qid":[self.qid],"q":[self.ques],"correct":[self.correct],"marks":[self.marks]}
                df=pd.DataFrame.from_dict(dict)
                df.to_csv('F:/nirma/Sem4/PSC/oneword_question.csv',mode='a',index=False,header=False)
            elif (self.type=="3"):#for short answer type questions.
                self.keywords=[]
                while(True):
                    self.temp=simpledialog.askstring(title="Keyword",prompt="Enter keyword word to be present in the answer and 1 to exit: ")#askig for the keywords to be present in the answer.
                    if(self.temp=="1"):
                        break
                    self.keywords.append(self.temp)
                self.qid='S'+self.qid
                dict={"qid":[self.qid],"q":[self.ques],"correct":[self.keywords],"marks":[self.marks]}
                df=pd.DataFrame.from_dict(dict)
                df.to_csv('F:/nirma/Sem4/PSC/short_question.csv',mode='a',index=False,header=False)
            elif (self.type=="4"):#for long answer type question
                self.keywords=[]
                while(True):
                    self.temp=simpledialog.askstring(title="Keyword",prompt="Enter keyword to be  present in the answer and 1 to exit: ")
                    if(self.temp=="1"):
                        break
                    self.keywords.append(self.temp)
                    
                self.qid='L'+self.qid
                dict={"qid":[self.qid],"q":[self.ques],"correct":[self.keywords],"marks":[self.marks]}
                df=pd.DataFrame.from_dict(dict)
                df.to_csv('F:/nirma/Sem4/PSC/long_question.csv',mode='a',index=False,header=False)
                
            self.ch=simpledialog.askstring(title="Choice",prompt="Enter 1 to continue 0 to exit: ")
            if(self.ch=="0"):
                break
                
                
app = teacher()