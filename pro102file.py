import os 
import shutil
from_dir='C:/Users/sweety/Downloads'
to_dir='f:/whj/pro 102'
ls=os.listdir(from_dir)

#//print(ls);
for i in ls:
    name,extension=os.path.splitext(i)
    #print(name)
    #print(extension)
    if extension=='': continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif','.pdf','.py']:
        path1=from_dir +'/'+ i
        path2=to_dir + '/' + 'pdf files'
        path3= to_dir + '/' + 'pdf files'+'/'+i    
        #print(path1)
        #print(path3)
        if os.path.exists(path2):
            print('moving'+i+'......')
            shutil.move(path1,path3)
            print("hello")
        else:
            print("hello")
            os.makedirs(path3)  
            print('moving'+i+'......')
            shutil.move(path1,path3)  
