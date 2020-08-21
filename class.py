class Flight:

	def __init__(self, origin, destination, duration):
		self.origin=origin #attribute
		self.destination=destination #attribute
		self.duration=duration #attribute

	def print_info(self):
		print(f"Flight origin: {self.origin}\n")
		print(f"Flight destination: {self.destination}\n")
		print(f"Flight duration: {self.duration}\n")


	def delay(self,amount):
		self.duration += amount
		print(f"The new duration is {self.duration}")




def main():

	f1=Flight(origin="New York", destination ="Paris", duration=540)
	f1.delay(30)
	f1.print_info()

	


	f2=Flight(origin="Tokyo", destination= "Shanghai", duration=185)
	f2.delay(10)
	f2.print_info()

	






	# print(f.origin)
	# print(f.destination)
	# print(f.duration)

	return

if __name__ == '__main__':
	main()