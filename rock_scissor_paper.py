import random
def rock_scissor_paper():
    rsp_list = ['가위', '바위', '보']
    score = {'승': 0, '무': 0, '패': 0}

    while True:
        player_choice = input("가위, 바위, 보 중 하나를 입력하세요")

        if player_choice not in rsp_list:
            print("잘못입력하였습니다. 가위, 바위, 보 중 하나를 입력하세요")
            continue

        dealer_choice = random.choice(rsp_list)

        print(f'플레이어: {player_choice}, 컴퓨터: {dealer_choice}')

        if (player_choice == '가위' and dealer_choice =='보') or \
                (player_choice == '바위' and dealer_choice =='가위') or \
                (player_choice == '보' and dealer_choice =='바위'):
            score['승'] += 1
            print(f"이겼습니다! 전적 = {score}")
        elif (player_choice == '가위' and dealer_choice =='바위') or \
                (player_choice == '바위' and dealer_choice =='보') or \
                (player_choice == '보' and dealer_choice =='가위'):
            print(f"졌습니다! 전적 = {score}")
            score['패'] += 1
        elif player_choice == dealer_choice:
            print(f"비겼습니다! 전적 = {score}")
            score['무'] += 1
        while True:
            retry = input("다시 시작하겠습니까? (Y/N)").lower()
            if retry == 'y':
                break
            elif retry == 'n':
                print(f"최종전적: {score}")
                return
            else:
                print("y나 n 중에 하나를 입력하세요")


rock_scissor_paper()