import logging

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

try:
    from _config import TOKEN, GROUP_ID
except ImportError:
    exit('Add config file')

def log_settings(log):
    file_formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s: %(message)s', datefmt='%m-%d-%Y %H:%M:%S')
    file_handler = logging.FileHandler(filename='bot.log', encoding='utf8', delay=True)
    file_handler.setLevel(level=logging.WARNING)
    file_handler.setFormatter(file_formatter)

    stream_formatter = logging.Formatter(fmt='%(levelname)s: %(message)s', datefmt='%m-%d-%Y %H:%M:%S')
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level=logging.INFO)
    stream_handler.setFormatter(stream_formatter)

    log.setLevel(logging.DEBUG)
    log.addHandler(file_handler)
    log.addHandler(stream_handler)


class Bot:
    def __init__(self, group_id, token):
        self.log = logging.getLogger('bot')
        log_settings(self.log)
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=token)
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception as err:
                self.log.exception(f'ошибка {err}')

    def on_event(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            peer_id = event.object['message']['peer_id']
            text = event.object['message']['text']
            self.api.messages.send(message=text, random_id=get_random_id(), peer_id=peer_id)
            self.log.info('Бот получил сообщение %s', text)
        else:
            self.log.warning('мы пока не умеем обрабатывать событие такого типа %s', event.type)


if __name__ == '__main__':
    bot = Bot(group_id=GROUP_ID, token=TOKEN)
    bot.run()
