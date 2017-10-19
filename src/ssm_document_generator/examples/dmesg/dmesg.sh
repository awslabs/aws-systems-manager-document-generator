oldIFS=$IFS
IFS="\n"

result=$(dmesg | egrep -i "fail|error|exception|kill|ixgbevf")

if ((${entitiesLimit} != 0)); then
    result=$(echo ${result} | tail -${entitiesLimit})
fi

# Assumes jq is present on the target system.
result=$(echo ${result} | jq -R -s -c '.')

# The only thing your script prints to stdout should be the command response.
cat <<EOT
{"status": "Success", "result_type": "PlainText", "result": ${result}}
EOT

IFS=${oldIFS}