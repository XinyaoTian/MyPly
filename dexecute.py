var_context = {}


class DyqExecute:
    def __init__(self, action=None, params=None):
        self.action = action
        self.params = params

    def execute(self):
        result = None
        if self.action == 'print':
            print(' '.join(str(DyqExecute.resolve(x)) for x in list(self.params)))
        elif self.action == 'assign':
            result = var_context[self.params[0]] = DyqExecute.resolve(self.params[1])
        elif self.action == 'get':
            result = var_context.get(self.params[0], 0)
        elif self.action == 'condition':
            if DyqExecute.resolve(self.params[0]):
                result = DyqExecute.resolve(self.params[1])
            elif len(self.params) > 2:
                result = DyqExecute.resolve(self.params[2])
        elif self.action == 'logop':
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
        elif self.action == 'binop':
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