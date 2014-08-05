from dosql import *

def index(req,month,day,color):
    a = doSql()
    _query = "SELECT equivalent_month FROM months WHERE month ='" + month + "'"
    month_equi = a.execqry(_query,False)
    _query = "SELECT equivalent_day FROM days WHERE days=" + str(day)
    days_equi = a.execqry(_query,False)
    _query = "SELECT equivalent_color FROM color WHERE color_name='"+ color + "'"
    color_equi = a.execqry(_query,False)
    return month_equi[0][0]+" " + days_equi[0][0] + " "+ color_equi[0][0]
