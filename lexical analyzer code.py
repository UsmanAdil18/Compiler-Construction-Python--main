keywords = {
    "super":"super",
    "this" : "this",
    "int" : "dt",
    "float" : "dt", 
    "char" : "dt",
    "string" : "dt",
    "Class" : "Class",
    "try" : "try",
    "catch" : "catch",
    "if": "if",
    "elif":"elif",
    "else": "else",
    "return": "return",
    "function":"function",
    "start":"start",
    "final":"final",
    "abstract":"abstract",
    "extends":"extends",
    "till":"till",
    "new":"new"
   }
operators = {
    "=" : "AS",
    "+=":"CA",
    "-=":"CA",
    "/=":"CA",
    "*=":"CA",
    "%=":"CA",
    "++":"incdec",
    "--":"incdec",
    "!":"!",
    "+":"PM",
    "-":"PM",
    "*":"MDM",
    "/":"MDM",
    "%":"MDM",
    "<" : "RO",
    ">" : "RO",
    ">=" : "RO",
    "<=" : "RO",
    "!=" : "RO",
    "&&" : "AND",
    "||" : "OR",
    "==" : "CO"
}
punctuators = {
    ":":":",
    "(" : "(",
    ")" : ")",
    "[" : "[",
    "]" : "]",
    ";" : ";",
    "," : ",",
    "{" : "{",
    "}" : "}",
}
from operator import le
import re
def isOpr(checkVar):
    if checkVar in operators:
        return operators[checkVar]
    else:
        return " "    
def isPunct(checkVar):
    if checkVar in punctuators:
        return True
    else:
        return False    
def isKW(checkVar):
    if checkVar in keywords:
        return keywords[checkVar]
    else:
        return " "
regex = '^[A-Za-z_][A-Za-z0-9_]*'
def isID(checkVar):
    if (re.search(regex,checkVar)):
        return True
    else:
        return False 
# Integer Validation RE
regex2 = '^([1-9]\d*|0)$'
def isInt(checkVar):
    if (re.search(regex2,checkVar)):
        return True
    else:
        return False
import re
#character validation RE
regex3 = "(^'.')|(^'\.')"
def isChar(checkVar):
    print(checkVar)
    if (re.match(regex3,checkVar)):
        return True
    else :
        return False     
#String validation
regex4 = '[\.\"\'\/]*[a-zA-z0-9]*'
def isStr(s):
    if (re.search(regex4,s)):
        return True
    else:
        return False   
#Float Validation
regex5 = '[+-]?([0-9]*[.])?[0-9]+$'
def isFloat(num):
    if(re.search(regex5,num)):
        return True
    else:
        return False                            
def isKW_or_isID(temp):
    Str = isKW(temp)
    if Str!=" ":
        obj = Tokens(Str,temp,lineNum)
        objects.append(obj)
    else:    
        ch = isID(temp)
        if (ch):
            obj = Tokens("ID",temp,lineNum)
            objects.append(obj)        
class Tokens:
    def __init__(self,cp,vp,linenum):
        self.cp = cp
        self.vp = vp
        self.lineNumber = linenum
with open ("work.txt","r") as f:
    data = f.read()    

