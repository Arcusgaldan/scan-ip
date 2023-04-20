## Ping Check

O Ping Check é um programa em Python que executa interminavelmente, pingando todos os hosts das redes informadas (de maneira rígida no código) e pegando seus nomes. Essas informações são salvas em Dataframes do Pandas, e toda vez que o scan termina, esses dataframes são salvos em .xlsx. Quando um conflito é detectado (ou seja, um IP que era de um hostname passa a estar com outro hostname), ele cria um registro no dataframe de conflitos (que também é salvo em .xlsx) e futuramente terá a opção de notificar via e-mail.

### Funcionalidades

- Pinga todos os hosts das redes informadas;
- Salva as informações em Dataframes do Pandas;
- Salva os dataframes em arquivos .xlsx;
- Detecta conflitos de IP e cria registros em um dataframe de conflitos (também salvo em .xlsx);
- Futuramente terá a opção de notificar via e-mail.

### Requisitos

- Python 3.x;
- Pandas.

### Como usar

1. Clone o repositório;
2. Instale os requisitos com `pip install -r requirements.txt`;
3. Execute o programa com `python ping_check.py`.

### Badges

Este programa é 100% em Python:

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)
