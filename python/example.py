import logging
from time import sleep
from fluent import handler

# Example from https://github.com/fluent/fluent-logger-python

custom_format = {
  'host': '%(hostname)s',
  'where': '%(module)s.%(funcName)s',
  'type': '%(levelname)s',
  'stack_trace': '%(exc_text)s'
}

logging.basicConfig(level=logging.INFO)
#l = logging.getLogger('fluent.test')
log = logging.getLogger(__name__)
#h = handler.FluentHandler('fluentd.test', host='localhost', port=24224, buffer_overflow_handler=overflow_handler)
h = handler.FluentHandler('fluentd.test', host='fluentd', port=24224)
formatter = handler.FluentRecordFormatter(custom_format)
h.setFormatter(formatter)
log.addHandler(h)
def test_function():
  log.info({
    'from': 'userA',
    'to': 'userB'
    })
  log.info('{"from": "userC", "to": "userD"}')
  log.info("This log entry will be logged with the additional key: 'message'.")

while True:
  test_function()
  sleep(10)
