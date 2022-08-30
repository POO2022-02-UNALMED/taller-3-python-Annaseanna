class TV:
    def __init__(self,marca,estado):
        self.marca=marca
        self.canal=1
        self.precio=500
        self.estado=estado
        self.volumen=1
        self.control=None
        numTV +=1

    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca
    def getCanal(self):
        return self.canal
    def setCanal(self,canal):
        if self.estado == True and canal > 0 and canal <= 120:
            self.canal = canal
    def getPrecio(self):
        return self.precio
    def setPrecio(self,precio):
        self.precio=precio
    def getEstado(self):
        return self.estado
    def getVolumen(self):
        return self.volumen
    def setVolumen(self,volumen):
        if self.estado == True and volumen > 0 and volumen <= 7:
            self.volumen = volumen
    def getControl(self):
        return self.control
    def setControl(self, control):
        self.control = control
    def getNumTV():
        return TV.numTV
    def setNumTV(num):
        TV.numTV = num
    
    def turnOn(self):
        self.estado=True
    def turnOff(self):
        self.estado=False
    def canalUp(self):
        self.setCanal(self.canal + 1)
    def canalDown(self):
        self.setCanal(self.canal - 1)
    def volumenUp(self):
        self.setVolumen(self.volumen + 1)
    def volumenDown(self):
        self.setVolumen(self.volumen - 1)
