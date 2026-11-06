list = [5e-12, 10e-6, 100e-9]

def charge(c,v):
    q = c*v
    return q

for c in list:

    a = charge(c,10)
    print(a)

    if a > 5:
        print(f"ok:{a:.2f}")
    else:
        print(f"Not ok:{a:.2f}")