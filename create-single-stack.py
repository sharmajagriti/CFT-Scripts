import os
import sys
import subprocess

# Define the parameters as variables
pProject = ""
pEnvironment = ""
pResourceName = ""
pRegion = ""

# Parse command-line arguments
args = sys.argv[1:]
i = 0
while i < len(args):
    if args[i] == "-p":
        pProject = args[i+1]
        i += 2
    elif args[i] == "-e":
        pEnvironment = args[i+1]
        i += 2
    elif args[i] == "-rn":
        pResourceName = args[i+1]
        i += 2
    elif args[i] == "-r":
        pRegion = args[i+1]
        i += 2
    else:
        print("Invalid argument:", args[i])
        sys.exit(1)

# AWS CLI command
command = [
    "aws",
    "cloudformation",
    "create-stack",
    "--region",
    "us-east-1",  # Default region
    "--stack-name",
    "dev-InfraStackT2",
    "--template-body",
    f"file://{os.getcwd()}/Templates/InfraStackT2.yml",
    "--parameters",
    f"file://{os.getcwd()}/Parameters/dev/InfraStackT2.json",
    "--capabilities",
    "CAPABILITY_NAMED_IAM",
    "--tags",
    "Key=pProject,Value=POC",
    "Key=pEnvironment,Value=dev",
    "Key=StackName,Value=dev-InfraStackT2"
]

# Execute AWS CLI command
try:
    subprocess.run(command, check=True)
except subprocess.CalledProcessError as e:
    print("Error:", e)
    sys.exit(1)
