from math import degrees, pi, sin, asin, cos, acos


try:
	# This is collecting the information on the triangle from the user
	angle_a = int(input("m<A: "))
	angle_b = int(input("m<B: "))
	angle_c = int(input("m<C: "))
	side_a = int(input("Side a: "))
	side_b = int(input("Side b: "))
	side_c = int(input("Side c: "))
except ValueError:
	input("Invalid input. Press 'ENTER'")


def main():
	global angle_a
	global angle_b
	global angle_c
	global side_a
	global side_b
	global side_c
	
	if side_a * side_b * side_c:
		def sss_lofc(a, b, c):
			return degrees(acos((c ** 2 - b ** 2 - a ** 2) / (-2.0 * a * b)))
		
		angle_a = sss_lofc(side_a, side_b, side_c)
		angle_b = sss_lofc(side_b, side_c, side_a)
		angle_c = sss_lofc(side_c, side_a, side_b)
		assert angle_a + angle_b + angle_c == 180
		
	print(angle_a)
	print(angle_b)
	print(angle_c)


if __name__ == "__main__":
	main()
