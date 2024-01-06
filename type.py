#type conversion

print(int(3.8)) #결과가 3으로 나오는 이유? 반올림이 아니라, 소숫점을 제거하고 정수부분만 읽음
print(float(3))

print(int("2") + int ("5")) # 결과는 7


#st은 string 의 문자형을 나타냄
print(str(2) + str(5))

age = 22
print("제 나이는 " + str(age) + "살 입니다. ")

print(str("Hello World")) #에러가 발생! 왜냐면," "안에 들어있는 건 문자형인데, int 형으로 바꿀 수 가 없기 때문이지.

#8.0을 찾아내기
print(2 ** 3.0)
print(int("3") + float("5"))
print(str(4.0) * 2)
print(float(int(42 / 5)))
print(2 * (3 + 1))



