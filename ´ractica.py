import time
#1
def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True        

def linear_sum_with_time(n):
    """Calcula la suma de los primeros n números primos y el tiempo que toma."""
    star_end=time.time()
    result=[]
    num=2
    while len(result)<n:
        if is_prime(num):
            result.append(num)
        num+=1
    total=sum(result)
    end_time=time.time()
    elapsed_time=end_time-star_end
    return total,elapsed_time  
print(linear_sum_with_time(5))  # (2 + 3 + 5 + 7 + 11 = 28, tiempo)
print(linear_sum_with_time(10)) # (suma de los primeros 10 primos)


#2
def linear_sum_with_time(n):
    """Calcula la suma de los primeros n números naturales y el tiempo que toma."""
    star_time=time.time()
    Total=sum(range(n+1))
    end_time=time.time()
    elapsed_time=end_time-star_time
    return Total, elapsed_time
print(linear_sum_with_time(100)[0] == 5050)
print(linear_sum_with_time(0)[0] == 0)
print(linear_sum_with_time(1)[0] == 1)
print(linear_sum_with_time(10)[0] == 55)
print(isinstance(linear_sum_with_time(5)[1], float))

#3
def factorial_recursive(n):
    """Calcula el factorial de un número recursivamente."""
    if n<0:
        return None
    if n==0 or n==1:
        return 1
    return n*factorial_recursive(n-1)

print(factorial_recursive(5) == 120)
print(factorial_recursive(0) == 1)
print(factorial_recursive(1) == 1)
print(factorial_recursive(3) == 6)
print(factorial_recursive(-1) == None)

#4
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Inserta un nuevo nodo al inicio de la lista."""
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def display(self):
        """Devuelve una representación en cadena de la lista."""
        current=self.head
        resul=[]
        while current:
            resul.append(str(current.data))
            current=current.next
        return ' -> ' .join(resul)   


# Casos de prueba
ll = LinkedList()
ll.insert_at_beginning(3)
print(ll.display() == '3')
ll.insert_at_beginning(2)
print(ll.display() == '2 -> 3')
ll.insert_at_beginning(1)
print(ll.display() == '1 -> 2 -> 3')
ll.insert_at_beginning(0)
print(ll.display() == '0 -> 1 -> 2 -> 3')
print(isinstance(ll.head.data, int))


#5
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    @staticmethod
    def display(head):
        if head is None:
            return 'Empty list'
        result = []
        current = head
        while current:
            result.append(str(current.data))
            current = current.next
        return ' -> '.join(result)

def delete_node(head, target):
    """Elimina la primera ocurrencia de un nodo con el valor dado."""
    if head is None:
        return None
    if head.data==target:
        return head.next
    current=head
    while current.next is not None:
        if current.next.data==target:
            current.next=current.next.next
            return head
        current=current.next
    return head

ll = LinkedList()
ll.insert_at_beginning(3)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
ll.insert_at_beginning(0)

head = delete_node(ll.head, 2)
print(LinkedList.display(head) == '0 -> 1 -> 3')

head = delete_node(head, 0)
print(LinkedList.display(head) == '1 -> 3')

head = delete_node(head, 3)
print(LinkedList.display(head) == '1')

head = delete_node(head, 1)
print(LinkedList.display(head) == 'Empty list')

head = delete_node(head, 4)
print(LinkedList.display(head) == 'Empty list')


#6
# --------------------------------------------
# Inserción al Final de Lista Enlazada
# --------------------------------------------

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """Inserta un nuevo nodo al final de la lista."""
        new_code=Node(data)
        if self.head is None:
            self.head=new_code
            return 
        
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=new_code


    def display(self):
        """Devuelve una representación en cadena de la lista."""
        if self.head is None:
            return 'Empty list'
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return ' -> '.join(result)

# Casos de prueba
ll = LinkedList()
ll.insert_at_end(1)
print(ll.display() == '1')
ll.insert_at_end(2)
print(ll.display() == '1 -> 2')
ll.insert_at_end(3)
print(ll.display() == '1 -> 2 -> 3')
print(isinstance(ll.head, Node))
 
#7
# --------------------------------------------
# Implementación de una Pila (Stack)
# --------------------------------------------

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Agrega un elemento al tope de la pila."""
        self.items.append(item)

    def pop(self):
        """Elimina y devuelve el elemento del tope de la pila."""
        if not self.is_empty():
            return self.items.pop()
        return None  # o lanzar una excepción

    def peek(self):
        """Devuelve el elemento del tope sin eliminarlo."""
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """Devuelve True si la pila está vacía."""
        return len(self.items) == 0


# Casos de prueba
s = Stack()
print(s.is_empty() == True)
s.push(10)
s.push(20)
s.push(30)
print(s.peek() == 30)
print(s.pop() == 30)
print(s.pop() == 20)
print(s.pop() == 10)
print(s.is_empty() == True)

#8
# Devuelve base elevado a exponente (base^exp) usando recursividad.
def potencia(base, exp):
    if exp==0:
        return 1
    return base*potencia(base,exp-1)

# Ejemplo:
print(potencia(2, 3))  # 8
print(potencia(5, 0))  # 1
#9
# Devuelve True si la cadena es un palíndromo.
def es_palindromo(cadena):
    cadena=cadena.replace(" ","").lower()
    if len(cadena)<=1:
        return True
    if cadena[0]==cadena[-1]:
        return es_palindromo(cadena[1:-1])
    return False
# Ejemplo:
print(es_palindromo("reconocer"))  # True
print(es_palindromo("python"))     # False

#10 
# Devuelve la cadena invertida usando recursividad.
def invertir_cadena(cadena):
    if len(cadena)==0:
        return ""
    return cadena[-1] +invertir_cadena(cadena[:-1])

# Ejemplo:
print(invertir_cadena("hola"))     # aloh
print(invertir_cadena("fer"))      # ref


#11
# Devuelve la suma de todos los elementos en una lista usando recursividad.
def suma_lista(lista):
    if not lista:
        return 0
    return lista[0] + suma_lista(lista[1:]) 
    

# Ejemplo:
print(suma_lista([1, 2, 3, 4]))    # 10
print(suma_lista([]))             # 0

#12 
# Devuelve la suma de los dígitos de un número entero.
def suma_digitos(n):
    if n<10:
        return n
    return (n%10)+ suma_digitos(n//10)    

# Ejemplo:
print(suma_digitos(123))          # 6
print(suma_digitos(9))            # 9

   





