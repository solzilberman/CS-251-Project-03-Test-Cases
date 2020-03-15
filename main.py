#Python script to build Products

#rPhone3; Ssamssung; $748.47; [1, 2, 3, 0]

import random
import string

def makeProd():
    name = ""
    name += random.choice(string.ascii_letters).lower()
    name += "Phone"
    name += str(random.randint(0,9))
    name += "; "
    comp = ["Samsung", "Apple", "HTC", "Google"]
    name += comp[random.randint(0,3)]
    name += "; $"
    name += "{:.2f}".format(random.uniform(500.00, 999.99))
    name += "; "
    rating = []
    for i in range(4):
        rating.append(random.randint(0,3))
    name += str(rating)
    return name   

def main():
    outF = open("myOutFile.txt", "w")
    print("File opened...")
    for i in range(10):
      outF.write(makeProd())
      outF.write("\n")
    outF.close()

main()
