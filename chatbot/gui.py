from tkinter import*

from tensorflow.keras.models import load_model
model = load_model("chatbot.h5")
import pickle
from nltk.stem.lancaster import LancasterStemmer
import pandas as pd
import requests
import numpy as np
import json
import random
intents = json.loads(open('intents.json').read())
url='https://api.covid19api.com/summary'
resp = requests.get(url)
data = resp.json()
url_dist='https://api.covid19india.org/state_district_wise.json'
resp1= requests.get(url_dist)
data1 = resp1.json()


def main_window():
    global main_frame
    
    main_frame=Frame(gui,width=400,height=489).place(x=0,y=0)
    background=Label(main_frame,image=bg).pack()
  
    yes_btn=Button(main_frame,text='Yes',padx=30,bg='green',command=chat_window).place(x=80,y=420)
    no_btn=Button(gui,text='No',padx=30,bg='red',command=gui.destroy).place(x=180,y=420)

def chat_window():
    global chat_frame
    global msg_entry
    
    global scrollable_frame
    chat_frame=Frame(main_frame,width=400,height=489,bg='#0F2727').place(x=0,y=0)
    msg_entry = Entry(chat_frame,textvariable = query,bd=5,fg='#5F22DA',bg='#42DFBC',font=('Cambria',12,'bold')).place(height=40,width=350,x=5,y=445)
    send=Button(chat_frame,text='Send',bg='#06B654',command=s).place(x=360,y=445,height=40)
    msg_frame=Frame(chat_frame,width=390,bg='#C3E545')
    canvas = Canvas(msg_frame,height=430,width=370,bg='#C3E545')
    scrollbar = Scrollbar(msg_frame, orient="vertical", bg='#C3E545',command=canvas.yview)
    scrollable_frame = Frame(canvas,bg='#C3E545')


    scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    msg_frame.place(x=5,y=5)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
   
 
    

