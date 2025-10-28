class DataSource:
    def read(self):
        pass
class StringSource(DataSource):
    def __init__(self, msg):
        self.msg = msg

    def read(self):
        return self.msg
