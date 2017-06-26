# T1qqqq full sim production

## Setup CMSSW

Checkout CMSSW version `8_0_21`:
```bash
export SCRAM_ARCH=slc6_amd64_gcc530
cmsrel CMSSW_8_0_21
cd CMSSW_8_0_21/src
cmsenv
mkdir -p Configuration/GenProduction/python/
cp ../../fragments/T1qqqq_fragment.py Configuration/GenProduction/python/
scram b -j 9
cd -
```

### GEN-SIM
Runs Madgraph and Pythia
```bash
cmsDriver.py Configuration/GenProduction/python/T1qqqq_fragment.py \
    --mc \
    --eventcontent RAWSIM \
    --customise_commands "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(50) \n process.source.firstRun = cms.untracked.uint32(3) \n process.generator.initialSeed = cms.untracked.uint32(3)" \
    --datatier GEN-SIM \
    --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v6 \
    --beamspot Realistic50ns13TeVCollision \
    --step GEN,SIM \
    --magField 38T_PostLS1  \
    --fileout file:T1qqqq_fullsim_GEN-SIM.root \
    --python_filename step1_T1qqqq_fullsim_GEN-SIM_cfg.py \
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
    --datamix PreMix \
    --era Run2_2016 \
    --filein file:T1qqqq_fullsim_GEN-SIM.root \
    --fileout file:T1qqqq_fullsim_PUMix.root \
    --python_filename step2_T1qqqq_fullsim_PUMix_cfg.py \
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
    --era Run2_2016 \
    --filein file:T1qqqq_fullsim_PUMix.root \
    --fileout file:T1qqqq_fullsim_AODSIM.root \
    --python_filename step3_T1qqqq_fullsim_AODSIM_cfg.py \
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
    --filein file:T1qqqq_fullsim_AODSIM.root \
    --fileout file:T1qqqq_fullsim_MINIAODSIM.root \
    --python_filename step4_T1qqqq_fullsim_MINIAODSIM_cfg.py \
    --no_exec \
    -n -1
```
