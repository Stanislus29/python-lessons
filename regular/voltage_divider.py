# Solve a voltage divider and gives you the unknown

def voltage_divider(vin, r1, r2):
    vout = vin * (r2 / (r1 + r2))
    return vout

def resistor_combination(vout, vin, r2):
    r1 = (r2*vin/vout) - r2
    return r1

def divider_ratio(vout, vin):
    ratio = vout / vin
    return ratio

def main():
    ratio = divider_ratio(3, 5)
    print(f"The ratio of Vout to Vin is: {ratio:.2f}")

    r1 = resistor_combination(3, 5, 5000)
    print(f"The value of R1 is: {r1:.2f} ohms")

    vout = voltage_divider(5, 5000, 1000)
    print(f"The output voltage (Vout) is: {vout:.2f} V")

if __name__ == "__main__":
    main()