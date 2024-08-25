import os
import json
from telethon import TelegramClient
from telethon.tl.types import Channel
from .utils import nome_arquivo_seguro, salvar_json, carregar_json, criar_pasta_se_necessario
from datetime import datetime

class TelegramDownloader:
    def __init__(self, api_id, api_hash, session_name):
        self.client = TelegramClient(session_name, api_id, api_hash)
        self.contador = 10000  

    async def coletar_metadados(self, chat_id, target_topic_id=None):
        """Coleta metadados das mensagens de um chat e salva em um arquivo JSON."""
        try:
            chat_entity = await self.client.get_entity(chat_id)
            chat_titulo = chat_entity.title
            nome_seguro = nome_arquivo_seguro(chat_titulo)
            
            pasta_chat = os.path.join(os.getcwd(), nome_seguro)
            criar_pasta_se_necessario(pasta_chat)

            metadados = []

            async for msg in self.client.iter_messages(chat_id):
                if target_topic_id and msg.reply_to_msg_id != target_topic_id:
                    continue
                mensagem_info = {
                    'id': msg.id,
                    'data': msg.date.isoformat(),  
                    'remetente': msg.sender_id,
                    'texto': msg.message if msg.message else '',
                    'tem_midia': bool(msg.media),
                    'media_tipo': msg.media.document.mime_type if msg.media and msg.media.document else None,
                    'media_tamanho': msg.media.document.size if msg.media and msg.media.document else None
                }
                metadados.append(mensagem_info)

            salvar_json(metadados[::-1], f'metadados_{nome_seguro}.json')
            print(f'Metadados das mensagens do chat "{chat_titulo}" salvos com sucesso.')

            await self.baixar_todas_mensagens(chat_id, chat_titulo, pasta_chat, target_topic_id)
        
        except Exception as e:
            print(f"Erro ao coletar metadados do chat: {e}")

    async def baixar_todas_mensagens(self, chat_id, chat_titulo, pasta_chat, target_topic_id=None):
        """Baixa todas as mensagens do chat, verificando o plano de download para evitar downloads duplicados."""
        metadados = carregar_json(f'metadados_{nome_arquivo_seguro(chat_titulo)}.json')
        plano = carregar_json(f'plano_download_{nome_arquivo_seguro(chat_titulo)}.json')
        ids_baixados = {msg['id'] for msg in plano}

        print(f"Baixando mensagens do chat: {chat_id}. Total de metadados: {len(metadados)}")

        for msg in metadados:
            if msg['id'] not in ids_baixados:
                try:
                    mensagem_telegram = await self.client.get_messages(chat_id, ids=msg['id'])

                    if mensagem_telegram.media:
                        arquivo_path = await mensagem_telegram.download_media(file=pasta_chat)
                        nome_arquivo = f"{self.contador:05d} - {os.path.basename(arquivo_path)}"
                        os.rename(arquivo_path, os.path.join(pasta_chat, nome_arquivo))
                        print(f'Mídia baixada: {os.path.join(pasta_chat, nome_arquivo)}')
                    else:
                        if mensagem_telegram.message:
                            nome_arquivo = f"{self.contador:05d} - {nome_arquivo_seguro(chat_titulo)}.txt"
                            with open(os.path.join(pasta_chat, nome_arquivo), 'w', encoding='utf-8') as file:
                                file.write(mensagem_telegram.message)
                            print(f'Mensagem de texto salva: {os.path.join(pasta_chat, nome_arquivo)}')

                    plano.append(msg)
                    salvar_json(plano, f'plano_download_{nome_arquivo_seguro(chat_titulo)}.json')

                    self.contador += 1

                except Exception as e:
                    print(f"Erro ao baixar mensagem {msg['id']}: {e}")

    async def listar_chats(self):
        """Lista todos os chats e salva IDs em um arquivo txt."""
        dialogs = await self.client.get_dialogs()
        with open('listagem_chats.txt', 'w') as file:
            for dialog in dialogs:
                if dialog.is_group or dialog.is_channel:
                    chat_id = dialog.entity.id
                    chat_name = dialog.name
                    file.write(f"Chat: {chat_name} (ID: {chat_id})\n")
                    print(f"Chat: {chat_name} (ID: {chat_id})")

    async def verificar_chat_forum(self, chat_id):
        """Verifica se o chat é um fórum e solicita o ID do tópico, se necessário."""
        try:
            entity = await self.client.get_entity(chat_id)
            if isinstance(entity, Channel) and entity.forum:
                topic_id = int(input(f"{entity.title} é um fórum. Digite o ID do tópico de origem: "))
                return entity.title, topic_id
            else:
                return entity.title, None
        except Exception as e:
            print(f"Erro ao obter informações do chat: {e}")
            return None, None
