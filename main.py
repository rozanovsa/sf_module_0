def game_core_v2(number):
    '''������� ������������� ����� random �����, � ����� ��������� ��� ����������� ���
       � ����������� �� ����, ������ ��� ��� ������ �������.
       ������� ��������� ���������� ����� � ���������� ����� �������'''
    count = 0
    predict = np.random.randint(1,100)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # ����� �� �����, ���� �������

# ���������
score_game(game_core_v2)