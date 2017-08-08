result=$(dmesg | egrep -i "fail|error|exception|kill|ixgbevf")

if ((${lineLimit} != 0)); then
    result=$(echo ${result} | tail -${lineLimit})
fi

result=$(echo ${result} | jq -R -s -c '.')

# The only thing you script prints to the stdout should be the command response.
cat <<EOT
{"result": "success", "content": ${result}}
EOT