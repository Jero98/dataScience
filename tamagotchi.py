class Tamagotchi:
    def __init__ (self, nombre, color, hambre=0, felicidad=100, energia=100):
        self.nombre = nombre
        self.color = color
        self.hambre = hambre
        self.felicidad = felicidad
        self.energia = energia

    def jugar(self):
            if self.energia > 0 and self.hambre < 70:
                self.felicidad +=10
                self.energia -=5
                self.hambre +=5
                print("yay!")
            else:
                print("estoy muy cansado para jugar :(")
        
    def comer(self):
            if self.hambre > 0 and self.hambre <=100:
                self.hambre -=10
                self.energia +=5
                print("ñom ñom ñom")
            else:
                print("estoy lleno x.x")
        
    def dormir(self):
            if self.energia < 100 and self.energia >= 0:
                self.energia +=20
                self.hambre +=5
                self.felicidad +=5
                print("zzzzzz")
            else:
                print("ya dormi lo suficiente ^.^")
