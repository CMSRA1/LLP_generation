from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'SMS_T1qqqq_fullsim'
config.General.workArea        = 'SMS_T1qqqq_fullsim_GEN-SIM'
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName   = 'step1_T1qqqq_fullsim_GEN-SIM_cfg.py'

config.Data.outputPrimaryDataset = 'T1qqqq_fullsim_Madgraph_Pythia'
config.Data.inputDBS             = 'global'
config.Data.splitting            = 'EventBased'
config.Data.unitsPerJob          = 500
config.Data.totalUnits           = 100000
config.Data.outLFNDirBase        = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'T1qqqq_fullsim_Madgraph_Pythia_GEN-SIM'

config.Site.storageSite = 'T2_UK_London_IC'
#config.Site.storageSite = 'T2_UK_SGrid_Bristol'
