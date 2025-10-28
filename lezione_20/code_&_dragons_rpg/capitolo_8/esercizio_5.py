import json
def to_json_lines(records: list[dict]) -> list[str]:
     return [json.dumps(record) for record in records]