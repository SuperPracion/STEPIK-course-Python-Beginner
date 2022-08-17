for bull in range(1, 100):
    for cow in range(1, 100):
        for calf in range(1, 100):
            if (bull * 10) + (cow * 5) + (calf * 0.5) == 100 == bull + cow + calf:
                print(bull, cow, calf, sep=' - ')