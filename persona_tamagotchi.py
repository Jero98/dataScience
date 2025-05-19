from tamagotchi import Tamagotchi
class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
        self.tamagotchis = []
        self.tamagotchi_activo = None

    def adoptar_tamagotchi(self, nombre, color):
        tamagotchi = Tamagotchi(nombre, color)
        self.tamagotchis.append(tamagotchi)
        print(f"{self.nombre} ha adoptado a {nombre}!")

    def evaluar_tamagotchis(self):
        for tamagotchi in self.tamagotchis:
            if tamagotchi.hambre > 70:
                print(f"{tamagotchi.nombre} tiene mucha hambre")
            elif tamagotchi.felicidad < 30:
                print(f"{tamagotchi.nombre} esta triste")
            elif tamagotchi.energia < 20:
                print(f"{tamagotchi.nombre} esta cansado")
            else:
                print(f"{tamagotchi.nombre} esta feliz")
    
    def mostrar_tamagotchis(self):
        for tamagotchi in self.tamagotchis:
            print(f"Nombre: {tamagotchi.nombre}, Color: {tamagotchi.color}, Hambre: {tamagotchi.hambre}, Felicidad: {tamagotchi.felicidad}, Energia: {tamagotchi.energia}")
    
    def seleccionar_tamagotchi(self):
        tama = input("con quien quieres jugar?")
        for tamagotchi in self.tamagotchis:
            if tamagotchi.nombre == tama:
                self.tamagotchi_activo = tamagotchi
                print(f"{tama} ha sido seleccionado!")
            
        else:
                print("no tengo un tamagotchi con ese nombre")
    def accion_tamagotchi(self, accion):
        if self.tamagotchi_activo is not None:
            if accion == "jugar":
                self.tamagotchi_activo.jugar()
            elif accion == "comer":
                self.tamagotchi_activo.comer()
            elif accion == "dormir":
                self.tamagotchi_activo.dormir()
            else:
                print("accion no valida")
        else:
            print("no hay tamagotchi seleccionado")
if __name__ == "__main__":
    persona = Persona("Juan", 25, "Estudiante")
    persona.adoptar_tamagotchi("Tama", "rojo")
    persona.adoptar_tamagotchi("pipitchi", "negro")
    persona.adoptar_tamagotchi("jojoba", "blanco")
    persona.mostrar_tamagotchis()
    persona.seleccionar_tamagotchi()
    persona.accion_tamagotchi("jugar")
    persona.accion_tamagotchi("comer")
    persona.accion_tamagotchi("dormir")
    persona.evaluar_tamagotchis()