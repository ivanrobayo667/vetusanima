secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
usuario = int(input("?:"))

while usuario != secret_number: 
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    usuario = int(input("?:"))
    
print("¡Bien hecho, muggle! Eres libre ahora")
