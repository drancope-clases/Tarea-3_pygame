# Tarea-3_pygame
completar el programa para dibujar una casa

El objetivo de la tarea es doble:
- aprender las funciones más sencillas de pygame
- configurar el entorno python de vuestro ordenador para usar pygame

La segunda tarea es la primera que hay que hacer.

## Instalar pygame.
La instalación de pygame es difícil dentro de Anaconda, ya que pygame no es compatible con python3. Se haría necesario crear un nuevo entorno de trabajo, distinto del "base", e instalar allí el python que necesitamos, que es una versión 2. Después hay que añadir los canales adecuados para descargar pygame, y por último instalarlos. O bien, tras crear el entorno de python2, instalar allí la instrucción pip y usarla para instalar pygame.

La opción sencilla es olvidarse de esto, y desactivar el entorno de Anaconda en un terminal. A continuación se instala pygame y se trabaja fuera de Anaconda. Esta opción funciona la mayoría de las veces sin problemas. Pero en algún sistema Linux que tenga instalaciones cruzadas y complejas, puede darse el caso de que no funcione (en mi ordenador Linux no funciona, más que nada porque no instalé python2 para no liarme con lo que estaba poniendo en el 3, y he tenido que crear el entorno de python2 en Anaconda, mientras que en el iMac sí ha funcionado, y lo puedo usar fuera de Anaconda).

Ambos procedimientos hay que aplicarlos con una receta rigurosa de orden de operaciones, que se encuentra, como todo, en Internet. La parte positiva es que sois doce personas, y entre todos juntos podéis colaborar para lograr la instalación correcta. Como he dicho antes, alguno irá directo y sin problemas, y algún otro tendrá que buscar ayuda.

## Instrucciones básicas.
Las instrucciones para dibujar se pueden encontrar en https://www.pygame.org

La idea básica es que una pantalla de pygame tiene unas dimensiones que se especifican con la instrucción .display.set_mode(tamaño). El tamaño es una pareja de valores X e Y, que se suele especificar como una "tupla", es decir, una clase de lista con valores inmutables, que no podemos cambiar. Se escribe como una lista, pero con paréntesis en lugar de corchetes. Si no entiendes esto, deberías volver a repasar el notebook de listas en el repositorio python.

En general, cualquier conjunto de datos que vamos a mantener fijos durante un programa, se crea como una tupla: colores, elementos de un fondo fijo de un dibujo, etc.

Para realizar líneas, figuras, etc., las instrucciones más usuales son: .draw.circle(), .draw.rect(), .draw.polygon() o draw.line() --todas con el nombre del módulo delante: pygame.draw.circle(pantalla,[color],[centro],radio,anchura,etc...)--

Todas estas funciones necesitan que les pasemos parámetros de posición dentro de la pantalla, en forma de coordenadas x e y, y colores. La x e y son números enteros entre el cero y el máximo valor de la pantalla que hemos creado. Los colores son tuplas de tres números, uno para cada color primario (RGB, Red, Green, Blue).

Cuando uno empieza con tareas verdaderas de programación, es obligatorio trabajar consultando el manual de referencia de las funciones. Allí encontraremos la sintáxis exacta que necesita cada función. A cada paso que demos, irán saliendo errores en las funciones que escribimos, y tendremos que resolverlas mirando el manual.

En este caso, podéis encontrar estas funciones del submódulo draw en la dirección https://www.pygame.org/docs/ref/draw.html

También se puede ir cogiendo ritmo leyendo artículos o viendo vídeos que expliquen estas funciones o tareas. Pero esto solamente algo inicial. Tenemos que ir independizándonos de los tutoriales para ir más al grano leyendo la documentación oficial.

