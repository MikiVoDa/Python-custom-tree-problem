# ex: n = 3
#   o
#  ooo
# ooooo

def functie(n):

    for nr in range(0, n):
        print(" " * (n-nr-1) + "æ" * (nr*2+1))

# driver code

functie(int(input("nr = ")))
