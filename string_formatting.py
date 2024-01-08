# 오늘은 2024년 1월 8일입니다.

year = 2024
month = 1
day = 8

#print("오늘은" + year + "년" + month + "월" + day + "일 입니다" ) #이게 안되는 이유는 문자열 + 정수형이랑 같이 있기때문임.


print("오늘은" + str(year) + "년" + str(month) + "월" + str(day) + "일 입니다" ) #string 으로 숫자들을 감싸줘야 실행이 됌. 왜냐면 형이 다르면 실행이 안되는데, 같게 해줬잖아.


#string_formatting
#값 넣을 것을 {} 중괄호로 배치함.
print("오늘은 {}년 {}월 {}일입니다.".format(year,month,day)) #.format과 같이 3개의 파라미터를 설정해줘

#이렇게하는 방법도 있더라
date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year,month,day))