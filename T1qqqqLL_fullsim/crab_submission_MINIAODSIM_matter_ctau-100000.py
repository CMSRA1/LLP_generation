from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'T1qqqqLL_pball0p5_ctau-100000'
config.General.workArea        = 'T1qqqqLL_pball0p5_ctau-100000_MINIAODSIM'
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName   = 'step4_T1qqqqLL_MINIAODSIM_cfg.py'
config.JobType.outputFiles = ['T1qqqqLL_MINIAODSIM.root']

#config.Data.inputDataset         = '/T1qqqqLL_1000_200_ctau-100000_custom_nocustom_Madgraph_Pythia_GEN-SIM/clanerog-T1qqqqLL_1000_200_ctau-100000_custom_nocustom_AODSIM-345ffc14093afa02be5d40462c1981d2/USER'
config.Data.inputDataset         = ''


config.Data.inputDBS             = 'phys03'
config.Data.splitting            = 'EventAwareLumiBased'
config.Data.unitsPerJob          = 100
config.Data.totalUnits           = -1
config.Data.outLFNDirBase        = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'T1qqqqLL_pball0p5_ctau-100000_MINIAODSIM'

config.Site.storageSite = 'T2_UK_London_IC'
