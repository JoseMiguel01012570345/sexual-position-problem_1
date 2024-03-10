# Sexual-position (Modelos Matemáticos Aplicados)

En este readme se resuelve el ejercicio 1 del proyecto de Modelos Matemáticos Aplicados. Nuestro objetivo es maximizar el tiempo del acto sexual escogiendo las posturas de forma tal que se cumplan las restricciones del problema.

## Restricciones

En todo momento la energía es mayor o igual a cero, sea $A_{ij}$ la energía de la participante $j$ después de concluir la postura $i$ , se tiene:

* $A_{ij} \geq 0$ , $\forall i \in N , \forall j \in J$

El placer después del acto sexual es mayor o igual
al placer necesario para alcanzar el orgasmo , sea $P_{nj}$ el placer del  participante $j$ y $\overline{P_j}$ el orgasmo de este participante.

* $P_{nj} \geq \overline{P_j}$ , $\forall j \in J$

## Solución

Para hallar el máximo tiempo que se puedo estar para una participante $j$ debemos iterar por las posiciones que menos energía consumen en orden ascendente, si $\exist i \in N$ tal que $\frac{P_{ij}}{c_{ij}}E_{0j} \geq \overline{P_j}$ , donde $c_{ij}$ es la energía que toma la posición $i$ entonces exite solución y si  $\frac{P_{ij}}{c_{ij}}E_{0j} = \overline{P_j}$ entonces la solución óptima es $\frac{E_{0j}}{c_{ij}}$ puesto que $\forall$ $(i-r)$ , $r \in \N , r=0,1,2...i$ se cumple que $\frac{P_{ij}}{c_{ij}}X \gt \frac{P_{(i-r)j}}{c_{(i-r)j}}X$ siendo $E_{0j} \geq X$ , lo que nos lleva a $\overline{P} = \frac{P_{ij}}{c_{ij}}E_{0j} \gt \frac{P_{(i-r)j}}{c_{(i-r)j}}E_{0j}$ por tanto la solución que da la postura $i$ es minimal con respecto al placer , luego es óptima dado que no podemos escoger una postura que nos de mas tiempo y llegar al orgasmo.

 Si $\frac{P_{ij}}{c_{ij}}E_{0j} \gt \overline{P_j}$ entonces hacemos $P = \frac{P_{ij}}{c_{ij}}E_{0j}$ y tenemos que $P=P_k +\overline{P_j}$

Por tanto $P-P_k=\overline{P_j}$ , ahora podemos calcular qué energía se necesita para la posición $i$ tal que se llegue al orgasmo , y como nos sobra energia, podemos continuar. 

Digamos que $P_k=\frac{P_{ij}}{c_{ij}}E_k$ por lo que podemos despejar esta energía y manternos en la posición que menos energía requiera hasta el final del acto, que es cuando el participante acabe su energía, o sea $E_j=0$ para ello tenemos $\frac{P_kc_ij}{P_{ij}}=E_k$ y ahora la cantidad de tiempo que podemos estar en la posición de menor energía es $\frac{E_k}{c{0j}}$ , siendo $c_{0j}$ la posición menos energética . Por tanto el tiempo final para en participante $i$ es $\frac{E_{0j}-E_k}{c_{ij}}+\frac{E_k}{c0j}$. Si $\not \exist$ $i$ tal que $\frac{P_{ij}}{c_{ij}}E_{0j} \geq \overline{P_j}$ entonces el participante $i$ no tiene forma de llegar al orgasmo si que termine con toda su energía , que es lo mismo que no hay solucion para $i$ .

## Como correrlo?
En la raiz del proyecto haga `py problem1.py` si esta en `windows` o si esta en `linux` python3 `problem1.py`
