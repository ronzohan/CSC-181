#REDO the Villain's Name Activity this time, using postgresql table(s).
#Recall the samples:
# To create a table:
#  CREATE TABLE teb (
#      teb_id int primary key,
#      col1 text
#   );
#To Insert:
#  INSERT INTO teb (teb_id, col1) values (1, 'dfd');
#To retrieve:
#  select * from teb;
#
# Don't forget to include test cases.

import sys
import psycopg2



class doSql(object):
    #attributes
    _cxn = ""
    _cur = ""
    errmsg ="" 
    #methods
    def __init__(self): #constructor
        self._cxn = psycopg2.connect("dbname='postgres' user='postgres' password='qwerty123' host='127.0.0.1' port='5432'")
        self._cur = self._cxn.cursor()
        
    def __del__(self): #destructor
        self._cur.close()
        self._cxn.close()

    def execqry(self, sql, apply_):
        rows = []
        try:
            self._cur.execute(sql)
            rows = self._cur.fetchall()
	    if apply_:
                self._cxn.commit()
            if self._cur.rowcount == 0:
                rows.append(['None'])
        except:
            #errmsg = sys.exc_type + ":" + sys.exc_value 
            errmsg =  str(sys.exc_info()[1])
            rows.append([errmsg])
        return rows    

    
#a = doSql()
#f = a.execqry("select insupattendance('1321', 'CENG1-LEC', getcurrsem(), now()::timestamp without time zone, true)")[0][0] 
#print f
#del a
