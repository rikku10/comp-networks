#192.168.1.5
import socket
import csv
import pandas as pd


header =64
port = 6809
ser  = '192.168.1.5'
ADDR = (ser, port)
form = 'utf-8'

cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cl.connect(ADDR)

df = pd.read_csv(r"C:\Users\abhij\OneDrive\Documents\HR.csv")
last_emp = df['Empid'].max()
tmp = []

cx='y'
#while(cx=='y'):
print("Menu  \n 1. View Table \n 2. New Employ")
ch=int(input("\n Enter choise(1/2):"))

if ch==1:
        print(df)
elif ch==2:
        e_id = last_emp+1
        tmp.append(e_id)
        e_name = input("Enter the Employee's Name ")
        tmp.append(e_name)
        e_addr = input("Enter the Address ")
        tmp.append(e_addr)
        e_plc = input("enter the Place ")
        tmp.append(e_plc)
        e_mob = int(input("Enter Mobile number "))
        tmp.append(e_mob)
        e_dpt = input("Enter the Dept")
        tmp.append(e_dpt)

        with open(rb"C:\Users\abhij\OneDrive\Documents\HR.csv", 'a', newline='') as f_ob:
            writer = csv.writer(f_ob)
            writer.writerow(tmp)
else :
        print("Wrong Choice")

    #cx = input('Do you wish to continue(y/n) : ')


cl.close()




