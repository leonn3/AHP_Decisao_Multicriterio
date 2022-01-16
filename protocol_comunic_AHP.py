# coding= UTF-8

from AHP import AHP
from matplotlib import pyplot as plt

exemplo = AHP(
            metodo='Autovalor', 
            precisao=3,
            alternativas=['HTTP','MQTT','Modbus','OPC UA'],
            criterios=['Eficiencia_Operacional','Seguranca','Confiabilidade','Escalabilidade'],
            subCriterios={},
            matrizesPreferencia={
                'Eficiencia_Operacional': [
                    [1,    1/7,   1/5,   1/7],
                    [7,    1,     2,     1],
                    [5,    1/2,   1,     1/2],
                    [7,    1,     2,     1]
                ],
                'Seguranca':[
                    [1,    1/3,   1/3,   1/3],
                    [3,    1,     1,     1],
                    [3,    1,     1,     1],
                    [3,    1,     1,     1]
                ],
                'Confiabilidade':[
                    [1,    1/5,   1/5,   1/5],
                    [5,    1,     2,   2],
                    [5,    1/2,   1,     1/2],
                    [5,    1/2,   2,     1]
                ],
                'Escalabilidade':[
                    [1,    1/3,     1/3,   1/3],
                    [3,    1,       2,     2],
                    [3,    1/2,     1,     1],
                    [3,    1/2,     1,     1]
                ],
                'criterios':[
                    [1,      1,       1,       3],
                    [1,      1,       1,       3],
                    [1,      1,       1,       3],
                    [1/3,    1/3,     1/3,     1],
                ] 
            },
            log= True
)
 
resultado = exemplo.Resultado()
print(resultado)

fig = plt.bar(resultado.keys(), resultado.values(), facecolor='c')
plt.ylabel('Prioridade do Protocolo de Comunicação')
plt.show()