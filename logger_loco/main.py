import inspect
import re
import uuid
import functools
import os

current_indent = 0

__DEBUG__=os.environ.get('__LOCO_DEBUG', False)

def loco(logger, indent_symbol=' ', indent_size=2):
  rules = {
    '#@': 'debug',
    '##': 'debug',
    '#-': 'info',
    '#!': 'warning',
    '#X': 'error'
  }

  random = str(uuid.uuid4()).replace('-', '_')

  def decorator(something):
    if inspect.isclass(something):
      c = something

      members = inspect.getmembers(c, predicate=inspect.isfunction)

      for name, method in members:
        if not name.startswith('__') and not name.endswith('__'):
          setattr(c, name, decorator(method))

      return c
    else:
      f = something

      lines = inspect.getsource(f)
      new_lines = []

      if __DEBUG__:
        print('Function sources:')
        print('--------------------')
        print(lines)
        print('--------------------')

      injects = {}
      extra_indention = 0

      global current_indent

      if __DEBUG__:
        print('Current indent:', current_indent)


      loco_matched = False
      outer_func_detected = False

      for line in lines.split('\n'):
        loco_matched_now = False
        
        if line.strip().startswith('@') and not outer_func_detected:
          extra_indention_len = len(line.split('@')[0])

          if __DEBUG__:
              print('Found decorator, extra indention:', extra_indention_len)
          
          if line.strip().startswith('@loco') or line.strip().startswith('@logger_loco.loco'):
              loco_matched = True
              loco_matched_now = True
              if __DEBUG__:
                print('Matched loco decorator', line)
        if 'def ' in line and ':' in line and loco_matched and not outer_func_detected:
          m = re.match('( *)def.+:.*', line)
          extra_indention = len(m.group(1))
          if __DEBUG__:
            print('Function found:', line)
          outer_func_detected = True
        if '-->' in line:
          current_indent += 1
          if __DEBUG__:
            print('Indent incremented', line)
        if '<--' in line:
          current_indent -= 1
          if __DEBUG__:
            print('Indent decremented', line)

        if not loco_matched_now:
            line = line[extra_indention_len:]
        else:
            line = '# Loco decorator was here'

        for trigger, method in rules.items():
          m = re.match(f'^(.+){trigger}(.+)$', line)
          if m:
            indent = m.group(1)
            content = m.group(2)

            content = content.replace('\'', '\u2019')
            content = indent_symbol * (current_indent * indent_size) + content

            line = "{}logger_{}.{}(f'{}')".format(indent, random, method, content)

        if __DEBUG__:
            print('Appending line:', line)
        new_lines.append(line)

      new_source = '\n' * (f.__code__.co_firstlineno-1) + '\n'.join(new_lines)

      generated = {
        f'logger_{random}': logger,
        **f.__globals__,
        **injects
      }

      if __DEBUG__:
        print('To be compiled:')
        print('--------------------')
        print(new_source)
        print('--------------------')

      code = compile(new_source, f.__code__.co_filename, 'exec')
      exec(code, generated)

      generated_func = generated[f.__name__]

      return generated_func

  return decorator
