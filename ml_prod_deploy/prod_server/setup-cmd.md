# Setup Ubuntu/ Linux Servers 
Below are the steps involved in setup a linux server as an API
- GITHUB SSH Setup and Clone Repository
- Setup Python & Virtual Environment
- Open the Security Group - Port
- Test the Server Code
- Start the server in the Background using Screen

## GITHUB SSH Setup and Clone Repository

### change directory to .ssh
```bash
cd ./.ssh
```

### Generate the ssh key
```bash
ssh-keygen -t ed25519 -C "example@email.com"
```

Below are steps to create an SSH key:

1. you will be prompted a name enter a name eg. aws-key
2. then you will be prompted a passphrase: enter a 4 digit key eg 7070 (optional else leave   blank by pressing enter)
3. then re-enter to confirm and press enter. 
4. now the public (.pub) and private key will be created in the .ssh folder

### Now cat the .pub file to update in the Github
```bash
cat aws-key.pub
```

Below are steps to setup an SSH key in the Github:
1. Now copy the key and paste in the github
2. Navigate to account settings in github --> Select SSH & GPG Keys
3. Click on the add new key
4. Enter the title
5. Paste the copied data from cat aws-key.pub
6. Click on the aws-key

### Start the ssh-agent
```bash
eval "$(ssh-agent -s)"
```

### Add the private key to the ssh-agent
```bash
ssh-add ~/.ssh/aws-key
```

### Clone the Repository
1. Now open the github repository.
2. Click on the code button under the tab SSH copy the link (eg. git@github.com/repo...)
3. Run the below command in the AWS server to clone the repository

```bash
git clone <copied-git@github.com/repo...>
```

### Now repository will be clone and master (default) branch will be visible.

## Setup Python & Virtual Environment (in server)
Setup the virtual environment help us run various servers in a single server under various ports and with different set of packages of python.

### Update the Linux Packages
```bash
sudo apt update && sudo apt upgrade -y
```

### Setup PIP package manager to install python packages
```bash
sudo apt install -y python3-pip
```

### Command to install virtualenv
```bash
sudo apt install -y virtualenv && pip3 install virtualenv
```

### Create a virtual environment
```bash
virtualenv --python=python3 venv
```

### Activate the Virtual Environment
```bash
## Linux
source venv/bin/activate

## Windows
venv/Scripts/activate
```

### Now install the requirements
```bash
pip3 install -r requirements.txt
``` 

