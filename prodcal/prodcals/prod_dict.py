class ProdDict(dict):
    def is_value(self, day):
        path = self[day.year][day.month] if day.year in self.keys() else ''
        if path:
            if day.day in path:
                return True
            else:
                return False
