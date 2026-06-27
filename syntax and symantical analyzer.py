class Tokens:
    def __init__(self,cp, vp, lineNumber):
        self.cp = cp
        self.vp = vp
        self.lineNumber = str(lineNumber)
    def __repr__(self):
        return f"Tokens(cp={self.cp}, vp={self.vp}, lineNumber={self.lineNumber})"
with open('C:/Users/Muhammad Sameer/OneDrive/Desktop/compiler/laxical.txt', 'r') as f:
    rows = [r.strip().split(' ') for r in f.readlines()]
    ts = [Tokens(*row) for row in rows]
class DT:
    def __init__(self):
        self.data_table()
    def data_table(self):
        self.data_table_list=[]
        self.x=0
    def insertDT(self,name,type,tm,ref):
        self.name = name
        self.type = type
        self.tm = tm
        self.ref = ref
        self.check = False 
        self.inner_list = [name,type,tm,ref] 
        if len(self.data_table_list)==0:
            self.data_table_list.append(self.inner_list)
            return True
        else:
            for i in self.data_table_list:
                if i[0]==name and i[3]==ref:
                    self.check = True
                    return False
        if self.check == False:
            self.data_table_list.append(self.inner_list)            
    def lookupDT(self,N,cname):
        self.a = False
        if len(self.data_table_list)==0:
            return False
        else:
            for i in self.data_table_list:
                if i[0]==N and i[3]==cname:
                    self.a = True 
                    break
            return self.a        
    def lookupDT3(self,name):
        self.name = name 
        for i in self.data_table_list:
            if i[0] == name:
                return i[1]
                break



    # def lookupDT2(self,N,pl,cname):
    #     if len(self.data_table_list)==0:
    #         return True
    #     else:    
    #         for i in self.data_table_list:
    #             if i[0]==N and   i[3]==cname:
    #                 return False
    #             else:
    #                 return True
    def insertDT2(self,N,type,tm,ref):
        self.N = N
        self.type = type
        self.tm = tm
        self.ref = ref
        self.inner_list = [N,type,tm,ref] 
        self.check = False
        if len(self.data_table_list)==0:
            self.data_table_list.append(self.inner_list)
            return True
        else:
            for i in self.data_table_list:
                if i[0]==self.inner_list[0] and i[3]==self.inner_list[3]:
                    self.check = True
                    return False
                # else:
                    # return True   
        if self.check == False:
            self.data_table_list.append(self.inner_list)
            # for j in range(len(self.data_table_list)):
            #     if(self.data_table_list[j][0]==N) and (self.data_table_list[j][3]==cname):   
            #         return False
            #     else:
            #         return True
    def rtList(self):
        return self.data_table_list

        
        

class MDT:
    def __init__(self):
        self.mdtList=[] 
    def addmdt(self,list):
        self.mdtList.append(list)
    def insertMt(self,name,type,tm,ext,ref):
        self.name = name
        self.type = type
        self.tm = tm
        self.ext  = ext
        self.ref = ref
        self.check = False
        self.mdt = [name,type,tm,ext,ref]
        if (len(self.mdtList))==0:
            self.addmdt(self.mdt)
            return True
        else:    
            for i in self.mdtList:
                if i[0]==name:
                    self.check = True
                    return False
        if self.check==False:
            self.addmdt(self.mdt)            
    def lookupMT(self,N):
        for i in self.mdtList:
            if i[0]==N:
                return i
            else:
                return False    


class FT:
    def __init__(self) :
        self.func_tbl_list=[]
    def addft(self,list):
        self.func_tbl_list.append(list)
    def insertFT(self,name,type,cs):
        self.name = name
        self.type = type
        self.cs = cs
        self.check = False
        self.innerlist = [name,type,cs]
        if (len(self.func_tbl_list))==0:
            self.addft(self.innerlist)
            return True
        else:
            for i in self.func_tbl_list:
                
                if i[0] == name and  i[1] == type and i[2] == cs :
                    self.check = True 
                    return False
                
        if self.check==False:
            self.addft(self.innerlist)            
                    
    def lookupFT(self,N,cs):
        self.a = False
        if len(self.func_tbl_list) == 0:
            return False
        else:    
            for i in self.func_tbl_list:
                if i[0]==N and i[2]==cs:
                    self.a = True 
            return self.a
    def lookupFT3(self,name):
        self.name=name
        for i in self.func_tbl_list:
            if i[0]==name:
                return i
                break


