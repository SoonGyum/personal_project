import random
target_num = random.randint(1, 100)
guess_num = 0
trial_num = 0
record = {'최고기록': 100}
def up_down(target_num, guess_num, trial_num):
    while True:
        guess_num = int(input("숫자를 입력하세요!(1~100 사이)"))
        if guess_num < 1 or guess_num > 100:
            guess_num = int(input("숫자를 다시 입력하세요(1~100 사이)"))
            continue
        elif guess_num > target_num:
            trial_num += 1
            print(f'다운! 시도({trial_num}회)')
        elif guess_num < target_num:
            trial_num += 1
            print(f'업! 시도({trial_num}회)')
        elif guess_num <= 0 or guess_num >= 100:
            guess_num = int(input(print("숫자를 다시 입력하세요")))
        elif guess_num == target_num:
            trial_num += 1
            print(f'정답입니다! 시도({trial_num}회)')
            while True:
                retry = input("다시 시작하겠습니까? (Y/N").lower()
                if retry == 'y':
                    trial_num = 0
                    break
                elif retry == 'n':
                    if trial_num <= record['최고기록']:
                        record['최고기록'] = trial_num
                        print(f"축하합니다! 최고기록입니다{record}")
                        return record
                    elif trial_num >record['최고기록']:
                        print(f'시도 횟수 :{trial_num}, 최고시도 횟수: {record}')
                        return record
                else:
                    print("y나 n 중에 하나를 입력하세요")
up_down(target_num, guess_num, trial_num)
