time=int(input())
hrs=0
if(time>=60):
  minutes=int(time/60)
  time-=minutes*60
if(minutes>=60):
   hrs=int(minutes/60)
                        #  time-=(hrs*60*60)
   minutes-=hrs*60
print(f"{hrs}:{minutes}:{time}")
