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

    inject_n = 0
    injects = {}

    for line in lines.split('\n'):
      if line.startswith('@'):
        continue

      for trigger, method in rules.items():
        m = re.match(f'^(.+){trigger}(.+)$', line)
        if m:
          indent = m.group(1)
          content = m.group(2)

          injects[f'inject_{inject_n}'] = content

          line = "{}logger_{}.{}(inject_{})".format(indent, random, method, inject_n)

          inject_n += 1

      new_lines.append(line)

    new_source = '\n'.join(new_lines)

    generated = {
      f'logger_{random}': logger,
      **f.__globals__,
      **injects
    }
    exec(new_source, generated)

    return generated[f.__name__]
  return decorator
