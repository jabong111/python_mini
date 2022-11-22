"""
Birthday paradox 생일 역설
생일 역설이란 ? -> https://namu.wiki/w/%EC%83%9D%EC%9D%BC%20%EB%AC%B8%EC%A0%9C
사람이 n명 있을때 같은 생일인 사람이 존재할 수 있는 확률이 얼마나 되는지 보는것
n이 점점 커질때 확률은 점점 늘어난다.

1. 한 집단에 몇명의 사람이 있는지 입력 받기
2. random으로 생일 받기 (년도는 상관 없음)
	a. random으로 생일 만들어주는 함수
	b. 몇번 돌릴지 함수 생성
	c. 같은 생일인 사람이 있는지 확인하는 함수
	d. 같은 생일이 있는 경우 퍼센트가 몇인지 확인하는 함수
	e. (점화식과 비교) 
"""

import datetime as dt, random

MAX_NUM=100
LOOP=100000
MONTHS = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')

"""
@ 랜덤 생일 생성기
@ arg : number (만들어야 되는 갯수), birthday (list)
@ ret : birthday (list) 
"""
def birthday_generator(number,birthday):
	for i in range(number):
		start_birth = dt.datetime(2019,1,1)  #달과 월만 확인하기 위해 년도는 상관하지 않는다.

		random_birth = dt.timedelta(random.randint(0,364)) #날짜를 더해주면 알아서 달을 계산해준다.
		
		birthday.append(start_birth+random_birth)


"""
@ 생일 같은 날이 있는지 검사
@ arg : number, birthday
@ ret : 1 -> 같은사람 있음, 0 -> 없음
"""
def birthday_check_function(number,birthday):

	for i in range(number):
		for j in range(i+2, number):
			if birthday[i] == birthday[j]:
				#print("correct  ? i{} j{} ".format(birthday[i], birthday[j]))
				return 1

	return 0

def get_birthday_paradox_percent(number, loop):

	cnt = 0
	match = 0
	while (cnt < loop):

		if (cnt % 10000 == 0):
			print("running.....")

		birthday = [] #빈 리스트 생성
		birthday_generator(number,birthday)
		#print("birthday : {}\n".format(birthday))
		if (birthday_check_function(number, birthday)):
				match += 1 #생일 같은 사람이 있으면 올린다.
		cnt += 1

	print("How many groups are matched : ",match)

	return ((match / loop) * 100)



def main():

	while True:
		print("How many birthdays shall I generate? (Max 100)")
		n = int(input("> "))

		if (n > MAX_NUM):
			print("you must input under {}".format(MAX_NUM))
			continue
		break
	
	print("birthday paradox : {}%".format(round(get_birthday_paradox_percent(n, LOOP),2)))
	
	

if __name__=="__main__":
	main()


