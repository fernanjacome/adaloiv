class FloatConverter:
    regex = r'-?\d+(\.\d+)?'  # Expresión regular para números de punto flotante

    def to_python(self, value):
        return float(value)  # Convierte el valor a un float

    def to_url(self, value):
        return str(value)  # Convierte el float a una cadena
