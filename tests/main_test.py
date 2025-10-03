"""
test src/debug_actions/main.py

run with:
```
uv run pytest tests/main_test.py
```
"""

import pytest

from debug_actions import main


def test_main():
    with pytest.raises(NotImplementedError):
        main.main()
