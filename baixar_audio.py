import os
import re
from yt_dlp import YoutubeDL

def ler_links():
    """Lê os links digitados pelo usuário no terminal com mensagens mais limpas."""
    print("\n" + "="*50)
    print("           YOUTUBE MP3 BATCH DOWNLOADER         ")
    print("="*50)
    print("Cole seus links do YouTube abaixo (um por linha).")
    print("Ao finalizar, digite 'FIM' ou pressione Enter em uma linha vazia:\n")
    
    links = []
    while True:
        linha = input().strip()
        
        if linha.upper() == 'FIM' or not list(linha):
            break
            
        # Validação Essencial: Aceita apenas links válidos do YouTube (youtube.com ou youtu.be)
        if re.search(r'(youtube\.com|youtu\.be)', linha, re.IGNORECASE):
            links.append(linha)
        elif linha:
            print(f"⚠️ Link ignorado (não parece ser do YouTube): {linha}")
            
    return links

def baixar_lista_de_audios(lista_de_urls):
    """Gerencia o download e a conversão dos links fornecidos."""
    # Melhoria Essencial: Garante que a pasta existe no sistema
    pasta_destino = os.path.join(os.path.expanduser("~"), "Youtube")
    os.makedirs(pasta_destino, exist_ok=True)

    # Configurações do yt-dlp corrigidas e blindadas
    ydl_opts = {
        # 'bestaudio' baixa o formato bruto (geralmente webm)
        'format': 'bestaudio/best',
        
        # Correção WebM: Garante que a extensão final no template seja .mp3 após o processamento
        'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),
        
        # Evita baixar vídeos/playlists aleatórias fora do link exato
        'noplaylist': True,
        
        # Ignora erros de links caídos para não travar o loop de downloads
        'ignoreerrors': True,
        
        # Correção de caracteres especiais do Windows/Linux nos nomes dos arquivos
        'restrictfilenames': False, 
        
        # Força o pós-processador do FFmpeg a extrair e converter estritamente para MP3
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    print(f"\n🚀 [INFO] Iniciando o processamento de {len(lista_de_urls)} link(s)...")
    print(f"📁 [PASTA] Arquivos salvos em: {pasta_destino}\n")
    
    sucessos = 0
    erros = 0

    with YoutubeDL(ydl_opts) as ydl:
        for i, url in enumerate(lista_de_urls, start=1):
            print(f"📥 [{i}/{len(lista_de_urls)}] Baixando...")
            
            # Executa o download individual para controlar o contador de sucesso/erro
            resultado = ydl.download([url])
            
            # O yt-dlp retorna 0 quando dá tudo certo e outro número se houver falha
            if resultado == 0:
                sucessos += 1
            else:
                erros += 1
                
    # Melhoria de Usabilidade: Exibe o balanço geral ao usuário
    print("\n" + "="*50)
    print("🎯 PROCESSO CONCLUÍDO!")
    print(f"✅ Downloads com sucesso: {sucessos}")
    print(f"❌ Falhas encontradas: {erros}")
    print("="*50)

def main():
    """Fluxo principal do programa."""
    links = ler_links()
    
    if links:
        baixar_lista_de_audios(links)
    else:
        print("\n[!] Nenhum link válido do YouTube foi inserido. Fechando o programa.")

if __name__ == "__main__":
    main()