def show_menu() -> None:
    print()
    print("=== Kalkulator CLI ===")
    print("1) Dodawanie")
    print("2) Odejmowanie")
    print("3) Mnożenie")
    print("4) Dzielenie")
    print("0) Wyjście")


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
        else:
            print(f"Wybrałeś: {choice} (ta opcja będzie dodana w kolejnym kroku)")    


if __name__ == "__main__":
    main()     




