import pytest

from .....messaging.base_handler import HandlerException
from .....messaging.message_delivery import MessageDelivery
from .....messaging.request_context import RequestContext
from .....messaging.responder import MockResponder

from ...handlers.ping_response_handler import PingResponseHandler
from ...messages.ping_response import PingResponse


@pytest.fixture()
def request_context() -> RequestContext:
    ctx = RequestContext()
    yield ctx


class TestPingResponseHandler:
    @pytest.mark.asyncio
    async def test_ping_response(self, request_context):
        request_context.message_delivery = MessageDelivery()
        request_context.message = PingResponse()
        request_context.connection_ready = True
        handler = PingResponseHandler()
        responder = MockResponder()
        await handler.handle(request_context, responder)
        messages = responder.messages
        assert len(messages) == 0
