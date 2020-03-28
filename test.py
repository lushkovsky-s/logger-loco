import logging
import logging.config

logging.config.dictConfig({
  'version': 1,
  'handlers': {
    'console': { 'class': 'logging.StreamHandler' }
  },
  'loggers': {
    'default': { 'level': 'DEBUG', 'handlers': ['console'] }
  }
})

logger = logging.getLogger('default')

from logger_loco import loco

external_var = 12
MYCONST = 10

@loco(logger)
def myfunc(a, b, x=MYCONST):
  # Regular comment

  #@ Debug
  #- Info
  #! Warning
  #X Error

  #@ Inject {a} + {b} = {a + b}
  #@ External var: {external_var}
  #@ Comment with manny backslashes \\\\\\ and quotes '''

  #-->
  #@ Indented
  #<--
  #@ Not indented

  return a + b

@loco(logger, indent_size=4)
def fun2():
  #-->
  #@ Indented with 4 spaces
  #-->
  #@ Indented deeper
  #<--
  #<--
  #@ Regular
  ...

@loco(logger)
def func3():
  # some
  # ...
  #...
  #...
  try:
    raise Exception('Some error')
  except Exception as e:
    print(e)

myfunc(1, 2)
fun2()
func3()

class OtherClass(object):
  pass

@loco(logger)
class MyCalss(OtherClass):
  def __init__(self, *args, **kw):
    super().__init__(*args, **kw)

  def method_a(self, a, b):
    #- Works inside class method a + b = {a + b}
    ...

MyCalss().method_a(1, 2)
