from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'T1qqqq'
config.General.workArea        = 'T1qqqq_MINIAODSIM'
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName   = 'step2_T1qqqq_MINIAODSIM_cfg.py'
config.JobType.outputFiles = ['SUS-RunIISpring16MiniAODv2-00193.root']

config.Data.inputDataset         = '/T1qqqq_fastsim_Madgraph_Pythia/sbreeze-T1qqqq_fastsim_Madgraph_Pythia_test_GEN-SIM-8b75c65b5e25064b691cce6206972a0a/USER'
config.Data.inputDBS             = 'phys03'
config.Data.splitting            = 'EventAwareLumiBased'
config.Data.unitsPerJob          = 500
config.Data.totalUnits           = -1
config.Data.outLFNDirBase        = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'T1qqqq_fastssim_Madgraph_Pythia_MINIAODSIM'

config.Site.storageSite = 'T2_UK_London_IC'
#config.Site.storageSite = 'T2_UK_SGrid_Bristol'
