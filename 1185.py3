class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
#         01/01/1971->Friday
#  if year divisible by 4->366, otherwise ->365
        v={3:"Sunday", 4:"Monday", 5:"Tuesday", 6:"Wednesday", 0:"Thursday", 1:"Friday", 2:"Saturday"}
        dayP={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        dayR={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        myDay={}
        sum=0
        if year%4==0:
            myDay=dayR
        else: 
            myDay=dayP
        
        for mm in range(1971,year):
            if mm%4==0:
                sum+=366
            else:sum+=365
        for i in myDay:
            if i<month:
                sum+=myDay[i]
            elif i==month:
                sum+=day
        for j in v:
            if sum%7==j:
                return v[j]
        
