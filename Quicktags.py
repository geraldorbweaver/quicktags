import csv
from Card import Card

def main():
	cards = []
	with open('cards.csv', 'r') as in_csv:
		reader = csv.reader(in_csv)
		for row in reader:
			card = Card.from_csvrow(row)
			cards.append(card)
	for card in cards:
		print (card)

if __name__ == '__main__':
	main()