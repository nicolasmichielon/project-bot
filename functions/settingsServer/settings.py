import os
import pymongo


def setPrefix(ctx):
    mongo = pymongo.MongoClient(os.getenv('DATABASE'))
    db = mongo.serverSettigs

    default_prefix = '?'
    server_id = str(ctx.guild.id)
    # Verifica se já existe um registro para o prefixo padrão
    existing_data = db[''].find_one({'prefixo': {'$exists': True}})
    if not existing_data:
        db['default_settings'].insert_one({
            'prefixo': default_prefix,
        })



def get_prefix(ctx):
    try:
        mongo = pymongo.MongoClient(os.getenv('DATABASE'))
        db = mongo.serverSettigs

        collection_name = f'{ctx.guild.id}'

        clan_data = db[collection_name].find_one({'prefixo': {'$exists': True}})
        if clan_data:
            return clan_data['prefixo']
        else:
            return '?'  # Prefixo padrão caso não esteja configurado

    except Exception as e:
        return '?'

def set_default_prefix():
    try:
        mongo = pymongo.MongoClient(os.getenv('DATABASE'))
        db = mongo.serverSettigs
        default_prefix = '?'

        # Verifica se já existe um registro para o prefixo padrão
        existing_data = db['default_settings'].find_one({'prefixo': {'$exists': True}})
        if not existing_data:
            db['default_settings'].insert_one({
                'prefixo': default_prefix,
            })

    except Exception as e:
        pass  # Lida com erros de maneira apropriada
