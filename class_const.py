attr_list=[]
input_attr=['']
input_fun=['']

def classname (classname):
    file.write ("class "+classname.upper()[0]+classname.lower()[1:]+':\n')

def attr (attri):
    for attr in attri:
        global attr_list
        if attr[0] == "-":
            attrib = ('self.__'+attr.lower()[1:]+'='+attr.lower()[1:])
            attr_list.append(attrib)
            file.write('\t\t'+attrib+'\n')
        elif attr[0] == "+":
            attrib = ('self.'+attr.lower()[1:]+'='+attr.lower()[1:])
            
            file.write('\t\t'+attrib+'\n')
        
        
def funtions (func,attri):
    global attr_list
    for fun in func:
        ind1,ind2=fun.index('('),fun.index(')')
        if ind2-ind1 == 1:
            file.write ("\tdef "+fun[:ind1+1].lower()+'self'+fun[ind2:]+':\n')
            
            if fun[0]=='_':
                attr(attri)
            else:
                file.write ("\t\tpass\n\n")
        else:
            file.write ("\tdef "+fun[:ind1+1].lower()+'self,'+fun[ind1+1:]+':\n')
            if fun[0]=='_':
                attr(attri)
            else:
                file.write ("\t\tpass\n\n")
            
    getter(attr_list)
        
def getter(attrib_list):
    for attrib in attrib_list:
        attr = attrib.split('=')
        self_ = attr[0]
        attr_ = attr[1]
        file.write ('\tdef get_'+attr_+'(self):\n')
        file.write ('\t\treturn '+self_+'\n')
        file.write ('\n')
    file.write ('\n')
    setter (attrib_list)
        
def setter (attrib_list):
    for attrib in attrib_list:
        attr = attrib.split('=')
        self_ = attr[0]
        attr_ = attr[1]
        file.write ('\tdef set_'+attr_+'(self,'+attr_+'):\n')
        file.write ('\t\t'+self_+'='+attr_+'\n')
        file.write ('\n')
        
        
def main():
    
    global input_attr
    global input_fun
    global cls
    
    print("Enter Attributes:\n")
    while input_attr[-1]!='#':
        input_attr.append(input())
    input_attr.pop(0)
    input_attr.pop(-1)
    
    print("Enter Functions:\n")
    while input_fun[-1]!='#':
        input_fun.append(input())
    input_fun.pop(0)
    input_fun.pop(-1)
    #file.writeing structure
    
    classname(cls)
    funtions(input_fun,input_attr)
     

cls=input("Enter Name of Class:\n")
filename=cls+'.txt'
file=open(filename,'a')
main()
