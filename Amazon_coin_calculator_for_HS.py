#! coding: Shift_JIS
#for Hearthstone
import math

have_coin = 0 #�莝���R�C��
coinback = 0 #�R�C���o�b�N�v�Z�p
total_num = 0 #���v��

#�l�i�ƌ��A���ꂼ��̗v�f�ԍ����Ή����Ă���K�v������
price_list	= [ 6000,	2400,	1200,	360 ]
num_list	= [ 40, 	15,  	7,  	2   ]

have_coin = int(input("�莝���R�C��:"))

coinback = int(input("�R�C���o�b�N(%):"))
if coinback != 0:
	coinback /= 100

print("") #��s

print("�菇:")
while ( have_coin / price_list[-1] ) >= 1:
	for i in range( 0, len( price_list ) ):
		if ( have_coin / price_list[i] ) >= 1:
			total_num += num_list[i]
			have_coin -= price_list[i]
			have_coin += price_list[i] * coinback
			math.ceil(have_coin)
			print("{0}�p�b�N�w��".format(num_list[i]))

print("") #��s

print("���v�p�b�N:{0}".format(total_num)) #���v��
print("�]��R�C��:{0}".format(int(have_coin))) #�]��R�C��
