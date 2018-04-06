var_context = {}


class DyqExecute:
    def __init__(self, action=None, params=None):
        self.action = action
        self.params = params

    def execute(self):
        result = None
        if self.action == 'print':
            self._print()
        elif self.action == 'assign':
            result = self._assign()
        elif self.action == 'get':
            result = self._get()
        elif self.action == 'condition':
            result = self._condition()
        elif self.action == 'logop':
            result = self._logop()
        elif self.action == 'binop':
            result = self._binop()
        else:
            print("Error, unsupported operation:", str(self))
        return result

    def __str__(self):
        return '[DEXE] %s %s' % (self.action, ';'.join(str(x) for x in self.params))

    @staticmethod
    def isADelayedAction(x=None):
        return ('x' is not None and isinstance(x, DyqExecute))

    @staticmethod
    def resolve(x):
        if not DyqExecute.isADelayedAction(x):
            return x
        else:
            return x.execute()

    def _print(self):
        print(' '.join(str(DyqExecute.resolve(x)) for x in list(self.params)))

    def _assign(self):
        result = var_context[self.params[0]] = DyqExecute.resolve(self.params[1])
        return result

    def _get(self):
        result = var_context.get(self.params[0], 0)
        return result

    def _condition(self):
        result = None
        if DyqExecute.resolve(self.params[0]):
            result = DyqExecute.resolve(self.params[1])
        elif len(self.params) > 2:
            result = DyqExecute.resolve(self.params[2])
        return result

    def _logop(self):
        params = list(self.params)
        result = DyqExecute.resolve(params.pop())
        while len(params) >= 2:
            prev = result
            op = DyqExecute.resolve(params.pop()).upper()
            comp = DyqExecute.resolve(params.pop())
            result = {
                'AND': lambda a, b: (a and b),
                'OR': lambda a, b: (a or b),
            }[op](prev, comp)
        return result

    def _binop(self):
        a = DyqExecute.resolve(self.params[0])
        b = DyqExecute.resolve(self.params[2])
        op = self.params[1]
        result = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
            '%': lambda a, b: a % b,
            '**': lambda a, b: a ** b,
            '>': lambda a, b: (a > b),
            '>=': lambda a, b: (a >= b),
            '<': lambda a, b: (a < b),
            '<=': lambda a, b: (a <= b),
            '==': lambda a, b: (a == b),
            '!=': lambda a, b: (a != b),
        }[op](a, b)
        return result


