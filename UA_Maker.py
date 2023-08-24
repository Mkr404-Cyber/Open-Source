#create by MKR
import os , random

def ua2():
	os.system('clear')
	print('\x1b[1;92m MKR \x1b[1;97m')
	print(' ════════════════════════════════════════')
	for xr in range(int(input(" UA  Limite : "))):
		print("")
		a='Mozilla/5.0 (Windows NT 10.0;'
		b=random.choice(['7.0','8.1.0','9','10','11','12','13','14'])
		c=random.choice(['Windows NT 10.0'])
		d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
		e=random.randrange(1, 999)
		f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
		g='AppleWebKit/537.36 (KHTML, like Gecko)'
		h=random.randrange(80,103)
		i='0'
		j=random.randrange(4200,4900)
		k=random.randrange(40,150)
		l='Chrome/109.0.0.0 Safari/537.36'
		m='\n'
		make=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}{m}'
		print(make)
ua2()
