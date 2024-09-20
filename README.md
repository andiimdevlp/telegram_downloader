# Telegram Downloader

Este projeto permite baixar mensagens de chats do Telegram, incluindo mídias, arquivos e textos, organizando-os em pastas. Ele também suporta a coleta de metadados das mensagens.

## Ferramentas e Bibliotecas

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)


* [VSCode](https://code.visualstudio.com/download) - Editor de Código
* [Python](https://www.python.org/downloads/) - Instalador do Python
* [telethon 1.24.0](https://pypi.org/project/Telethon/) - Biblioteca
* [Git](https://git-scm.com/downloads) - Gerenciador de Versões

## Estrutura do Projeto

- `telegram_downloader/`: Diretório principal com o código fonte.
  - `config.py`: Configurações de API e sessão.
  - `downloader.py`: Funções principais para baixar mensagens e mídias.
  - `utils.py`: Funções utilitárias para manipulação de arquivos.
  - `main.py`: Script principal para executar o projeto.
- `requirements.txt`: Dependências do projeto.
- `README.md`: Documentação do projeto.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/andiimdevlp/telegram-downloader.git
   cd telegram-downloader
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   ```

Ative o ambiente virtual:

   ```bash
   # No Linux/MacOS:
   source venv/bin/activate

   # No Windows:
   venv\Scripts\activate
  ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure suas credenciais do Telegram:
 - Abra o arquivo telegram_downloader/config.py.
 - Insira seu `API_ID` e `API_HASH`, obtidos no [My Telegram](https://my.telegram.org/auth).

## Uso
1. Inicie o script principal:
  
  ```bash
   python -m telegram_downloader.main
  ```
2. Após iniciar o script, todos os chats serão listados e salvos no arquivo `listagem_chats.txt`. Use essa listagem para escolher o ID do chat que deseja baixar.

3. Digite o `chat_id` desejado quando solicitado.

  - Se o chat for um fórum, você será solicitado a inserir o ID do tópico específico para baixar as mensagens.
4. O script coletará os metadados e fará o download das mensagens do chat.

## Estrutura de Pastas

As mensagens e mídias baixadas serão organizadas em uma pasta que utiliza o nome do chat como base. Dentro dessa pasta, arquivos de texto e mídias estarão nomeados de acordo com o ID da mensagem para garantir unicidade.

## Exemplo de Estrutura de Pastas

  ```bash
  telegram_downloader/
  │
  ├── metadados_Plataforma_Cafeina.json
  ├── plano_download_Plataforma_Cafeina.json
  ├── Plataforma_Cafeina/
  │   ├── Plataforma_Cafeina_mensagens_texto.json
  │   ├── 123457_imagem.jpg
  │   └── 123458_video.mp4
  └── listagem_chats.txt
  ```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

  1. Fork o repositório.
  2. Crie sua branch (git checkout -b minha-branch).
  3. Commit suas mudanças (git commit -am 'Minha nova funcionalidade').
  4. Envie para o branch (git push origin minha-branch).
  5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](https://choosealicense.com/licenses/mit/) para mais detalhes.

 
