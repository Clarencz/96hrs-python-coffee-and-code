import math
def paint_wall(height,width,one_can=7):
    wall_painted = height * width
    number_cans = math.ceil(wall_painted/one_can)
    print(f"number of cans required is {number_cans}")

# h = int(input("what is the height of the wall? "))
# w = int(input("enter width of the wall? "))
# paint_wall(h,w)
paint_wall(height=int(input("Height of wall: ")), width=int(input("Width of wall: ")))