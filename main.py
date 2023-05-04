login_1 = 'Erik'
password_1 = '1234fq'

wrong = 3
while True:
	input_login = input('Give login: ')
	if wrong < 2:
		print('У Вас не залишилось спроб. Ви заблоковані!')
		break
	if input_login != login_1:
		print(f'Помилка! Спробуйте ще раз! Спроб залишилось {wrong - 1}.')
		wrong -= 1
	else:
		input_password = input('Give password: ')
		if input_password != password_1:
			print(f'Помилка! Спробуйте ще раз! Спроб залишилось {wrong - 1}.')
			wrong -= 1
		else:
			print('Ви уввійшли в систему!')
			break
