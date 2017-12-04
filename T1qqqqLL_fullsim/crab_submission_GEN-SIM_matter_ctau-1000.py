from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName      = 'T1qqqqLL_pball0p5_ctau-1000'
config.General.workArea        = 'T1qqqqLL_pball0p5_ctau-1000_GEN-SIM'
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName   = 'step1_T1qqqqLL_pball0p5_ctau-1000_GEN-SIM_cfg.py'

config.Data.outputPrimaryDataset = 'T1qqqqLL_pball0p5_ctau-1000'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'EventBased'
config.Data.unitsPerJob          = 270
config.Data.totalUnits           = 135000
config.Data.outLFNDirBase        = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'T1qqqqLL_pball0p5_ctau-1000_GEN-SIM'

config.Site.storageSite = 'T2_UK_London_IC'
