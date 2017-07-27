def run_command(parameters):
    # print(parameters)
    # command = 'dmesg | egrep -i \"fail|error|exception|kill|ixgbevf\" | tail -20 | gawk -v uptime=\$( grep btime /proc/stat | cut -d \' \' -f 2 ) \'/^[[ 0-9.]*]/ { print strftime(\"[%Y/%m/%d %H:%M:%S]\", substr(\$0,2,index(\$0,\".\")-2)+uptime) substr(\$0,index(\$0,\"]\")+1) }\''
    line_limit = parameters['lineLimit']

    # open(encoding='utf-8')
    return {'result': 'success', 'content': open('/var/log/messages').readlines(), 'parameters': parameters}
