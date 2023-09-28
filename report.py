# Tạo danh sách kết hợp chứa các cặp (x, y)
pairs_bien = [(-1, 3), (0, 3), (1, 3), (14, 3), (15, 3), (16, 3), (24, 3), (25, 3), (26, 3), 
         (12, -1), (12, 0), (12, 1), (12, 2), (12, 4),(12, 5), (12, 6), (12, 3)]

pairs_phoach = [(-1, 3), (0, 10), (1, 1), (6, 3), (3, 5), (18, 1), (23, 4), (30, 3)]
# In danh sách
for x, a in pairs_bien:
    if (x < 0) or (a < 0) or (a > 5):
        print(f"x = {x}, a = {a}", "output = ", -1)
    else:
        if (x <= 15):
            if (a <= 1):
                print(f"x = {x}, a = {a}", "output = ", 0)
            else: print(f"x = {x}, a = {a}", "output = ", 1)
        else:
            if (x <= 25):
                if (a <= 1):
                    print(f"x = {x}, a = {a}", "output = ", 0)
                else:
                    if (a <= 4):
                        print(f"x = {x}, a = {a}", "output = ", 1)
                    else: print(f"x = {x}, a = {a}", "output = ", 2)
            else:
                if (a <= 1):
                    print(f"x = {x}, a = {a}", "output = ", 1)
                else: print(f"x = {x}, a = {a}", "output = ", 2)

for x, a in pairs_phoach:
    if (x < 0) or (a < 0) or (a > 5):
        print(f"x = {x}, a = {a}", "output = ", -1)
    else:
        if (x <= 15):
            if (a <= 1):
                print(f"x = {x}, a = {a}", "output = ", 0)
            else: print(f"x = {x}, a = {a}", "output = ", 1)
        else:
            if (x <= 25):
                if (a <= 1):
                    print(f"x = {x}, a = {a}", "output = ", 0)
                else:
                    if (a <= 4):
                        print(f"x = {x}, a = {a}", "output = ", 1)
                    else: print(f"x = {x}, a = {a}", "output = ", 2)
            else:
                if (a <= 1):
                    print(f"x = {x}, a = {a}", "output = ", 1)
                else: print(f"x = {x}, a = {a}", "output = ", 2)
