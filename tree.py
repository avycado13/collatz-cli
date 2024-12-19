import matplotlib.pyplot as plt
from helpers import collatz
# TODO Test script


def plot_collatz_tree(root, max_depth, depth=0, parent=None, x_offset=0, y_offset=0):
    if depth > max_depth:
        return

    plt.text(
        x_offset,
        y_offset,
        str(root),
        ha="center",
        va="center",
        bbox=dict(facecolor="white", edgecolor="black"),
    )

    if parent is not None:
        plt.plot([parent[0], x_offset], [parent[1], y_offset], color="blue")

    if depth < max_depth:
        plot_collatz_tree(
            3 * root + 1,
            max_depth,
            depth + 1,
            (x_offset, y_offset),
            x_offset - 20,
            y_offset - 20,
        )
        plot_collatz_tree(
            (root - 1) // 3,
            max_depth,
            depth + 1,
            (x_offset, y_offset),
            x_offset + 20,
            y_offset - 20,
        )


def main(root_value, max_depth):
    plt.figure(figsize=(12, 8))
    plt.title("Collatz Tree (Max Depth = {})".format(max_depth))
    plt.xlabel("Value")
    plt.ylabel("Depth")

    plot_collatz_tree(root_value, max_depth)

    plt.gca().invert_yaxis()  # Invert y-axis to make it look more like a tree
    plt.show()
