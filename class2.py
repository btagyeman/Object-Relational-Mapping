class Flights:

	counter=1

	def __init__(self,origin, destination, duration):
		self.id=Flights.counter
		Flights.counter += 1

		self.passengers = []
		self.origin = origin
		self.destination = destination
		self.duration = duration

	def print_info(self):
		print(f"\nFlight origin: {self.origin}\n")
		print(f"Flight destination: {self.destination}\n")
		print(f"Flight duration: {self.duration}\n\n")




		print("passengers: \n")
		for passenger in self.passengers:
			print(f"{passenger.name}\n")


	def add_passenger(self, p):
		self.passengers.append(p)
		p.flight_id=self.id


class Passenger:

	def __init__(self, name):
		self.name=name



def main():


	f1= Flights(origin="New York", destination="Paris", duration=540)


	alice=Passenger(name="Bernard")
	bob=Passenger(name="Ehorm")

	f1.add_passenger(alice)
	f1.add_passenger(bob)

	f1.print_info()

	return


if __name__ == '__main__':
	main()




