for a in range(1, 1000):
    for b in range(1, 1000-a):
        c = 1000-a-b
        if c*c == a*a + b*b:
            print("Sağlayan Sayılar ->",a, b, c, "  ","Sorunun Cevabı ->", a*b*c)
            break

