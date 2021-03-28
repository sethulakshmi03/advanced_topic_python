res = lambda a,b: a*b if (a*b)>100 else (a*b)+10
res2 = lambda a,b:a*b

def calculate_order_price(l):
    f_res = [(i[0],res(i[2],i[3])) for i in l]
    return f_res

def calculate_product_price(l):
    f_res = []
    for i in l:
        a = 0
        for j in i[1:]:
            a += res2(j[1],j[2])
        f_res.append([i[0],a])
    return f_res

def main():
    l = [["34587", "Learning Python, Mark Lutz", 4, 40.95],
        ["98762", "Programming Python, Mark Lutz", 5, 56.80],
        ["77226", "Head First Python, Paul Barry", 3, 32.95],
        ["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]]

    m = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)],
           [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
           [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]

    print(calculate_order_price(l))
    print()
    print(calculate_product_price(m))

if __name__ == "__main__":
    main()

