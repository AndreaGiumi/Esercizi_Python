class Command:
    def execute(self):
        pass


class Add(Command):
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def execute(self, ctx):
        if self.key not in ctx:
            ctx[self.key] = 0
        ctx[self.key] += self.value


class Mul(Command):
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def execute(self, ctx):
        if self.key not in ctx:
            ctx[self.key] = 0
        ctx[self.key] *= self.value


class Pipeline(Command):
    def __init__(self, commands):
        self.commands = commands
    
    def execute(self, ctx):
        for command in self.commands:
            command.execute(ctx)