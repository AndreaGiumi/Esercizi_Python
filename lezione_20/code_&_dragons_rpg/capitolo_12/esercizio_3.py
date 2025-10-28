import json

class Serializer:
    def dumps(self):
        pass

    def loads(self):
        pass

class JsonSerializer(Serializer):
    def dumps(self, obj):
        return json.dumps(obj)
    
    def loads(self, s):
        return json.loads(s)