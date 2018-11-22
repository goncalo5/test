printer = lambda level, msg: print(
        '[%(level)s] %(msg)s' % locals()
)
loggers = {level: lambda msg: printer(level, msg)
           for level in ("info", "err")
          }

loggers["info"]("an info msg")
loggers["err"]("an err msg")
