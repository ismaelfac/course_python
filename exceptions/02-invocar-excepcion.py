# Excepciones personalizada
class MiError(Exception):
    "Esta clase es para representar mi error"
    
    def __init__(self, message, code):
        self.message = message
        self.code = code

    def __str__(self):
        return f"{self.message} - Codigo: {self.codigo}"


def division(n=0):
    if n == 0:
        raise MiError("No se puede dividir por 0", 805)
    return 5 / n

try:
    division()
except ZeroDivisionError as e:
    print(e)
