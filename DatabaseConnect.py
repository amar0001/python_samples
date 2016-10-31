
import sqlite3
'''conn = sqlite3.connect('/Users/apple/PycharmProjects/untitled/CPP.sqlite')
c = conn.cursor()

my_list =[(1, 'IBM', 1000, 45.00),
             (2, 'MSFT', 1000, 72.00),
             (3, 'IBM', 500, 53.00)
            ]
for item in my_list:
  print 'item',item
  c.execute('insert into table_python values (?,?,?,?)', item)
  print 'inser success'''


#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('CPP.sqlite')

print "Opened database successfully";

conn.execute("INSERT INTO table_python (_id,program_name,cpp_program,output) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ')");

conn.commit()

 
conn.close()
