import os
from yt_dlp import YoutubeDL

def baixar_lista_de_audios(lista_de_urls):
    pasta_destino = os.path.join(os.path.expanduser("~"), "Youtube")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ignoreerrors': True, # Se um link der erro, ele pula pro próximo da lista sem travar
    }

    print(f"\n[+] Iniciando o download em lote de {len(lista_de_urls)} vídeos...")
    
    with YoutubeDL(ydl_opts) as ydl:
        # O yt-dlp aceita uma lista de links nativamente!
        ydl.download(lista_de_urls)
        
    print("\n[✓] Todos os downloads da lista foram processados!")

if __name__ == "__main__":
    print("=== DOWNLOADER EM LOTE (10 ou + LINKS) ===")
    print("Cole todos os seus links abaixo (um por linha).")
    print("Quando terminar de colar todos, digite 'FIM' ou dê Enter em uma linha vazia para começar:\n")
    
    links = []
    while True:
        linha = input().strip()
        
        # Condição para parar de receber links
        if linha.upper() == 'FIM' or not linha:
            break
            
        # Adiciona o link na lista (ignora linhas que não começam com http)
        if linha.startswith("http"):
            links.append(linha)
    
    # Se o usuário colou links, manda pra função de download
    if links:
        baixar_lista_de_audios(links)
    else:
        print("Nenhum link válido foi inserido.")