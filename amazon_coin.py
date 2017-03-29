#! coding: Shift_JIS
import math

have_coin = 0 #手持ちコイン
coinback = 0 #コインバック計算用
total_pack = 0 #合計パック数

have_coin = int(input("手持ちコイン:"))

coinback = int(input("コインバック(%):"))
if coinback != 0:
	coinback /= 100

print("") #空行

print("手順:")
while ( have_coin / 360 ) >= 1:
	if ( have_coin / 6000 ) >= 1:
		total_pack += 40
		have_coin -= 6000
		have_coin += 6000 * coinback
		math.ceil(have_coin)
		print("40パック購入")
	elif ( have_coin / 2400 ) >= 1:
		total_pack += 15
		have_coin -= 2400
		have_coin += 2400 * coinback
		math.ceil(have_coin)
		print("15パック購入")
	elif ( have_coin / 1200 ) >= 1:
		total_pack += 7
		have_coin -= 1200
		have_coin += 1200 * coinback
		math.ceil(have_coin)
		print("7パック購入")
	elif ( have_coin / 360 ) >= 1:
		total_pack += 2
		have_coin -= 360
		have_coin += 360 * coinback
		math.ceil(have_coin)
		print("2パック購入")

print("") #空行

print("合計パック:{0}".format(total_pack)) #合計パック
print("余りコイン:{0}".format(int(have_coin))) #余りコイン
