# 🎵 YouTube MP3 Batch Downloader

![Python](https://img.shields.io/badge/Python-3.13-blue)
![yt-dlp](https://img.shields.io/badge/yt--dlp-Latest-red)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Required-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Baixe e converta vídeos do YouTube para **MP3** de forma simples e rápida utilizando **Python**, **yt-dlp** e **FFmpeg**.

Este projeto permite colar **quantos links desejar** e realizar o download automaticamente, convertendo todos os arquivos para **MP3 (192 kbps)** e salvando-os na pasta **Youtube** do usuário.

---

## ✨ Recursos

* ✅ Download de múltiplos vídeos simultaneamente
* ✅ Conversão automática para MP3
* ✅ Qualidade de áudio em **192 kbps**
* ✅ Ignora links inválidos sem interromper o processo
* ✅ Interface simples via terminal
* ✅ Salva automaticamente os arquivos na pasta **~/Youtube**

---

## 🛠 Tecnologias

* Python 3
* yt-dlp
* FFmpeg

---

# 📋 Pré-requisitos

Antes de executar o projeto, instale:

### Python 3

Verifique se está instalado:

```bash
python --version
```

ou

```bash
python3 --version
```

---

### Instalar o yt-dlp

```bash
pip install yt-dlp
```

---

### Instalar o FFmpeg

O FFmpeg precisa estar instalado e disponível no **PATH** do sistema.

#### Windows

1. Baixe o FFmpeg.
2. Extraia os arquivos.
3. Adicione a pasta **bin** às variáveis de ambiente (PATH).

Verifique a instalação:

```bash
ffmpeg -version
```

#### Linux

```bash
sudo apt install ffmpeg
```

#### macOS

```bash
brew install ffmpeg
```

---

# 🚀 Como usar

Execute o script:

```bash
python downloader.py
```

ou

```bash
python3 downloader.py
```

O programa solicitará que você cole os links.

Exemplo:

```
https://www.youtube.com/watch?v=xxxxx
https://www.youtube.com/watch?v=yyyyy
https://www.youtube.com/watch?v=zzzzz

FIM
```

Também é possível apenas pressionar **Enter** em uma linha vazia para iniciar o download.

---

# 📂 Resultado

Após a conclusão, todos os arquivos serão salvos automaticamente em:

```
~/Youtube
```

No Windows normalmente será:

```
C:\Users\SeuUsuario\Youtube
```

---

# 📦 Estrutura do projeto

```
YouTube-MP3-Downloader
│
├── downloader.py
└── README.md
```

---

# ⚙️ Como funciona

O script:

1. Recebe uma lista de URLs do YouTube.
2. Faz o download do melhor áudio disponível.
3. Utiliza o FFmpeg para converter automaticamente para MP3.
4. Salva todos os arquivos na pasta **Youtube**.
5. Caso algum link apresente erro, o processo continua normalmente com os demais.

---

# 💡 Exemplo

```
=== DOWNLOADER EM LOTE ===

Cole os links abaixo:

https://youtu.be/xxxxx
https://youtu.be/yyyyy
https://youtu.be/zzzzz

FIM

[+] Iniciando o download...

...

[✓] Todos os downloads da lista foram processados!
```

---

# ❗ Observações

* O projeto realiza apenas o download do áudio.
* O nome do arquivo é definido automaticamente pelo título do vídeo.
* É necessário possuir conexão com a internet.
* Alguns vídeos podem não estar disponíveis devido a restrições do YouTube.

---

# 🤝 Contribuições

Contribuições são bem-vindas!

Caso encontre algum problema ou tenha uma sugestão de melhoria, fique à vontade para abrir uma *Issue* ou enviar um *Pull Request*.

---

# 📄 Licença

Este projeto é disponibilizado apenas para fins educacionais e de uso pessoal.

Respeite sempre os direitos autorais e os Termos de Serviço do YouTube ao realizar downloads de conteúdo.
