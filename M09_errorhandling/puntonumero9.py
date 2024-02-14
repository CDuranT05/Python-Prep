class Modulo7:
    def __init__(self, lista_numeros = []):
        self.lista_numeros = lista_numeros
        
        for i in lista_numeros:
            if type(i) != int :
                raise ValueError(' Se esperaba una lista de números enteros')
                break  
        
        if len(lista_numeros) <= 0:
            raise ValueError('Se ha creado una lista vacía.')
        # return self.lista_numeros
        
    def verifica_primo(self):
        lista_primos = []
        for i in self.lista_numeros:
            if (self.esprimo(i)):
                lista_primos.append(True)
            else:
                lista_primos.append(False)
        return lista_primos

    
    def conversion_grados(self, origen, destino):
        parametros_esperados = ['Celsius','Kelvin','Farenheit']
        conversion=[] 
        
        if origen not in parametros_esperados or destino not in parametros_esperados:
            print('los parametros esperados son:', parametros_esperados)
            return conversion

        for i in self.lista_numeros:
            conversion.append(self.conversion_de_grados(i, origen, destino))
        return conversion
    
            
    def factor(self): 
         num=[] 
         for  i in  self.lista_numeros:
             num.append(self.factorial(i))
         return num
        
              
    
   # def num_repetidos(self):
        #    self.repetidos(self.lista_numeros)
          #  return self.repetidos(self.lista_numeros)
                
        
    def esprimo(self, num):
        primo=True
        if num % 2 == 0:
            primo=False
        return primo
        
    
    def repetidos(self):
        
        repetidos_dict =  {}
    
        for num in self.lista_numeros:
            if num in repetidos_dict:
                repetidos_dict[num] += 1
            else:
                repetidos_dict[num] = 1
        
        maximo_repetido = None    
        veces_se_repite = 0
        
        
        for num, count in repetidos_dict.items():
            if count > veces_se_repite:
                veces_se_repite = count
                maximo_repetido = num
                
        return  maximo_repetido,veces_se_repite
        
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