def s():
    global k
    global a
    
    
    ques=query.get()
    
    per=Label(scrollable_frame,image=boy,bg='#C3E545').grid(column=0,row=a,sticky=W)
    a=a+2
    text=Message(scrollable_frame,text=ques,bg='#75DE9A',width=220,highlightbackground='#0CD853',highlightthickness=3).grid(column=2,row=a,sticky=W)
    a=a+1
    
    m=classify(ques)
   
    st.append(m)
    if m=='pass':
        msg1='In order to travel interstate during lockdown, you will need an e-pass.'
        msg2='Indian government has developed a website for this. You can easily obtain an e-pass by filling in the required details.'
        msg3='URL : https://serviceonline.gov.in/epass'
        bot=Label(scrollable_frame,image=logo,bg='#C3E545').grid(column=0,row=a,sticky=W)
        a=a+2
        text=Message(scrollable_frame,text=msg1,bg='#EFCB71',width=220,highlightbackground='#F05318',highlightthickness=3).grid(column=2,row=a,sticky=W)
        a=a+2
        text=Message(scrollable_frame,text=msg2,bg='#EFCB71',width=220,highlightbackground='#F05318',highlightthickness=3).grid(column=2,row=a,sticky=W)
        a=a+2
        text=Message(scrollable_frame,text=msg3,bg='#EFCB71',width=220,highlightbackground='#F05318',highlightthickness=3).grid(column=2,row=a,sticky=W)
        a=a+2
        
      
    elif m=='statistics':
        bot=Label(scrollable_frame,image=logo,bg='#C3E545').grid(column=0,row=a,sticky=W)
        a=a+2
        pos_global='Globally, '+str(data['Global']['TotalConfirmed'])+' people have been tested corona positive.'
        text=Message(scrollable_frame,text=pos_global,bg='#EFCB71',width=220,highlightbackground='#F05318',highlightthickness=3).grid(column=2,row=a,sticky=W)
        a=a+2
        death_global=str(data['Global']['TotalDeaths'])+' people have died and '+str(data['Global']['TotalRecovered'])+' have recovered from the disease till now'
        text=Message(scrollable_frame,text=death_global,bg='#EFCB71',width=220,highlightbackground='#F05318',highlightthickness=3).grid(column=2,row=a,sticky=W)
        a=a+2
        text=Message(scrollable_frame,text='Which country are you from?',bg='#EFCB71',width=220,highlightbackground='#F05318',highlightthickness=3).grid(column=2,row=a,sticky=W)
        a=a+2
    elif m=='helpline':
        ans=response(m)
        bot=Label(scrollable_frame,image=logo,bg='#C3E545').grid(column=0,row=a,sticky=W)
        a=a+2
        text=Message(scrollable_frame,text=ans,bg='#EFCB71',width=220,highlightbackground='#F05318',highlightthickness=3).grid(column=2,row=a,sticky=W)
        a=a+2
        text=Message(scrollable_frame,text='Which state are you from?',bg='#EFCB71',width=220,highlightbackground='#F05318',highlightthickness=3).grid(column=2,row=a,sticky=W)
        a=a+2
        
   
    else:
        if k==0:
            ans=response(m)
            bot=Label(scrollable_frame,image=logo,bg='#C3E545').grid(column=0,row=a,sticky=W)
            a=a+2
            text=Message(scrollable_frame,text=ans,bg='#EFCB71',width=220,highlightbackground='#F05318',highlightthickness=3).grid(column=2,row=a,sticky=W)
            a=a+2
        if k>=1:
            if st[k-1]=='helpline':
                x=pd.read_csv('state.csv')
                for i in range(len(x)):
                    if x['State'][i]==ques:
                        hp=x['num'][i]
                        bot=Label(scrollable_frame,image=logo,bg='#C3E545').grid(column=0,row=a,sticky=W)
                        a=a+2
                        text=Message(scrollable_frame,text=hp,bg='#EFCB71',width=220,highlightbackground='#F05318',highlightthickness=3).grid(column=2,row=a,sticky=W)
                        a=a+2
            if st[k-1]=='statistics':
                l=len(data['Countries'])
                for i in range(l):
                    if data['Countries'][i]['Country']==ques:
                        pos_cntry='A total of '+str(data['Countries'][i]['TotalConfirmed'])+' have been tested positive in '+ques
                        death_cntry=str(data['Countries'][i]['TotalDeaths'])+' have died and '+str(data['Countries'][i]['TotalRecovered'])+' have recovered till now'
                        bot=Label(scrollable_frame,image=logo,bg='#C3E545').grid(column=0,row=a,sticky=W)
                        a=a+2
                        text=Message(scrollable_frame,text=pos_cntry,bg='#EFCB71',width=220,highlightbackground='#F05318',highlightthickness=3).grid(column=2,row=a,sticky=W)
                        a=a+2
                        text=Message(scrollable_frame,text=death_cntry,bg='#EFCB71',width=220,highlightbackground='#F05318',highlightthickness=3).grid(column=2,row=a,sticky=W)
                        a=a+2
                        text=Message(scrollable_frame,text='Enter your State and District name separated by comma(,) ',bg='#EFCB71',width=220,highlightbackground='#F05318',highlightthickness=3).grid(column=2,row=a,sticky=W)
                        a=a+2
                        text=Message(scrollable_frame,text='Example Andhra Pradesh,Visakhapatnam',bg='#EFCB71',width=220,highlightbackground='#F05318',highlightthickness=3).grid(column=2,row=a,sticky=W)
                        a=a+2
                            
           
            if st[k-2]=='statistics':
                district=ques.split(',')
                state=district[0]
                dist=district[1]
                pos_dist= ' In '+dist+' '+str(data1[state]['districtData'][dist]['confirmed'])+' have been tested corona positive till now'
                death_dist=str(data1[state]['districtData'][dist]['deceased'])+' people have died and '+str(data1[state]['districtData'][dist]['recovered'])+' have recovered'
                active_dist='Total active cases in ' +dist+' is '+str(data1[state]['districtData'][dist]['active'])
                bot=Label(scrollable_frame,image=logo,bg='#C3E545').grid(column=0,row=a,sticky=W)
                a=a+2
                text=Message(scrollable_frame,text=pos_dist,bg='#EFCB71',width=220,highlightbackground='#F05318',highlightthickness=3).grid(column=2,row=a,sticky=W)
                a=a+2
                text=Message(scrollable_frame,text=death_dist,bg='#EFCB71',width=220,highlightbackground='#F05318',highlightthickness=3).grid(column=2,row=a,sticky=W)
                a=a+2
                text=Message(scrollable_frame,text=active_dist,bg='#EFCB71',width=220,highlightbackground='#F05318',highlightthickness=3).grid(column=2,row=a,sticky=W)
                a=a+2
            
                
                        
                    
        
            if st[k-1]!='helpline'and st[k-1]!='statistics' and st[k-2]!='statistics':
                ans=response(m)
                bot=Label(scrollable_frame,image=logo,bg='#C3E545').grid(column=0,row=a,sticky=W)
                a=a+2
                text=Message(scrollable_frame,text=ans,bg='#EFCB71',width=220,highlightbackground='#F05318',highlightthickness=3).grid(column=2,row=a,sticky=W)
                a=a+2
        
            
    
    k=k+1
    
   


    
def classify(line):
    vocab = pickle.load(open("vocab.pkl",'rb'))
    label= pickle.load(open("label.pkl",'rb'))
    stemmer = LancasterStemmer()
    
    new_sentence=[]
    new_sentence.append(line.split())
    
    ignore_words=['?','!']
    for st in new_sentence:
        features=[stemmer.stem(w.lower()) for w in st if w not in ignore_words]
    bag=[0]*len(vocab)
    
    for w in vocab:
        if w in features:
            bag.append(1)
        else:
            bag.append(0)
    p=np.array(bag)
    
    res=model.predict(np.array([p]))[0]
    
    for [i,r] in enumerate(res):
        if(r>0.5):
            return (label[i])
    

def response(m):
    intent_list= intents["intents"]
    for i in intent_list:
        if(i['tag']==m):
            return random.choice(i['responses'])

gui = Tk()
gui.title('CovidBOT')
gui.geometry("400x489")
gui.iconbitmap(r'icon.ico')
bg=PhotoImage(file="bg.png")

logo=PhotoImage(file='ch.png')
boy=PhotoImage(file='boy.png')
query=StringVar()
ans=StringVar()
a=0
st=[]
k=0



main_window()
gui.mainloop() 
