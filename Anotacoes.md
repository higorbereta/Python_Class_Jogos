# Anotações sobre Python 
 
 Link da documentação do Python: https://docs.python.org/3/ 
 
 Comparando o Python 2 com Python 3: https://pyformat.info/
 
## Anotações iniciais
 
 - No Python não é necessário definir o tipo da variavél, já que ele utiliza tipagem dinâmica. Porém o tipo da variável pode ser convertido. 
 - Por convenção padrão o Python usa o **_Snake_Case_** para nomes de variavéis.
 - Para indentação deve-se utilizar _**:**_
 - Cada indentação deve ter 4 espaços. _(1 tab no PyCharm)_
 - Comando input sempre receberá valores tipo string.
 
 ## Operadores
 
 - O operador **/** trás sempre um resultado float, e por isso ele é chamado de **_float division_**.
 - Existe outro operador para divisão. O operador // que trás apenas o resultado inteiro sem arredondamento. Também chamado de **_integer division_**.
 
## Funções
 
 - type() => Essa funão verifica o tipo da variável.
 - int() => Converte uma variável do tipo string.
 - elif() => Comando Else If
 
No comando do if, é possível realizar a validação através de uma variável boolena, sem colocar a condicão completa.

Exemplo: 

```python
numero_secreto = 42

chute = int(input("Digite seu número: "))
print("Voce digitou ", chute)

acertou = numero_secreto == chute #Variável booleana

if (acertou):
    print("Voce acertou!")
```

### Strig Interpolation

Utiliza a função .format(). Exemplo:
```python
print("Tentativas {} de {}: ".format(rodada, total_tentativas))
```

###Função .format()

Essa função é utilizada para formatações de valores que serão utilizados na String. 

##### Tipos de formatação
- Utilizada durante a concatenação de string, onde podemos informas os valores dentro do format. Nesse caso, o local onde a variável deverá entrar deve estar com {}, e os valores a serem concatenados deverão estar dentro do () da função.

```Python
print("Tentativa {} de {}".format(3,10))
```

- Transformar o tipo da variável, onde o tipo deverá ser mencionado dentro das {}. Como exemplo, o do float **_{:f}_**

```python
print("R$ {:07.2f}".format(32.59))      #Para tipo float
print("R$ {:07.2d}".format(1234.8))  
print("Data {:02d}/{:02d}".format(9,4)) #Para tipo inteiro
```
_**Nota:** na formatação do format, após os : podemos definir a quantidade de caracteres de um valor a ser exibido, porém ao utilizar um valor antes do divisor de inteiros, caso o número seja menor, ele será preenhcido com ~~espaços vazios~~. Para substituir isso por 0, devemos colocar o 0 antes após os : dentro das {}._

### Função round()
Essa função é utilizada para arredondar um valor float para inteiro. O Python 3 usa uma forma de arredondar, que também é chamado de Banker's rounding e sempre arredonda para o próximo valor par.
No exemplo abaixo, ele irá arredondar o valor e demostrar apenas o resultado arredondado.
```python
numero = 38.6
round(numero)
```
### Função abs()

Função utilizada para exibir somente o valor abstrato.

```python
abs(-10)
>>> 10

abs(10)
>>> 10
```

### Função find()

Função do tipo String usada para buscar as informações dentro de uma String, devolvendo a posição da letra, e caso não exista a letra ele devolve posição negativa.

Uma limitação desse comando é que ele mostra apenas a primeira posição encontrada e não todas.
```python
palavra = "Canada"
palavra.find("c")
>>> 0 #Devolve a posição da letra

palavra.find("b")
>>> -1

palavra.find("a")
>>> 1
```

## Laços de repetição

- **_break_** => Interormpe o laço totalmente.
- **_continue_** => Interrompe aquela execução do laço e vai para o próximo incremento.

### While

Comando de laço padrão que executa enquanto a condição for verdadeira.
É necessário colocar o incremento da validação da lógica dentro do while para que ele possa ser executado corretamente.

Exemplo:

```python
total_tentativas = 4
while(rodada <= total_tentativas):
print(rodada)
rodada = rodada + 1
 ```
### For

Laço que já faz um auto incremento no medidor.

#### for in range

O comando _in rage_ é utilizado para informar o range de incremento do laço, onde a primeira variável é o número inicial, e  a segunda variavél é o valor final. 
Existe a possibilidade de se adicionar uma terceira variável, que seria o **_step_**, que indica o valor a ser incrementado em cada execução, sendo que por padrão é adicionado 1.

```python
for rodada in range(1,total_tentativas +1, 2):
print(rodada)
 ```
Também é possível utilizar o laço sem o comando **_range_**, sendo necessário informar as validações manualmente.
Exemplo:

```python
for rodada in (1,2,3,4):
print(rodada)
```

#### for _variavel_ in 

Uma palavra nada mais é do que uma sequência de caracteres. Tanto isso é verdade, que podemos usar o laço for para iterar/percorrer por uma varíavel.

A primeira variável é o apelido que damos para ter acesso a iteração, e a segunda variável é o item que será iterado.

Nesse caso, o for será executada a quantidade de caracteres existentes na variável.

Exemplo de código:

```python
posicao = 0
palavra = "ABCD"
for letra in palavra:
    print(posicao)
    posicao = posicao + 1  
```
O resultado exibido será:
```
0
1
2
3
```


### Random

Esse módulo tem a função de aleatoriedade, porém é um módulo pseudo.random que ao utilizar a mesma seed, poderá gerar o mesmo valor novamente. Por isso ele é pseudo random, já que não é totalmente randómico e é previsível.
```python
random.seed(100)
random.randrage(1,101)
>>> 19
``` 

## Coleções

### List

- Lista sequencia de valores.
- List e String são parecidos.
- Os valores podem ser alterados por comandos como append() e pop().
- Os valores devem ser declarados entre [ ] 

#### List Comprehension

- Forma de preencher uma lista através de código.
- Exemplo:

```python
inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]COPIAR 
```

### Tuple

- Sequencia tuple não pode ser alterada. 
- Comandos como .append ou .pop() não funcionam na Tuple.
- Diferente da lista que é declarada com [ ], os valores da tuple é declardo com ( )
- A tuple pode ser inserida dentro de uma lista.

### Set
- O set não é uma sequencia e por isso não possui um índice.
- O set não é ordenado
- Os valores devem ser declarados entre { }
- Função para adicionar elementos é a add() - append não funciona

###Dictionary
- O dicionário é dinifido igual um SET, porém serve para vincular dois valores, facilitando uma futura busca.

``` python
instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
```

## Arquivos no Python

### Comando Open

- Comando para abrir um arquivo, onde temos que definir alguns parametros no código.
- Função Built-in
   