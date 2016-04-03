from channels.routing import route
from channels.staticfiles import StaticFilesConsumer

from oliver_screen.consumers import ws_message, ws_connect, ws_disconnect

channel_routing = [
    route('http.request', StaticFilesConsumer()),

    route("websocket.receive", ws_message),
    route("websocket.connect", ws_connect),
    route("websocket.disconnect", ws_disconnect),
]