curr_scope = 0
scope_stack=[]
index = 0
def sst():
    global index
    
    global objN1
    global objN2
    global objch1
    global objch2
    
    if (obj_dec()):
        if objch1 == False:
            print("Undeclared classname", objN1)
        if objch2 == False:
            print("Undeclared classname", objN2)
        return True
    if (inc_dec()):
        return True
    elif (dec()):
        return True
    elif (till()):
         return True
    elif (if_else()):
         return True
    elif (assgn_st()):
        return True
    elif (func_call()):
        return True
    
    else:
        return False
def mst():
    global curr_scope
    global index
    if (sst()):
        if (mst()):
             return True
        else:
            return False
    elif ts[index].cp == "}":
        index += 1

        
        
        return True
    else:
        return False
scope_main =[]
curr_scope_main = 0
def defs():
    global scope_main
    global curr_scope
    global scope_stack
    global index
    x=index
    if (class_init()):
        
        if (defs()):
            return True
        else:
            return False
    elif (func_init()):
        if (defs()):
            return True
        else:
            return False
    elif ts[index].cp == "function":
        index += 1
        if ts[index].cp == "start":
            index += 1
            if ts[index].cp == "(":
                index += 1
                if ts[index].cp == ")":
                    curr_scope+=1
                    
                    index += 1
                    return True
                else:
                    index = x
                    return False
            else:
                index = x
                return False
        else:
            index = x
            return False        
    elif (dec()):
        
        if (defs()):
            return True
        else:
            return False
    else:
        index = x
        return False
ftm = ""        
def AF3():
    global ftm
    global index
    if ts[index].cp == "abstract" or ts[index].cp == "final":
        
        ftm = ts[index].cp
        index += 1
        return True
    elif ts[index].cp == "dt":
        return True
    else:
        return False

def func_init():
    global index
    x = index
    if ts[index].cp == "function":
        index += 1
        if ts[index].cp == "ID":
            index += 1
            if ts[index].cp == "(":
                
                index += 1
                if (param()):
                    if ts[index].cp == "{":
                        index += 1
                        if (mst()):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    index=x
                    return False
            else:
                index=x
                return False
        else:
            index=x
            return False
    else:
        index=x
        return False
def arr():
    global index
    x = index
    if ts[index].cp == "DT":
        index+=1
        if ts[index].cp =="ID":
            index+=1
            if ts[index].cp == "=":
                index+=1
                if ts[index].cp =="[":
                    index+=1
                    if paramArray():
                        index+=1
                        if ts[index].cp ==";":
                            return True
                        else:
                            index = x
                            return False
                    else:
                        index = x
                        return False
                else:
                    index = x
                    return False
            else:
                index = x
                return False
        else:
            index = x
            return False
def S():
    global index
    if (defs()):
        if ts[index].cp == "{":
            
            index += 1
            if (mst()):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def paramArray():
    global index
    x=index
    if ts[index].cp == "ID":
        index += 1
        if (paramsArray()):
            return True
        else:
            index=x
            return False
    elif (const()):
        if (paramsArray()):
            return True
    elif ts[index].cp == "]":
        index += 1
        return True
    else:
        index=x
        return False
def paramsArray():
    global index
    x=index
    if ts[index].cp == ",":
        index += 1
        if ts[index].cp == "ID":
            index += 1
            if (params()):
                return True
            else:
                index=x
                return False
        elif (const()):
             if (params()):
                return True
        else:
            index=x
            return False
    elif ts[index].cp == "]":
        index += 1
        return True
    else:
        return False       
