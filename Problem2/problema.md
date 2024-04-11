# Problema 2 

## explicación del problema
 se necesita maximizar el placer obtenido por el participante que menos placer tenga después del acto sexual , variando la cantidad de tiempo que se aplica por posición 

## modelación
 ### Siguiendo la modelación y las restricciones expuestas en el problema 1 se llego a la función objetivo que sería $Max min(P[i,N]) \forall i \in J$ 

### Como ya que probar las combinaciones posibles de tiempos dedicados por posición es NP-hard se decidió aproximar la solución óptima utilizando la metaheutistica Partículas en suspensión que aproxima el resultado haciendo una simulación multiagente dónde cada agente computa una solución y se toman las que maximisen la función de fitness definida anteriormente , como criterio de parada decidimos hacer solo 10000 iteraciones por motivos prácticos relacionados a la disponibilidad de tiempo y capacidad de cómputo , aún así obtuvimos buenos resultados durante la experimentación 

## Cómo correr la solución
  ## simplemente ejecute el archivo __main__.py  con un intérprete de python , En el archivo Problem2.py puede cambiar los datos del problema de momento se generan de forma aleatoria