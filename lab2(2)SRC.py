def longest_sequence(cards):
    cards.sort()
    jokers = cards.count(0)
    max_length = 1
    current_length = 1
    
    for i in range(1, len(cards)):
        diff = cards[i] - cards[i - 1]
        
        if diff == 0:
            continue
        
        if diff == 1:
            current_length += 1
        else:
            if jokers >= diff - 1:
                current_length += diff - 1
                jokers -= diff - 1
            else:
                current_length = 1 + jokers
                jokers = 0
        
        max_length = max(max_length, current_length)
    
    return max_length

