class Processor(object):
    def __init__(self):
        self.next_processor = None

    def process(self, input_data):
        result = self._process(input_data)
        if self.next_processor:
            return self.next_processor.process(result)

        return result

    def _process(self, input_data):
        return input_data

    def chain(self, next_processor):
        self.next_processor = next_processor
        return next_processor
