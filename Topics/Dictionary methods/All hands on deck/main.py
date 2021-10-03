cards = {str(key): key for key in range(2, 11)}
face_cards = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
cards.update(face_cards)
counter = rank_of_hand = 0
while counter < 6:
    card = input()
    counter += 1
    rank_of_hand += cards.get(card)
print(rank_of_hand / 6)
