'''PROJECT-2 : Identify a Problem Statement Within your Chosen Domain and devise a solution for it.
               Then, articulate the problem and your proposed solution.
        NAME : Akanksha Negi
      DOMAIN : Python programming '''

#************************************* PROJECT -2 : PROBLEM & SOLUTION ***********************************************

#PROBLEM :-

'''Management is the process which is universally applicable to all organisation . And so maintaining
              records is part of it. Python programming language not only used for developing websites and software,
              task automation, data analysis, and data visualisation.Since it's relatively easy to learn, Python has
              been adopted by many non-programmers,such as accountants, bankers and scientists, for a variety of
              everyday tasks, like organising finances.
              But the question is how are we able to organise & maintain
              records in finances and other organisation using python ? How we are able to visualise it ?'''

# SOLUTION :-

import pandas as pd
import matplotlib.pyplot as plt

def content():


    print()
    print("#################################")
    print("       BANK MANAGEMENT SYSTEM     ")
    print("##################################")
    print()
    print("          0.ABOUT THE PROJECT  ")
    print("      1.Reading file Bank")
    print("      2.Add details of new acount Holder ")
    print("      3.Delete account if it is closed")
    print("      4.Balance Enquiry")
    print("      5.Read few records")
    print("      6.Read 2 records from top and 2 from bottom")
    print("      7.Arrange details in Ascending order by name of accounts")
    print("      8.Maximum balance from all accounts in bank")
    print("      9.Reading file account")
    print("     10.Deposit in account")
    print("     11.Withdrawal from account")
    print("     12.Line plot")
    print("     13.Line1 plot")
    print("     14.Bar plot")
    print("     15.Bar1 plot")
    print("     16.pie plot")
    print("     17.Barh plot")
    print("     18.Barh1 plot")
    print()

    print("#################################################")

content()



def about():
    print(" In BANK MANAGEMENT SYSTEM project there are 2 CSV files named as Bank and account\
 There are 18 options including 7 plots")


    

def bankcsv():
    print('Reading file bank')
    print()
    print()
    df=pd.read_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\BANK FILE.csv")
    print(df)



    

def new_acholder():
    print('Adding new account holder in file account')
    print()
    df=pd.read_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\ACCOUNT FILE.csv",index_col=0)
    print(df)
    print()
    print()
    df1=pd.Series(data={'accno':'4044','name':'Anaya','Debit':'930','credit':'9000','Bal':'6000'},name='x')
    df=df.append(df1, ignore_index=True)
    print(df)


    

def removeacc():
    print('Deleting account holder from file account')
    df=pd.read_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\ACCOUNT FILE.csv",index_col=0)
    print(df)
    accno=int(input("enter account No. :"))
    df.drop(accno,axis=0,inplace=True)
    print(df)
    #df.to_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\ACCOUNT FILE.csv")  #safe the data permanently
    #print(df)


    


def balenquiry():
    print("Display only Accountno.,Name and Balance")
    df=pd.read_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\BANK FILE.csv",usecols=['accno','name','balance'])
    print(df)


    


def read_rows():
    print("Show only few records")
    df=pd.read_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\BANK FILE.csv",nrows=2)
    print('Show 2 records')
    print(df)


    

def top_bottom():
    print('Show only few records from top and bottom')
    df=pd.read_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\BANK FILE.csv")
    print('top 2 records')
    print(df.head(2))
    print()
    print()
    print('Last 2 records')
    print(df.tail(2))


    


def sort_names():
    print('Sorting Account holders names in ascending order')
    df=pd.read_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\BANK FILE.csv",index_col=0)
    df=df.sort_values('name')
    print(df)


    


def maxbal():
    df=pd.read_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\BANK FILE.csv")
    print(df)
    print("Highest Balance")
    print(df.balance.max())


    


def accountread():
    print('Reading File account')
    print()
    print()
    df=pd.read_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\ACCOUNT FILE.csv",index_col=0)
    print(df)

    


def deposit():
    df=pd.read_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\ACCOUNT FILE.csv")
    print('Previous statement')
    print(df)
    df.loc[df['accno']==4040,['Credit']]=df['Credit']+4000
    df['Bal']=df[['Debit','Credit']].diff(axis=1).iloc[:,1].cumsum().astype(int)
    print(df)

    


