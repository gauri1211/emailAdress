from flask import Flask,request

app=Flask(__name__)

@app.route('/',methods=['GET'])
def welcome():
    return{
        "response":"app working fine",
        "status":200
    }

@app.route('/email/<string:email>',methods=['GET','POST'])
def email1(email):
    num=['1','2','3','4','5','6','7','8','9','0']
    name=''
    domainname=''
    extension=''  
    reg_char=['.' , '@']  
    atcounter=0
    dotcounter=0 
    for i in email:
      if atcounter==0 and i not in num and i not in reg_char:
        name+=i
      elif atcounter==1 and dotcounter==0 and i not in reg_char:
        domainname+=i
      elif atcounter==1 and dotcounter==1 and i not in reg_char:
        extension+=i
      elif i=='@':
        atcounter+=1
      elif i=='.':
        dotcounter+=1
      else:
        continue
    
    dict1={"name":name,"domainname":domainname,"extension":extension}
    return {
        "response":dict1,
        "email":email,
        "status":200
      }


app.run(debug=True,host="0.0.0.0",port =1111)