import random as rn
import re, collections

def player(prev_play, opponent_history=[]):
    pace = 4
    #keys = ['R', 'P', 'S']
    beat = {'R': 'P', 'P': 'S', 'S': 'R'}
    seq = ''

    # Track the last 1000 plays of opponent
    if prev_play != '':
        opponent_history.append(prev_play)
    if len(opponent_history) >= 1000:
        opponent_history.pop(0)
    #    opponent_history.clear()
    #    print(len(opponent_history))

    # not enough data to predict play at random
    if len(opponent_history) <= pace:
        return 'R'
        #return keys[rn.randint(0, 2)]

    # last x plays sequence
    if len(opponent_history) > pace:
        seq = ''.join(opponent_history[-pace:])

    # if sequence not occurred play paper
    if seq not in ''.join(opponent_history)[0:-pace]:
        return 'S'
        #return keys[rn.randint(1, 2)]

    # predict
    regex = re.compile( seq + '[R,P,S]')
    seq_list = re.findall(regex, ''.join(opponent_history))
    predict = collections.Counter(seq_list).most_common()[0][0][-1]
    return beat[predict]