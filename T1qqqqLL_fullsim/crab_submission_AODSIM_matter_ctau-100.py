from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'T1qqqqLL_pball0p5_ctau-100'
config.General.workArea        = 'T1qqqqLL_pball0p5_ctau-100_AODSIM'
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName   = 'step3_T1qqqqLL_AODSIM_cfg.py'
config.JobType.outputFiles = ['T1qqqqLL_AODSIM.root',]
config.JobType.numCores = 4

#config.Data.inputDataset         = '/T1qqqqLL_1000_200_ctau-100_custom_nocustom_Madgraph_Pythia_GEN-SIM/clanerog-T1qqqqLL_1000_200_ctau-100_custom_nocustom_PUMix-16ca0fac1b892ff3c3d45d801745cbbf/USER'
config.Data.inputDataset         = ''

config.Data.inputDBS             = 'phys03'
config.Data.splitting            = 'EventAwareLumiBased'
config.Data.unitsPerJob          = 100
config.Data.totalUnits           = -1
config.Data.outLFNDirBase        = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'T1qqqqLL_pball0p5_ctau-100_AODSIM'

config.Site.storageSite = 'T2_UK_London_IC'
