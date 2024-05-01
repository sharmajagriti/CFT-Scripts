#!/usr/bin/env bash


# Define the parameters as variables
pProject=""
pEnvironment=""
pResourceName=""
pRegion=""

PARAMS=""
while (( "$#" )); do
  case "$1" in
    -p)
      pProject=$2
      shift 2
      ;;
    -e)
      pEnvironment=$2
      shift 2
      ;;
    -rn)
    pResourceName=$2
      shift 2
      ;;
    -r)
      pRegion=$2
      shift 2
      ;;
  esac
done

aws cloudformation create-stack  --region us-east-1 --stack-name "dev-InfraStackT2" \
                     --template-body file://$(pwd)/Templates/InfraStackT2.yml \
                     --parameters file://$(pwd)/Parameters/dev/InfraStackT2.json \
                     --capabilities CAPABILITY_NAMED_IAM \
                     --tags \
                         Key=pProject,Value=POC \
                         Key=pEnvironment,Value=dev \
                         Key=StackName,Value="dev-InfraStackT2"