paramN=""
fun_ch = False
def param():
    global curr_scope
    global index
    global paramN
    global fun_ch
    x=index
    if ts[index].cp=="dt":
        tp = ts[index].vp
        paramN = ts[index].vp
        index+=1
        if ts[index].cp == "ID":
            N=ts[index].vp
            if (ft_instance.insertFT(N,tp,curr_scope))==False:
                print("Redeclaration Error of ",N)
            else:
                fun_ch = True
            index += 1
            if (params()):
                return True
            else:
                index=x
                return False
    elif (const()):
        if (params()):
            return True
    elif ts[index].cp == ")":
        index += 1
        return True
    else:
        index=x
        return False
paramsN = ""        


def params():
    global index
    global curr_scope
    global paramsN
    global fun_ch
    x=index
    if ts[index].cp == ",":
        index += 1
        if ts[index].cp=="dt":
            tp = ts[index].vp
            paramsN = ts[index].vp
            index+=1
            if ts[index].cp == "ID":
                N=ts[index].vp
                if fun_ch!=True:
                    if (ft_instance.insertFT(N,tp,curr_scope))==False:
                        print("Redeclaration Error of ",N)
                index += 1
                if (params()):
                    return True
                else:
                    index=x
                    return False
        elif (const()):
             if (params()):
                return True
        else:
            index=x
            return False
    elif ts[index].cp == ")":
        index += 1
        return True
    else:
        return False
def ass_func_call():
    global index
    x = index
    if ts[index].cp == "ID":
        index += 1
        if ts[index].cp == ".":
            index += 1
            if ts[index].cp == "ID":
                index += 1
                if ts[index].cp == "(":
                    index += 1
                    if (param()):
                        return True
                    else:
                         return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        index = x
        return False
def lhp():
    global index
    if ts[index].cp==".":
        index+=1
        if ts[index].cp=="ID":
            index+=1
            return True
        # elif (arr_call()):
        #     if(lhp()):
        #         return True
        #     else:
        #         return False
    else:
        return False

def assgn_st():
    global index
    global dectp
    global dataTable
    global t1
    global typ_list_ind
    x=index
    if ts[index].cp == "ID":
        N = ts[index].vp
        dectp = dataTable.lookupDT3(N)


        index += 1
        if ts[index].cp=="AS":
            index+=1
            if (OE()):
                typ_list_ind = 0
                t1 = ""
                index+=1
                return True
            else:
                return False
        else:
            return False
    else:
        index=x
        return False
    #     if ts[index].cp==".":
    #         index+=1
    #         if (ass_func_call()):
    #             if(lhp()):
    #                 if(assgn_st()):
    #                     if ts[index].cp=="AS":
    #                         index+=1
    #                         if(OE()):
    #                             if ts[index].cp==";":
    #                                 index+=1
    #                                 return True
    #                             else:
    #                                 index=x
    #                                 return False
    #                         else:
    #                             index = x
    #                             return False  
    #                     else:
    #                         index = x
    #                         return False
    #                 else:
    #                     index=x
    #                     return False                
    #             else:
    #                 index = x
    #                 return False
    #         else :
    #             index = x
    #             return False
    #     else:
    #         index = x
    #         return False                
    # elif(ass_func_call()):
    #     if(lhp()):
    #         if(assgn_st()):
    #             if ts[index].cp=="AS":
    #                     index+=1
    #                     if(OE()):
    #                         if ts[index].cp==";":
    #                             index+=1
    #                             return True
    #                         else:
    #                             index=x
    #                             return False    
    #                     else:
    #                         index = x
    #                         return False
    #             else:
    #                 index = x    
    #                 return False        
    #         else:
    #             index = x
    #             return False            
    #     else:
    #         index = x
    #         return False

    # elif ts[index].cp=="AS":
    #     if (OE()):
    #         return True                            
def func_call():
    global index
    x = index
    if ts[index].cp == "ID":
        index += 1
        if ts[index].cp == ".":
            index += 1
            if ts[index].cp == "ID":
                index += 1
                if ts[index].cp == "(":
                    index += 1
                    if (param()):
                        if ts[index].cp == ";":
                            index += 1
                            return True
                        else:
                            index = x
                            return False
                    else:
                         index = x
                         return False
                else:
                    index = x
                    return False
            else:
                index = x
                return False
        else:
            index = x
            return False
    else:
        index = x
        return False
