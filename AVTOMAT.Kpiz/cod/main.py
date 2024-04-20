class Calculator:
    def divide(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("x and y must be numeric")
        if y == 0:
            raise ZeroDivisionError("Cannot divede by zero")
        return x / y
    def add(self, x , y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("x and y must be numeric")
        return x + y

    def multiply(self,x ,y ):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x and y must be numeric")
        return x * y
