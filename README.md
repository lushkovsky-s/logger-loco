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

  #-->
  #@ This is indented log
  #-->
  #@ This is deeper indented log
  #<--
  #<--
  #@ This is not indented log

somefunc(1, 2)

@loco(logger)
class Someclass(object):
  def mymethod(self):
    #@ Also works with classes
    pass

Someclass().mymethod()
```
  
Will print:  
```raw
DEBUG: This is debug
INFO: This is info
WARNING: This is warning
ERROR: This is error
DEBUG: You could also use variables interpolation: 1 + 2 = 3
DEBUG:   This is indented log
DEBUG:     This is deeper indented log
DEBUG: This is not indented log
DEBUG: Also works with classes
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
