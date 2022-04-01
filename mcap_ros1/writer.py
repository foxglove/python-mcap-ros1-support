from io import BufferedWriter, BytesIO
from typing import IO, Any, Dict, Optional, Union
from mcap.mcap0.writer import Writer as McapWriter
import time


class Writer:
    def __init__(self, output: Union[str, IO[Any], BufferedWriter]):
        self.__writer = McapWriter(output=output)
        self.__schema_ids: Dict[str, int] = {}
        self.__channel_ids: Dict[str, int] = {}
        self.__writer.start(profile="ros1", library="python-mcap-ros1-support")
        self.__finished = False

    def finish(self):
        if not self.__finished:
            self.__writer.finish()
            self.__finished = True

    def write_message(
        self,
        topic: str,
        message: Any,
        log_time: Optional[int] = None,
        publish_time: Optional[int] = None,
        sequence: int = 0,
    ):
        if message._type not in self.__schema_ids.keys():
            schema_id = self.__writer.register_schema(
                name=message._type,
                data=message.__class__._full_text.encode(),
                encoding="ros1msg",
            )
            self.__schema_ids[message._type] = schema_id
        schema_id = self.__schema_ids[message._type]

        if topic not in self.__channel_ids.keys():
            channel_id = self.__writer.register_channel(
                topic=topic,
                message_encoding="ros1",
                schema_id=schema_id,
            )
            self.__channel_ids[topic] = channel_id
        channel_id = self.__channel_ids[topic]

        buffer = BytesIO()
        message.serialize(buffer)
        self.__writer.add_message(
            channel_id=channel_id,
            log_time=log_time or time.time_ns(),
            publish_time=publish_time or time.time_ns(),
            sequence=sequence,
            data=buffer.getvalue(),
        )