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
import logging


class Handler(object):
    """The root handler"""

    def handle(self, data):
        return True


class BaseHandler(Handler):
    """Base handler for decorating use"""

    _handler: Handler = None

    def __init__(self, handler: Handler = None) -> None:
        self._handler = handler

    @property
    def handler(self):
        return self._handler

    def handle(self, data):
        if self._handler:
            return self._handler.handle(data)
        return True


class NoOpHandler(Handler):
    """No Operation handler

    """

    def handle(self, data):
        return True


class UnknownOpHandler(Handler):
    """Unknown Operation handler

    """

    def handle(self, data):
        event_type = data.get('event_type')
        event_name = data.get('event_name')
        logging.getLogger(__name__).error("Unknown event, type: %s, name: %s", event_type, event_name)
        return False


class UserCreateHandler(BaseHandler):
    """A handler for creating user

    """

    def handle(self, data):
        result = BaseHandler.handle(self, data)
        if not result:
            return False
        event_name = data.get('event_name')
        logging.getLogger(__name__).info("Handling event: %s", event_name)
        return True


class UserDestroyHandler(BaseHandler):
    """A handler for destroying user

    """

    def handle(self, data):
        result = BaseHandler.handle(self, data)
        if not result:
            return False
        event_name = data.get('event_name')
        logging.getLogger(__name__).info("Handling event: %s", event_name)
        return True


class GroupCreateHandler(BaseHandler):
    """A handler for creating group

    """

    def handle(self, data):
        result = BaseHandler.handle(self, data)
        if not result:
            return False
        event_name = data.get('event_name')
        logging.getLogger(__name__).info("Handling event: %s", event_name)
        return True


class GroupRenameHandler(BaseHandler):
    """A handler for renaming group

    """

    def handle(self, data):
        result = BaseHandler.handle(self, data)
        if not result:
            return False
        event_name = data.get('event_name')
        logging.getLogger(__name__).info("Handling event: %s", event_name)
        return True


class GroupDestroyHandler(BaseHandler):
    """A handler for destroying group

    """

    def handle(self, data):
        result = BaseHandler.handle(self, data)
        if not result:
            return False
        event_name = data.get('event_name')
        logging.getLogger(__name__).info("Handling event: %s", event_name)
        return True


class UserAddToGroupHandler(BaseHandler):
    """A handler for adding user to group

    """

    def handle(self, data):
        result = BaseHandler.handle(self, data)
        if not result:
            return False
        event_name = data.get('event_name')
        logging.getLogger(__name__).info("Handling event: %s", event_name)
        return True


class UserRemoveFromGroupHandler(BaseHandler):
    """A handler for removing user from group

    """

    def handle(self, data):
        result = BaseHandler.handle(self, data)
        if not result:
            return False
        event_name = data.get('event_name')
        logging.getLogger(__name__).info("Handling event: %s", event_name)
        return True


class ProjectCreateHandler(BaseHandler):
    """A handler for creating project

    """

    def handle(self, data):
        result = BaseHandler.handle(self, data)
        if not result:
            return False
        event_name = data.get('event_name')
        logging.getLogger(__name__).info("Handling event: %s", event_name)
        return True


class ProjectRenameHandler(BaseHandler):
    """A handler for renaming project

    """

    def handle(self, data):
        result = BaseHandler.handle(self, data)
        if not result:
            return False
        event_name = data.get('event_name')
        logging.getLogger(__name__).info("Handling event: %s", event_name)
        return True


class ProjectUpdateHandler(BaseHandler):
    """A handler for updating project

    """

    def handle(self, data):
        result = BaseHandler.handle(self, data)
        if not result:
            return False
        event_name = data.get('event_name')
        logging.getLogger(__name__).info("Handling event: %s", event_name)
        return True


class ProjectDestroyHandler(BaseHandler):
    """A handler for destroying project

    """

    def handle(self, data):
        result = BaseHandler.handle(self, data)
        if not result:
            return False
        event_name = data.get('event_name')
        logging.getLogger(__name__).info("Handling event: %s", event_name)
        return True


class PushHandler(BaseHandler):
    """A handler for pushing commits

    """

    def handle(self, data):
        result = BaseHandler.handle(self, data)
        if not result:
            return False
        event_name = data.get('event_name')
        logging.getLogger(__name__).info("Handling event: %s", event_name)
        return True


class TagPushHandler(BaseHandler):
    """A handler for pushing tag

    """

    def handle(self, data):
        result = BaseHandler.handle(self, data)
        if not result:
            return False
        event_name = data.get('event_name')
        logging.getLogger(__name__).info("Handling event: %s", event_name)
        return True


class RepositoryUpdateHandler(BaseHandler):
    """A handler for updating repository

    """

    def handle(self, data):
        result = BaseHandler.handle(self, data)
        if not result:
            return False
        event_name = data.get('event_name')
        logging.getLogger(__name__).info("Handling event: %s", event_name)
        return True


class MergeRequestHandler(BaseHandler):
    """A handler for merging request

    """

    def handle(self, data):
        result = BaseHandler.handle(self, data)
        if not result:
            return False
        event_type = data.get('event_type')
        logging.getLogger(__name__).info("Handling event: %s", event_type)
        return True


class HandlerFactory:
    _HANDLERS = {
        "user_create": UserCreateHandler(),
        "user_destroy": UserDestroyHandler(),
        "group_create": GroupCreateHandler(),
        "group_rename": GroupRenameHandler(),
        "group_destroy": GroupDestroyHandler(),
        "user_add_to_group": UserAddToGroupHandler(),
        "user_remove_from_group": UserRemoveFromGroupHandler(),
        "project_create": ProjectCreateHandler(),
        "project_rename": ProjectRenameHandler(),
        "project_update": ProjectUpdateHandler(),
        "project_destroy": ProjectDestroyHandler(),
        "push": PushHandler(),
        "repository_update": RepositoryUpdateHandler(),
        "merge_request": MergeRequestHandler(),
    }

    @staticmethod
    def get_handler(event_type: str, event_name: str) -> Handler:
        if event_type:
            if event_type in HandlerFactory._HANDLERS.keys():
                return HandlerFactory._HANDLERS.get(event_type)
        if event_name in HandlerFactory._HANDLERS.keys():
            return HandlerFactory._HANDLERS.get(event_name)
        return UnknownOpHandler()
