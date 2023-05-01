import discord


def ajuda(mensagem):
    mensagem = ("?clear -> Apaga X mensagens do chat\n" +
                "?forecast -> Ver o clima nos próximos 5 dias\n"+
                "?joke -> Conta uma piada\n" +
                "?news -> Pesquisar uma notícia\n" +
                "?roll -> Rola um dado até X valor limite\n"+
                "?forecast -> Ver o clima nos próximos 5 dias\n" +
                "?weather -> Ver o clima agora\n" +
                "?coinflip -> Cara ou coroa"
                )
    embed = discord.Embed(title="Comandos", description= mensagem)
    return embed