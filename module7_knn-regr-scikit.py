import numpy as np
from sklearn.neighbors import KNeighborsRegressor


def read_positive_int(prompt: str) -> int:
    while True:
        try:
            v = int(input(prompt).strip())
            if v <= 0:
                print("Please enter a positive integer.")
                continue
            return v
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a real number (e.g., 3.5, -2, 0.01).")


def main():
    # 1) Read N and k
    N = read_positive_int("Enter N (positive integer): ")
    k = read_positive_int("Enter k (positive integer): ")

    if k > N:
        print(f"Error: k ({k}) cannot be greater than N ({N}).")
        return

    # 2) Read N (x, y) points using NumPy arrays for storage
    xs = np.empty(N, dtype=float)
    ys = np.empty(N, dtype=float)

    print("Enter N (x, y) points. For each point, enter x then y.")
    for i in range(N):
        xs[i] = read_float(f"Point {i+1} - x: ")
        ys[i] = read_float(f"Point {i+1} - y: ")

    # 3) Variance of labels in training data
    #    (population variance; use ddof=1 for sample variance if your class expects that)
    y_variance = float(np.var(ys, ddof=0))
    print(f"Training label variance (Var(y)) = {y_variance}")

    # 4) Read query X
    X_query = read_float("Enter X (real number) to predict Y: ")

    # 5) k-NN regression using scikit-learn
    #    scikit-learn expects X as 2D array: shape (n_samples, n_features)
    X_train = xs.reshape(-1, 1)
    y_train = ys

    model = KNeighborsRegressor(n_neighbors=k, weights="uniform", metric="minkowski", p=2)
    model.fit(X_train, y_train)

    y_pred = float(model.predict(np.array([[X_query]], dtype=float))[0])
    print(f"Predicted Y (k-NN regression, k={k}) = {y_pred}")


if __name__ == "__main__":
    main()
