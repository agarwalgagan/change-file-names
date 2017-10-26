import os

def rename_files():
    file_list = os.listdir(r"E:\python") #lists all directory prsesnt in the directory
    print(file_list)
    saved_path = os.getcwd() #return current working directory
    os.chdir(r"E:\python") #changes the current directory
    
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789")) 

    os.chdir(saved_path)
    
rename_files()
