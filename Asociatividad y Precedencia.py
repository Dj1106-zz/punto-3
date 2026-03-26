class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

    def imprimir(self, nivel=0):
        if self.der:
            self.der.imprimir(nivel + 1)
        print("   " * nivel + self.valor)
        if self.izq:
            self.izq.imprimir(nivel + 1)


class ParserIzquierda:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def actual(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consumir(self, t):
        if self.actual() == t:
            self.pos += 1
        else:
            raise Exception("Error sintáctico")

    def parse(self):
        nodo = self.T()
        while self.actual() == '+':
            self.consumir('+')
            nuevo = Nodo('+')
            nuevo.izq = nodo
            nuevo.der = self.T()
            nodo = nuevo
        return nodo

    def T(self):
        if self.actual() == 'id':
            self.consumir('id')
            return Nodo('id')
        raise Exception("Error en T")


class ParserDerecha:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def actual(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consumir(self, t):
        if self.actual() == t:
            self.pos += 1
        else:
            raise Exception("Error sintáctico")

    def parse(self):
        nodo = self.T()
        if self.actual() == '+':
            self.consumir('+')
            nuevo = Nodo('+')
            nuevo.izq = nodo
            nuevo.der = self.parse()
            return nuevo
        return nodo

    def T(self):
        if self.actual() == 'id':
            self.consumir('id')
            return Nodo('id')
        raise Exception("Error en T")


class ParserPrecedenciaNormal:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def actual(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consumir(self, t):
        if self.actual() == t:
            self.pos += 1
        else:
            raise Exception("Error sintáctico")

    def E(self):
        nodo = self.T()
        while self.actual() == '+':
            self.consumir('+')
            nuevo = Nodo('+')
            nuevo.izq = nodo
            nuevo.der = self.T()
            nodo = nuevo
        return nodo

    def T(self):
        nodo = self.F()
        while self.actual() == '*':
            self.consumir('*')
            nuevo = Nodo('*')
            nuevo.izq = nodo
            nuevo.der = self.F()
            nodo = nuevo
        return nodo

    def F(self):
        if self.actual() == 'id':
            self.consumir('id')
            return Nodo('id')
        raise Exception("Error en F")


class ParserPrecedenciaInvertida:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def actual(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consumir(self, t):
        if self.actual() == t:
            self.pos += 1
        else:
            raise Exception("Error sintáctico")

    def E(self):
        nodo = self.T()
        while self.actual() == '*':
            self.consumir('*')
            nuevo = Nodo('*')
            nuevo.izq = nodo
            nuevo.der = self.T()
            nodo = nuevo
        return nodo

    def T(self):
        nodo = self.F()
        while self.actual() == '+':
            self.consumir('+')
            nuevo = Nodo('+')
            nuevo.izq = nodo
            nuevo.der = self.F()
            nodo = nuevo
        return nodo

    def F(self):
        if self.actual() == 'id':
            self.consumir('id')
            return Nodo('id')
        raise Exception("Error en F")


if __name__ == "__main__":
    print("PRUEBA 1")
    tokens = ['id', '+', 'id', '+', 'id']

    print("IZQUIERDA")
    p1 = ParserIzquierda(tokens)
    p1.parse().imprimir()

    print("DERECHA")
    p2 = ParserDerecha(tokens)
    p2.parse().imprimir()

    print("PRUEBA 2")
    tokens = ['id', '+', 'id', '*', 'id']

    print("NORMAL")
    p3 = ParserPrecedenciaNormal(tokens)
    p3.E().imprimir()

    print("INVERTIDA")
    p4 = ParserPrecedenciaInvertida(tokens)
    p4.E().imprimir()