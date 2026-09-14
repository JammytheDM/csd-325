def countdown(bottles):
    while bottles >= 1:
        if bottles == 1:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")

        print(f"Take one down and pass it around, {bottles - 1} bottle(s) of beer on the wall.")
        print()

        bottles -= 1
        
def main():
    bottles = int(input("How many bottles of beer are on the wall? "))

    countdown(bottles)

    print("Time to buy more bottles of beer.")


main()
    