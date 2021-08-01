import os

def rename_file():
    i = 0
    path = r'D:\Video_block\Python_program\Python Automation\Files'
    for filenames in os.listdir(path):
        name_to_replace = 'Dog_img'+str(i)+'.jpg'
        file_name = path+'\\'+filenames
        name_to_replace = path+'\\'+name_to_replace
        # print(file_name)
        # print(name_to_replace)
        os.rename(file_name,name_to_replace)
        i +=1

rename_file()