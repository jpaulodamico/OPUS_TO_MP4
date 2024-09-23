# Conversor de `.opus` para `.mp4` em Lote

![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue)
![FFmpeg](https://img.shields.io/badge/FFmpeg-4.0%2B-red)
![License](https://img.shields.io/badge/License-MIT-green)

## 📄 Descrição

Este projeto consiste em um script Python que permite a conversão em lote de arquivos de áudio no formato `.opus` para o formato `.mp4` utilizando o `FFmpeg`. É ideal para quem precisa converter múltiplos arquivos de áudio de maneira rápida e eficiente, mantendo a qualidade e facilitando a compatibilidade com diversos players e dispositivos.

## 🚀 Funcionalidades

- **Conversão em Lote**: Converte todos os arquivos `.opus` em um diretório especificado para `.mp4`.
- **Simplicidade**: Uso fácil através da linha de comando.
- **Configuração Personalizável**: Permite ajustar parâmetros como codec de áudio e taxa de bits.
- **Tratamento de Erros**: Informa ao usuário sobre quaisquer problemas durante a conversão.

## 🛠️ Pré-requisitos

Antes de utilizar o script, certifique-se de que os seguintes componentes estão instalados no seu sistema:

1. **Python 3.6 ou Superior**:
   - **Verificar Instalação**:
     ```bash
     python --version
     ```
   - **Instalar Python**: [Download Python](https://www.python.org/downloads/)

2. **FFmpeg 4.0 ou Superior**:
   - **Instalação no Windows**:
     - Baixe o FFmpeg no [site oficial](https://ffmpeg.org/download.html).
     - Extraia os arquivos e adicione o diretório `bin` ao PATH do sistema.
   - **Instalação no macOS**:
     ```bash
     brew install ffmpeg
     ```
   - **Instalação no Linux (Ubuntu)**:
     ```bash
     sudo apt update
     sudo apt install ffmpeg
     ```

3. **Pacotes Python Necessários**:
   - O script utiliza módulos padrão, mas é recomendável criar um ambiente virtual:
     ```bash
     python -m venv venv
     source venv/bin/activate  # Para Linux/macOS
     venv\Scripts\activate     # Para Windows
     ```

## 📦 Instalação

1. **Clonar o Repositório**:
   ```bash
   git clone https://github.com/seu-usuario/conversor-opus-para-mp4.git
   ```

2. **Navegar para o Diretório do Projeto**:
   ```bash
   cd conversor-opus-para-mp4
   ```

3. **(Opcional) Criar e Ativar um Ambiente Virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/macOS
   venv\Scripts\activate     # Para Windows
   ```

4. **Instalar Dependências**:
   - Não há dependências externas além do FFmpeg e Python padrão.

## 📝 Como Usar

1. **Preparar os Arquivos**:
   - Coloque todos os arquivos `.opus` que deseja converter em um único diretório.

2. **Executar o Script**:
   - **Converter no Diretório Atual**:
     ```bash
     python converter_opus_para_mp4.py
     ```
   - **Converter em um Diretório Específico**:
     ```bash
     python converter_opus_para_mp4.py /caminho/para/seu/diretorio
     ```

   - **Exemplos**:
     ```bash
     # No diretório atual
     python converter_opus_para_mp4.py

     # Especificando um diretório
     python converter_opus_para_mp4.py /home/usuario/musicas_opus
     ```

3. **Resultados**:
   - Os arquivos convertidos `.mp4` serão salvos no mesmo diretório dos arquivos `.opus` originais, mantendo o mesmo nome de arquivo.

## ⚙️ Explicação do Script

- **Importações**:
  - `os`, `subprocess`, e `pathlib.Path` são utilizados para manipular caminhos de arquivos e executar comandos do sistema.

- **Função `converter_opus_para_mp4`**:
  - Verifica se o diretório fornecido existe.
  - Lista todos os arquivos com extensão `.opus`.
  - Para cada arquivo `.opus`, cria um arquivo `.mp4` correspondente.
  - Utiliza o `ffmpeg` para realizar a conversão, especificando o codec de áudio `aac` e uma taxa de bits de `192k`.
  - Trata e exibe erros caso ocorram durante a conversão.

- **Bloco `__main__`**:
  - Utiliza o módulo `argparse` para permitir que o usuário especifique o diretório via linha de comando.
  - Se nenhum diretório for especificado, o script usa o diretório atual.

## 🧩 Personalização

- **Codec de Áudio**:
  - O script utiliza `aac` por padrão, mas pode ser alterado ajustando o parâmetro `-c:a` no comando `ffmpeg`.

- **Taxa de Bits do Áudio**:
  - A taxa de bits está definida para `192k`. Você pode ajustar isso alterando o valor de `-b:a` conforme necessário.

- **Adicionar Vídeo ou Imagem de Fundo**:
  - Atualmente, o script converte apenas o áudio e coloca no contêiner `.mp4` sem conteúdo de vídeo. Para adicionar um vídeo ou uma imagem, o script precisará ser modificado para incluir esses elementos.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Se você deseja contribuir, por favor, siga os passos abaixo:

1. **Fork este Repositório**
2. **Crie uma Branch para sua Feature ou Correção de Bug**:
   ```bash
   git checkout -b feature/nova-feature
   ```
3. **Faça Commit das suas Alterações**:
   ```bash
   git commit -m "Adiciona nova feature"
   ```
4. **Faça Push para a Branch**:
   ```bash
   git push origin feature/nova-feature
   ```
5. **Abra um Pull Request**

## 📞 Contato

Para quaisquer dúvidas ou sugestões, sinta-se à vontade para abrir uma [Issue](https://github.com/seu-usuario/conversor-opus-para-mp4/issues) ou entrar em contato diretamente.

---

**Nota**: Substitua `https://github.com/seu-usuario/conversor-opus-para-mp4.git` pelo URL real do seu repositório e atualize as seções de contato conforme necessário.
