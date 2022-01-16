# coding= UTF-8

from AHP import AHP
from matplotlib import pyplot as plt

exemplo = AHP(
            metodo='Autovalor', 
            precisao=3,
            alternativas=['SQL','NoSQL'],
            criterios=['Custo_Beneficio','Escalabilidade','Seguranca','Desempenho','Flexibilidade'],
            subCriterios={},
            matrizesPreferencia={
                'Custo_Beneficio': [
                    [1,    1/3],
                    [3,    1],
                ],
                'Escalabilidade':[
                    [1,    1/3],
                    [3,    1],
                ],
                'Seguranca':[
                    [1,      2],
                    [1/2,    1],
                ],
                'Desempenho':[
                    [1,    1/5],
                    [5,    1],
                ],
                'Flexibilidade':[
                    [1,    1/3],
                    [3,    1],
                ],
                'criterios':[
                    [1,    1,     1/5,   1/3,  1],
                    [1,    1,     1/5,   1/3,  1],
                    [5,    5,     1,     2,    5],
                    [3,    3,     1/2,   1,    3],
                    [1,    1,     1/5,   1/3,  1],
                ] 
            },
            log= True
)
 
resultado = exemplo.Resultado()
print(resultado)

fig = plt.bar(resultado.keys(), resultado.values(), facecolor='c')
plt.ylabel('Prioridade do SGBD')
plt.show()