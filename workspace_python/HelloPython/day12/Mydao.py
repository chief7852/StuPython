from day12 import MysqlConfig

class MyEmpDao :
    def __init__(self):
        pass
        
    def getEmps(self):
        arr=[]
        conn = MysqlConfig.conn

        sql = 'SELECT sabun,e_name,dept,mobile FROM emp';
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for e in rows:
            temp = {'sabun':e[0],'e_name':e[1],'dept':e[2],'mobile':e[3]}
            arr.append(temp)
        
       
        
        return arr
    
    def selEmps(self,sabun):
        arr=[]
        conn = MysqlConfig.conn
        sql = f"SELECT sabun,e_name,dept,mobile FROM emp where sabun ={sabun}";
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for e in rows:
            temp = {'sabun':e[0],'e_name':e[1],'dept':e[2],'mobile':e[3]}
            arr.append(temp)
        return arr
    
    def insEmps(self,sabun,e_name,dept,mobile):
        conn = MysqlConfig.conn
        cur = conn.cursor()
        sql = f"insert into emp (sabun ,e_name ,dept, mobile) values ({sabun},{e_name},{dept},{mobile})"
        cnt = cur.execute(sql)
        conn.commit()
        
        conn.close()
        return cnt
    
    def update(self,sabun,name,dept,mobile):
        conn = MysqlConfig.conn
        sql = f"update emp set name = '{name}',dept = '{dept}',mobile = '{mobile}' where sabun ='{sabun}'";
        cur = conn.cursor()
        cnt =cur.execute(sql)
        conn.commit()
        
        conn.close()
        return cnt
    
    def delEmp(self,sabun):
        conn = MysqlConfig.conn
        cur = conn.cursor()
        sql = f"delete from emp where sabun = {sabun}"
        cnt =cur.execute(sql)
        conn.commit()
        
        conn.close()
        return cnt
    
if __name__ == '__main__':
    sabun = '1'
    list = MyEmpDao().selEmps(sabun)
    print(list)
    # cnt = MyEmpDao().insEmps('3', '3', '3', '3')
    # print(cnt)