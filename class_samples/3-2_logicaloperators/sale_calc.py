print('Enter the amount of purchases, in cents')
x = int(raw_input())

y = x / 100
l = int(y) * float(.10)
h = int(y) - l
k = int(h) *100

if y > 10:
	print("You spent over $10! Your final price is "  +  str(k) +  " cents")
if y < 10:
        print("Sorry for no discount for you.")

