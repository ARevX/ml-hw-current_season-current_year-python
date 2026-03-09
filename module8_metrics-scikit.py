import numpy as np
from sklearn.metrics import precision_score, recall_score


def read_positive_integer(prompt: str) -> int:
    """Read a positive integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Error: N must be a positive integer.")
        except ValueError:
            print("Error: please enter a valid integer.")


def read_binary_value(prompt: str) -> int:
    """Read a binary class label (0 or 1) from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value in (0, 1):
                return value
            print("Error: value must be 0 or 1.")
        except ValueError:
            print("Error: please enter either 0 or 1.")


def main() -> None:
    n = read_positive_integer("Enter N (positive integer): ")

    # Data initialization with NumPy
    data = np.zeros((n, 2), dtype=int)

    # Read N (x, y) points
    for i in range(n):
        print(f"\nPoint {i + 1}:")
        x = read_binary_value("  Enter x (ground truth, 0 or 1): ")
        y = read_binary_value("  Enter y (predicted class, 0 or 1): ")

        # Data insertion with NumPy
        data[i, 0] = x
        data[i, 1] = y

    # Split into ground truth and predictions
    y_true = data[:, 0]
    y_pred = data[:, 1]

    # Compute metrics with scikit-learn
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)

    # Output results
    print("\nResults:")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")


if __name__ == "__main__":
    main()