def withdrawal():
    df=pd.read_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\ACCOUNT FILE.csv")
    print('Previous statement')
    print()
    print(df)
    print()
    df.loc[df['accno']==4041,['Debit']]=df['Debit']-3000
    #print(df)
    print()
    df['Bal']=df['Bal']-3000
    print(df)

    


def line1_plot():
    print('Line plot')
    df=pd.read_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\BANK FILE.csv")
    print(df)
    x=df['name']
    y=df['balance']
    plt.title('Balance of account Holders')
    plt.plot(x,y,marker='x',linestyle='dashed',linewidth=4,color='r')
    plt.show()

    


def line2_plot():
    df=pd.read_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\BANK FILE.csv")
    print(df)
    plt.plot(df['accno'],df['balance'],marker='o',label='Fare')
    plt.title('Flights wise fare')
    plt.xlabel('accno')
    plt.ylabel('balance')
    plt.xticks(rotation=30)
    plt.legend()
    plt.grid(True)
    plt.show()

    


def bar_plot():
    print('Bar plot')
    df=pd.read_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\ACCOUNT FILE.csv")
    print(df)
    x=df['name']
    y=df['Bal']
    plt.title('Balance of account holders')
    plt.xlabel('name')
    plt.ylabel('Bal')
    plt.bar(x,y,color='red')
    plt.show()

    


def bar1_plot():
    print('Bar1 plot')
    df=pd.read_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\ACCOUNT FILE.csv")
    print(df)
    x=df['name']
    y=df['Bal']
    plt.title('Balance of account holders')
    plt.xlabel('name')
    plt.ylabel('Bal')
    plt.bar(x,y,color=['red','green'])
    plt.legend()
    plt.show()

    


def pie_plot():
    print('Pie plot')
    df=pd.read_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\ACCOUNT FILE.csv")
    print(df)
    plt.title('Credit,Debit,Balance of account holders')
    z=eval(input('Enter Debit , Credit , Balance details in sq brackets'))      
    plt.pie(z,colors=['red','orange','purple'],labels=['Credit','Debit','Bal'],explode=[0,0,0.2])
    plt.show()
    



def barh_plot():
    print('Horizontal bar plot')
    df=pd.read_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\ACCOUNT FILE.csv")
    print(df)
    x=df['name']
    y=df['Bal']
    plt.title('Curved in various States and UT')
    plt.xlabel('name')
    plt.ylabel('Bal')
    plt.bar(x,y,color='blue',edgecolor='pink')
    plt.show()

    


def barh1_plot():
    print('Horizontal bar plot-2')
    df=pd.read_csv("C:\\Users\\sanjana\\OneDrive\\Documents\\ACCOUNT FILE.csv")
    print(df)
    x=df['name']
    y=df['Bal']
    plt.title('Debit & Credit')
    plt.xlabel('name')
    plt.ylabel('Bal')
    plt.bar(x,y,color='orange',edgecolor='green')
    plt.show()

   

    
    
opt=""
opt=int(input("ENTER YOUR CHOICE : "))
if opt==0:
    about()
elif opt==1:
    bankcsv()
elif opt==2:
    new_acholder()
elif opt==3:
    removeacc()
elif opt==4:
    balenquiry()
elif opt==5:
    read_rows()
elif opt==6:
    top_bottom()
elif opt==7:
    sort_names()
elif opt==8:
    maxbal()
elif opt==9:
    accountread()
elif opt==10:
    deposit()
elif opt==11:
    withdrawal()
elif opt==12:
    line1_plot()
elif opt==13:
    line2_plot()
elif opt==14:
    bar_plot()
elif opt==15:
    bar1_plot()
elif opt==16:
    pie_plot()
elif opt==17:
    barh_plot()
elif opt==18:
    barh1_plot()
else:
    print('invalid option')
    print("\a")
    
# CONCLUSION :-
'''Problem Statement Within the python programming Domain and had devise a solution for it as per the above mentioned
   problem and had created a "BANK MANAGEMENT SYSTEM " to solve the above problem.'''

   
    
