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
  print(external_var)

  return a + b

myfunc(1, 2)
