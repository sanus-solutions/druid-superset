import random, requests
from datetime import *
from faker import Faker
from random import randrange, randint


units = [
	"Neonatal intensive care", "Pediatric intensive care", "Coronary care and cardiothoracic", 
	"Surgical intensive care", "Medical intensive care", "Long term intensive care"
	]

event_types = [
	["entry", "clean", "not clean"],
	["dispenser", "face", "no face"],
	["alert"]
	]

names = ['Steven Macdonald',
	'Bonnie Petty',
	'Allison Daniel',
	'Jennifer Beck',
	'Elizabeth Newman',
	'Daniel Stevenson',
	'Rachael White',
	'Joshua Haney',
	'Katherine Cline',
	'Hector Knight',
	'Amanda Green',
	'Brandon Martinez',
	'Allison Vance',
	'Jacqueline Mercado',
	'Rhonda White',
	'Tricia Harrison',
	'Mary Murphy',
	'Deborah Humphrey',
	'Rachel Bates DDS',
	'Diane Arnold',
	'Daniel Johnson',
	'Wendy Smith',
	'Emily Cohen',
	'Megan Garcia',
	'Katherine Long',
	]

def nodeID_generator():
	return randint(1,25)

def random_date():
	# end = datetime.strptime('9/1/2018 1:30 PM', '%m/%d/%Y %I:%M %p')
	# start = datetime.strptime('9/8/2009 4:50 AM', '%m/%d/%Y %I:%M %p')
	start = datetime.utcnow()
	#int_delta = (delta.days * 24 * 60 * 60 * 1000000) + delta.microseconds
	int_delta = 60*60*1000000 + delta.microseconds
	random_second = randrange(int_delta)
	return (start + timedelta(microseconds=random_second)).isoformat()

if __name__ == "__main__":
	headers = {'Content-Type' : 'application/json'}
	url = 'http://localhost:8200/v1/post/hospital'
	
	for i in range(200):
		payload = {
			'time' : datetime.utcnow().isoformat(),
			'unit': random.choice(units), 'type': random.choice(event_types)[0], 
			'staff_name': random.choice(names), 'response': None, 
			'nodeID': nodeID_generator()			
			}
		print payload
		result = requests.post(url, json=payload, headers=headers).json()
		print result
