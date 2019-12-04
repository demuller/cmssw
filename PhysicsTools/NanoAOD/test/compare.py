from ROOT import *

gROOT.SetBatch(kTRUE)
gStyle.SetOptStat(0)

f_old = TFile.Open("test.root")
f_new = TFile.Open("/portal/ekpbms2/home/dmueller/private_nAODv5/TOP-RunIIAutumn18NanoAODv5-00207_mod.root")

t_old = f_old.Get("Events")
t_new = f_new.Get("Events")

var_list = ["Electron_pt",
    "Electron_eta",
    "nElectron",
    "Muon_pt",
    "Muon_eta",
    "nMuon",
    "Jet_pt",
    "Jet_eta",
    "nJet"]

for i in var_list:
    c = TCanvas("c")
    print(i)
    t_new.Draw(i+">>h_new_"+i,"","HIST")
    t_old.Draw(i+">>h_old_"+i,"","HISTsame")
    h_old = gPad.GetPrimitive("h_old_"+i)
    h_new = gPad.GetPrimitive("h_new_"+i)
    norm_old = 1./(h_old.Integral())
    norm_new = 1./(h_new.Integral())
    h_old.Scale(norm_old)
    h_new.Scale(norm_new)
    h_old.SetLineColor(kRed)
    h_new.SetLineColor(kBlue)
    
    if h_old.GetMaximum() > h_new.GetMaximum():
        max_y = 1.1*h_old.GetMaximum()
        h_new.SetMaximum(max_y)
    else:
        max_y = 1.1*h_new.GetMaximum()
        h_new.SetMaximum(max_y)
    
    min_x = 0
    xbin_min_old = h_old.FindFirstBinAbove()
    min_x_old = h_old.GetXaxis().GetBinCenter(xbin_min_old)
    xbin_min_new = h_new.FindFirstBinAbove()
    min_x_new = h_old.GetXaxis().GetBinCenter(xbin_min_new)
    if min_x_old < min_x_new:
        min_x = min_x_old
    else:
        min_x = min_x_new

    max_x = 0
    xbin_max_old = h_old.FindLastBinAbove()
    max_x_old = h_old.GetXaxis().GetBinCenter(xbin_max_old)
    xbin_max_new = h_new.FindLastBinAbove()
    max_x_new = h_old.GetXaxis().GetBinCenter(xbin_max_new)
    if max_x_old > max_x_new:
        max_x = max_x_old
    else:
        max_x = max_x_new
    
    h_old.GetXaxis().SetRangeUser(min_x,max_x)
    h_new.GetXaxis().SetRangeUser(min_x,max_x)
    
    c.Update()
    c.SaveAs("plot_"+i+".pdf")
    print("Saved plot_"+i+".pdf!")
    h_old.Reset()
    h_new.Reset()
    c.Clear()

f_old.Close()
f_new.Close()
print("Done!")
