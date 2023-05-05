from math import degrees, pi, sin, asin, cos, acos


try:
	# This is collecting the information on the triangle from the user
	a_a = float(input("m<A: "))
	a_b = float(input("m<B: "))
	a_c = float(input("m<C: "))
	s_a = float(input("Side a: "))
	s_b = float(input("Side b: "))
	s_c = float(input("Side c: "))
except ValueError:
	input("Invalid input. Press 'ENTER'")
	quit("Invalid FloatI")


def main():
	global a_a
	global a_b
	global a_c
	global s_a
	global s_b
	global s_c
	
	if (a_a * a_b * a_c) and (a_a + a_b + a_c != 180):
		input("Invalid angle input.\nPress 'ENTER' to continue.")
		quit("Invalid AngleI")
	
	if s_a * s_b * s_c:
		def sss_lofc(a, b, c):
			return degrees(acos((c ** 2 - b ** 2 - a ** 2) / (-2.0 * a * b)))
		
		a_a = sss_lofc(s_a, s_b, s_c)
		a_b = sss_lofc(s_b, s_c, s_a)
		a_c = sss_lofc(s_c, s_a, s_b)
		assert a_a + a_b + a_c == 180
		
	print(a_a)
	print(a_b)
	print(a_c)


if __name__ == "__main__":
	main()
