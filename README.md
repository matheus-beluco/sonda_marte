# Explorando Marte
Um programa para pousar e movimentar sondas em marte.

## Como faço para rodar o programa?
- Faça dowload do arquivo **[gui.exe](./dist/gui.exe)**.

## Como instalar e rodar os testes?
**Atenção**: O guia de instalação é certificado apenas para o sistema operacional Ubuntu 20.04LTS.
1. Clone **[este repositório](https://github.com/matheus-beluco/sonda_marte)**
2. Crie um ambiente virtual
```
python -m venv venv
```
3. Entre no ambiente virtual
```
source venv/bin/activate
```
4. Instale as dependências do projeto
```
pip install -r requirements.txt
```
5. Rode os testes
```
pytest -ssv
```


## Descrição
A descrição do exercício está no arquivo **[explorando_marte.pdf](./explorando_marte.pdf)**.

**Atenção**: Os valores negativos não foram tratados, pois em um plano cartesiano o X e Y podem assumir valores negativos.