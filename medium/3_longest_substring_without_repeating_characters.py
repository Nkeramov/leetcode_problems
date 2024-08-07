import pytest


class Solution:
    def solve(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i, j = 0, 0
        ans = 0
        seen = set()
        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                while s[i] != s[j]:
                    seen.remove(s[i])
                    i += 1
                seen.remove(s[i])
                i += 1
        return ans


@pytest.mark.parametrize("s, expected_value", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("umvejcuuk", 6),
    ("bpfbhmipx", 7),
    (" ", 1),
    ("", 0)
])
def test_problem(s, expected_value):
    solution = Solution()
    ans = solution.solve(s)
    assert ans == expected_value
