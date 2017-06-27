# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/SMS-T1qqqq_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16FSPremix-80X_mcRun2_asymptotic_v12-v2/AODSIM --fileout file:SUS-RunIISpring16MiniAODv2-00193.root --mc --eventcontent MINIAODSIM --runUnscheduled --fast --datatier MINIAODSIM --conditions 80X_mcRun2_asymptotic_2016_miniAODv2_v0 --step PAT --era Run2_25ns --python_filename step2_T1qqqq_MINIAODSIM_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 2880
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('PAT',eras.Run2_25ns,eras.fastSim)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2880)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/RunIISpring16FSPremix/SMS-T1qqqq_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/80X_mcRun2_asymptotic_v12-v2/40000/00491177-A52D-E611-A9D9-001EC9B218F3.root', 
        '/store/mc/RunIISpring16FSPremix/SMS-T1qqqq_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/80X_mcRun2_asymptotic_v12-v2/40000/004F1CBD-762D-E611-A778-C4346BC78E90.root', 
        '/store/mc/RunIISpring16FSPremix/SMS-T1qqqq_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/80X_mcRun2_asymptotic_v12-v2/40000/006C1FD0-932D-E611-911B-0CC47A4C8EE2.root', 
        '/store/mc/RunIISpring16FSPremix/SMS-T1qqqq_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/80X_mcRun2_asymptotic_v12-v2/40000/007F710A-AE2D-E611-ACA5-02163E014862.root', 
        '/store/mc/RunIISpring16FSPremix/SMS-T1qqqq_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/80X_mcRun2_asymptotic_v12-v2/40000/00B31747-A62D-E611-84F1-002590D9D8D4.root', 
        '/store/mc/RunIISpring16FSPremix/SMS-T1qqqq_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/80X_mcRun2_asymptotic_v12-v2/40000/00DE2953-672D-E611-B63C-0025905D1CB2.root', 
        '/store/mc/RunIISpring16FSPremix/SMS-T1qqqq_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/80X_mcRun2_asymptotic_v12-v2/40000/0204EB38-EC2E-E611-AEBB-44A842CF05CC.root', 
        '/store/mc/RunIISpring16FSPremix/SMS-T1qqqq_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/80X_mcRun2_asymptotic_v12-v2/40000/020D0486-8D2D-E611-BB0A-0090FAA57BA0.root', 
        '/store/mc/RunIISpring16FSPremix/SMS-T1qqqq_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/80X_mcRun2_asymptotic_v12-v2/40000/0273E888-7C2D-E611-886E-0025905D1CAC.root', 
        '/store/mc/RunIISpring16FSPremix/SMS-T1qqqq_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/80X_mcRun2_asymptotic_v12-v2/40000/02B8D1EB-862D-E611-B497-C45444922BFE.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:2880'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('file:SUS-RunIISpring16MiniAODv2-00193.root'),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_2016_miniAODv2_v0', '')

# Path and EndPath definitions
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
process.Flag_globalSuperTightHalo2016Filter = cms.Path(process.globalSuperTightHalo2016Filter)
process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
process.Flag_METFilters = cms.Path(process.metFilters)
process.Flag_chargedHadronTrackResolutionFilter = cms.Path(process.chargedHadronTrackResolutionFilter)
process.Flag_globalTightHalo2016Filter = cms.Path(process.globalTightHalo2016Filter)
process.Flag_CSCTightHaloTrkMuUnvetoFilter = cms.Path(process.CSCTightHaloTrkMuUnvetoFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter)
process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter)
process.Flag_trkPOG_toomanystripclus53X = cms.Path(~process.toomanystripclus53X)
process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
process.Flag_trkPOG_manystripclus53X = cms.Path(~process.manystripclus53X)
process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)
process.Flag_muonBadTrackFilter = cms.Path(process.muonBadTrackFilter)
process.Flag_CSCTightHalo2015Filter = cms.Path(process.CSCTightHalo2015Filter)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.Flag_HBHENoiseFilter,process.Flag_HBHENoiseIsoFilter,process.Flag_CSCTightHaloFilter,process.Flag_CSCTightHaloTrkMuUnvetoFilter,process.Flag_CSCTightHalo2015Filter,process.Flag_globalTightHalo2016Filter,process.Flag_globalSuperTightHalo2016Filter,process.Flag_HcalStripHaloFilter,process.Flag_hcalLaserEventFilter,process.Flag_EcalDeadCellTriggerPrimitiveFilter,process.Flag_EcalDeadCellBoundaryEnergyFilter,process.Flag_goodVertices,process.Flag_eeBadScFilter,process.Flag_ecalLaserCorrFilter,process.Flag_trkPOGFilters,process.Flag_chargedHadronTrackResolutionFilter,process.Flag_muonBadTrackFilter,process.Flag_trkPOG_manystripclus53X,process.Flag_trkPOG_toomanystripclus53X,process.Flag_trkPOG_logErrorTooManyClusters,process.Flag_METFilters,process.endjob_step,process.MINIAODSIMoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)
process.load('Configuration.StandardSequences.PATMC_cff')
from FWCore.ParameterSet.Utilities import cleanUnscheduled
process=cleanUnscheduled(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC 

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.metFilterPaths_cff
from PhysicsTools.PatAlgos.slimming.metFilterPaths_cff import miniAOD_customizeMETFiltersFastSim 

#call to customisation function miniAOD_customizeMETFiltersFastSim imported from PhysicsTools.PatAlgos.slimming.metFilterPaths_cff
process = miniAOD_customizeMETFiltersFastSim(process)

# End of customisation functions
