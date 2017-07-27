class Preprocessor:
    def __init__(self):
        self.next_processor = None  # Todo noop processor?

    def process(self, input_data):
        # do some work and then pass it to the next processor
        # call some method here that'd be overriden in derived
        result = input_data
        if self.next_processor:
            return self.next_processor.process(result)

        return result

    def chain(self, next_processor):
        self.next_processor = next_processor
        return next_processor
