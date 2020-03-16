import inspect
import re
import uuid


def loco(logger):
  rules = {
    '#@': 'debug',
    '#-': 'info',
    '#!': 'warning',
    '#X': 'error'
  }
  
  random = str(uuid.uuid4()).replace('-', '_')

  def decorator(f):
    lines = inspect.getsource(f)
    new_lines = []

    for line in lines.split('\n'):
      if line.startswith('@'):
        continue

      for trigger, method in rules.items():
        m = re.match(f'^(.+){trigger}(.+)$', line)
        if m:
          line = "{}logger_{}.{}(f'{}')".format(m.group(1), random, method, m.group(2).replace('\'', '\\\''))

      new_lines.append(line)

    new_source = '\n'.join(new_lines)

    generated = {
      f'logger_{random}': logger
    }
    exec(new_source, generated)

    return generated[f.__name__]
  return decorator
