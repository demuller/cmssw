
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h" 
#include "SimDataFormats/GeneratorProducts/interface/LHERunInfoProduct.h" 
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"


#include <TFile.h> 
#include <TTree.h>
#include <TBranch.h>

#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <cmath> 
#include <stdexcept>

using namespace std;

void get_weights(){

TFile* ifile = new TFile("test.root","READ");

TTree* itree = (TTree*)ifile->Get("Events");

TBranch* ibranch = (TBranch*)itree->GetBranch("LHEEventProduct_externalLHEProducer__SIM.obj.weights.id");

int LHEsize = ibranch.size();
std::cout << LHEsize << std::endl; 

for (int i = 0; i < LHEsize; i++)
{
 std::cout << "bla" << std::endl;

}

}
