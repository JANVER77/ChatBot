lista = [];


def add_fruit(fruta, name):
    lista.append(fruta);
    print("Hola ", name)
    return "De doy lo que necesites, al terminar de ejecutarme"





print(lista);

add_fruit("Manzana", "Pedro");

add_fruit("Granadilla", "Maria");

necesito = add_fruit("Banana", "Ana");

print(lista);
print(necesito);



nums = [1, 2, 3, 4, 5, 6, 7, 8, 9];

print( sum(nums));

suma = 0;

for i in nums:
    suma += i;
    print(suma);

