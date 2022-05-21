# data-verify
---
In current directory, `algo_num_test.py` and `algo_str_test.py` are the `modules` to be tested.
### Usage
---
- for specific test file
```bash
pytest-3 utils/tests/algo_num_test.py
```
- on current directory (ideal)
```bash
pytest-3 --pyargs utils
```
- for specific marking
```bash
pytest-3 -m basic utils/tests/algo_num_test.py
```
- to create plain-text machine-readable result file
```bash
pytest-3 --pyargs utils --resultlog=./test.log
```
