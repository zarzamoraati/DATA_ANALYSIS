class Timer:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def next_second(self):
            # self.__seconds += 1
            # if self.__seconds > 59:
            #     self.__seconds = 0
            #     self.__minutes += 1
            #     if self.__minutes > 59:
            #         self.__minutes = 0
            #         self.__hours += 1
            #         if self.__hours > 23:
            #             self.__hours = 0
      
    def get_hora(self):
        return print(format_horas(self.horas, self.minutos, self.segundos))

def format_horas(horas, min, sec):
    if len(str(horas)) == 1:
        horas = "0" + str(horas)
    if len(str(min)) == 1:
        min = "0" + str(min)
    if len(str(sec)) == 1:
        sec = "0" + str(sec)
    return f"{horas}:{min}:{sec}" 

contador = Timer(23, 57, 57)
for i in range(0, 180):
    contador.get_hora()
    contador.next_second()