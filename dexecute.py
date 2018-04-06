var_context = {}


class DyqExecute:
    def __init__(self, action=None, params=None):
        self.action = action
        self.params = params

    def execute(self):
        action_dict = {
            'print': self._print,
            'assign': self._assign,
            'get': self._get,
            'condition': self._condition,
            'logop': self._logop,
            'binop': self._binop,
            'loop': self._loop,
            # '': self._,
        }
        result = action_dict.get(self.action, self._error)()
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
        return None

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
        # 如果失败了则执行else后面的参数
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

    def _loop(self):
        for i in self.params[1]:
            var_context[self.params[0]] = i
            DyqExecute.resolve(self.params[2])

    def _error(self):
        print("Error, unsupported operation:", str(self))
        return None


