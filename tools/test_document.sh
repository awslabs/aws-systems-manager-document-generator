#!/usr/bin/env bash
#```Bash
#stickytape ./test_module/test_file_complex.py --output-file stickytype_test.py

#pyminifier --lzma -o minified.py stickytype_test.py
#pyminifier --bzip2 -o minified.py stickytype_test.py


documentToUpload=../src/ssm_to_upload.json
# aws ssm create-document --content file://${documentToUpload} --name "generate_test" --document-type "Command" --region us-east-1
documentVersion=$(aws ssm update-document --content file://${documentToUpload} --name "generate_test" --document-version "\$LATEST" --output text --query "DocumentDescription.DocumentVersion"  --region us-east-1)

aws ssm update-document-default-version --name "generate_test" --document-version "${documentVersion}"  --region us-east-1

instanceId=i-06bd22443bdc58bdf
#invocationId=$(aws ssm send-command --instance-id ${instanceId}  --document-name "generate_test" --parameters '{"excludeFilter":["blah", "foo"], "filePath": ["/var/log/messages"]}' --output text --query "Command.CommandId" --region us-east-1 --output-s3-bucket-name sitalov-ssm-test2 --output-s3-key-prefix OWLS)
invocationId=$(aws ssm send-command --instance-id ${instanceId}  --document-name "generate_test" --parameters '{"filePath": ["/var/log/messages"]}' --output text --query "Command.CommandId" --region us-east-1 --output-s3-bucket-name sitalov-ssm-test2 --output-s3-key-prefix OWLS)

sleep 2

aws ssm get-command-invocation --command-id ${invocationId} --instance-id ${instanceId} --region us-east-1 > command_output
cat command_output

#```
