class Style:
    style_obj_id = ''
    style_length = 50
    style_char = '.'
    style_end = ': '
    style_return = ''

    def __init__(self, paramter_length=50, parameter_char='.', parameter_end=': '):
        self.style_length = paramter_length
        self.style_char = parameter_char
        self.style_end = parameter_end

    def fit_number(self, number, length=5):
        if isinstance(number, str):
            cache = number
        else:
            cache = str(number)
        self.style_return = ''
        for i in range(length - len(cache)):
            self.style_return += '0'
        self.style_return += cache
        return self.style_return

    def paint(self, parameter_text='', parameter_subject='Console', parameter_request_input=False):
        self.style_return = parameter_subject

        for space in range(len(parameter_subject), self.style_length):
            self.style_return += self.style_char

        self.style_return += self.style_end

        if not parameter_request_input:
            print(self.style_return + str(parameter_text))
        else:
            return input(self.style_return)
