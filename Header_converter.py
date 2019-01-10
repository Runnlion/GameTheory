import os 
import string
path = "C:/Users/Administrator/Desktop/DSP 1-11"
def text_create(name, msg):   
    Target_path = path+'/Converter_Data'    
    full_path = name + '.txt' 
    file = open(full_path,'w')             
    file.write(msg) 
    file.close() 
    print('Done')
def file_name(file_dir): 
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.h':
                L.append(os.path.join(root, file))
    return L
List = file_name(path)

for i in range(len(List)):
    print(i,List[i])
    f = open(List[i],'r')
    print(f)
    Text = f.read()
    NUM = Text[Text.rfind('NUM[MWSPT_NSEC]',1)+20:Text.rfind('DL[MWSPT_NSEC]',1)-10]
    DEN = Text[Text.rfind('DEN[MWSPT_NSEC]',1)+20:len(Text)]
    NUM = NUM.replace("{","[",1).replace("{","",1).replace("},","",).replace("{","").replace("}","",1).replace("};","];")
    DEN = DEN.replace("{","[",1).replace("{","",1).replace("},","",).replace("{","").replace("}","",1).replace("};","];")
    # print("NUM = ",NUM)
    # print("DEN = ",DEN)
    DATA = "NUM = " + NUM + "DEN = " + DEN
    Name = List[i]
    print(Name)
    text_create(List[i].replace(".h",""),DATA)