objch1 = ''
objch2 = ''
objN1=''
objjN2 = ''

def obj_dec():
    global index
    global mt_instance
    global objch1
    global objch2
    global objN1
    global objN2
    x = index
    if ts[index].cp == "ID":
        
        objN1 = ts[index].vp
        objch1 = mt_instance.lookupMT(objN1)
        index += 1
        if ts[index].cp == "ID":
            index += 1
            if ts[index].cp == "AS":
                index += 1
                if ts[index].cp == "new":
                    index += 1
                    if ts[index].cp == "ID":
                        objN2 = ts[index].vp
                        objch2 = mt_instance.lookupMT(objN2)
                        index += 1
                        if ts[index].cp == "(":
                            index += 1
                            if (param()):
                                if ts[index].cp == ";":
                                    index += 1
                                    return True
                                else:
                                    index = x
                                    return False
                            else:
                                index = x
                                return False
                        else:
                            index = x
                            return False
                else:
                    index = x
                    return False
            else:
                index = x
                return False
        else:
            index = x
            return False
    else:
        index = x
        return False


def inc_dec_op2():
    global index
    if ts[index].cp == "incdec":
        index += 1
        return True

def inc_dec_op():
    global index
    x = index
    if ts[index].cp == "incdec":
        index += 1
        if ts[index].cp == ";":
            index += 1
            return True
        else:
            return False
    else:
        index = x
        return False
def inc_dec():
    global index
    global scope_stack
    x = index
    global dataTable
    global cname
    global ft_instance
    global curr_scope
    ch2=True
    if ts[index].cp == "ID":
        N = ts[index].vp
        ch1 = dataTable.lookupDT(N,cname)
        if len(scope_stack) == 1:
            
            if ch1 == False:
                print("undeclared variable ",N)
        elif len(scope_stack)>1:

            ch2 = ft_instance.lookupFT(N,curr_scope)
            
        
        if ch1 == False  and ch2 == False:
            print("undeclared variable ",N )
        if len(scope_stack)==0:

            ch2 = ft_instance.lookupFT(N,curr_scope)
            if ch2==False:
                print("Undeclared Variable",N) 
        index += 1
        if (inc_dec_op()):
            return True
        else:
            return False
    elif (inc_dec_op2()):
        if ts[index].cp == "ID":
            N = ts[index].vp
            ch = ft_instance.lookupFT(N,curr_scope)       
            if ch == False:
                print("undeclared variable ",N )
            if ts[index].cp == ";":
                index += 1
                return True
            else:
                return False
        else:
            return False
    else:
        index=x
        return False
    
def Oelse():
    global curr_scope
    global scope_stack
    global index
    if ts[index].cp == "else":
        index += 1
        if ts[index].cp == "{":
            curr_scope+=1
            scope_stack.append(curr_scope)

            index += 1
            if (mst()):
                if ts[index].cp == "}":
                        scope_stack.pop()
                        index += 1
                        return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif ts[index-1].cp=="}" and ts[index].cp!="else":
        return True
    else:
        return False
def if_else():
    global scope_stack
    global curr_scope
    global index
    global typ_list_ind
    global t1
    x=index
    if ts[index].cp == "if":
        index += 1
        if ts[index].cp == "(":
            index += 1
            if (OE()):
                if ts[index].cp == ")":
                    t1=""
                    typ_list_ind = ""
                    index += 1
                    
                    if ts[index].cp == "{":
                        curr_scope+=1
                        scope_stack.append(curr_scope)
                        index += 1
                        if (sst()):
                            if ts[index].cp == "}":
                                scope_stack.pop()
                                index += 1
                                if (Oelse()):
                                        return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
def till_body():
    global index
    if (sst()):
        return True
    else:
        return False
