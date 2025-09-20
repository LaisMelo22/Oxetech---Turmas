import random
import sqlite3

# Conexão com banco de dados
conn = sqlite3.connect("chatbot_conversa.db")
cursor = conn.cursor()

# Criação de tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS mensagens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT,
    texto TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

# Função para salvar mensagens
def salvar_mensagem(usuario, texto):
    cursor.execute("INSERT INTO mensagens (usuario, texto) VALUES (?, ?)", (usuario, texto))
    conn.commit()

# Regras de diálogo
def resposta_regras(msg):
    msg = msg.lower()

    # Saudações
    if any(palavra in msg for palavra in ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"]):
        return random.choice([
            "Oi! Como você está hoje?",
            "Olá, tudo bem?",
            "Oi, prazer falar com você!"
            
        ])

    # Perguntar como vai
    elif "como você está" in msg or "tudo bem" in msg:
        return random.choice([
            "Estou bem, obrigado por perguntar! E você?",
            "Estou ótimo e você, como está?",
            "Melhor agora conversando com você!"
            "Como você tá, diva?"
        ])

    # Perguntar nome
    elif "qual seu nome" in msg or "quem é você" in msg:
        return "Sou um chatbot que aprende um pouquinho a cada conversa! Pode me chamar de Mini-GPT"

    # Perguntar sobre Python
    elif "python" in msg:
        return "Python é uma das minhas linguagens favoritas! Você também programa em Python?"

    # Despedida
    elif any(palavra in msg for palavra in ["tchau", "até logo", "até mais"]):
        return random.choice([
            "Até logo! Foi bom conversar com você ",
            "Tchau! Espero falarmos de novo.",
            "Até mais, se cuida!"
        ])

    # Caso não saiba
    else:
        return None

# Função para conversa
def chat():
    print("Chatbot Conversacional (digite 'sair' para encerrar)")
    
    while True:
        user = input("Você: ")
        if user.lower() in ["sair", "exit", "quit"]:
            print("Bot: Até a próxima!")
            break

        salvar_mensagem("user", user)

        resposta = resposta_regras(user)

        if not resposta:
            resposta = random.choice([
                "Interessante, me conta mais!",
                "Não tenho certeza sobre isso, mas quero aprender.",
                "Legal! Pode explicar melhor?",
                "Hum... isso é novo pra mim. O que você acha?",
                "Tem que me treinar mais"
            ])

        print("Bot:", resposta)
        salvar_mensagem("bot", resposta)

# Executar
if __name__ == "__main__":
    chat()
    conn.close()
