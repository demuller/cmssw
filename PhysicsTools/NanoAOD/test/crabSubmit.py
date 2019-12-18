from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import os

config = Configuration()

config.section_("General")
config.General.requestName = 'priv_nAODv5_ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nano1X_cfg.py'
config.JobType.numCores = 2
config.JobType.maxMemoryMB = 2500
#config.JobType.outputFiles = ['lzma.root']

config.section_("Data")
config.Data.inputDataset = '/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM'
config.Data.inputDBS = 'global'
#config.Data.splitting = 'EventAwareLumiBased'
#config.Data.unitsPerJob = 2000
config.Data.splitting = 'FileBased' 
config.Data.unitsPerJob = 5
#config.Data.totalUnits = 10000
config.Data.outLFNDirBase = '/store/user/%s/priv_nAODv5/2017/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'TopNanoAODv5p1_201X'

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
