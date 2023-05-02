import discord


def ajuda(mensagem):
    mensagem = ("***?clear*** -> Apaga X mensagens do chat\n" +
                "***?coinflip***-> Cara ou coroa\n"+
                "***?dollar*** -> Ver o valor do dólar hoje\n" +
                "***?forecast*** -> Ver o clima nos próximos 5 dias\n"+
                "***?gif*** -> Procure um gif\n" +
                "***?hug*** -> De um abraço no seu amigo\n" +
                "***?joke*** -> Conta uma piada\n" +
                "***?kiss*** -> De um beijo no seu amigo\n" +
                "***?laugh*** -> Ri\n" +
                "***?news*** -> Pesquisar uma notícia\n" +
                "***?pokemon*** -> Gerar um Pokémon aleatório\n"+
                "***?punch*** -> De um soco no seu amigo\n" +
                "***?roll*** -> Rola um dado até X valor limite\n"+
                "***?slap*** -> De um tapa no seu amigo\n" +
                "***?weather*** -> Ver o clima agora")
    embed = discord.Embed(title="Comandos", description= mensagem)
    return embed