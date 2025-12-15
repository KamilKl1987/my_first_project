def show_menu() -> None:
    print()
    print("=== Kalkulator CLI ===")
    print("1) Dodawanie")
    print("2) Odejmowanie")
    print("3) Mnożenie")
    print("4) Dzielenie")
    print("0) Wyjście")


def add(a: float, b: float) -> float:
    return a+b 

def subtract(a: float, b: float) -> float:
    return a-b   

def multiply(a: float, b: float) -> float:
    return a*b 

def divide(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a/b


def main () -> None:
    while True:
        show_menu()
        choice = input("Wybierz opcję: ").strip()

        if choice == "0":
            print("Do zobaczenia!")
            break

        elif choice == "1":
            first = float(input("Podaj pierwszą liczbę: "))
            second = float(input("Podaj drugą liczbę: "))

            result = add(first, second)
            print(f"Wynik dodawania: {result}")

        elif choice == "2":
            first = float(input("Podaj pierwszą liczbę: "))
            second = float(input("Podaj drugą liczbę: "))

            result = subtract(first, second)
            print(f"Wynik odejmowania: {result}") 

        elif choice == "3":
            first = float(input("Podaj pierwszą liczbe: ")) 
            second = float(input("Podaj drugą liczbę "))

            result = multiply(first, second)
            print(f"Wynik mnożenia: {result}")   

        elif choice == "4":
            first = float(input("Podaj pierwszą liczbę "))
            second = float(input("Podaj drugą liczbę "))

            result = divide(first, second)

            if result is None:
                print("Nie można dzielić przez zero!")
            else:
                print(f"Wynik dzielenia: {result}")        


        else:
            print(f"Wybrałeś: {choice} (ta opcja będzie dodana w kolejnym kroku)")    


if __name__ == "__main__":
    main()     




