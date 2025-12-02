from conn import con,cur
from tabulate import tabulate
class Bank:  
    def deposit(self,amt,anum):
        cur.execute("select acno from bank")
        self.acnums=cur.fetchall()
        self.amt=amt
        self.anum=anum
        for (i,) in self.acnums:
            if self.anum == i:
                cur.execute("update bank set balance=balance+%s where acno=%s",(self.amt,self.anum))
                con.commit()
                cur.execute("select acname from bank where acno=%s",(self.anum,))
                self.name=cur.fetchone()
                cur.execute("insert into transaction (acno,acname,action,Amount) values(%s,%s,%s,%s)",(self.anum,self.name[0],"Deposit",self.amt))
                con.commit()
                return "Amount deposited Successfully!"
        return "Invalid Account Number!"
    def withdraw(self,wid,anum):
        cur.execute("select acno from bank")
        self.acnums=cur.fetchall()
        self.wid=wid
        self.accno=anum
        for (i,) in self.acnums:
            if self.accno ==i:
                cur.execute("select balance from bank where acno=%s",(anum,))
                self.data=cur.fetchone()
                self.bal_wid=int(self.data[0])
                if(self.bal_wid<wid):
                    return "Insufficient Funds"
                else:
                    cur.execute("update bank set balance=balance-%s where acno=%s",(wid,self.accno))
                    con.commit()
                    cur.execute("select acname from bank where acno=%s",(self.accno,))
                    self.name=cur.fetchone()
                    cur.execute("insert into transaction (acno,acname,action,Amount) values(%s,%s,%s,%s)",(self.accno,self.name[0],"Withdraw",self.wid))
                    con.commit()
                    return "Amount withdrawn Successfully!"
        return "Invalid Account Number"
    def showbal(self,acnum):
        cur.execute("select acno from bank")
        self.acnums=cur.fetchall()
        self.acnum=acnum
        for (i,) in self.acnums:
            if self.acnum == i:
                self.findnum=self.acnum
                cur.execute("Select * from bank where acno=%s",(self.findnum,))
                row=cur.fetchone()
                return (tabulate([row],headers=["account_number","account_holderName","Balance","Account_Type"],tablefmt="grid"))
        
        return "Invalid Account Number!"
    def mini_statement(self,acnum:int):
        self.miniac=acnum
        cur.execute("select acno from bank")
        self.acnums=cur.fetchall()
        for (i,) in self.acnums:
            if self.miniac == i:
                self.findnum=self.miniac
                cur.execute("Select * from transaction where acno=%s",(self.findnum,))
                row=cur.fetchall()
                return (tabulate(row,headers=["account_number","account_holderName","action","transaction_timee","Amount"],tablefmt="grid"))
class admin():
    def insert(self,accnum:int,accname:str,bal:int,acctype:str,add:str,mob:int):
        self.acnum=accnum
        self.acname=accname
        self.actype=acctype
        self.balance=bal
        self.address=add
        self.mob=mob
        cur.execute("insert into bank values (%s,%s,%s,%s,%s,%s)",(self.acnum,self.acname,self.balance,self.actype,self.address,self.mob))
        con.commit()
        return "Account Created Successfully!"
    def delete_user(self,acnum):
        cur.execute("select acno from bank")
        self.acnums=cur.fetchall()
        self.acnum=acnum
        for (i,) in self.acnums:
            if self.acnum == i:
                cur.execute("delete from bank where acno=%s",(self.acnum))
                con.commit()
                return "Account Deleted Successfully!"
        return "Invalid Account Number!"
    def updname(self,acnum:int,acname:str):
        self.upname=acname
        cur.execute("select acno from bank")
        self.upacnum=acnum
        self.acnums=cur.fetchall()
        for (i,) in self.acnums:
            if self.upacnum == i:
                cur.execute("update bank set acname=%s where acno=%s",(self.upname,self.upacnum))
                con.commit()
                return "Change Successful!"
            else:
                return "Invalid Account Number!"
    def updadd(self,acnum:int,acad:str):
        cur.execute("select acno from bank")
        self.upacnum=acnum
        self.acnums=cur.fetchall()
        for (i,) in self.acnums:
            if self.upacnum == i:
                self.new_add=acad
                cur.execute("update bank set acadd=%s where acno=%s",(self.new_add,self.upacnum))
                con.commit()
                return "Change Successful!!!"
        return "Invalid Account Number!"
    def updmob(self,acnum:int,acmob:int):
        cur.execute("select acno from bank")
        self.upacnum=acnum
        self.acnums=cur.fetchall()
        for (i,) in self.acnums:
            if self.upacnum == i:
                self.mob=acmob
                cur.execute("update bank set acmobnum=%s where acno=%s",(self.mob,self.upacnum))
                con.commit()
                return "Change Successful!"
        return "Invalid Account number!" 
    def updtype(self,acnum:int,actype:str):
        cur.execute("select acno from bank")
        self.upacnum=acnum
        self.acnums=cur.fetchall()
        for (i,) in self.acnums:
            if self.upacnum == i:
                self.new_type=actype
                cur.execute("update bank set acctype=%s where acno=%s",(self.new_type,self.upacnum))
                con.commit()
                return "Change Successful!"
        return "Invalid Account Number!"
      
    def view_table(self):
        cur.execute("Select * from bank")
        self.disp=cur.fetchall()
        return tabulate(self.disp,headers=["account_number","Account_Holder_Name","Balance","Acc_type","Cust_address","Cust_Number"],tablefmt="grid")