def till():
    global scope_stack
    global index
    global curr_scope
    global typ_list_ind
    global t1
    x=index 
    if ts[index].cp == "till":
        index += 1
        if ts[index].cp == "(":
            index += 1
            if (OE()):
                if ts[index].cp == ")":
                    typ_list_ind = 0
                    t1 = ""
                    index += 1
                    if ts[index].cp == "{":
                            curr_scope+=1
                            scope_stack.append(curr_scope)
                            index += 1
                            if (till_body()):
                                if ts[index].cp == "}":
                                    scope_stack.pop()
                                    index += 1
                                    return True
                                else:
                                    return False
                            else:
                                return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
def const():
    global index
    if ts[index].cp == "int_const" or ts[index].cp == "float_const" or ts[index].cp == "chr_const" or ts[index].cp == "str_const":
        index += 1
        return True
    else:
        return False
def init():
    global index
    global typ_list_ind 
    global t1 
    if ts[index].cp == "AS":
        index += 1
        if (OE()):
            typ_list_ind = 0
            t1 = ""
        # \if ts[index].cp == "ID":
            # index += 1
            if (init()):
                return True
            else:
                return False
        # elif (const()):
        #     if (init()):
        #         return True
    elif (olist()):

        return True
    else:
         return False
def olist():
    global index
    global dectp
    global scope_stack
    if ts[index].cp == ";":
        index += 1
        return True
    elif ts[index].cp == ",":
        index += 1
        if ts[index].cp == "ID":
            N = ts[index].vp
            if len(scope_stack)==1:
                    
                    row = dataTable.lookupDT(N,cname)
                    if row == True :
                        dataTable.insertDT(N,dectp,dectm,cname)
                        
                    else:
                        print("Redeclaration of ",N)
            elif len(scope_stack)>1:
                    row = ft_instance.lookupFT(N,curr_scope) 
                    if row == True:
                        ft_instance.insertFT(N,dectp,curr_scope)
                    else:
                        print("Redeclaration of ", N)
                
            index += 1
            if (init()):
                return True
            else:
                return False

        else:
            return False
    else:
        return False
dectm=""        
def AF2():
    global dectm
    global index
    if ts[index].cp == "abstract" or ts[index].cp == "final":
        dectm = ts[index].cp
        index += 1
        return True
    elif ts[index].cp == "dt":
        return True
    else:
        return False
 #x=a.v().g().C+b*c*d+1;
dectp=""            
def dec():
    global index
    global scope_stack
    global dataTable
    global dectm
    global cname
    global ft_instance
    global curr_scope
    global dectp
    x = index
    if AF2():
        if ts[index].cp == "dt":
            dectp=ts[index].vp
            index += 1
            if ts[index].cp == "ID":
                N=ts[index].vp
                if len(scope_stack)==1:
                    row = dataTable.insertDT(N,dectp,dectm,cname)
                    if row == False:
                        print("Redeclaration error of ",N) 
                elif len(scope_stack)>1 or len(scope_stack)==0:
                    row = ft_instance.insertFT(N,dectp,curr_scope) 
                    if row == False:
                        print("Redeclaration error of ", N)
                index += 1

                if (init()):
                    return True
                else:
                    return False
            else:
                return False
        else:
            index = x
            return False
