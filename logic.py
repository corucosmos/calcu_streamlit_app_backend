# backend/logic.py

class Calculadora:
    @staticmethod
    def suma(a: float, b: float) -> float:
        return a + b
    
    @staticmethod
    def resta(a: float, b: float) -> float:
        return a - b
    
    @staticmethod
    def multiplicacion(a: float, b: float) -> float:
        return a * b
    
    @staticmethod
    def division(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b