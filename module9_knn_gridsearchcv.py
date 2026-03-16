# module8_knn_bestk.py
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def read_real(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a real number.")


def read_non_negative_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")


def main():
    # Read training set
    n = read_positive_integer("Enter N (size of training set): ")

    train_x = np.zeros(n, dtype=float)
    train_y = np.zeros(n, dtype=int)

    print("Enter the training pairs (x, y):")
    for i in range(n):
        train_x[i] = read_real(f"Training pair {i + 1} - x: ")
        train_y[i] = read_non_negative_integer(f"Training pair {i + 1} - y: ")

    # Read test set
    m = read_positive_integer("Enter M (size of test set): ")

    test_x = np.zeros(m, dtype=float)
    test_y = np.zeros(m, dtype=int)

    print("Enter the test pairs (x, y):")
    for i in range(m):
        test_x[i] = read_real(f"Test pair {i + 1} - x: ")
        test_y[i] = read_non_negative_integer(f"Test pair {i + 1} - y: ")

    # Reshape for scikit-learn: each x is a single-feature sample
    X_train = train_x.reshape(-1, 1)
    y_train = train_y
    X_test = test_x.reshape(-1, 1)
    y_test = test_y

    # Try k in range 1 to 10, but k cannot exceed number of training samples
    max_k = min(10, n)

    best_k = 1
    best_accuracy = -1.0

    for k in range(1, max_k + 1):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        if acc > best_accuracy:
            best_accuracy = acc
            best_k = k

    print(f"Best k: {best_k}")
    print(f"Test accuracy: {best_accuracy:.4f}")


if __name__ == "__main__":
    main()
