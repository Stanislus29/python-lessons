# Class library for Voltage Dividers

# Solve a voltage divider and gives you the unknown

class VDiv:

    def __init__(self, vin, r1, r2):
        self.vin = vin
        self.r1 = r1
        self.r2 = r2

    def voltage_divider(self):
        vout = self.vin * (self.r2 / (self.r1 + self.r2))
        return vout

    def resistor_combination(self, vout):
        r1 = (self.r2*self.vin/vout) - self.r2
        return r1

    def divider_ratio(self, vout):
        ratio = vout / self.vin
        return ratio

    def main():
        from regular.vdivclass import VDiv

        calculator = VDiv(5, 5000, 1000)
        
        ratio = calculator.divider_ratio(4.2)
        print(f"The ratio of Vout to Vin is: {ratio:.2f}")

        r1 = calculator.resistor_combination(4.2)
        print(f"The value of R1 is: {r1:.2f} ohms")

        vout = calculator.voltage_divider()
        print(f"The output voltage (Vout) is: {vout:.2f} V")

    if __name__ == "__main__":
        main()