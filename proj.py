import random
import datetime
from datetime import date
class Weather_monitoring():
    def __init__(self):
        self.date={}
        self.report={}
        self.total={'success':0,'failure':0}
        self.user={'total users':0,'total search':0}
    def create(self,dte,key,val,mor,noon,evening):
        if dte in self.date:
            print("this date data already exist")
            details = self.date[dte]
            if details['location']!=key:
                print("already exist")
            else:
                self.date[dte]={'location': key,'status':val,'morning':mor,'afternoon':noon,'evening':evening}
                print(self.date)
        else:
            self.date[dte]={'location': key,'status':val,'morning':mor,'afternoon':noon,'evening':evening}
            print(self.date)
    def search(self, dat, loc,temp,nm):
        if dat in self.date:
            details = self.date[dat]
            if details['location']==loc:
                rmd=random.randint(0,1)
                print(rmd)
                if nm in self.report:
                    detail=self.report[nm]
                    if rmd == 0:
                        global count
                        count = detail['failure']+ 1
                        detail['failure'] = count
                        tem=self.total['failure']
                        self.total['failure']=tem+1
                        #self.total['failure']=count
                        return
                    elif rmd==1:
                        if "morning"==temp:
                            print(details['morning'])
                        elif "afternoon"==temp:
                            print(details['morning'])
                        elif "evening"==temp:
                            print(details['evening'])
                        else:
                            print("invalid time")
                        time=datetime.datetime.now()
                        cont = detail['success'] + 1
                        count=detail['failure']
                        detail['success'] = cont
                        tmp=self.total['success']
                        self.total['success']=tmp+1
                    self.report[nm]={'success':cont,'failure':count,'time':time}
                   # total={'success':cont,'failure':count}
                else:
                    print("user name does not exist")
            else:
                print("Location not found for the given date.")
        else:
            print("Data not available for the given date.")
    def display(self):
        print(self.date)
    def delete(self, dat, loc):
        if dat in self.date:
            details = self.date[dat]
            if details['location'] == loc:
                del self.date[dat]
                print("The data has been deleted successfully.")
            else:
                print("Location not available to delete.")
        else:
            print("No data available for that date.")
    def update(self, dat, loc,update):
        if dat in self.date:
            details = self.date[dat]
            if details['location'] == loc:
                if "morning" == update:
                    details['morning'] = input("Enter the updated weather status for morning: ")
                    print("Morning data updated successfully.")
                elif "afternoon" == update:
                    details['aftenoon'] = input("Enter the updated weather status for afternoon: ")
                    print("Afternoon data updated successfully.")
                elif "evening" == update:
                    details['evening'] = input("Enter the updated weather status for evening: ")
                    print("Evening data updated successfully.")
                else:
                    print("Invalid time.")
            else:
                print("Location not found for the given date.")
        else:
            print("Data not available for the given date.")
    def reports(self):
        print(self.report)
    def create_user(self,nm):
        if nm not in self.report:
            self.report[nm] = {'success': 0, 'failure': 0, 'time': None}
            tmp=self.user['total users']
            self.user['total users']=tmp+1
            print("created sccessfully")
        else:
            print("user already exist")
    def totals(self):
        tmp=self.total['success']
        tem=self.total['failure']
        self.user['total search']=tmp+tem
        print(self.user)
        print(self.total)
m1=Weather_monitoring()
while True:
    print("""
1.create
2.search weather status of the location
3.display all the data
4.delete
5.update
6.report of search history
7.create user
8.total failures and total success
9.exit""")
    ch=int(input("enter your choice "))
    if ch==1:
        dte=input("enter the date in dd:mm:yy ")
        key=input("enter the location ")
        key=key.lower()
        val=input("enter the weather status ")
        mor=input("enter the morning status ")
        noon=input("enter the afternoon status ")
        evening=input(" enter the evening status ")
        m1.create(dte,key,val,mor,noon,evening)
    elif ch==2:
        dat=input("enter the date to search ")
        loc=input("enter the location ")
        loc=loc.lower()
        print("""
1.morning
2.aternoon
3.evening""")
        c=int(input("enter the choice "))
        if c==1:
            temp="morning"
        elif c==2:
            temp="afternoon"
        elif c==3:
            temp="evening"
        else:
            print("wrong choice")
        nm=input("enter the user name ")
        nm=nm.lower()
        m1.search(dat,loc,temp,nm)
    elif ch==3:
        m1.display()
    elif ch==4:
        dte=input("enter the date in dd:mm:yy ")
        key=input("enter the location ")
        key=key.lower()
        m1.delete(dte,key)
    elif ch==5:
        dat=input("enter the date to search ")
        loc=input("enter the location ")
        loc=loc.lower()
        print("""do you want the weather of
1.morning
2.aternoon
3.evening""")
        c=int(input("enter the choice "))
        if c==1:
            update="morning"
        elif c==2:
            update="afternoon"
        elif c==3:
            update="evening"
        else:
            print("wrong choice")
        m1.update(dat,loc,update)
    elif ch==6:
        m1.reports()
    elif ch==7:
        nm=input("enter the user name: ")
        nm=nm.lower()
        m1.create_user(nm)
    elif ch==8:
        m1.totals()
    elif ch==9:
        break
    else:
        print("invalid choice ")
