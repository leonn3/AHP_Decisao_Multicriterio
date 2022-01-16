# coding= UTF-8

from AHP import AHP
from matplotlib import pyplot as plt

exemplo = AHP(
            metodo='Autovalor', 
            precisao=3,
            alternativas=['Flask','Django'],
            criterios=['Desempenho','Simplicidade','Facil_Integ_BD','Seguranca','Aut_e_Controle'],
            subCriterios={},
            matrizesPreferencia={
                'Desempenho': [
                    [1,    3],
                    [1/3,  1],
                ],
                'Simplicidade':[
                    [1,    1/3],
                    [3,    1],
                ],
                'Facil_Integ_BD':[
                    [1,    1/3],
                    [3,    1],
                ],
                'Seguranca':[
                    [1,    1/3],
                    [3,    1],
                ],
                'Aut_e_Controle':[
                    [1,    1/3],
                    [3,    1],
                ],
                'criterios':[
                    [1,      3,     3,     1,    3],
                    [1/3,    1,     1,     1/5,  1],
                    [1/3,    1,     1,     1/5,  1],
                    [1,      5,     5,     1,    5],
                    [1/3,    1,     1,     1/5,  1],
                ] 
            },
            log= True
)
 
resultado = exemplo.Resultado()
print(resultado)

fig = plt.bar(resultado.keys(), resultado.values(), facecolor='c')
plt.ylabel('Prioridade de Framework')
plt.show()