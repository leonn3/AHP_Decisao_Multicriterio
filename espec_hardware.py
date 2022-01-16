# coding= UTF-8

from AHP import AHP
from matplotlib import pyplot as plt

exemplo = AHP(
            metodo='Autovalor', 
            precisao=3,
            alternativas=['CLP','Microcontrolador'],
            criterios=['Simplicidade','Baixo custo','Segurança','Eficiência Operacional','Confiabilidade'],
            subCriterios={},
            matrizesPreferencia={
                'Simplicidade': [
                    [1,      3],
                    [1/3,    1],
                ],
                'Baixo custo':[
                    [1,    1/9],
                    [9,    1],
                ],
                'Segurança':[
                    [1,      2],
                    [1/2,    1],
                ],
                'Eficiência Operacional':[
                    [1,      3],
                    [1/3,    1],
                ],
                'Confiabilidade':[
                    [1,      5],
                    [1/5,    1],
                ],
                'criterios':[
                    [1,    1,     1/3,     1/3,    1/3],
                    [1,    1,     1/3,     1/3,    1/3],
                    [3,    3,     1,       1,      1],
                    [3,    3,     1,       1,      1],
                    [3,    3,     1,       1,      1],
                ] 
            },
            log= True
)
 
resultado = exemplo.Resultado()
print(resultado)

plt.bar(resultado.keys(), resultado.values())
fig = plt.bar(resultado.keys(), resultado.values(), facecolor='c')
plt.show()