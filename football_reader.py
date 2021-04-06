import csv

def get_smallest_difference_amoung_teams(file_name):
	smallest_difference = None
	team = None
	with open(file_name) as f:
		reader = csv.DictReader(f, delimiter=",")
		for data in reader:
			diff = int(data["Goals"]) - int(data["Goals Allowed"])
			if smallest_difference is None:
				smallest_difference = diff
				team = data['Team']
			if smallest_difference and smallest_difference > diff:
				smallest_difference = diff
				team = data['Team']
				
	return team

print get_smallest_difference_amoung_teams("football.csv")