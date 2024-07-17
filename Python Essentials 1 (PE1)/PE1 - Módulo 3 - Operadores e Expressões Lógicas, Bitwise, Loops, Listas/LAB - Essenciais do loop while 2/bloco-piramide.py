# LAB: Essenciais do loop while

blocks = int(input("Enter the number of blocks: "))

height = 0
layer = 1

while True:

    if blocks < layer:
        break

    blocks -= layer
    layer += 1
    height += 1

print("The height of the pyramid:", height)
