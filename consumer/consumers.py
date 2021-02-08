#  The MIT License (MIT)
#
#  Copyright (c) 2021. Scott Lau
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
import json
import logging

from rocketmq.client import PushConsumer, ConsumeStatus
from scutils import Singleton

from consumer.exceptions import ConsumeException
from consumer.handlers import HandlerFactory
from consumer.utils import config


class ScConsumer(metaclass=Singleton):
    """RocketMQ message Consumer"""

    _consumer: PushConsumer = None
    _group_id: str = None
    _name_server_ip: str = None
    _port: int = None
    _topic: str = None

    def __init__(self):
        self._group_id = config.get("rocketmq.group_id")
        self._name_server_ip = config.get("rocketmq.name_server_ip")
        self._port = config.get("rocketmq.name_server_port")
        self._consumer = PushConsumer(self._group_id, orderly=True)
        self._consumer.set_name_server_address("{}:{}".format(self._name_server_ip, self._port))
        self._topic = config.get("rocketmq.msg_topic")

    def _callback(self, msg):
        msg_body = str(msg.body, 'UTF-8')
        logging.getLogger(__name__).info("consume message: id: %s, body: %s", msg.id, msg_body)
        msg_data = json.loads(msg_body)
        event_type = msg_data.get('event_type')
        event_name = msg_data.get('event_name')
        handler = HandlerFactory.get_handler(event_type, event_name)
        try:
            logging.getLogger(__name__).info("using handler: %s", type(handler))
            handler.handle(msg_data)
            return ConsumeStatus.CONSUME_SUCCESS
        except ConsumeException as e:
            logging.getLogger(__name__).exception("failed to handle message:%s, event type: %s, event name: %s", msg.id,
                                                  event_type, event_name, exc_info=e)
            return ConsumeStatus.RECONSUME_LATER

    def start(self):
        logging.getLogger(__name__).info("subscribe to topic: %s", self._topic)
        self._consumer.subscribe(self._topic, self._callback)
        logging.getLogger(__name__).info("connecting to %s:%s", self._name_server_ip, self._port)
        self._consumer.start()

    def shutdown(self):
        self._consumer.shutdown()
