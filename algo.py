import math
from autocorrect import Speller
from textblob import TextBlob

# khai báo các kiểu
spell = Speller(lang='en')
f= open('symptoms.txt', 'r+')
f2 = open('conversation.txt', 'r+')
linestext = []
symptoms=[]
mp ={}
conversation={}

# hàm phân tách dấu phẩy ","
def handle_j(s):
    data = list(map(str,s.split(",")))
    return data

# hàm phân tách dấu cách " "
def handle_sp(s):
    data = list(map(str,s.split()))
    return data

# hàm sửa lỗi chính tả từ
def correct_word(s):
    data = TextBlob(s)
    return data.correct()

# phân tách text thành các từ
def handle(s):
    data = handle_j(s)
    res=[]
    for t in data:
        data2 = handle_sp(t)
        res+=data2
    return res

# đọc file xử lí symptoms
for s in f.readlines():
    linestext.append(s.strip())
for linetext in linestext:
    linelist = handle_j(linetext)
    for word in linelist:
        word = word.strip().lower()
        if word not in mp.keys():
            mp[word]=1
            symptoms.append(word)

# đọc file xử lí conversation
for s in f2.readlines():
    bot, pp = s.strip().split(":")
    conversation[bot.lower()]=pp

# tạo check dictionary ex:"01010010101"
def check_dic(s):
    data = handle(s)
    check={}
    for key in mp:
        check[key]=0
    for i in range(0,len(data)):
        if (data[i] in symptoms):
            check[data[i]]=1
        if (i>0):
            double_world=data[i-1]+" "+data[i]
            if (double_world in symptoms):
                check[double_world]=1
        if (i>1):
            tripple_world = data[i-2]+" "+data[i-1]+" "+data[i]
            if (tripple_world in symptoms):
                check[tripple_world]=1
    return check

# trả về list các symptoms
def list_symptoms():
    return symptoms

# trả về độ dài của database
def lendata():
    return len(linestext)

# check độ khớp với symptoms
def check_samples_symp(dica, dicb):
    res =0
    for word in symptoms:
        word = word.lower()
        if (dica[word]==1 and dicb[word]==1):
            res+=1
    return res


#take conversation
def conversation_dic():
    return conversation

# basic train 
def train_mode(mode,data):
    if (mode == "trainmode/conversation"):
        f2.write("\n"+data)
    #if (mode == "trainmode/symptoms"):

        
        

    
    





        