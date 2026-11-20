"""
Reverse a list of characters in place.
An empty list stays empty.

Example: ["h", "e", "y"] → ["y", "e", "h"]

Pattern: Two pointers — opposite ends
"""


def reverse_string(chars: list[str]) -> None:
    left = 0
    right = len(chars) - 1

    while left < right:
        # Swap the characters at opposite ends.
        chars[left], chars[right] = chars[right], chars[left]

        left += 1
        right -= 1


if __name__ == "__main__":
    letters = ["h", "e", "y"]
    reverse_string(letters)
    assert letters == ["y", "e", "h"]

    empty: list[str] = []
    reverse_string(empty)
    assert empty == []

    print("Both checks passed.")


# Time: O(n)
# Extra space: O(1)
