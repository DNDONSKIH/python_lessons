from unittest import TestCase, main
from unittest.mock import Mock, patch, ANY

from vk_api.bot_longpoll import VkBotMessageEvent, VkBotEventType

from main import Bot
from _config import _RAW_EVENT


class TestBot(TestCase):

    def test_bot_start(self):
        count = 5
        obj = [{'a': 1}]
        events = [obj] * count

        long_poller_mock = Mock(return_value=events)
        long_poller_listen_mock = Mock()
        long_poller_listen_mock.listen = long_poller_mock

        with patch('main.vk_api.VkApi'), patch('main.VkBotLongPoll', return_value=long_poller_listen_mock):
            bot = Bot('', '')
            bot.on_event = Mock()
            bot.run()

            bot.on_event.assert_called()
            bot.on_event.assert_any_call(obj)
            assert bot.on_event.call_count == count

    def test_on_event(self):
        event = VkBotMessageEvent(raw=_RAW_EVENT)
        send_mock = Mock()

        with patch('main.vk_api.VkApi'), patch('main.VkBotLongPoll'):
            bot = Bot('', '')
            bot.api = Mock()
            bot.api.messages.send = send_mock
            bot.on_event(event)

        send_mock.assert_called_once_with(message=_RAW_EVENT['object']['message']['text'],
                                          random_id=ANY,
                                          peer_id=_RAW_EVENT['object']['message']['peer_id'])
