import textwrap

from ssm_document_generator.definition.parameters.common import entities_limit, regex_filter_expression

bash_code_template = """
resultStatus="Success"

process_result() {
    result=$(echo "${result}" | grep -E "${filterExpression}")

    if ((${entitiesLimit} != 0)); then
        result=$(echo "${result}" | tail -${entitiesLimit})
    fi
}

command () {
    set -e
    %s
}

result=$(command)

if [ $? -eq 0 ]; then
    process_result
else
    resultStatus="Failed"
fi

result=$(echo "${result}" | jq -R -s -c '.')

cat <<EOT
{"status": "${resultStatus}", "result_type": "PlainText", "result": ${result}}
EOT
"""


class BashSimpleResultFormatMixin:
    """
    A mixin to simplify the command definition for bash commands.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parameters.extend([entities_limit(), regex_filter_expression()])

    def generate_commands(self):
        return (textwrap.dedent(bash_code_template) % '\n'.join(super().generate_commands())).splitlines()
