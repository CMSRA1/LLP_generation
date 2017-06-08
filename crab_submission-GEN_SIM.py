from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'Test_T1qqqqLL'
config.General.workArea        = 'Test_T1qqqqLL_IC'
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName   = 'T1qqqqLL_cfg.py'

config.Data.outputPrimaryDataset = 'T1qqqqLL_MadgraphPythia-GEN-SIM'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'EventBased'
config.Data.unitsPerJob          = 5
config.Data.totalUnits           = 10
config.Data.outLFNDirBase        = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'T1qqqqLL_MadgraphPythia_test-GEN-SIM'

config.Site.whitelist   = ["T2_UK_London_IC"]
config.Site.storageSite = 'T2_UK_London_IC'
