from flask import Flask, request, jsonify
import MySQLdb;
import algo

# connect server sql
db = MySQLdb.connect(host="127.0.0.1",    
                    user="root",         
                    passwd="minh01072007",  
                    db="sys")        

# khai báo


cur = db.cursor()
datasize = algo.lendata()
conv = algo.conversation_dic()
symplist = algo.list_symptoms()
sympsize = len(symplist)
default = {"id" : "0",
           "name" : "I can't help you",
           "medication" : "",
           "signs_symptoms" : "",
           "recommendation" : ""}

# get thông tin by id
def get_by_id(id):
    if (id==0):
        return default
    dic ={}
    cur.execute("SELECT * FROM illnesses WHERE id= %s" % id)
    data = cur.fetchall()
    dic["id"]=data[0][0]
    dic["name"]=data[0][1]
    dic["medication"]=data[0][2]
    dic["signs_symptoms"]=data[0][3]
    dic["recommendation"]=data[0][4]
    return dic

# tìm căn bệnh từ symptoms được cung cấp
def find_disease(s):      
    res=[]
    dic_input = algo.check_dic(s)
    for i in range(1,datasize+1):
        dic_id = get_by_id(i)
        sample = algo.check_samples_symp(dic_input,algo.check_dic(dic_id["signs_symptoms"].strip().lower()))
        if (sample>0):
            res.append((sample,i))
    res.sort()
    return res


def get_response(s):
    s =s.lower()
    t = s
    if s in conv.keys():
        return conv[s]
    if (t.find("trainmode")!=-1):
        mode, data = t.lower().split(">")
        if (mode=="trainmode/conversation" or mode == "trainmode/symptomps"):
            algo.train_mode(mode,data)
            return "Thank for teach me!"
    datalist = find_disease(s)
    n = len(datalist)-1
    if (n<0):
        return "Sorry I can't help you, my knowledge is limited."
    dic1 = get_by_id(datalist[n][1])
    recommendlist = dic1["recommendation"].split(".")
    res = "I think you have " + dic1["name"] + "<br>You should drink some: " + dic1["medication"].lower() + ".<br>I would recommend you:"
    for s in recommendlist:
        if (s != ""):
            res += "<br> +)" + s + "."
    #<a href="http://hoclaptrinh.vn">Hoclaptrinh.vn</a>
    #res += "<br>You could also find more about the disease on Wikipedia:" + f"https://en.wikipedia.org/wiki/{dic1['name']}"+'"'+">"+dic1["name"]+"</a>"

    if n>0:
        res += "<br>You could also have:"
        dic2 = get_by_id(datalist[n-1][1])
        res += "<br>+) " + dic2["name"]
    if n>1:
        dic3 = get_by_id(datalist[n-2][1])
        res += "<br>+) " + dic3["name"] + "."
    return res
