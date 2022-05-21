# pytest
---
writing python testcases using `pytest`
### Installation 
---
```bash
sudo apt install python3-pytest -y
```
### Usage
---
- for specific test file
```bash
pytest-3 /path/to/testfile.py
```
- on packaged directory (ideal)
```bash
pytest-3 --pyargs utils
```
- for specific marking
```bash
pytest-3 -m marking /path/to/testfile.py
```
- to create plain-text machine-readable result file
```bash
pytest-3 --pyargs utils --resultlog=./test.log
```
### Reading Material
---
- [x] [zetcode/Pytest tutorial](https://zetcode.com/python/pytest/)
- [ ] [tutorialspoint/pytest](https://www.tutorialspoint.com/pytest/index.htm)
- [ ] [Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/)
- [ ] [What is __ init __.py? : A guide](https://careerkarma.com/blog/what-is-init-py/)
- [ ] [pluralsight/intro-to-pytest](https://github.com/pluralsight/intro-to-pytest)
- [ ] [Revving up Continuous Integration with Parallel Testing](https://semaphoreci.com/blog/revving-up-continuous-integration-with-parallel-testing)
- [ ] [Awesome Pytest](https://github.com/augustogoulart/awesome-pytest)
