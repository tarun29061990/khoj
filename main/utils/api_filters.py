from .exception import InvalidValueException
from enum import Enum

class ApiFiltersOperatorEnum(Enum):
    OR = "OR"
    AND = "AND"

class ApiFilters(object):
    def __init__(self, filter_str):
        self.filters = {}
        self.operators = {}
        self.keys = []
        if not filter_str:
            return
        segments = filter_str.split(";")
        for segment in segments:
            segment = segment.strip()
            if not segment:
                continue
            parts = segment.split(":", 1)
            if len(parts) < 2:
                raise InvalidValueException("Invalid filters format")
            key = parts[0]
            values = parts[1]
            if not key:
                raise InvalidValueException("Invalid filters format")
            if not values:
                continue
            if "," in values:
                self.operators[key] = ApiFiltersOperatorEnum.OR.value
                self.filters[key] = [value.strip() for value in values.split(",")]
            elif "$" in values:
                self.operators[key] = ApiFiltersOperatorEnum.AND.value
                self.filters[key] = [value.strip() for value in values.split("$")]
            else:
                self.operators[key] = ApiFiltersOperatorEnum.OR.value
                self.filters[key] = [value.strip() for value in values.split(",")]
            self.keys.append(key)

    def get(self, key, default=None):
        if key in self.filters:
            return self.filters[key][0]
        else:
            return default

    def get_list(self, key, default=None):
        if key in self.filters:
            return self.filters[key]
        else:
            return default

    def operator(self, key, default=None):
        if key in self.operators:
            return self.operators[key]
        else:
            return default

    def get_all(self, key, default=None):
        if key in self.filters:
            return self.filters[key]
        else:
            return default

    def has(self, key):
        return key in self.filters

    def get_all_keys(self):
        return self.keys
