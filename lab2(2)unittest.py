import unittest

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

class TestLongestSequence(unittest.TestCase):
    def test_example(self):
        cards = [1, 2, 0, 4, 5, 7, 8, 0]
        self.assertEqual(longest_sequence(cards), 6)

if __name__ == '__main__':
    unittest.main()
