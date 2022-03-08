from mcap.mcap0.stream_reader import StreamReader
from mcap_ros1.ros1_decoder import Ros1Decoder

from .generate import generate_sample_data


def test_ros_decoder():
    with generate_sample_data() as m:
        stream_reader = StreamReader(m)
        ros_reader = Ros1Decoder(stream_reader)
        messages = [m for m in ros_reader.messages]
        assert len(messages) == 10
