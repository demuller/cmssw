## Setting up the framework

mainly based on the instructions given in https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookNanoAOD#How_to_check_out_the_code_and_pr
```
export SCRAM_ARCH=slc6_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_10_2_18
cd CMSSW_10_2_18/src/
cmsenv
git cms-merge-topic cms-nanoAOD:master-102X
git checkout -b nanoAOD cms-nanoAOD/master-102X
git-cms-addpkg PhysicsTools/NanoAOD
```
before compiling it, modify
- the file `PhysicsTools/NanoAOD/python/nano_cff.py` (i.e. remove PDF4LHC from the list of preferred PDF sets)
- the file `PhysicsTools/NanoAOD/plugins/GenWeightsTableProducer.cc`:
 - l. 286-292:
```C++
int vectorSize = genProd.weights().size(); // this number should be 14 (2+12) or 46 (2+12+32)
std::vector<double> wPS(vectorSize, 1);
if (vectorSize > 1 ) {
    for (int i=0; i<vectorSize; i++){
        wPS[i] = genProd.weights()[i]; // save all PS weights
    }
}
```
- l. 322-327:
```C++
std::vector<double> wPS(vectorSize, 1);
if (vectorSize > 1 ){
    for (int i=0; i<vectorSize; i++){
        wPS[i] = genProd.weights()[i];
    }
}
```
- l. 330: (description of branch)
```C++
outPS->addColumn<float>("", wPS, vectorSize > 1 ? "PS weights (w_var); [0] and [1] are central ME weight value and replica; [2] is ISR=0.707 FSR=1; [3] is ISR=1 FSR=0.707; [3] is ISR=1.414 FSR=1; [5] is ISR=1 FSR=1.414; [6] is ISR=0.5 FSR=1; [7] is ISR=1 FSR=0.5; [8] is ISR=2 FSR=1; [9] is ISR=1 FSR=2; [10] is ISR=0.25 FSR=1; [11] is ISR=1 FSR=0.25; [12] is ISR=4 FSR=1; [13] is ISR=1 FSR=4; [14]-[45] are decorrelated PS weights" : "dummy PS weight (1.0) " , nanoaod::FlatTable::FloatColumn, lheWeightPrecision_);
```
Compile it:
```
scram b -j 8
```

## Getting the setup config from the official nanoAOD campaign

1. Go to the MCM pdmv web page and search for a prep id of a nanoAOD sample which you want to reproduce privately from MiniAOD and get the setup command, e.g.: https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_setup/TOP-RunIIAutumn18NanoAODv5-00207
```bash
#!/bin/bash
export SCRAM_ARCH=slc6_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_2_15/src ] ; then 
 echo release CMSSW_10_2_15 already exists
else
scram p CMSSW CMSSW_10_2_15
fi
cd CMSSW_10_2_15/src
eval `scram runtime -sh`
scram b
cd ../../
cmsDriver.py step1 --filein "dbs:/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext3-v2/MINIAODSIM" --fileout file:TOP-RunIIAutumn18NanoAODv5-00207.root --mc --eventcontent NANOEDMAODSIM --datatier NANOAODSIM --conditions 102X_upgrade2018_realistic_v19 --step NANO --nThreads 2 --era Run2_2018,run2_nanoAOD_102Xv1 --python_filename TOP-RunIIAutumn18NanoAODv5-00207_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10000 || exit $? ;
```

2. Modify it accordingly to your CMSSW version and replace `--eventcontent NANOEDMAODSIM` by `--eventcontent NANOAODSIM` in the cmsDriver command
3. You can run it locally with `cmsRun TOP-RunIIAutumn18NanoAODv5-00207_1_cfg.py` or submit it via crab, an example for a crab config is given in `PhysicsTools/nanoAOD/test/crab_tw_antitop_ext1.py` with the corresponding PSet config file `PhysicsTools/nanoAOD/test/nano_cfg.py`
4. Important: make sure to set the following variable in the OutputModule section of the PSet config: `fakeNameForCrab =cms.untracked.bool(True),`

## Troubleshooting

In case you accidentally published a dataset twice under the same publication name, one can invalidate specific files of the dataset: https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3DataHandling#Changing_a_dataset_or_file_statu
```python
python $DBS3_CLIENT_ROOT/examples/DBS3SetFileStatus.py --url=https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter --status=invalid --recursive=False  --files=<LFN>
```
To invalidate a complete dataset, use this command:
```python
python $DBS3_CLIENT_ROOT/examples/DBS3SetDatasetStatus.py --dataset=<datasetname> --url=https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter --status=INVALID --recursive=False
```

