import random 
from datetime import *
from faker import Faker
from random import randrange

#header = 'Content-Type:application/json'
#url = 'http://localhost:8082/druid/v2/sql'
#payload = {'unit': unit, 'event_type': event_type, 'staffID': staffID, 'response': response, 'nodeID': nodeID, 'timestamp', timestamp}
#requests.post(url, json=payload, headers=headers)


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
	return random.randint(1,25)

def random_date():
	end = datetime.strptime('9/1/2018 1:30 PM', '%m/%d/%Y %I:%M %p')
	start = datetime.strptime('9/8/2009 4:50 AM', '%m/%d/%Y %I:%M %p')
	delta = end - start
	int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
	random_second = randrange(int_delta)
	return (start + timedelta(seconds=random_second)).isoformat()

if __name__ == "__main__":
	header = 'Content-Type:application/json'
	url = 'http://localhost:8082/druid/v2/?pretty'
	
	for i in range(25):
		payload = {
			'unit': random.choice(units), 'event_type': random.choice(event_types), 
			'staff_name': random.choice(names), 'response': None, 
			'nodeID': nodeID_generator(), 'timestamp': random_date()
			}
		#result = requests.post(url, json=payload, headers=headers).json()
