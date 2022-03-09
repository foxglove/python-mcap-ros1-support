# Python MCAP Ros1 support

This package provides ROS1 support for the Python MCAP file format reader &amp; writer.

## Installation

Install via [Pipenv](https://pipenv.pypa.io/en/latest/) by adding `mcap-ros1-support` to your `Pipfile` or via the command line:

```bash
pipenv install mcap-ros1-support
```

## Example Usage

```python
from mcap.mcap0.stream_reader import StreamReader
from mcap_ros1.decoder import Ros1Decoder

reader = StreamReader("my_data.mcap")
decoder = Ros1Decoder(reader)
for m in decoder.messages:
    print(m)
```

## Stay in touch

Join our [Slack channel](https://foxglove.dev/join-slack) to ask questions, share feedback, and stay up to date on what our team is working on.
