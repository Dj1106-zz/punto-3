Asociatividad y precedencia

En este punto se implementaron diferentes versiones de un analizador sintáctico en Python para observar cómo cambian los resultados dependiendo de la asociatividad y la precedencia de los operadores.

Primero se trabajó con la asociatividad. Se implementó una versión donde las operaciones se agrupan hacia la izquierda y otra donde se agrupan hacia la derecha. Al probar ambas con la misma expresión, se pudo ver que el árbol sintáctico cambia completamente, lo que demuestra que la forma en que se define la gramática afecta directamente cómo se interpreta la expresión.

Luego se trabajó con la precedencia de operadores. En la versión correcta, la multiplicación tiene mayor prioridad que la suma, por lo que se evalúa primero. Sin embargo, al invertir esta precedencia, la estructura del árbol cambia y la expresión se interpreta de manera diferente, lo que puede llevar a resultados incorrectos.

Las pruebas realizadas muestran claramente que, aunque la cadena de entrada sea la misma, el resultado depende totalmente de cómo esté definida la gramática. Esto evidencia la importancia de establecer correctamente tanto la asociatividad como la precedencia en el diseño de lenguajes y compiladores.

En conclusión, este punto permitió entender que pequeños cambios en la gramática pueden generar grandes diferencias en la interpretación de una expresión, lo cual es fundamental en el análisis sintáctico.
