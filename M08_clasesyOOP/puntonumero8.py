class Modulo7:
    def __init__(self, lista):
        self.lista= lista 
    
    def es_primo(self):
        for i in self.lista:
            if(self.esprimo(i)):
                print('el elemento ', i, ' es primo')
            else: print('el elemento ', i, ' no es primo')
    
    def conversion(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, ' son ', self.conversion_de_grados(i, origen, destino), 'grados', destino)
            
    def factorial_lista(self):
        for i in self.lista:
            print('el factorial de ', i, 'es', self.factorial(i))
    
        
    def esprimo(self, num):
        primo=True
        if num % 2 == 0:
            primo=False
        return primo
        
    
    def repetidos(lista):
            lista_repetidos={}
            for i in lista:
                if i in lista_repetidos:
                    lista_repetidos[i] += 1
                else: lista_repetidos[i] = 1
        
            maximo_repetido= None    
            veces_se_repite= 0
    
            for num, count in lista_repetidos.items():
                if count > veces_se_repite:
                    veces_se_repite = count
                    maximo_repetido = num
            return maximo_repetido, veces_se_repite
        
    def conversion_de_grados(self, valor, origen,destino):
            conversion=0
            if origen == 'Celcius':
                if destino == 'Celsius':
                    conversion = valor
                elif destino == 'Farenheit':
                    conversion = (valor * 9/5) + 32
                elif destino == 'Kelvin':
                    conversion= valor + 273.15
            
            if origen == 'Farenheit':
                if destino == 'Farenheit':
                    conversion = valor
                elif destino== 'Celsius':
                    conversion = (valor - 32) * 9/5
                elif destino == 'Kelvin':
                    conversion = ((valor - 32) * 9/5) + 273.15
            
            if origen== 'Kelvin' :
                if destino == 'Kelvin':
                    conversion = valor
                elif destino == 'Celsius':
                    conversion = valor - 273.15
                elif destino == 'Farenheit':
                    conversion = ((valor - 273.15) * 9/5  + 32)
        
            return conversion
    def factorial(self, numero):
   
            if numero < 0:
                return 'Debe ser positivo' 
            if type(numero) != int:
                return 'Debe ser entero'
            if numero > 1:
                numero=numero*self.factorial(numero - 1)
            return numero