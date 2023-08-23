class Flig:
    def __init__(self):
        self.fligh = [
            {"Flight ID": "AI161E90", "From": "BLR", "To": "BOM", "Price": 5600},
            {"Flight ID": "BR161F91", "From": "BOM", "To": "BBI", "Price": 6750},
            {"Flight ID": "AI161F99", "From": "BBI", "To": "BLR", "Price": 8210},
            {"Flight ID": "VS171E20", "From": "JLR", "To": "BBI", "Price": 5500},
            {"Flight ID": "AS171G30", "From": "HYD", "To": "JLR", "Price": 4400},
            {"Flight ID": "AI131F49", "From": "HYD", "To": "BOM", "Price": 3499},
        ]
        self.ci_map = {
            "BLR": "Bengaluru",
            "BOM": "Mumbai",
            "BBI": "Bhubaneswar",
            "HYD": "Hyderabad",
            "JLR": "Jabalpur",
        }

    def sea(self, ci):
        print(f"Flights to/from {self.ci_map.get(ci, 'Unknown ci')}:")
        for flight in self.fligh:
            if flight["From"] == ci or flight["To"] == ci:
                print(f"Flight ID: {flight['Flight ID']}, Price: {flight['Price']}")

    def seah(self, ci):
        print(f"Flights from {self.ci_map.get(ci, 'Unknown ci')}:")
        for flight in self.fligh:
            if flight["From"] == ci:
                print(f"Flight ID: {flight['Flight ID']}, Price: {flight['Price']}")

    def seahr(self, ci1, ci2):
        print(f"Flights between {self.ci_map.get(ci1, 'Unknown ci')} and {self.ci_map.get(ci2, 'Unknown ci')}:")
        for flight in self.fligh:
            if (flight["From"] == ci1 and flight["To"] == ci2) or (flight["From"] == ci2 and flight["To"] == ci1):
                print(f"Flight ID: {flight['Flight ID']}, Price: {flight['Price']}")

if __name__ == "__main__":
    flt = Flig()

    while True:
        print("\nChoose a search parameter:")
        print("1. Flights for a particular ci")
        print("2. Flights From a ci")
        print("3. Flights between two given cities")
        choi = input("Enter your choi: ")

        if choi == "1":
            ci = input("Enter the ci code: ")
            flt.sea(ci)
        elif choi == "2":
            ci = input("Enter the ci code: ")
            flt.seah(ci)
        elif choi == "3":
            ci1 = input("Enter the first ci code : ")
            ci2 = input("Enter the second ci code: ")
            flt.seahr(ci1, ci2)

        
        else:
            print("Invalid choi. Please try again.")
