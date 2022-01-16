# coding= UTF-8

from AHP import AHP
from matplotlib import pyplot as plt

exemplo = AHP(
            metodo='Autovalor', 
            precisao=3,
            alternativas=['C++','Java','Delphi','Python'],
            criterios=['Desempenho','Confiabilidade','Legibilidade','Custo','Suporte_e_Comunidade', 'Flexibilidade','Simplicidade','Exp_Dev'],
            subCriterios={},
            matrizesPreferencia={
                'Desempenho': [
                    [1,    1,     3,     1],
                    [1,    1,     3,     1],
                    [1/3,  1/3,   1,     1/3],
                    [1,    1,     3,     1]
                ],
                'Confiabilidade':[
                    [1,    1/5,   1/3,   1/5],
                    [5,    1,     1,     1],
                    [3,    1,     1,     1],
                    [5,    1,     1,     1]
                ],
                'Legibilidade':[
                    [1,    3,     3,     1/5],
                    [1/3,  1,     1,     1/7],
                    [1/3,  1,     1,     1/7],
                    [5,    7,     7,     1]
                ],
                'Custo':[
                    [1,    1/5,   1/3,   1/7],
                    [5,    1,     3,     1/3],
                    [3,    1/3,   1,     1/5],
                    [7,    3,     5,     1]
                ],
                'Suporte_e_Comunidade':[
                    [1,      1/2,     3,     1/3],
                    [2,      1,       5,     1/2],
                    [1/3,    1/5,     1,     1/3],
                    [3,      2,       3,     1]
                ],
                'Flexibilidade':[
                    [1,      1,       3,       1/3],
                    [1,      1,       3,       1/3],
                    [1/3,    1/3,     1,       1/5],
                    [3,      3,       5,       1]
                ],
                'Simplicidade':[
                    [1,      3,     3,     1/5],
                    [1/3,    1,     1,     1/7],
                    [1/3,    1,     1,     1/7],
                    [5,      7,     7,     1]
                ],
                'Exp_Dev':[
                    [1,    5,     1,     1/3],
                    [1/5,  1,     1/3,   1/5],
                    [1,    3,     1,     1/3],
                    [3,    5,     3,     1]
                ],
                'criterios':[
                    [1,    1,     3,     3,    3,    3,     3,     3],
                    [1,    1,     3,     3,    3,    3,     3,     3],
                    [1/3,  1/3,   1,     1,    1,    1,     1,     1],
                    [1/3,  1/3,   1,     1,    1,    1,     1,     1],
                    [1/3,  1/3,   1,     1,    1,    1,     1,     1],
                    [1/3,  1/3,   1,     1,    1,    1,     1,     1],
                    [1/3,  1/3,   1,     1,    1,    1,     1,     1],
                    [1/3,  1/3,   1,     1,    1,    1,     1,     1]
                ] 
            },
            log= True
)
 
resultado = exemplo.Resultado()
print(resultado)

fig = plt.bar(resultado.keys(), resultado.values(), facecolor='c')
plt.ylabel('Prioridade da Linguagem de Programacao')
plt.grid(False)
plt.show()