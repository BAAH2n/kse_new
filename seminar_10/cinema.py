from data.data import get_data, load_data

file_path = "/Users/arsen2000/Documents/КШЕ/ОП/kse_new/seminar_10/data/data.json"

def create_hall(file_path):
    halls = get_data(file_path)
    name = str(input("Enter name of the hall: "))
    if name in halls:
        print("A hall with this name is existing")
    else:
        rows = int(input("Enter number of the rows in the hall: "))
        quantity = int(input("Enter number of the seat in the each row: "))
        new_hall_dict = {name: []}
        for i in range(1, rows+1):
            for j in range(1, quantity+1):
                seat_dict = {f"{i}-{j}": False}
                new_hall_dict[name].append(seat_dict)
        halls.update(new_hall_dict)
    load_data(halls, file_path)

def shows_empty_seats(file_path):
    halls = get_data(file_path)
    hall_name = input("What is the hall name?")
    if hall_name not in halls:
        print("Hall is not exist")
        return None
    else:
        selected_hall = halls[hall_name]
        empty_seats = []
        for seat in selected_hall:
            for key, value in seat.items():
                if value is False:
                    empty_seats.append(key)
        return empty_seats

while True:
    entry = int(input("""Введіть 1, якщо хочете створити зал;
2, якщо хочете побачити вільні місця;
3, якщо хочете забронювати місце;
4, якщо хочете зняти бронь;
0, якщо хочете вийти: """))
    if entry == 0:
        break
    elif entry == 1:
        print("add_hall")
        create_hall(file_path)
    elif entry == 2:
        print("Show empty seats: ")
        shows_empty_seats(file_path)
    elif entry == 3:
        print("Book the seat")
        pass
    elif entry == 4:
        print("Decline reserve")
        pass