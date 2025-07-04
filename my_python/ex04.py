time=int(input("시간을 입력하시오:"))
minute=int(input("시간을 입력하시오:"))
second=(time*3600)+(minute*60) #1시간=3600초(60*60), 1분=60초
print(time, "시간", minute,"분은",second,"초 입니다.")