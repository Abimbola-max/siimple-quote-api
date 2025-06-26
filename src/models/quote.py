class Quote:

    def __init__(self, description: str, date_quoted: str):
        self.description = description
        self.date_quoted = date_quoted


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def date_quoted(self):
        return self.__date_quoted

    @date_quoted.setter
    def date_quoted(self, value):
        self.__date_quoted = value