import pandas as pd

# fmc1,fmc2
components_ids = {52659,52660,55022,55025,64729,64788,204095}

import matplotlib.pyplot as plt

classes_csv_names = [
                     'turmas-2016.1.csv',
                     'turmas-2016.2.csv',
                     'turmas-2017.1.csv',
                     'turmas-2017.2.csv',
                     'turmas-2018.1.csv',
                     'turmas-2018.2.csv',
                     'turmas-2019.1.csv',
                     'turmas-2019.2.csv',
                     'turmas-2020.1.csv',
                     'turmas-2020.5.csv',
                     'turmas-2020.6.csv',
                     'turmas-2021.1.csv',
                     'turmas-2021.2.csv'  
                    ]
classes_ids = set()

for name in classes_csv_names:
    df = pd.read_csv(name,encoding='UTF-8',sep=';',usecols=['id_turma','id_componente_curricular'])
    filtered_df = df[df['id_componente_curricular'].isin(components_ids)]     
    for id in df['id_turma'].array.tolist():
        classes_ids.add(id)

students_quantities_in_classes = dict()    
matriculate_dfs = []
matriculate_csv_names = [
                        'matriculas-2016.1.csv',
                        'matriculas-2016.2.csv',
                        'matriculas-2017.1.csv',
                        'matriculas-2017.2.csv',
                        'matriculas-2018.1.csv',
                        'matriculas-2018.2.csv',
                        'matriculas-2019.1.csv',
                        'matriculas-2019.2.csv',
                        'matriculas-2020.1.csv',
                        'matriculas-2020.2.csv',
                        'matriculas-2020.5.csv',
                        'matriculas-2020.6.csv',
                        'matriculas-2021.1.csv',
                        'matriculas-2021.2.csv'
                        ]

for name in matriculate_csv_names:
    matriculate_dfs.append(pd.read_csv(name,encoding='UTF-8',sep=';',usecols=['id_turma','discente']))    

for df in matriculate_dfs:
    filtered_df = df[df['id_turma'].isin(classes_ids)]
    for i in filtered_df.index:
        try:
            students_quantities_in_classes[filtered_df['discente'][i]] += 1
        except:
            students_quantities_in_classes[filtered_df['discente'][i]] = 1
     

plt.bar(students_quantities_in_classes.keys(),students_quantities_in_classes.values())
plt.title = "Reccorência dos possiveis alunos formados em 2021 nas turmas de fmc 1 e 2"
plt.show()

