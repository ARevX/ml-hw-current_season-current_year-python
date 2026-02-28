import numpy as np


class KNNRegressor1D:
    """
    Simple k-NN regressor for 1D input x and real-valued output y.
    Uses Euclidean distance in 1D: |x - xi|.
    """

    def __init__(self):
        self.x = None  # shape (N,)
        self.y = None  # shape (N,)

    def fit(self, x: np.ndarray, y: np.ndarray) -> None:
        x = np.asarray(x, dtype=float).reshape(-1)
        y = np.asarray(y, dtype=float).reshape(-1)
        if x.shape[0] != y.shape[0]:
            raise ValueError("x and y must have the same length.")
        if x.shape[0] == 0:
            raise ValueError("Training data is empty.")
        self.x = x
        self.y = y

    def predict(self, X: float, k: int) -> float:
        if self.x is None or self.y is None:
            raise ValueError("Model is not fitted yet.")
        n = self.x.shape[0]
        if k <= 0:
            raise ValueError("k must be a positive integer.")
        if k > n:
            raise ValueError(f"Error: k ({k}) cannot be greater than N ({n}).")

        # Compute distances (vectorized)
        dists = np.abs(self.x - float(X))  # shape (N,)

        # Indices of k smallest distances (efficient; does not fully sort)
        k_idx = np.argpartition(dists, kth=k - 1)[:k]

        # k-NN regression: average of neighbors' y values
        return float(np.mean(self.y[k_idx]))


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
    # Read N and k
    N = read_positive_int("Enter N (positive integer): ")
    k = read_positive_int("Enter k (positive integer): ")

    if k > N:
        print(f"Error: k ({k}) cannot be greater than N ({N}).")
        return

    # Initialize numpy arrays for data insertion
    xs = np.empty(N, dtype=float)
    ys = np.empty(N, dtype=float)

    # Read N points (x, y) one by one
    print("Enter N (x, y) points. For each point, enter x then y.")
    for i in range(N):
        xs[i] = read_float(f"Point {i+1} - x: ")
        ys[i] = read_float(f"Point {i+1} - y: ")

    # Read query X
    X_query = read_float("Enter X (real number) to predict Y: ")

    # Fit and predict
    model = KNNRegressor1D()
    model.fit(xs, ys)
    y_pred = model.predict(X_query, k)

    print(f"Predicted Y (k-NN regression, k={k}) = {y_pred}")


if __name__ == "__main__":
    main()
