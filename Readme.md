# Escritório do Prossan

Uma aplicação para gerenciar registros de alunos, voluntários e qualquer outra informação conveniente.

<img src="./assets/images/sample.png" alt="Texto alternativo da imagem" width="600">


## Propósito

Atualmente, os registros são armazenados em documentos físicos, e a ideia deste projeto é facilitar o gerenciamento por meio de uma interface gráfica amigável.

## Tecnologias

- Interface Gráfica: Tkinter
- Banco de Dados: TinyDB

## Instalação

Siga as etapas abaixo para instalar:

1. Primeiramente, certifique-se de ter Python 3 instalado em seu sistema.

2. Instale as dependências do projeto executando o seguinte comando no terminal:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

## Execução   
Execute o programa usando o seguinte comando:

   ```bash
   python3 main.py
   ```

## To-Do

- [x] CRUD Crianças.
- [x] CRUD Adultos.
- [ ] CRUD Voluntários.
- [x] PDF Crianças.
- [x] PDF Adultos.
- [ ] PDF Voluntáios.
- [x] Exportar Crianças.
- [x] Exportar Adultos.
- [ ] Exportar Voluntáios.
- [x] Pesquisar Crianças.
- [x] Pesquisar Adultos.
- [ ] Pesquisar Voluntáios.

## Pyinstaller.

windows
```bash
pyinstaller --add-data "assets;assets" --icon="assets/images/logo.ico" --hidden-import='PIL._tkinter_finder' --noconsole main.py
```

linux
```bash
pyinstaller --add-data "assets:assets" --icon="assets/images/logo.ico" --hidden-import='PIL._tkinter_finder' --noconsole main.py
```

## Contribuições

Contribuições são bem-vindas! Se você quiser contribuir para o projeto, sinta-se à vontade para abrir 
uma issue ou enviar um pull request.
