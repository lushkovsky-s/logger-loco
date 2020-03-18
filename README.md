# Logger LOCO
LoCo = log via comments  
Python >= 3.6 only  
  
Usage:  
```python
import logging
from logger_loco import loco

logger = logging.getLogger('mylogger')

@loco(logger)
def somefunc(a, b):
  # This is a regular comment

  c = a + b 

  #@ This is debug  
  #- This is info 
  #! This is warning
  #X This is error

  #@ You could also use variables interpolation: {a} + {b} = {c}

somefunc(1, 2)
```
  
Will print:  
```raw
DEBUG: This is debug
INFO: This is info
WARNING: This is warning
ERROR: This is error
DEBUG: You could also use variables interpolation: 1 + 2 = 3
```

## Development

Deploy package to <test.pypi.org>:
```
python3 setup.py sdist
python3 -m twine upload ---repository-url https://test.pypi.org/legacy/ dist/*
```

Deploy package to <pypi.org>:
```
python3 setup.py sdist
python3 -m twine upload dist/*
```
