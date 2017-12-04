from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'T1qqqqLL_pball0p5_ctau-1'
config.General.workArea        = 'T1qqqqLL_pball0p5_ctau-1_PUMix'
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName   = 'step2_T1qqqqLL_PUMix_cfg.py'
config.JobType.outputFiles = ['T1qqqqLL_PUMix.root',]
config.JobType.numCores = 4

"""
CHANGE ME
"""
#config.Data.inputDataset         = '/T1qqqqLL_pball0p1_ctau-1/clanerog-T1qqqqLL_pball0p1_ctau-1_GEN-SIM-7f672af1bdf669dd15dea686fba43d17/USER'
config.Data.inputDataset         = ''

config.Data.inputDBS             = 'phys03'
config.Data.splitting            = 'EventAwareLumiBased'
config.Data.unitsPerJob          = 100
config.Data.totalUnits           = -1
config.Data.outLFNDirBase        = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'T1qqqqLL_pball0p5_ctau-1_PUMix'

config.Site.storageSite = 'T2_UK_London_IC'
