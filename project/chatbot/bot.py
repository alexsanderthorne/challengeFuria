def get_bot_response(message):
    message = message.lower()
    if "furia" in message:
        return "A FURIA é uma das maiores organizações de esports do Brasil!"
    elif "jogo" in message:
        return "O próximo jogo será anunciado em breve no calendário oficial."
    else:
        return "Sou a Pantera! Pergunte sobre o time, jogos ou curiosidades."
