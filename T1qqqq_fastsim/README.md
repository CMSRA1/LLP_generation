# Setup commands

## Gridpack to AODSIM
```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
if [ -r CMSSW_8_0_5_patch1/src ]
then
    echo release CMSSW_8_0_5_patch1 already exists
else
    scram p CMSSW CMSSW_8_0_5_patch1
fi
cd CMSSW_8_0_5_patch1/src
eval `scram runtime -sh`

export X509_USER_PROXY=$HOME/private/personal/voms_proxy.cert
mkdir -p Configuration/GenProduction/python/
cp ../../fragments/T1qqqq_fragment.py Configuration/GenProduction/python/

scram b
cd ../../
cmsDriver.py Configuration/GenProduction/python/T1qqqq_fragment.py \
    --fileout file:SUS-RunIISpring16FSPremix-00008.root \
    --pileup_input "dbs:/Neutrino_E-10_gun/RunIISpring16FSPremix-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/GEN-SIM-DIGI-RAW" \
    --mc \
    --eventcontent AODSIM \
    --fast \
    --customise SimGeneral/DataMixingModule/customiseForPremixingInput.customiseForPreMixingInput,Configuration/DataProcessing/Utils.addMonitoring \
    --datatier AODSIM \
    --conditions 80X_mcRun2_asymptotic_v12 \
    --beamspot Realistic50ns13TeVCollision \
    --customise_commands "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)" \
    --step GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,L1Reco,RECO,HLT:@fake1 \
    --datamix PreMix \
    --era Run2_25ns \
    --python_filename step1_T1qqqq_AODSIM_cfg.py \
    --no_exec \
    -n 2880 || exit $?
```

## AODSIM to MINIAODSIM

```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
if [ -r CMSSW_8_0_5_patch1/src ]
then 
    echo release CMSSW_8_0_5_patch1 already exists
else
    scram p CMSSW CMSSW_8_0_5_patch1
fi
cd CMSSW_8_0_5_patch1/src
eval `scram runtime -sh`

export X509_USER_PROXY=$HOME/private/personal/voms_proxy.cert

scram b
cd ../../
cmsDriver.py step1 \
    --filein "dbs:/SMS-T1qqqq_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16FSPremix-80X_mcRun2_asymptotic_v12-v2/AODSIM" \
    --fileout file:SUS-RunIISpring16MiniAODv2-00193.root \
    --mc \
    --eventcontent MINIAODSIM \
    --runUnscheduled \
    --fast \
    --datatier MINIAODSIM \
    --conditions 80X_mcRun2_asymptotic_2016_miniAODv2_v0 \
    --step PAT \
    --era Run2_25ns \
    --python_filename step2_T1qqqq_MINIAODSIM_cfg.py \
    --no_exec 
    --customise Configuration/DataProcessing/Utils.addMonitoring \
    -n 2880 || exit $?
```
