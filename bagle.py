'''
숫자는 맞지만 위치가 틀린경우	 pico
숫자도 맞고 자리도 맞으면		 Fermi
맞는 숫자가 없으면				Bagels

0. 정답을 맞춰야하는 3-digit 만들기 반복되면 안된다.
1. 입력 받기 기본 포맷 확인해보기 (main)
2. 문자열 계산

'''
import random

NUMBER_DIGIT = 3 #맞춰야 되는 수의 갯수
MAX_GAME = 10	 #게임 카운트

"""
@ 맞춰야 하는 digit 생성	
@ arg : void
@ ret : 0~9 로 만들어진 n개의 숫자 (str)
"""
def create_digit():
	number = list('0123456789')

	secret_number = ''
	random.shuffle(number)

	for num in range(NUMBER_DIGIT):
		secret_number += number[num] 
	
	return secret_number

	
"""
@ 맞춰야 되는 숫자와 입력받은 숫자를 비교해서 pico, fermi, bagels 출력
@ arg : secret_num(맞춰야 되는 숫자), input_num(입력한 숫자)
@ ret : 'pico(위치만)', 'fermi(위치,숫자)', 'bagels' 
"""
def check_digit(secret_num, input_num):
	# 0~n 까지 비교해서 
	pico_cnt = 0
	fermi_cnt = 0
	clue = []
	if( secret_num == input_num):
		print("You got it!")
		return 0

	for i in range(NUMBER_DIGIT):
		if (secret_num[i] == input_num[i]):
			clue.append("Fermi")
			continue
		elif (input_num[i] in secret_num):
			clue.append("Pico")
			continue

	if (len(clue) == 0):
		print("Bagels")
	else:
		clue.sort() #pico 나 fermi가 나오는 위치로 힌트를 얻을 수도 있으니 섞어버림
		print(' '.join(clue))

	return 1

	
"""
@ 게임을 더 진행 할지 말지
@ arg : cnt (게임 진행 횟수), secret_number (정답) 
@ ret : 1 (더 진행), 0 (게임 끝)
"""
def do_you_wanna_play_more_game(cnt, secret_number):
	if cnt > MAX_GAME:
		print("#### You Lose  ####");
		print("Secret number : {}".format(secret_number))
	else:
		print("#### SCORE ####");
		print("Guess : {}".format(cnt));
	

	print("Do you want to play again? (yes or no)")
	again = input('> ')
	if (again == 'yes'):
		print("play one more time")
		return 1
	else:
		print("Thanks for playing!")
		return 0

def main():

	while True: #main loop

		number = create_digit()
		cnt = 1 #10번의 기회를 준다.

		while (cnt <= MAX_GAME): # game loop
			print("Guess #{}".format(cnt),)
			input_number = input('> ')

			if ((len(input_number) != NUMBER_DIGIT) or (input_number == None)):
				print("you must input {} letter or lower than {}".format(NUMBER_DIGIT,NUMBER_DIGIT))
				continue

			ret = check_digit(number,input_number)
			if (ret == 0): # correct digit end game right now!!!
				break

			cnt += 1

		game = do_you_wanna_play_more_game(cnt, number)
		if game:
			continue
		elif not game:
			break


if __name__=='__main__':
	main()

#TODO : 입력값 중복 검사
#	  : 게임 횟수를 넘었을때 실패 메세지 

