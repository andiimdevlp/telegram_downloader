import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from telegram_downloader.downloader import TelegramDownloader
from telegram_downloader.config import API_ID, API_HASH, SESSION_NAME

async def main():
    downloader = TelegramDownloader(API_ID, API_HASH, SESSION_NAME)
    await downloader.client.start()

    await downloader.listar_chats()

    chat_id = input("Digite o ID do chat que deseja baixar: ")
    if chat_id.isdigit():
        chat_id = int(chat_id)

    chat_titulo, target_topic_id = await downloader.verificar_chat_forum(chat_id)

    if chat_titulo:
        await downloader.coletar_metadados(chat_id, target_topic_id)

    print("Processo de coleta de metadados concluído.")

if __name__ == '__main__':
    asyncio.run(main())
