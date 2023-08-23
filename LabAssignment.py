class Flight:
        def __init__(self, id, src, des, price):
            self.id = id
            self.src = src
            self.des = des
            self.price = price

class FltTbl:
        def __init__(self):
            self.flights = []

        def adflt(self, flight):
            self.flights.append(flight)

        def srchcty(self, city):
            res = []
            for flight in self.flights:
                if flight.src == city or flight.des == city:
                    res.append(flight)
            return res

        def srchfromcty(self, SrcCty):
            res = []
            for flight in self.flights:
                if flight.src == SrcCty:
                    res.append(flight)
            return res
        def srchbwcty(self, SrcCty, destination_city):
            res = []
            for flight in self.flights:
                if flight.src == SrcCty and flight.des == destination_city:
                    res.append(flight)
            return res
FltTbl = FltTbl()
FltTbl.adflt(Flight("AI161E90", "BLR", "BOM", 5600))
FltTbl.adflt(Flight("BR161F91", "BOM", "BBI", 6750))
FltTbl.adflt(Flight("AI161F99", "BBI", "BLR", 8210))
FltTbl.adflt(Flight("VS171E20", "JLR", "BBI", 5500))
FltTbl.adflt(Flight("AS171G30", "HYD", "JLR", 4400))
FltTbl.adflt(Flight("AI131F49", "HYD", "BOM", 3499))

print("Search Options:")
print("1. Flights for a particular City")
print("2. Flights From a city")
print("3. Flights between two given cities")

choice = int(input("Enter your choice: "))
if choice == 1:
        city = input("Enter the city: ")
        res = FltTbl.srchcty(city)
elif choice == 2:
        SrcCty = input("Enter the source city: ")
        res = FltTbl.srchfromcty(SrcCty)
elif choice == 3:
        SrcCty = input("Enter the source city: ")
        destination_city = input("Enter the destination city: ")
        res = FltTbl.srchbwcty(SrcCty, destination_city)
else:
        print("Invalid choice")
        res = []

if res:
        print("Flight ID   From   To   Price")
        for flight in res:
            print(flight.id, flight.src, flight.des, flight.price)
else:
        print("No flights found")