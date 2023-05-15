class Note (object):
        def __init__(self, name, text, date, id):
                self._id = id
                self._name = name
                self._text = text
                self._date = date

        def get_name(self):
                return self._name

        def set_name(self, value):
                self._name = value

        def get_text(self):
                return self._text

        def set_text(self, value):
                self._text = value

        def get_id(self):
                return self._id

        def get_date(self):
                return self._date
        
        def set_date(self, value):
                self._date = value