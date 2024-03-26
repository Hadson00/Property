class bombaCombusivel():
    def __init__(self, tipoCombustivel, qntdCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = 5.75
        self.qntdCombustivel = qntdCombustivel
    
    def abastecerPorValor(self, valor):
        combustivelCarro = (valor / self.valorLitro)
        return combustivelCarro

    def abasecerPorLitro(self, litro):
        self.qntdCombustivel -= litro
        return self.valorLitro * litro
    
    def alterarValor(self, novoLitro):
        self.valorLitro = novoLitro
        return self.valorLitro

    def alterarCombustivel(self, novoCombustivel):
        return novoCombustivel

    def aterarQuantidadeCombustivel(self, novoQntdCombustivel):
        return novoQntdCombustivel

musculo = bombaCombusivel('Diesel', 60000)
print(musculo)