"""
Resumen sobre la clase Daynames:

¿Qué es la clase Daynames?
La clase Daynames se comporta como un nodo en una lista enlazada, donde cada nodo representa un día de la semana. Cada nodo contiene dos variables de instancia: un valor que guarda el nombre del día (`day_name`) y una referencia al siguiente nodo (`next_day`). Esta estructura es útil para representar secuencias de días, donde cada día apunta al siguiente. 

¿Cuándo se usa?
Se utiliza en escenarios donde necesitamos representar una secuencia de elementos de forma dinámica, como una lista de días de la semana o cualquier otra secuencia lineal de eventos donde cada uno depende del anterior.

Pros y Contras de las listas enlazadas:

Pros:
- Facilita la representación de secuencias dinámicas, donde los elementos pueden cambiar de lugar o eliminarse sin reordenar toda la estructura.
- Permite agregar o eliminar elementos de manera eficiente en cualquier punto de la secuencia.

Contras:
- El acceso a un elemento específico es secuencial, lo que puede hacer que la búsqueda de un elemento sea más lenta.
- Al igual que otros nodos, cada uno consume más memoria debido a la necesidad de almacenar la referencia al siguiente nodo.

Esta clase es un ejemplo básico de cómo usar nodos para representar una secuencia de días y cómo se puede recorrer dicha secuencia de manera dinámica.
"""

# Clase Daynames trabaja como un Nodo, con dos variables de instancia: el nombre del día del nodo 
# y el siguiente día del nodo

class Daynames:   # nodo de nombre daynames
    def __init__(self, day_name=None): 
        self.day_name = day_name 
        self.next_day = None 

    def print_weekday(self):
        print(f"Hoy es {self.day_name}")

    def print_tomorrow(self):
        if self.next_day == None:
            print("Aún no se ha establecido el valor para el siguiente día.")
        else: 
            print(f"Mañana es {self.next_day.day_name}")

if __name__ == "__main__":  
    # Crea un objeto Daynames llamado Monday con el valor 'Monday'
    monday = Daynames('Monday')
    monday.print_weekday()

    # Crea un objeto de la clase Daynames con el valor 'Tuesday'
    tuesday = Daynames('Tuesday')
    tuesday.print_weekday()

    # Llama a la función print_tomorrow de la clase Daynames para el objeto Monday, 
    monday.print_tomorrow()  # Imprime None (el siguiente día de Monday es None)

    # Establece la variable next_day de monday al objeto tuesday creando un enlace entre Monday y Tuesday
    monday.next_day = tuesday
    monday.print_tomorrow() 
    print("")

    # Crea el objeto Wednesday
    wednesday = Daynames('Wednesday')
    tuesday.next_day = wednesday        # Establece el valor next_day de tuesday al objeto Wednesday 
    
    thursday = Daynames('Thursday')

    # Itera a través de Monday-Tuesday 
    first_day = monday
    while first_day:
      print(first_day.day_name)
      first_day = first_day.next_day    # No imprime 'Thursday' porque el enlace no está establecido aún