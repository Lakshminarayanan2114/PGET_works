from CRUD import Bank,admin
from conn import con
while(True):
    print("Banking System")
    print("1.Admin")
    print("2.Customer")
    print("3.Exit")
    choice=int(input("Enter Your Choice:"))
    if(choice==1):
        passwd=input("Enter your password:")
        if(passwd=="admin"):
            print("Welcome Admin!")
            while(True):
                print("1.Add_Customer")
                print("2.Update Customer")
                print("3.Delete Customer")
                print("4.View Customer Records")
                print("5.Exit")
                admchoice=int(input("Enter your option:" ))
                if(admchoice==1):
                    print("Enter the following Details:")
                    acno=int(input("Enter account Number:"))
                    name=input("Enter Customer Name:")
                    bal=input("Enter Account Balance:")
                    actype=input("Enter Account Type: ")
                    add=input("Enter Customer Address: ")
                    mob=int(input("Enter Customer Mobile Number: "))
                    user=admin()
                    print(user.insert(acno,name,bal,actype,add,mob))
                elif(admchoice==2):
                    acno=int(input("Enter Account Number:"))
                    while(True):
                        print("1.Update Name")
                        print("2.Update Address")
                        print("3.Update Number")
                        print("4.Update Type of Account")
                        print("5.exit")
                        upd=admin()
                        op=int(input("Enter your Choice:"))
                        if(op==1):   
                            new_name=input("enter name:")
                            print(upd.updname(acno,new_name))        
                        elif(op==2):
                            new_add=input("Enter Address:")
                            print(upd.updadd(acno,new_add))                  
                        elif(op==3):
                            new_mob=int(input("enter Mobile Number:"))
                            print(upd.updmob(acno,new_mob))
                        elif(op==4):
                            new_type=input("enter type(Savings/Current):")
                            print(upd.updtype(acno,new_type))
                        elif(op==5):
                            print("Thank You!")
                            break
                        else:
                            print("Choose Valid Option!")
                        
                elif(admchoice==3):
                    delacno=int(input("enter Account Number: "))
                    deluser=admin()
                    print(deluser.delete_user(delacno))
                elif(admchoice==4):
                    view=admin()
                    print(view.view_table())
                elif(admchoice==5):
                    print("Thank you")
                    break
                else:
                    print("Enter Valid Choice")
        else:
            print("Invalid Login!")
    elif(choice==2):
        while(True):
            print("Welcome Customer!")
            print("1.Deposit Money")
            print("2.Withdraw Money")
            print("3.Mini Statement")
            print("4.Exit")
            cust=int(input("Enter your Option:"))
            if (cust==1):
                depo_acc=int(input("Enter the account number to deposit: "))
                depo_amt=int(input("Enter Amount to deposit:"))
                depo=Bank()
                print(depo.deposit(depo_amt,depo_acc))
            elif(cust==2):
                wid_acc=int(input("Enter the Account Number to Withdraw:"))
                wid_amt=int(input("Enter amount to Withdraw: "))
                wid=Bank()
                print(wid.withdraw(wid_amt,wid_acc))
            elif(cust==3):
                minac=int(input("Enter Account Number:"))
                minstat=Bank()
                print(minstat.mini_statement(minac))
            elif(cust==4):
                print("Thank you!")
                break
            else:
                print("Enter Correct Option")
    elif(choice==3):
        print("Thank You!")
        con.close()
        break
    else:
        print("Enter Valid option!!")
        


                
