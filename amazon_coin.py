#! coding: Shift_JIS
import math

have_coin = 0 #�莝���R�C��
coinback = 0 #�R�C���o�b�N�v�Z�p
total_pack = 0 #���v�p�b�N��

have_coin = int(input("�莝���R�C��:"))

coinback = int(input("�R�C���o�b�N(%):"))
if coinback != 0:
	coinback /= 100

print("") #��s

print("�菇:")
while ( have_coin / 360 ) >= 1:
	if ( have_coin / 6000 ) >= 1:
		total_pack += 40
		have_coin -= 6000
		have_coin += 6000 * coinback
		math.ceil(have_coin)
		print("40�p�b�N�w��")
	elif ( have_coin / 2400 ) >= 1:
		total_pack += 15
		have_coin -= 2400
		have_coin += 2400 * coinback
		math.ceil(have_coin)
		print("15�p�b�N�w��")
	elif ( have_coin / 1200 ) >= 1:
		total_pack += 7
		have_coin -= 1200
		have_coin += 1200 * coinback
		math.ceil(have_coin)
		print("7�p�b�N�w��")
	elif ( have_coin / 360 ) >= 1:
		total_pack += 2
		have_coin -= 360
		have_coin += 360 * coinback
		math.ceil(have_coin)
		print("2�p�b�N�w��")

print("") #��s

print("���v�p�b�N:{0}".format(total_pack)) #���v�p�b�N
print("�]��R�C��:{0}".format(int(have_coin))) #�]��R�C��
