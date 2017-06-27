from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'Test_T1qqqqLL'
config.General.workArea        = 'Test_T1qqqqLL_GEN-SIM'
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName   = 'step1_T1qqqqLL_GEN-SIM_cfg.py'

config.Data.outputPrimaryDataset = 'T1qqqqLL_Madgraph_Pythia_GEN-SIM'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'EventBased'
config.Data.unitsPerJob          = 50
config.Data.totalUnits           = 100
config.Data.outLFNDirBase        = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'T1qqqqLL_Madgraph_Pythia_test_GEN-SIM'

config.Site.storageSite = 'T2_UK_London_IC'
#config.Site.storageSite = 'T2_UK_SGrid_Bristol'
