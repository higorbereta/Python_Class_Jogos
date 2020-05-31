# Anotações sobre Python 
 
 Link da documentação do Python: https://docs.python.org/3/ 
 
 Comparando o Python 2 com Python 3: https://pyformat.info/
 
## Anotações iniciais
 
 - No Python não é necessário definir o tipo da variavél, já que ele utiliza tipagem dinâmica. Porém o tipo da variável pode ser convertido. 
 - Por convenção padrão o Python usa o **_Snake_Case_** para nomes de variavéis.
 - Para indentação deve-se utilizar _**:**_
 - Cada indentação deve ter 4 espaços. _(1 tab no PyCharm)_
 - Comando input sempre receberá valores tipo string.
 
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
### Laços de repetição

- **_break_** => Interormpe o laço totalmente.
- **_continue_** => Interrompe aquela execução do laço e vai para o próximo incremento.

#### While

Comando de laço padrão que executa enquanto a condição for verdadeira.
É necessário colocar o incremento da validação da lógica dentro do while para que ele possa ser executado corretamente.

Exemplo:

```python
total_tentativas = 4
while(rodada <= total_tentativas):
print(rodada)
rodada = rodada + 1
 ```
#### For

Laço que já faz um auto incremento.

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
####Função .format()

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
