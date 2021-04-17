class Currency:
    def __init__(self, symbol, name, symbol_native, decimal_digits, rounding, code, name_plural):
        self.symbol = symbol
        self.name = name
        self.symbol_native = symbol_native
        self.decimal_digits = decimal_digits
        self.rounding = rounding
        self.code = code
        self.name_plural = name_plural

    def __str__(self):
        return self.name + "," + self.code

