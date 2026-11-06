p = 10**-12
n = 10**-9
u = 10**-6

components ={ 
    "electrolytic": [5*u, 50*p, 500*p],
    "ceramic": [1*n, 10*n]
}

store = [[], []]

def charge(capacitance, voltage):
    return capacitance * voltage

for i,j in components.items():
    for k in range(len(j)):
        capacitance = j[k]
        voltage = 1200
        q = charge(capacitance, voltage)  # Assuming a voltage of 5 volts for the calculation
        print(q,"F")

        for l in range(len(j)):
            if i == 0:
                store[i] = []
            store[i].append(q,i,j)