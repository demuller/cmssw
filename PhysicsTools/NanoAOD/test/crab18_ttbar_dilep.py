from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import os

config = Configuration()

config.section_("General")
config.General.requestName = 'priv_nAODv5_TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8'
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
config.Data.inputDataset = '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
#config.Data.splitting = 'EventAwareLumiBased'
#config.Data.unitsPerJob = 2000
config.Data.splitting = 'FileBased' 
config.Data.unitsPerJob = 5
#config.Data.totalUnits = 10000
config.Data.outLFNDirBase = '/store/user/%s/priv_nAODv5/2018/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'NanoAOD'

config.section_("Site")
config.Site.storageSite = 'T1_DE_KIT_Disk'

config.section_("User")
config.User.voGroup = 'dcms'
