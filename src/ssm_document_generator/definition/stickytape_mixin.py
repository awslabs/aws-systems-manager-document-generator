from tempfile import NamedTemporaryFile

import sys
import stickytape


class StickyTapeMixin:
    def __init__(self, add_python_paths=sys.path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_python_paths = add_python_paths

    def generate_commands(self):
        commands = super().generate_commands()

        with NamedTemporaryFile(mode='w') as temp_file:
            temp_file.write('\n'.join(commands))
            temp_file.flush()
            return stickytape.script(temp_file.name, add_python_paths=self.add_python_paths).splitlines()
