import pytest


class Solution:
    def solve(self, n: int) -> int:
        if n <= 2:
            return 0
        a = [True] * n
        for i in range(2, int(n**0.5) + 1):
            if a[i]:
                # a[i * i : n : i] = [False] * ((n - 1 - i * i) // i + 1)
                for j in range(i * i, n, i):
                    a[j] = False
        return sum(a) - 2


@pytest.mark.parametrize("input_value, expected_value", [
    (10, 4), (0, 0), (1, 0), (4, 2), (13, 5)
])
def test_problem(input_value, expected_value):
    solution = Solution()
    ans = solution.solve(input_value)
    assert ans == expected_value