objects = []   
x=0
i=0
temp ="" 
temp2 = ""
lineNum = 1
while i<len(data):
    if data[i] == "\n":
        if (isInt(temp)):
            obj = Tokens("int_const",temp,lineNum)
            objects.append(obj)
        else:
            isKW_or_isID(temp)
        temp=""    
        lineNum +=1
    #breaking if space occurs and check temp for kw and ID
    elif data[i] == " ":
        if (isInt(temp)):
            obj = Tokens("int_const",temp,lineNum)
            objects.append(obj)
        else:
            isKW_or_isID(temp)
        temp = ""    
       
    elif (isPunct(data[i])):
        if (isInt(temp)):
            obj = Tokens("int_const",temp,lineNum)
            objects.append(obj)
        else:
            isKW_or_isID(temp)
        temp = ""
    #breaking at punctuators and creating its object and checking temp for kw and id
        isKW_or_isID(temp)     
        temp = ""
        obj = Tokens(data[i],data[i],lineNum)
        objects.append(obj)
    #single line comments    
    elif data[i]=="#":
        while data[i]!="\n":
            temp+=data[i]
            i+=1
        lineNum+=1    
        temp=""    
    
    elif data[i] == "="  or data[i] == "/" or data[i] == "*" or data[i] == "%" or data[i] == ">" or data[i] == "<" or data[i] == "!": 
        #Breaking on operators and checking temp for kw and ID
        
        if (isInt(temp)):
            obj = Tokens("int_const",temp,lineNum)
            objects.append(obj)
        else:       
            isKW_or_isID(temp)
        temp = ""
            

        #Checking for compound assignment and relational operators
        if data[i+1]=="=":
            
            temp = data[i] + data[i+1]
            i+=1
            Str = isOpr(temp)
            if Str!=" ":
                obj = Tokens(Str,temp,lineNum)   
                objects.append(obj)
        else:
            temp = data[i]
            Str = isOpr(temp)
            if Str!=" ":
                obj = Tokens(Str,temp,lineNum)   
                objects.append(obj)
        temp=""        
    elif (data[i]=='+'):  
        if (isInt(temp)):
            obj = Tokens("int_const",temp,lineNum)
            objects.append(obj)
        else:    
            isKW_or_isID(temp)
        temp = ""
        if(data[i+1]=='+' or data[i+1]=='='):
            temp = data[i] + data[i+1]
            i+=1
            Str = isOpr(temp)
            if Str!=" ":
                obj = Tokens(Str,temp,lineNum)   
                objects.append(obj)
        else:
            temp = data[i]
            Str = isOpr(temp)
            if Str!=" ":
                obj = Tokens(Str,temp,lineNum)   
                objects.append(obj)
        temp=""        
    elif (data[i]=='-'):  
        if (isInt(temp)):
            obj = Tokens("int_const",temp,lineNum)
            objects.append(obj)
        else:    
            isKW_or_isID(temp)
        temp = ""
        if(data[i+1]=='-' or data[i+1]=='='):
            temp = data[i] + data[i+1]
            i+=1
            Str = isOpr(temp)
            if Str!=" ":
                obj = Tokens(Str,temp,lineNum)   
                objects.append(obj)
        else:
            # print("check")
            temp = data[i]
            Str = isOpr(temp)
            if Str!=" ":
                obj = Tokens(Str,temp,lineNum)   
                objects.append(obj)
        temp=""                
    elif (data[i]=='&'):  
        if (isInt(temp)):
            obj = Tokens("int_const",temp,lineNum)
            objects.append(obj)
        else:    
            isKW_or_isID(temp)
        temp = ""
        if(data[i+1]=='&'):
            temp = data[i] + data[i+1]
            i+=1
            Str = isOpr(temp)
            if Str!=" ":
                obj = Tokens(Str,temp,lineNum)   
                objects.append(obj)
        else:
            temp = data[i]
            Str = isOpr(temp2)
            if Str!=" ":
                obj = Tokens(Str,temp2,lineNum)   
                objects.append(obj)
        temp=""
    elif (data[i]=='|'):  
        if (isInt(temp)):
            obj = Tokens("int_const",temp,lineNum)
            objects.append(obj)
        else:    
            isKW_or_isID(temp)
        temp = ""
        if(data[i+1]=='|'):
            temp = data[i] + data[i+1]
            i+=1
            Str = isOpr(temp)
            if Str!=" ":
                obj = Tokens(Str,temp,lineNum)   
                objects.append(obj)
        else:
            temp = data[i]
            Str = isOpr(temp2)
            if Str!=" ":
                obj = Tokens(Str,temp2,lineNum)   
                objects.append(obj)
        temp=""                

    #Character 
    elif data[i]=="\'":
        if (isInt(temp)):
            obj = Tokens("int_const",temp,lineNum)
            objects.append(obj)
        else:    
            isKW_or_isID(temp)
        temp=""    
        spec_chars=['n','r','t','b','0','\'','\"','\\']
        temp+=data[i]
        i+=1
        b=True
        while b:
            if data[i]=="\'":
                temp+=data[i]
                b=False
            elif data[i] =='\\':
                temp+=data[i]+data[i+1]
                i+=2
            elif data[i] == data[-1] :
                temp+=data[i]
                obj = Tokens("invalid-chr",temp,lineNum)  
                objects.append(obj)
                b=False
            else:
                temp+=data[i]
                i+=1
        if len(temp)>4:
            obj = Tokens("invalid-chr",temp,lineNum)
            objects.append(obj)
        elif len(temp)==3:
            if(isChar(temp)):
                obj = Tokens("chr_const",temp,lineNum)
                objects.append(obj)
        elif len(temp)==4:
            if temp[1]=='\\' and temp[2] in spec_chars:
                obj = Tokens("chr_const",temp,lineNum)
                objects.append(obj)
            else:
                obj = Tokens("invalid-chr",temp,lineNum)
                objects.append(obj) 
        temp=""    

    elif data[i]=="\"":
        temp+=data[i]
        a = True
        i+=1
        while a:
            if data[i]=="\"":
                a=False
            elif data[i] =='\\':
                temp+=data[i]+data[i+1]
                i+=2
            elif data[i] == data[-1] :
                temp+=data[i]
                obj = Tokens("invalid-string",temp,lineNum)  
                objects.append(obj)
                a=False
                
            else:
                temp+=data[i]
                i+=1
        if(isStr(temp)):
            obj = Tokens("str_const",temp,lineNum)   
            objects.append(obj)
        temp = ""
    #float work
    elif data[i]=='.':
        if (temp.isnumeric()) or temp == "":
            temp+=data[i]
            i+=1
            p = True
            while p:
                if data[i] in operators or data[i] in punctuators or data[i]=="\n" or data[i]=='.' :

                    if (isID(temp[1:])):
                        obj = Tokens(".",".",lineNum)   
                        objects.append(obj)
                        obj = Tokens("ID",temp[1:],lineNum)
                        objects.append(obj)

                    elif (isFloat(temp)):
                         obj = Tokens("float_const",temp,lineNum)   
                         objects.append(obj)
                    else:
                        obj = Tokens("invalid_float_const",temp,lineNum)   
                        objects.append(obj)
                    temp=""
                    i-=1    
                    p = False    
                else:
                    temp+=data[i]
                    i+=1        
        
        elif (isInt(temp)):
            i-=1
            obj = Tokens("int_const",temp,lineNum)
            objects.append(obj)
        else:
            i-=1    
            isKW_or_isID(temp)
        temp=""
        
    else:
        temp+=data[i]
    i+=1
obj = Tokens("$","$",lineNum-1)   
objects.append(obj)
values = []
# # print(type(objects[0]))
for i in objects:
     values.append([i.cp,i.vp,str(i.lineNumber)])
for i in objects:
    print(i.cp,i.vp,i.lineNumber)         
with open('C:/Users/Muhammad Sameer/OneDrive/Desktop/compiler/laxical.txt','w')as f:
    for i in values:
        f.write(i[0]+" "+i[1]+" "+i[2]+"\n")
# print(values)
