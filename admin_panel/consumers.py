from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class AdminPanelConsumer(WebsocketConsumer):
    def connect(self):
        """Подключение"""
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"admin_panel_{self.room_name}"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, code):
        """Отключение"""
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        """Принять данные"""
        # text_data =

    def chat_message(self, event):
        """Отправить данные"""
