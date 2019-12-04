from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import os

config = Configuration()

config.section_("General")
config.General.requestName = 'priv_nAODv5_RunIIAutumn18_ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nano18_cfg.py'
config.JobType.numCores = 2
config.JobType.maxMemoryMB = 2500
#config.JobType.outputFiles = ['lzma.root']

config.section_("Data")
config.Data.inputDataset = '/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v3/MINIAODSIM'
config.Data.inputDBS = 'global'
#config.Data.splitting = 'EventAwareLumiBased'
#config.Data.unitsPerJob = 2000
config.Data.splitting = 'FileBased' 
config.Data.unitsPerJob = 5
#config.Data.totalUnits = 10000
config.Data.outLFNDirBase = '/store/user/%s/priv_NanoAODv5_RunIIAutumn18/2018/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'NanoAODv5_RunIIAutumn18'

config.section_("Site")
config.Site.storageSite = 'T2_DE_DESY'

config.section_("User")
config.User.voGroup = 'dcms'
