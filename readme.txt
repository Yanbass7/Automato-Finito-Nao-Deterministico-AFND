Autômato Finito Não Determinístico (AFND)

Descrição
Implemente um algoritmo que simule um AFND. A entrada consiste da especificação de um AFND
e de um conjunto de palavras. A saída consiste de uma lista indicando ‘S’ caso o AFND reconheça a
palavra em questão e ‘N’ caso contrário.

Você deve redigir um relatório técnico de no máximo duas páginas que contenha pelo menos os
seguintes tópicos: como projetou o algoritmo, quais as estruturas de dados, como você gerenciou o
não determinismo. O relatório deve ser enviado para: rlopes@ufrb.edu.br

Observação:
• Leitura e escrita na entrada/saída padrão.
• Qualquer divergência na saída com relação ao formato especificado implicará em nota zero.
• A implementação não pode fazer uso de recursão.
• A palavra vazia será denotada por *. Podendo ser utilizada em transições e como palavra de
entrada.

Entrada
Na primeira linha, há uma lista de estados. Na segunda linha, há uma lista do alfabeto. Na terceira
linha, há o número total n de transições. Para cada uma das n linhas seguintes, há uma tripla <o,c,d>
onde ‘o’ é o estado de origem, ‘c’ é o caractere e ‘d’ é o estado de destino. Em seguida, há um
caractere informando o estado inicial. Em seguida, há uma lista de estados finais. Por fim, há uma
lista de palavras de teste a ser reconhecida. Os itens da listas serão separados por espaço em branco.

Saída
Seu programa deve imprimir para cada palavra de teste ‘S’ se o AFD reconhece a palavra ou ‘N’
caso contrário.

Exemplos

Entrada                 Saída
0 1                       N
a b                       S
3                         N
0 a 0                     S
0 b 0
0 b 1
0
1
a b aba abb
