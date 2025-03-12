
# Instrucciones

Ahora tienes la oportunidad de construir una mejor calculadora. Tu calculadora puede funcionar como tú desees, pero **debe ser utilizable como una calculadora**.

Primero, vamos a **separar la lógica interactiva** dentro de la función `main()`, de la siguiente manera:

```python
def main():
  print("Hello learners!")

if __name__ == "__main__":
  main()
```

Este es un código *boilerplate* (plantilla básica) de Python, que **solo se ejecutará cuando el programa sea invocado por una persona**. Todo tu código ahora debe estar dentro de una función: ya sea en la función `main()` (donde puedes poner cosas como entradas del usuario) o en otra función.

La calificación automática se puntuará sobre 8, y evaluará la funcionalidad de las siguientes funciones:

* `addmultiplenumbers([num, num, ..])` - Esta función debe existir en tu programa, debe recibir una lista de números como entrada y devolver la **suma de esos números**.
* `multiplymultiplenumbers([num, num, ..])` - Esta función debe existir en tu programa, debe recibir una lista de números como entrada y devolver el **resultado de multiplicar cada número en secuencia**.
* `isiteven(num)` - Esta función debe existir en tu programa, debe recibir un solo número como entrada y devolver un valor booleano: `True` si el número es **entero y par**, `False` en caso contrario.
* `isitaninteger(num)` - Esta función debe existir en tu programa, debe recibir un solo número como entrada y devolver un valor booleano: `True` si el número es **un entero**, `False` en caso contrario.

**¡Recuerda!** Este proyecto será calificado automáticamente, ¡y las computadoras son muy literales!

**Nota:** ¡Usa las pruebas! No hay nada de malo en ejecutar las pruebas hasta que pasen. **¡No es trampa!**

**Nota:** Si te atoras haciendo que una función funcione, intenta trabajar en otra diferente. Podrías darte cuenta de que puedes resolver las funciones posteriores más rápido que las primeras.
