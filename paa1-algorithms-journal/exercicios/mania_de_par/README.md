**Problema:** [Mania de Par](https://judge.beecrowd.com/pt/problems/view/1931)

---

## 📌 Descrição do Problema

> Devemos achar o custo do menor caminho com número de estradas par que leve até a cidade alvo C, indicada no inicio do problema. 

---

## 💡 Abordagem

>A ideia para a solução do problema foi aplicar o algoritmo de dijkstra, mas adaptado para colocar na heap uma tupla com 3 parâmetros (custo, nodo, paridade 0: par 1: impar). Em sumo, é como se cada nodo pudesse haver uma duplicata, sendo uma par e outra impar, que após a tupla ser processada é colocada no grupo dos processados. 

---

## ❌ O Que Não Funcionou

> Não cheguei a aplicar outras alternativa diferentes para esse problema, mas levei um bom tempo para ponderar o que eu poderia ou não fazer para resolver o problema. Nenhuma das outras ideias que tive estavam muito claras, mas sabia que primeiro tinha que fazer parar ao ter o nodo alvo como processado. 

---

## 📊 Análise de Complexidade

### Tempo

> Complexidade: O((|E| + |V|) log |V|) --> Devido ao dijkstra


### Espaço

> *(Justifique usando notação assintótica. Considere estruturas de dados usadas, recursão, etc.)*

## 🔍 Corretude

> A minha solução está correta porque o algoritmo de dijkstra por si só vai colocando os nodos em dois grupos, processados e os próximos a serem processados na heap. A minha adaptação é quase isso, mas vai colocando os vizinhos na heap considerando a paridade deles também, então caso tenha um jeito de chegar no nodo com valor impar e outro com valor par, é como se tivesse duas cópias do mesmo nodo. Além disso, coloquei a condição de que se o nodo for o nodo alvo e também tiver paridade par significa que ele será marcado como processado e portanto o caminho já é par e é o menor pelo que provamos em aula. 

---

## 🚀 O Que Poderia ser Melhorado

> *(Reflita: existe solução mais eficiente? O código poderia ser mais legível? Há casos extremos mal tratados?)*


---

## 📸 Evidência de Submissão

> *(Adicione o print do Beecrowd mostrando "Accepted" abaixo)*

![Accepted no Beecrowd](accepted.png)
