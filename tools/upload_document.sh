#!/usr/bin/env bash
#```Bash
#stickytape ./test_module/test_file_complex.py --output-file stickytype_test.py

#pyminifier --lzma -o minified.py stickytype_test.py
#pyminifier --bzip2 -o minified.py stickytype_test.py


# aws ssm create-document --content file://ssm_to_upload.json --name "generate_test" --document-type "Command" --region us-east-1

documentVersion=$(aws ssm update-document --content file://ssm_to_upload.json --name "generate_test" --document-version "\$LATEST" --output text --query "DocumentDescription.DocumentVersion"  --region us-east-1)

aws ssm update-document-default-version --name "generate_test" --document-version "${documentVersion}"  --region us-east-1

invocationId=$(aws ssm send-command --instance-id i-06bd22443bdc58bdf  --document-name "generate_test"  --output text --query "Command.CommandId" --region us-east-1)

sleep 2

aws ssm get-command-invocation --command-id ${invocationId} --instance-id i-06bd22443bdc58bdf --region us-east-1 > command_output
cat command_output

#```
