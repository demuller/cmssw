## Setting up the framework

mainly based on the instructions given in https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookNanoAOD#How_to_check_out_the_code_and_pr
```
mkdir submitTopNanoAOD/
cd submitTopNanoAOD/
export SCRAM_ARCH=slc6_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_10_2_18
cd CMSSW_10_2_18/src/
cmsenv
git cms-merge-topic cms-nanoAOD:master-102X
git checkout -b nanoAOD cms-nanoAOD/master-102X
git-cms-addpkg PhysicsTools/NanoAOD
```
Update the following files to get the desired info for PDF and PS weights (more info about the modifications done here: `afs/cern.ch/work/m/mullerd/public/priv_nAOD/modifications.txt`):
```
cp -p /afs/cern.ch/work/m/mullerd/public/priv_nAOD/GenWeightsTableProducer.cc ~/submitTopNanoAOD/CMSSW_10_2_18/src/PhysicsTools/NanoAOD/plugins/
cp -p /afs/cern.ch/work/m/mullerd/public/priv_nAOD/nano_cff.py ~/submitTopNanoAOD/CMSSW_10_2_18/src/PhysicsTools/NanoAOD/python/
```
Compile it:
```
scram b -j 8
```

## For CRAB submission

```bash
cd ~/submitTopNanoAOD/CMSSW_10_2_18/src/PhysicsTools/NanoAOD/test
cp -p /afs/cern.ch/work/m/mullerd/public/priv_nAOD/nano*_cfg.py .
cp -p /afs/cern.ch/work/m/mullerd/public/priv_nAOD/crabSubmit.py .
```
Update the following parameters in crabSubmit.py:
- `config.General.requestName`: name for your local directory
- `config.JobType.psetName` and `config.Data.outputDatasetTag` (X=6, 7 or 8 but the same in both entries)
- `config.Site.storageSite`: your storage element
- `config.Data.outLFNDirBase`: path of your storage element
- `config.Data.inputDataset`: miniAOD to be preocessed

## Troubleshooting

In case you accidentally published a dataset twice under the same publication name, one can invalidate specific files of the dataset: https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3DataHandling#Changing_a_dataset_or_file_statu
```python
python $DBS3_CLIENT_ROOT/examples/DBS3SetFileStatus.py --url=https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter --status=invalid --recursive=False  --files=<LFN>
```
To invalidate a complete dataset, use this command:
```python
python $DBS3_CLIENT_ROOT/examples/DBS3SetDatasetStatus.py --dataset=<datasetname> --url=https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter --status=INVALID --recursive=False
```

