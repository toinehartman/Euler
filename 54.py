#!/usr/bin/env python

# DICTIONARY om kaarten in rang te ordenen
card_to_value = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
value_to_card = {v: k for k, v in card_to_value.iteritems()}

def poker(hand1, hand2):
	hand1 = hand1.split()
	hand2 = hand2.split()

	c1 = [None] * len(hand1)
	c2 = [None] * len(hand2)

	for i in xrange(len(hand1)):
		c1[i] = [card_to_value[hand1[i][0]], hand1[i][1]]
		c2[i] = [card_to_value[hand2[i][0]], hand2[i][1]]

	# c1 = [[7, 'C'], [9, 'S'], [12, 'C'], [8, 'H'], [3, 'D']]
	# 7 of clovers, 9 of spades, 12 of clovers, 8 of hearts, 3 of diamonds

	c1.sort()
	c2.sort()

	return (c1, c2)

def rank(cards):
	if royal_flush(cards): return [1, royal_flush(cards)[1], high_card(cards)]
	if straight_flush(cards): return [2, straight_flush(cards)[1], high_card(cards)]
	if four_of_a_kind(cards): return [3, four_of_a_kind(cards)[1], high_card(cards)]
	if full_house(cards): return [4, full_house(cards)[1], high_card(cards)]
	if flush(cards): return [5, flush(cards)[1], high_card(cards)]
	if straight(cards): return [6, straight(cards)[1], high_card(cards)]
	if three_of_a_kind(cards): return [7, three_of_a_kind(cards)[1], high_card(cards)]
	if two_pair(cards): return [8, two_pair(cards)[1], high_card(cards)]
	if pair(cards): return [9, pair(cards)[1], high_card(cards)]
	return [10, high_card(cards)]

def win(cards_1, cards_2):
	ranks = {1: 'ROYAL FLUSH', 2: 'STRAIGHT FLUSH', 3: 'FOUR OF A KIND', 4: 'FULL HOUSE', 5: 'FLUSH', 6: 'STRAIGHT', 7: 'THREE OF A KIND', 8: 'TWO PAIR', 9: 'PAIR', 10: 'HIGH CARD'}

	if rank(cards_1)[0] < rank(cards_2)[0]:
		print '{0} wint van {1}'.format(ranks[rank(cards_1)[0]], ranks[rank(cards_2)[0]])
		return 1
	elif rank(cards_1)[0] > rank(cards_2)[0]:
		print '{0} wint van {1}'.format(ranks[rank(cards_2)[0]], ranks[rank(cards_1)[0]])
		return 2
	else:
		if rank(cards_1)[1] > rank(cards_2)[1]:
			print 'Allebei {0}, {1} als hoogste wint van {2}'.format(ranks[rank(cards_1)[0]], value_to_card[rank(cards_1)[1]], value_to_card[rank(cards_2)[1]])
			return 1
		elif rank(cards_1)[1] < rank(cards_2)[1]:
			print 'Allebei {0}, {1} als hoogste wint van {2}'.format(ranks[rank(cards_1)[0]], value_to_card[rank(cards_2)[1]], value_to_card[rank(cards_1)[1]])
			return 2
		else:
			if rank(cards_1)[2] > rank(cards_2)[2]:
				print'High card: {0} wint van {1}'.format(value_to_card[rank(cards_1)[2]], value_to_card[rank(cards_2)[2]])
				return 1
			elif rank(cards_2)[2] < rank(cards_2)[2]:
				print'High card: {0} wint van {1}'.format(value_to_card[rank(cards_2)[2]], value_to_card[rank(cards_1)[2]])
				return 2

# FUNCTIES om verschillende scores te herkennen

def royal_flush(cards):
	v = sorted(set([c[0] for c in cards]))
	if v == [9, 10, 11, 12, 13] and len(set([c[1] for c in cards])) == 1:
		return (True, max(v))
	return False

def straight_flush(cards):
	v = sorted(set([c[0] for c in cards]))
	if max(v) - min(v) == 4 and len(v) == 5 and len(set([c[1] for c in cards])) == 1:
		return (True, max(v))
	return False

def four_of_a_kind(cards):
	v = sorted(set([c[0] for c in cards]))
	if len(v) == 2 and [c[0] for c in cards].count(v[0]) in [1, 4]:
		for value in v:
			if v.count(value) == 4: h = value
		return (True, h)
	return False

def full_house(cards):
	v = sorted(set([c[0] for c in cards]))
	if len(v) == 2 and [c[0] for c in cards].count(v[0]) in [2, 3]:
		for value in v:
			if [c[0] for c in cards].count(value) == 3: h = value
		return (True, h)
	return False

def flush(cards):
	if len(set([c[1] for c in cards])) == 1:
		return (True, max([c[0] for c in cards]))
	return False

def straight(cards):
	v = sorted(set([c[0] for c in cards]))
	if max(v) - min(v) == 4 and len(v) == 5:
		return (True, high_card(cards))
	return False

def three_of_a_kind(cards):
	v = sorted(set([c[0] for c in cards]))
	if len(v) in [2, 3] and any([c[0] for c in cards].count(v[i]) == 3 for i in xrange(len(v))):
		for i in xrange(len(v)):
			if [c[0] for c in cards].count(v[i]) == 3: h = v[i]
		return (True, h)
	return False

def two_pair(cards):
	v = sorted(set([c[0] for c in cards]))
	h = []
	if len(v) == 3 and not three_of_a_kind(cards):
		for i in xrange(len(v)):
			if [c[0] for c in cards].count(v[i]) == 2: h.append(v[i])
		# print v
		return (True, max(h))
	return False

def pair(cards):
	v = sorted(set([c[0] for c in cards]))
	if len(v) == 4:
		h = filter(lambda x: [c[0] for c in cards].count(x) == 2, v)
		return (True, max(h))
	return False

def high_card(cards):
	v = sorted(set([c[0] for c in cards]))
	return max(v)

# MAIN

wins_1 = 0
wins_2 = 0
hands = open('poker.txt', 'r')

for line in hands:
	line = line.strip('\n')
	hand_1 = line[:14].strip()
	hand_2 = line[14:].strip()

	hand_1, hand_2 = poker(hand_1, hand_2)
	
	print 'PLAYER 1               PLAYER 2'
	print line[:14], '|', line[15:]

	if win(hand_1, hand_2) == 1:
		wins_1 += 1
		print 'PLAYER 1 wins\n'
	else:
		wins_2 += 1
		print 'PLAYER 2 wins\n'

print 'Player 1 wins {0} hands, player 2 wins {1} hands!'.format(wins_1, wins_2)
	
