#convert a text file to excel file 
#to enable us access the file we import the os and sys modules
import os
import sys

#write a text file 
book_name = ['merlin \n', 'buga \n', 'obidient \n', 'lion \n', 'python \n']
book_name2 = ['movie \n', 'music\n', 'labour party \n', 'animal \n', 'software \n']
book_name3 = ['things fall apart \n', 'micrco soft\n', 'google \n', 'amazon \n', 'the place \n']

#write an excel file 
with open(os.path.join(sys.path[0],'book_name.xls'), 'w') as book:
    book_name_write = book.writelines(book_name)
    book_name_write2 = book.writelines(book_name2)
    book_name_write3 = book.writelines(book_name3)
    print('your excel file have written successfully')
    #check your folder a file has been created 
