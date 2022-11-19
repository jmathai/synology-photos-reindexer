# Reindex Synology Photos

Simple script to call Synology Photo's reindex API that can be scheduled to run periodically.

## Instructions

### Clone the repository.

```
git clone https://github.com/jmathai/synology-photos-reindexer.git
```

### Change into the directory.

```
cd synology-photos-reindexer
```

### Create virtual environment (optional but recommended)

```
python3 -m venv .env
source .env/bin/activate
```

### Install dependencies.

```
pip3 install -r requirements.txt
```

### Export environment variables.

```
export SYNO_USERNAME=<your synology username>
export SYNO_PASSWORD=<your synology password>
export SYNO_HOSTNAME=<your synology hostname or ip address>
```

### Run the script.

You may see some errors about an `InsecureRequestWarning` which can be ignored.

```
./main.py
```

## Schedule the script

Schedule this to run using Synology's Task scheduler which can be found in the Control Panel.

From the Task Scheduler click Create -> Scheduled Task -> User defined script.

On the Task Settings tab you'll use the following commands from above customized with your values.

```
export SYNO_USERNAME=<your synology username>
export SYNO_PASSWORD=<your synology password>
export SYNO_HOSTNAME=<your synology hostname or ip address>
cd <path to git repo>
source .env/bin/activate
./main.py
```
