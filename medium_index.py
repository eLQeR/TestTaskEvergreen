
def medium_index(numbers: list[int]) -> int | None:
    if len(numbers) <= 1:
        return None
    for i in range(len(numbers)):
        if sum(numbers[:i]) == sum(numbers[i + 1:]):
            return i
    return None


if __name__ == '__main__':
    arr = [1, 7, 3, 6, 5, 6]
    print(medium_index(arr))
