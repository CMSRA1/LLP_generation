# SMS Long-lived particle MC production
This repository contains the CMSSW and CRAB config files used to generate SMS
LLP (long-lived particle) MC.

## Setup the environment

### Everytime you login
Source the relevant CMS environment, crab environment and setup your grid proxy:
```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
source /cvmfs/cms.cern.ch/crab3/crab.sh
voms-proxy-init --voms cms --valid 168:00
```

### Only once
Create a directory to keep all your LLP files and directories and move into it.
Checkout the master branch of this repository:
```bash
git clone git@github.com:benkrikler/LLP_generation.git
cd LLP_generation
```

## Commands to produce the CMSSW config files
This repository already contains the files produced by the following commands.
But for reference, here are the commands for each step.

## How to submit
To submit locally, just run pass the CMSSW config file to cmsRun:
```bash
cmsRun ${CMSSW_CFG}
```

To submit to the grid using CRAB, pass the CRAB config file to the relevant crab
commands:
```bash
crab submit -c ${CRAB_CFG}
```

To monitor your grid job:
```bash
crab status -d ${CRAB_DIR}
```

There are many other fun CRAB commands that I will let you discover yourself.
