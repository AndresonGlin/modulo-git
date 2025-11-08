"""
Desafio Módulo Git

Neste arquivo você encontrará funções **incompletas** que representam
tarefas relacionadas ao aprendizado de Git e GitHub.

Seu objetivo é:
- Criar uma issue para cada função.
- Implementar a função em uma branch específica.
- Fazer commit, criar tag e abrir Pull Request.
- Repetir o processo até concluir todas as funções.

Boa sorte e bons commits! 🚀
"""

def mostrar_mensagem_inicial():
    """
    Exibe uma mensagem de boas-vindas ao desafio.
    Retorno esperado: string com a mensagem "Bem-vindo ao Desafio de Git!"
    """
    return f"Bem-vindo ao Desafio de Git!"

def listar_comandos_git_basicos():
    """
    Retorna uma lista com os principais comandos básicos do Git.
    Exemplo de saída:
    ["git init", "git add", "git commit", "git status", "git push"]
    """
    comandos = [
        "git init",     # Inicia um novo repositório
        "git clone",    # Baixa um repositório existente
        "git add",      # Adiciona arquivos ao staging area
        "git commit",   # Confirma as mudanças
        "git status",   # Vê o estado do repositório
        "git push",     # Envia mudanças para o repositório remoto
        "git pull"      # Baixa e integra mudanças do repositório remoto
    ]
    return comandos

def criar_mensagem_commit(funcao_nome):
    """
    Recebe o nome de uma função e retorna uma mensagem de commit padronizada.
    Exemplo:
    criar_mensagem_commit("listar_comandos_git_basicos") ->
    "Implementa função listar_comandos_git_basicos"
    """
    pass


def verificar_tag_valida(tag):
    """
    Verifica se uma tag está no formato 'vX.Y' (ex: v1.0, v2.1).
    Retorna True se o formato for válido, caso contrário False.
    """
    pass


def gerar_relatorio_final(funcoes_concluidas):
    """
    Recebe uma lista com os nomes das funções implementadas
    e retorna uma mensagem final do desafio.

    Exemplo:
    gerar_relatorio_final(["mostrar_mensagem_inicial", "listar_comandos_git_basicos"])
    ->
    "Desafio concluído! 2 funções implementadas com sucesso."
    """
    pass


def main():
    """
    Função principal para executar e exibir o resultado das funções.
    """
    # Exibe a mensagem inicial
    mensagem = mostrar_mensagem_inicial()
    print("---1# Mensagem ---")
    print(mensagem)
    
    # Exibe a lista de comandos
    comandos = listar_comandos_git_basicos()
    print("\n---2# Comandos Git Básicos ---")
    
    if comandos:
        for i, comando in enumerate(comandos, 1):
            print(f"{i}. {comando}")
    else:
        print("Nenhum comando foi listado.")    

if __name__ == "__main__":
    main()