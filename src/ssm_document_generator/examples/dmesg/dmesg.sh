resultStatus="Success"

process_result() {
    result=$(echo "${result}" | grep -E "${filterExpression}")

    if ((${entitiesLimit} != 0)); then
        result=$(echo "${result}" | tail -${entitiesLimit})
    fi
}

command () {
    set -e
    dmesg
}

result=$(command)

if [ $? -eq 0 ]; then
    process_result
else
    resultStatus="Failed"
fi

result=$(echo "${result}" | jq -R -s -c '.')

# The only thing your script prints to stdout should be the command response.
cat <<EOT
{"status": "${resultStatus}", "result_type": "PlainText", "result": ${result}}
EOT