def compat(t1,t2,op):
    if op == "*" or op=="/":
        if t1 == "int" or t1=="int_const": 
            if t2 == "int" or  t2=="int_const":
                return "int"
            elif t2 == "float" or t2 =="float_const":
                return "float"
            else:
                return False
        elif t1 == "float" or t1 =="float_const":
            if (t2 == "int" or  t2 ==" int_const") or (t2=="float" or t2=="float_const"):
                return "float"
            else:
                return False 
        elif t1 == "string" or t1=="str_const" or t2=="string" or t2=="str_const":
            return False
    elif op == "+":
        if t1 == "int" or t1=="int_const": 
            if t2 == "int" or t2=="int_const":
                return "int"
            elif t2 == "float" or t2=="float_const":
                return "float"
            else:
                return False
        elif t1 == "float" or t1 == "float_const":
            if t2 == "int" or t2=="int_const" or t2=="float" or t2=="float_const":
                return "float"
            else:
                return False
        elif (t1 == "string" or t1=="str_const") and (t2=="string" or t2=="str_const"):
            return "string"
        else:
            return False    
    elif op == "-":
        if t1 == "int" or t1 == "int_const": 
            if t2 == "int" or t2=="int_const":
                return "int"
            elif t2 == "float" or t2=="float_const":
                return "float"
            else:
                return False
        elif t1 == "float" or t1=="float_const":
            if t2 == "int" or t2=="float":
                return "float"
            else:
                return False                
        elif t1=="string" or t1=="str_const" or t2 == "string" or t2=="string":
            return False
    elif op == ">" or op =="<" or op ==">=" or op=="<=" or op =="!=":
        if t1 =="int" or t1=="int_const":
            if t2=="float" or t2=="float_const" or t2=="int" or t2=="int_const":
                return True
            else:
                return False
        elif t1=="float" or t1=="float_const":
            if t2=="int" or t2=="int_const" or t2=="float" or t2=="float_const":
                return True
            else:
                return False
        else:
            return False

# EXPRESSION
# EXPRESSION
def OE_func():
    global index
    x = index
    if ts[index].cp==".":
        index+=1
        if ts[index].cp=="ID":
            index+=1
            if ts[index].cp=="(":
                index+=1
                if (param()):
                    if (OE_func()):
                        return True
                    else:
                        return False
                else:
                    return False            
            else:
                return True                    
    elif ts[index].cp != ".":
        return True 
    else:
        return False                           

def TS():
    global index
    
    if ts[index].cp=="this":
        
        index+=1
        if ts[index].cp==".":
            
            index+=1
            if ts[index].cp=="ID":
                
                return True
        else:
            return False    
   
    else:
        return False            
typ=""
type_list = []
typ_list_ind = -1
def F():
    global type_list
    global ft_instance
    global dataTable
    global index
    global typ
    global typ_list_ind
    global t1
    if(TS()):
        index+=1
        return True
    elif ts[index].cp=="ID":
        N = ts[index].vp
        
        typ = dataTable.lookupDT3(N)
        if typ == None:
            typ = ft_instance.lookupFT3(N)
            if typ == None:
                print("Undefined variable ", N)
            else:
                typ_list_ind += 1
                type_list.append(typ)
        else:
            typ_list_ind += 1
            type_list.append(typ)
        index+=1
        if(OE_func()):
            return True
    elif ts[index].cp == "super " or ts[index].cp == "this" or ts[index].cp == "ID" or ts[index].cp == "float_const" or ts[index].cp == "int_const"  or ts[index].cp == "chr_const" or ts[index].cp == "str_const" or ts[index].cp == "!" or ts[index].cp == "(": 
        
        typ = ts[index].cp
        typ_list_ind += 1
        type_list.append(typ)
        t1 = typ
        index+=1
        return True
    else:
        return False     
t2=""
o1 = ""                    
def T1():
    global index
    global o1
    global type_list
    global typ_list_ind
    global t1
    global t2
    global dectp
    if ts[index].cp=="MDM":
        o1 = ts[index].vp
        index+=1
        # return T()
        if (T()):
            t2 = type_list.pop()
            t3 = compat(t1,t2,o1)
            if t3 != False:
                t1=t3
            if t3 == False:
                print("Type matching error of ",t1 , " and ",t2)
            else:
                if dectp != t3:

                    print(t3, " cannot be assigned to ",dectp, "at line number ",ts[index].lineNumber)
                     
            return True
        else:
            return False    

    elif ts[index].cp=="PM" or ts[index].cp=="RO" or ts[index].cp=="AND" or ts[index].cp=="OR" or  ts[index].cp==")" or ts[index].cp=="," or ts[index].cp==";":
        return True
    else:
        return False
t1 = ""
def T():
    global t1
    global type_list
    global typ_list_ind
    global typ
    # t1 = ""
    # if t1 == "":
    #     t1 = typ    
    if(F()):
        if t1 == "":
            t1 = type_list[typ_list_ind]
        if(T1()):

            return True
        else:
            return False
