from module5_mod import NumberCollection


def main():
    # Read N
    while True:
        try:
            N = int(input("Enter a positive integer N: "))
            if N > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Create object
    collection = NumberCollection(N)

    # Read N numbers
    for i in range(N):
        while True:
            try:
                num = int(input(f"Enter number {i + 1}: "))
                collection.insert_number(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # Read X
    while True:
        try:
            X = int(input("Enter number X to search: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Search and print result
    result = collection.search_number(X)
    print(result)


if __name__ == "__main__":
    main()
