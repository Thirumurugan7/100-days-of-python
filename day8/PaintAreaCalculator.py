
import math
def paint_calc(height,width,cover):
	noc=((height*width)/cover)
	print(f"You will need {math.ceil(noc)} of cans")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


