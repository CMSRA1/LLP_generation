from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'Test_T1qqqqLL'
config.General.workArea        = 'Test_T1qqqqLL_PUMix'
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName   = 'step2_T1qqqqLL_PUMix_cfg.py'
config.JobType.outputFiles = ['T1qqqqLL_PUMix.root',]

config.Data.inputDataset         = '' # Update this
config.Data.inputDBS             = 'phys03'
config.Data.splitting            = 'EventAwareLumiBased'
config.Data.unitsPerJob          = 50
config.Data.totalUnits           = -1
config.Data.outLFNDirBase        = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'T1qqqqLL_Madgraph_Pythia_test_PUMix'

config.Site.storageSite = 'T2_UK_London_IC'
#config.Site.storageSite = 'T2_UK_SGrid_Bristol'
