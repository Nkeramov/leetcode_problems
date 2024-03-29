import pytest


class Solution:
    def solve(self, x: int) -> int:
        sign = 1
        if x < 0:
            x = abs(x)
            sign = -1
        ans = 0
        while x > 0:
            ans = ans * 10 + x % 10
            x = x // 10
        return sign * ans if -2**31 <= ans <= 2**31 - 1 else 0


@pytest.mark.parametrize("input_value, expected_value", [
    (0, 0), (123, 321), (123, 321), (120, 21), (777, 777)
])
def test_problem(input_value, expected_value):
    solution = Solution()
    ans = solution.solve(input_value)
    assert ans == expected_value
