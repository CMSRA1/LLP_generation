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

Run the above commands before the "Only once" section. Run the following after
the "Only once" section:
```bash
cd CMSSW_8_0_21/src
cmsenv
cd -
```

### Only once
Create a directory to keep all your LLP files and directories and move into it.
Checkout the master branch of this repository:
```bash
git clone git@github.com:benkrikler/LLP_generation.git
cd LLP_generation
```

Checkout CMSSW version `8_0_21`:
```bash
export SCRAM_ARCH=slc6_amd64_gcc530
cmsrel CMSSW_8_0_21
cd CMSSW_8_0_21/src
cmsenv
mkdir -p Configuration/GenProduction/python/
cp ../../fragments/T1qqqqLL_fragment.py Configuration/GenProduction/python/
scram b -j 9
cd -
```

## Commands to produce the CMSSW config files
This repository already contains the files produced by the following commands.
But for reference, here are the commands for each step.

### GEN-SIM
Runs Madgraph and Pythia
```bash
cmsDriver.py Configuration/GenProduction/python/T1qqqqLL_fragment.py \
    --mc \
    --eventcontent RAWSIM \
    --customise_commands "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(50) \n process.source.firstRun = cms.untracked.uint32(3) \n process.generator.initialSeed = cms.untracked.uint32(3)" \
    --datatier GEN-SIM \
    --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 \
    --beamspot Realistic50ns13TeVCollision \
    --step GEN,SIM \
    --magField 38T_PostLS1  \
    --fileout file:T1qqqqLL_GEN-SIM.root \
    --python_filename step1_T1qqqqLL_GEN-SIM_cfg.py \
    --no_exec \
    -n 50
```

### PU Mixing
Run the PU mixing step over all events produced by the GEN-SIM step
```bash
cmsDriver.py --mc \
    --eventcontent PREMIXRAW \
    --datatier GEN-SIM-RAW \
    --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 \
    --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:@frozen2016 \
    --nThreads 4 \
    --datamix PreMix \
    --era Run2_2016 \
    --filein file:T1qqqqLL_GEN-SIM.root \
    --fileout file:T1qqqqLL_PUMix.root \
    --python_filename step2_T1qqqqLL_PUMix_cfg.py \
    --pileup_input "/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v2-v2/90023/FED016AB-6A85-E611-96E7-002590A80DF0.root" \
    --no_exec \
    -n -1
```

### AODSIM
```bash
cmsDriver.py --mc \
    --eventcontent AODSIM,DQM \
    --runUnscheduled \
    --datatier AODSIM,DQMIO \
    --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 \
    --step RAW2DIGI,RECO,EI,DQM:DQMOfflinePOGMC \
    --nThreads 4 \
    --era Run2_2016 \
    --filein file:T1qqqqLL_PUMix.root \
    --fileout file:T1qqqqLL_AODSIM.root \
    --python_filename step3_T1qqqqLL_AODSIM_cfg.py \
    --no_exec \
    -n -1
```

### MINIAODSIM
```bash
cmsDriver.py --mc \
    --eventcontent MINIAODSIM \
    --runUnscheduled \
    --datatier MINIAODSIM \
    --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 \
    --step PAT \
    --era Run2_2016 \
    --filein file:T1qqqqLL_AODSIM.root \
    --fileout file:T1qqqqLL_MINIAODSIM.root \
    --python_filename step4_T1qqqqLL_MINIAODSIM_cfg.py \
    --no_exec \
    -n -1
```

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
