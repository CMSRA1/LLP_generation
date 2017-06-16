from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

# config.General.requestName     = 'NNPDF30_13TeV_Pseudoscalar_100_1'
# config.General.workArea        = 'ICL-POWHEG_DMS'
# config.General.transferOutputs = True
# config.General.transferLogs    = True
# 
# config.JobType.pluginName = 'ANALYSIS'
# config.JobType.psetName   = 'AODSIM_step1_cfg.py'
# config.JobType.outputFiles = ['AODSIM_step1.root',]
# 
# config.Data.inputDataset         = '' # Change inputDataset
# config.Data.inputDBS             = 'phys03'
# config.Data.splitting            = 'EventAwareLumiBased'
# config.Data.unitsPerJob          = 400
# config.Data.totalUnits           = -1
# config.Data.outLFNDirBase        = '/store/user/%s/' % (getUsernameFromSiteDB())
# config.Data.publication          = True
# config.Data.outputDatasetTag     = 'ICL-POWHEG_DMS_NNPDF30_13TeV_Pseudoscalar_100_1-2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU-GEN-SIM-RAW'
# 
# config.Site.whitelist   = ["T2_UK_London_IC"]
# config.Site.storageSite = 'T2_UK_London_IC'
# 
# 
##### ##### ##### ##### ##### ##### ##### ##### #
### ##### ##### ##### ##### ##### ##### ##### ###
# ##### ##### ##### ##### ##### ##### ##### #####

config.General.requestName     = 'Test_T1qqqqLL'
config.General.workArea        = 'Test_T1qqqqLL-step1_premix_take7'
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName   = 'step1_DIGIPREMIX_S2_DATAMIX_L1_DIGI2RAW_HLT_PU.py'
config.JobType.outputFiles = ['step1.root',]

config.Data.inputDataset         = '/T1qqqqLL_MadgraphPythia-GEN-SIM/bkrikler-T1qqqqLL_MadgraphPythia_test-GEN-SIM-6732483590170656bd2270b84748c6a8/USER'
config.Data.inputDBS             = 'phys03'
config.Data.splitting            = 'EventAwareLumiBased'
config.Data.unitsPerJob          = 5
config.Data.totalUnits           = -1
config.Data.outLFNDirBase        = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication          = True
config.Data.outputDatasetTag     = 'T1qqqqLL_MadgraphPythia_test-GEN-SIM'


#config.Site.whitelist   = ["T2_UK_SGrid_Bristol","T2_RU_INR","T2_TH_CUNSTDA"]
config.Site.storageSite = 'T2_UK_SGrid_Bristol'
