#LEMBRAR DE EXECUTAR ESTE SCRIPT DENTRO DA PASTA ONDE ESTÃO OS ARQUIVOS A SEREM TRANSFORMADOS!!!!!
#LEMBRAR DE EXECUTAR ESTE SCRIPT DENTRO DA PASTA ONDE ESTÃO OS ARQUIVOS A SEREM TRANSFORMADOS!!!!!
#LEMBRAR DE EXECUTAR ESTE SCRIPT DENTRO DA PASTA ONDE ESTÃO OS ARQUIVOS A SEREM TRANSFORMADOS!!!!!
#LEMBRAR DE EXECUTAR ESTE SCRIPT DENTRO DA PASTA ONDE ESTÃO OS ARQUIVOS A SEREM TRANSFORMADOS!!!!!
#LEMBRAR DE EXECUTAR ESTE SCRIPT DENTRO DA PASTA ONDE ESTÃO OS ARQUIVOS A SEREM TRANSFORMADOS!!!!!



import os
import subprocess
from pathlib import Path

diretorio = "C:\\Users\\JPDSVerdade\\Downloads\\WhatsApp Chat - M Caravieri"

def converter_opus_para_mp4(diretorio):
    """
    Converte todos os arquivos .opus no diretório especificado para .mp4.
    
    Args:
        diretorio (str): Caminho para o diretório contendo os arquivos .opus.
    """
     
    # Verifica se o diretório existe
    path = Path(diretorio)
    if not path.is_dir():
        print(f"O diretório {diretorio} não existe.")
        return
    
    # Lista todos os arquivos .opus no diretório
    arquivos_opus = list(path.glob("*.opus"))
    
    if not arquivos_opus:
        print("Nenhum arquivo .opus encontrado no diretório.")
        return
    
    # Percorre cada arquivo .opus e converte para .mp4
    for arquivo_opus in arquivos_opus:
        arquivo_mp4 = arquivo_opus.with_suffix('.mp4')
        comando = [
            'ffmpeg',
            '-i', str(arquivo_opus),
            '-c:a', 'aac',  # Codec de áudio para MP4
            '-b:a', '192k',  # Taxa de bits de áudio
            str(arquivo_mp4)
        ]
        
        print(f"Convertendo {arquivo_opus.name} para {arquivo_mp4.name}...")
        
        try:
            # Executa o comando ffmpeg
            subprocess.run(comando, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Conversão concluída: {arquivo_mp4.name}")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao converter {arquivo_opus.name}: {e.stderr.decode('utf-8')}")
    
    print("Todas as conversões foram concluídas.")

if __name__ == "__main__":
    import argparse

    # Configura o parser de argumentos
    parser = argparse.ArgumentParser(description="Converter arquivos .opus para .mp4 em lote.")
    parser.add_argument(
        'diretorio',
        nargs='?',
        default='.',
        help='Diretório contendo os arquivos .opus. Padrão é o diretório atual.'
    )
    
    args = parser.parse_args()
    
    converter_opus_para_mp4(args.diretorio)