o2 = ""       
t4 = ""     
def E1():
    global index
    global o2
    global t1
    if ts[index].cp=="PM":
        o2 = ts[index].vp
        index+=1
        # return E()
        if (E()):
            t4 = type_list.pop()
            t3 = compat(t1,t4,o1)
            if t3 != False:
                t1=t3
            if t3 == False:
                print("Type matching error of ",t1 , " and ",t2)
            else:
                if dectp != t3:

                    print(t3, " cannot be assigned to ",dectp," at line number ",ts[index].lineNumber)
            
            return True 
        else:
            return False

            

    elif ts[index].cp=="RO" or ts[index].cp=="OR" or ts[index].cp=="AND" or ts[index].cp==")" or ts[index].cp==";":
        return True
    else:
        return False
t4 = ""                      
def E():
    global index
    global typ
    
    if(T()):
        if(E1()):
            return True
        else:
            return False
    else:
        return False
def RE1():
    global index
    global t1
     
    if ts[index].cp=="RO":
        o4 = ts[index].vp
        index+=1
        # return RE()
        if (RE()):
            t5 = type_list.pop()
            t6 = compat(t1,t5,o4)
            if t6 == False :
                print("Incompatible types ",t1,t5)

            return True
        else:
            return False     
    elif ts[index].cp=="AND" or ts[index].cp=="OR" or ts[index].cp==";" or ts[index].cp==")":
        return True
    else:
        return False                 
def RE():
    global index
    if(E()):
        if(RE1()):
            return True
        else:
            return False
    else:
        return False
def AE1():
    global index
    if ts[index].cp=="AND":
        index+=1
        if (RE()):
            if (AE1()):
                return True
            else:
                return False
        else:
            return False
    elif ts[index].cp=="OR" or ts[index].cp=="," or ts[index].cp==")" or ts[index].cp==";":
        return True
    else:
        return False
def AE():
    global index
    if (RE()):
        if(AE1()):
            return True
        else:
            return False
    else:
        return False
def OE1():
    global index
    if ts[index].cp == "OR":
        index+=1
        if(AE()):
            if(OE1()):     
                return True
            else:
                return False    
    elif ts[index].cp=="," or ts[index].cp==")" or ts[index].cp==";" or ts[index].cp=="]":
        
        return True 
    else:
        return False        
def OE():
    global index
            
    if(AE()):
        if(OE1()):
            return True
        else:
            return False
    else:
        return False
def mst_oop():
    global index
    x=index
    if ts[index].cp == "this":
        index += 1
        if ts[index].cp == ".":
            index += 1
            if ts[index].cp == "ID":
                index += 1
                if ts[index].cp=="AS":
                    index+=1
                    if (OE()):
                        if ts[index].cp==";":
                            index+=1
                            if (mst_oop()):
                                return True
                            else:
                                index=x
                        else:
                            index=x
                            return False        
                    else:
                        return False               
                else:
                    return False
            else:
                return False
        else:
            return False
    elif ts[index].cp == "super":
        index += 1
        if ts[index].cp == "(":
            index += 1
            if ts[index].cp == ")":
                index += 1
                if ts[index].cp==";":
                    index+=1
                    if (mst_oop()):
                        return True
                    else:
                        return False
                else:
                    return False        
            else:
                return False
        else:
            return False
    elif (mst()):
        return True
    else:
        return False

ft_instance = FT()       
cname = "" 

def class_func():
    global index
    global curr_scope
    global dataTable
    global ftm
    global scope_stack
    global cname
    global mt_instance
    global paramN
    global paramsN
    global fun_ch
    x=index
    a = True 
    if (AF3()):
        
        if ts[index].cp == "dt":


            ftp = ts[index].vp
            index+=1
            if ts[index].cp == "function":
                index += 1
                if ts[index].cp == "ID":
                    N=ts[index].vp
                    index += 1
                    if ts[index].cp == "(":
                        index += 1
                        curr_scope+=1
                        scope_stack.append(curr_scope)
                        if (param()):
                            if ftm=="abstract":
                                for i in mt_instance.mdtList:
                                    if i[0] == cname:
                                        if i[2] != "abstract":
                                            print("class must also be abstract")
                                            a = False
                                if(a):
                                           ftp +=  " ->" +  paramN+paramsN
                                           if (dataTable.insertDT2(N,ftp,ftm,cname))==False:
                                                print("Redeclaration Error of function ",N)
                                                if (fun_ch):    
                                                    ft_instance.func_tbl_list.pop()
                                                    
                                if ts[index].cp == "{":
                                    index += 1
                                if (mst_oop()):
                                    scope_stack.pop()
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    index = x
                    return False
            else:
                index = x
                return False
        else:
            index=x
            return False
    else:
        index=x
        return False        
