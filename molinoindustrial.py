class MolinoIndustrial:
    def __init__(self):
        self.encendido = False
        self.velocidad = 0
        self.produccion = 0

    def encender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False
        self.velocidad = 0 

    def esta_encendido(self):
        return self.encendido
    
    def moler(self):
        if self.encendido:
            self.produccion += 1  
            return "Molino está moliendo"
        else:
            return "Molino apagado, no puede moler"
    
    def __str__(self):
        estado = "encendido" if self.encendido else "apagado"
        return f"Molino {estado}" 