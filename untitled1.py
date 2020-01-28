import random as rm

def name_player_first():
    name_player_first = input("Имя первого игрока")
    return name_player_first

def name_player_second():
    name_player_second = input("Имя второго игрока")
    return name_player_second
def start_game():
    first_name = name_player_first()
    second_name = name_player_second()
    count_sticks = int(input("Введите кол-во палочек"))
    
    num_players = round(rm.random())
    if num_players == 0:
        player_1 = first_name
        player_2 = second_name
        print("Первый игрок ", first_name)
    else:
        player_1 = second_name
        player_2 = first_name
        print("Первый игрок ", second_name)
    i = 1
    while count_sticks != 0:
       if i%2 != 0:
           print(f"Палочек осталось {count_sticks}")
           stick_take_player = int(input(f"{player_1}, сколько палочек убираешь?"))
           if (stick_take_player < 1 or stick_take_player > 3):
               print(f"{player_1}, можно взять 1, 2 или 3 палочки")
           elif count_sticks - stick_take_player < 0:
               print(f"Слишком много взял, {player_1}.")
           elif count_sticks - stick_take_player == 0:
               count_sticks -= stick_take_player
               print(f"Проиграл, {player_1}")
           else:
               count_sticks -= stick_take_player
               i += 1
               
               
       else:
           print(f"Палочек осталось {count_sticks}")
           stick_take_player = int(input(f"{player_2}, сколько палочек убираешь?"))
           if (stick_take_player < 1 or stick_take_player > 3):
               print(f"{player_2}, можно взять 1, 2 или 3 палочки")
           elif count_sticks - stick_take_player < 0:
               print(f"Слишком много взял, {player_2}.")
           elif count_sticks - stick_take_player == 0:
               count_sticks -= stick_take_player
               print(f"Проиграл, {player_2}")
           else:
               count_sticks -= stick_take_player
               i += 1
                

start_game()