def construct():
    global index
    x=index
    ftp = ""
    ftm = ""
    global curr_scope
    global scope_stack
    global cname
    if ts[index].cp == "ID":
            N = ts[index].vp
            index += 1
            if ts[index].cp == "(":
                curr_scope+=1
                scope_stack.append(curr_scope)
                index += 1
                if (param()):
                    ftp +=  " ->" +  paramN+paramsN
                    if (dataTable.insertDT2(N,ftp,ftm,cname))==False:
                                print("Redeclaration Error of function ",N)
                                if (fun_ch):    
                                             ft_instance.func_tbl_list.pop()
                    
                    if ts[index].cp == "{":
                        
                        index += 1
                        if (mst_oop()):
                            scope_stack.pop()
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                index = x
                return False
    else:
        index=x
        return False
def class_body():
    global index
    if (class_func()):
        if (class_body()):
            return True
    elif (dec()):
        if (class_body()):
            return True
    elif (construct()):
        if (class_body()):
            return True
    elif (assgn_st()):
        if (class_body()):
            return True        
    elif ts[index-1].cp == "}":
        return True        
    else:
        return False
TM = ""
def AF():
    global index
    global TM
    if ts[index].cp == "abstract" or ts[index].cp == "final":
        TM = ts[index].cp
        index += 1
        return True
    elif ts[index].cp == "Class":
        return True
    else:
        return False
NE=""
mt_instance = MDT()    
check = True

def ET():
    global check
    global index
    global NE
    
    if ts[index].cp == "extends":
        
        index += 1
        if ts[index].cp == "ID":
            NE=ts[index].vp
            RMT=mt_instance.lookupMT(NE)
            if (RMT == None):
                print("undeclared ID",NE)
                check=False
            elif(RMT[1]!="Class"):
                print("It should be Class")
                check=False
            elif(RMT[2]=="final"):
                print(NE," Cant be extended")
                check=False                    
            index += 1
            return True
            
    elif ts[index].cp == "{":
        return True
    else:
        return False
dataTable = DT()      
def class_init():
    global index
    global NE    
    global TM
    global check
    global curr_scope
    global dataTable
    global scope_stack
    global cname
    x=index 
    if (AF()):
        if ts[index].cp == "Class":
            TP=ts[index].vp
            index += 1
            if ts[index].cp == "ID":
                N=ts[index].vp
                cname=N
                index += 1
                if (ET()):
                    if(check):
                        ref = id(dataTable.data_table_list)
                        if (mt_instance.insertMt(N,TP,TM,NE,ref))==False:
                            print("Redeclaration Error of class ",N)
                        
                        if ts[index].cp == "{":
                            curr_scope+=1
                            
                            scope_stack.append(curr_scope)
                            print("SCOPE STACK",scope_stack)
                            index += 1
                            if (class_body()):
                                if ts[index].cp == "}":
                                    print(dataTable.data_table_list," data table")
                                    dataTable.data_table_list=[]
                                    scope_stack=[]
                                    index += 1
                                    return True
                                    
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        else:
            return False
    else:
        index=x
        return False
if (S()):
    
    if (ts[index].cp == "$"):
        print("no syntax error")
    else:
        print("syntax error at", ts[index].lineNumber)
else:
    print("syntax error at", ts[index].lineNumber)

print(mt_instance.mdtList, " main table")
print(ft_instance.func_tbl_list, " function table")

