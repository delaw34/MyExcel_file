#convert a text file to excel file 
import os
import sys

#write a excel file 
#write a file 
book_name = ['merlin \n', 'buga \n', 'obidient \n', 'lion \n', 'python \n']
book_name2 = ['movie \n', 'music\n', 'labour party \n', 'animal \n', 'software \n']

with open(os.path.join(sys.path[0],'book_name.xls'), 'w') as book:
    book_name_write = book.writelines(book_name)
    book_name_write2 = book.writelines(book_name2)
    print('your excel file have written successfully')
    #check your folder a file has been created 