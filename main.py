import numpy as np
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

def score_game(game_core_v1):
    '''��������� ���� 1000 ���, ���� ������ ��� ������ ���� ��������� �����'''
    count_ls = []
    np.random.seed(1)  # ��������� RANDOM SEED, ����� ��� ����������� ��� �������������!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"��� �������� ��������� ����� � ������� �� {score} �������")
    return(score)

# ���������
score_game(game_core_v2)