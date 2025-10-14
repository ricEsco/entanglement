import ROOT

##############################################################################
### This file stores histograms to be filled in a separate analysis script ###
###                     e.g. entanglement_nanoGen.py                       ###
##############################################################################

# ROOT histogram initialization syntax:
# h_name = ROOT.TH1F("h_name", "Title;x-axis_label;y-axis_label", nbins, xlow, xup)
# (note the semicolon separated single string "Title;x-axis label;y-axis label")

##########################
### Particle kinematics###
##########################
# Top quarks
h_topPt = ROOT.TH1F("h_topPt", "Top Quark p_{T};p_{T} (GeV);Events", 150, 0, 1000)
h_topEta = ROOT.TH1F("h_topEta", "Top Quark #eta;#eta;Events", 50, -5, 5)
h_topPhi = ROOT.TH1F("h_topPhi", "Top Quark #phi;#phi;Events", 12, -3.14, 3.14)
h_topMass = ROOT.TH1F("h_topMass", "Top Quark Mass;M (GeV);Events", 100, 150, 200)
h_antitopPt = ROOT.TH1F("h_antitopPt", "antiTop Quark p_{T};p_{T} [GeV];Events", 150, 0, 1000)
h_antitopEta = ROOT.TH1F("h_antitopEta", "antiTop Quark #eta;#eta;Events", 50, -5, 5)
h_antitopPhi = ROOT.TH1F("h_antitopPhi", "antiTop Quark #phi;#phi;Events", 12, -3.14, 3.14)
h_antitopMass = ROOT.TH1F("h_antitopMass", "antiTop Quark Mass;M (GeV);Events", 100, 150, 200)
h_invariantMass = ROOT.TH1F("h_invariantMass", "ttbar Invariant Mass;M (GeV);Events", 9940, 300, 50000)
h_scattering_angle = ROOT.TH1F("h_scattering_angle", "Top Scattering Angle;#theta^{*};Events", 12, 0, 3.14)
h_beta = ROOT.TH1F("h_beta", "ttbar System Velocity;#beta;Events", 50, 0, 1)
h_deltaAbsY = ROOT.TH1F("h_deltaAbsY", "#Delta|y| = |y_{t}| - |y_{#bar{t}}|;#Delta|y|;Events", 6, -5, 5)
h_hypTan_deltaAbsY = ROOT.TH1F("h_hypTan_deltaAbsY", "hyperbolic_tangent(#Delta|y|);tanh(#Delta|y|);Events", 6, -1, 1)
# Bottom quarks
h_bquark_pt = ROOT.TH1F("h_bquark_pt", "b-quark p_{T};p_{T} (GeV);Events", 150, 0, 500)
h_bquark_eta = ROOT.TH1F("h_bquark_eta", "b-quark #eta;#eta;Events", 50, -5, 5)
h_bquark_phi = ROOT.TH1F("h_bquark_phi", "b-quark #phi;#phi;Events", 12, -3.14, 3.14)
h_antibquark_pt = ROOT.TH1F("h_antibquark_pt", "antib-quark p_{T};p_{T} (GeV);Events", 150, 0, 500)
h_antibquark_eta = ROOT.TH1F("h_antibquark_eta", "antib-quark #eta;#eta;Events", 50, -5, 5)
h_antibquark_phi = ROOT.TH1F("h_antibquark_phi", "antib-quark #phi;#phi;Events", 12, -3.14, 3.14)
h_Had_bquark_pt = ROOT.TH1F("h_Had_bquark_pt", "Hadronic b-quark p_{T};p_{T} (GeV);Events", 150, 0, 500)
h_Had_bquark_eta = ROOT.TH1F("h_Had_bquark_eta", "Hadronic b-quark #eta;#eta;Events", 50, -5, 5)
h_Had_bquark_phi = ROOT.TH1F("h_Had_bquark_phi", "Hadronic b-quark #phi;#phi;Events", 12, -3.14, 3.14)
h_Had_antibquark_pt = ROOT.TH1F("h_Had_antibquark_pt", "Hadronic anti-b-quark p_{T};p_{T} (GeV);Events", 150, 0, 500)
h_Had_antibquark_eta = ROOT.TH1F("h_Had_antibquark_eta", "Hadronic anti-b-quark #eta;#eta;Events", 50, -5, 5)
h_Had_antibquark_phi = ROOT.TH1F("h_Had_antibquark_phi", "Hadronic anti-b-quark #phi;#phi;Events", 12, -3.14, 3.14)
# W bosons
h_Wplus_pt = ROOT.TH1F("h_Wplus_pt", "W^{+} p_{T};p_{T} (GeV);Events", 150, 0, 500)
h_Wplus_eta = ROOT.TH1F("h_Wplus_eta", "W^{+} #eta;#eta;Events", 50, -5, 5)
h_Wplus_phi = ROOT.TH1F("h_Wplus_phi", "W^{+} #phi;#phi;Events", 12, -3.14, 3.14)
h_Wplus_mass = ROOT.TH1F("h_Wplus_mass", "W^{+} Mass;M (GeV);Events", 50, 0, 200)
h_Wminus_pt = ROOT.TH1F("h_Wminus_pt", "W^{-} p_{T};p_{T} (GeV);Events", 150, 0, 500)
h_Wminus_eta = ROOT.TH1F("h_Wminus_eta", "W^{-} #eta;#eta;Events", 50, -5, 5)
h_Wminus_phi = ROOT.TH1F("h_Wminus_phi", "W^{-} #phi;#phi;Events", 12, -3.14, 3.14)
h_Wminus_mass = ROOT.TH1F("h_Wminus_mass", "W^{-} Mass;M (GeV);Events", 50, 0, 200)
# Leptons
h_lepton_pt = ROOT.TH1F("h_leptonPt", "Lepton p_{T};p_{T} (GeV);Events", 50, 0, 300)
h_lepton_eta = ROOT.TH1F("h_leptoneta", "Lepton #eta;#eta;Events", 50, -5, 5)
h_lepton_phi = ROOT.TH1F("h_leptonphi", "Lepton #phi;#phi;Events", 12, -3.14, 3.14)
h_antilepton_pt = ROOT.TH1F("h_antiLeptonPt", "Anti-Lepton p_{T};p_{T} (GeV);Events", 50, 0, 300)
h_antilepton_eta = ROOT.TH1F("h_antiLeptoneta", "Anti-Lepton #eta;#eta;Events", 50, -5, 5)
h_antilepton_phi = ROOT.TH1F("h_antiLeptonphi", "Anti-Lepton #phi;#phi;Events", 12, -3.14, 3.14)
h_neutrino_pt = ROOT.TH1F("h_neutrinoPt", "Neutrino p_{T};p_{T} (GeV);Events", 50, 0, 300)
h_neutrino_eta = ROOT.TH1F("h_neutrinoeta", "Neutrino #eta;#eta;Events", 50, -5, 5)
h_neutrino_phi = ROOT.TH1F("h_neutrinophi", "Neutrino #phi;#phi;Events", 12, -3.14, 3.14)
h_antineutrino_pt = ROOT.TH1F("h_antiNeutrinoPt", "Anti-Neutrino p_{T};p_{T} (GeV);Events", 50, 0, 300)
h_antineutrino_eta = ROOT.TH1F("h_antiNeutrinoeta", "Anti-Neutrino #eta;#eta;Events", 50, -5, 5)
h_antineutrino_phi = ROOT.TH1F("h_antiNeutrinophi", "Anti-Neutrino #phi;#phi;Events", 12, -3.14, 3.14)
# Light quarks from hadronic W decay
h_utype_quark_pt = ROOT.TH1F("h_utype_quark_pt", "u-type quark p_{T};p_{T} (GeV);Events", 150, 0, 500)
h_utype_quark_eta = ROOT.TH1F("h_utype_quark_eta", "u-type quark #eta;#eta;Events", 50, -5, 5)
h_utype_quark_phi = ROOT.TH1F("h_utype_quark_phi", "u-type quark #phi;#phi;Events", 12, -3.14, 3.14)
h_antiUtype_quark_pt = ROOT.TH1F("h_antiUtype_quark_pt", "anti-u-type quark p_{T};p_{T} (GeV);Events", 150, 0, 500)
h_antiUtype_quark_eta = ROOT.TH1F("h_antiUtype_quark_eta", "anti-u-type quark #eta;#eta;Events", 50, -5, 5)
h_antiUtype_quark_phi = ROOT.TH1F("h_antiUtype_quark_phi", "anti-u-type quark #phi;#phi;Events", 12, -3.14, 3.14)
h_dtype_quark_pt = ROOT.TH1F("h_dtype_quark_pt", "d-type quark p_{T};p_{T} (GeV);Events", 150, 0, 500)
h_dtype_quark_eta = ROOT.TH1F("h_dtype_quark_eta", "d-type quark #eta;#eta;Events", 50, -5, 5)
h_dtype_quark_phi = ROOT.TH1F("h_dtype_quark_phi", "d-type quark #phi;#phi;Events", 12, -3.14, 3.14)
h_antiDtype_quark_pt = ROOT.TH1F("h_antiDtype_quark_pt", "anti-d-type quark p_{T};p_{T} (GeV);Events", 150, 0, 500)
h_antiDtype_quark_eta = ROOT.TH1F("h_antiDtype_quark_eta", "anti-d-type quark #eta;#eta;Events", 50, -5, 5)
h_antiDtype_quark_phi = ROOT.TH1F("h_antiDtype_quark_phi", "anti-d-type quark #phi;#phi;Events", 12, -3.14, 3.14)

##################################
### Spin correlation variables ###
##################################

### LEPTON EXCLUSIVE Polarization ###
#####################################
h_cos_theta1k_antilepton = ROOT.TH1F("h_cos_theta1k_antilepton", "antilepton #hat{k}-polarization;cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1r_antilepton = ROOT.TH1F("h_cos_theta1r_antilepton", "antilepton #hat{r}-polarization;cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1n_antilepton = ROOT.TH1F("h_cos_theta1n_antilepton", "antilepton #hat{n}-polarization;cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton = ROOT.TH1F("h_cos_theta1rStar_antilepton", "antilepton #hat{r}*-polarization ;cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton = ROOT.TH1F("h_cos_theta1kStar_antilepton", "antilepton #hat{k}*-polarization ;cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton = ROOT.TH1F("h_cos_theta2n_lepton", "lepton #hat{n}-polarization;cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton = ROOT.TH1F("h_cos_theta2r_lepton", "lepton #hat{r}-polarization;cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton = ROOT.TH1F("h_cos_theta2k_lepton", "lepton #hat{k}-polarization;cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton = ROOT.TH1F("h_cos_theta2rStar_lepton", "lepton #hat{r}*-polarization ;cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton = ROOT.TH1F("h_cos_theta2kStar_lepton", "lepton #hat{k}*-polarization ;cos(#theta_{lk*});Events", 6, -1, 1)
### Polarization ###
####################
# lepton/b-quark analyzers
h_lb_cos_theta1n = ROOT.TH1F("h_lb_cos_theta1n", "top decay (lb) #hat{n}-polarization;(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r = ROOT.TH1F("h_lb_cos_theta1r", "top decay (lb) #hat{r}-polarization;(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k = ROOT.TH1F("h_lb_cos_theta1k", "top decay (lb) #hat{k}-polarization;(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar = ROOT.TH1F("h_lb_cos_theta1rStar", "top decay (lb) #hat{r}*-polarization;(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar = ROOT.TH1F("h_lb_cos_theta1kStar", "top decay (lb) #hat{k}*-polarization;(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n = ROOT.TH1F("h_lb_cos_theta2n", "antitop decay (lb) #hat{n}-polarization;(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r = ROOT.TH1F("h_lb_cos_theta2r", "antitop decay (lb) #hat{r}-polarization;(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k = ROOT.TH1F("h_lb_cos_theta2k", "antitop decay (lb) #hat{k}-polarization;(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar = ROOT.TH1F("h_lb_cos_theta2rStar", "antitop decay (lb) #hat{r}*-polarization;(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar = ROOT.TH1F("h_lb_cos_theta2kStar", "antitop decay (lb) #hat{k}*-polarization;(lb) cos(#theta_{2k*});Events", 6, -1, 1)
# lepton/down-type W-daughter analyzers
h_ld_cos_theta1n = ROOT.TH1F("h_ld_cos_theta1n", "top decay (ld) #hat{n}-polarization;(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r = ROOT.TH1F("h_ld_cos_theta1r", "top decay (ld) #hat{r}-polarization;(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k = ROOT.TH1F("h_ld_cos_theta1k", "top decay (ld) #hat{k}-polarization;(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar = ROOT.TH1F("h_ld_cos_theta1rStar", "top decay (ld) #hat{r}*-polarization;(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar = ROOT.TH1F("h_ld_cos_theta1kStar", "top decay (ld) #hat{k}*-polarization;(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n = ROOT.TH1F("h_ld_cos_theta2n", "antitop decay (ld) #hat{n}-polarization;(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r = ROOT.TH1F("h_ld_cos_theta2r", "antitop decay (ld) #hat{r}-polarization;(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k = ROOT.TH1F("h_ld_cos_theta2k", "antitop decay (ld) #hat{k}-polarization;(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar = ROOT.TH1F("h_ld_cos_theta2rStar", "antitop decay (ld) #hat{r}*-polarization;(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar = ROOT.TH1F("h_ld_cos_theta2kStar", "antitop decay (ld) #hat{k}*-polarization;(ld) cos(#theta_{2k*});Events", 6, -1, 1)
### Correlation Matrix elements ###
###################################
# lepton/b-quark analyzers
h_lb_Cnn = ROOT.TH1F("h_lb_Cnn", "(lb) C_{nn};C_{nn};Events", 6, -1, 1)
h_lb_Cnr = ROOT.TH1F("h_lb_Cnr", "(lb) C_{nr};C_{nr};Events", 6, -1, 1)
h_lb_Cnk = ROOT.TH1F("h_lb_Cnk", "(lb) C_{nk};C_{nk};Events", 6, -1, 1)
h_lb_Crn = ROOT.TH1F("h_lb_Crn", "(lb) C_{rn};C_{rn};Events", 6, -1, 1)
h_lb_Crr = ROOT.TH1F("h_lb_Crr", "(lb) C_{rr};C_{rr};Events", 6, -1, 1)
h_lb_Crk = ROOT.TH1F("h_lb_Crk", "(lb) C_{rk};C_{rk};Events", 6, -1, 1)
h_lb_Ckn = ROOT.TH1F("h_lb_Ckn", "(lb) C_{kn};C_{kn};Events", 6, -1, 1)
h_lb_Ckr = ROOT.TH1F("h_lb_Ckr", "(lb) C_{kr};C_{kr};Events", 6, -1, 1)
h_lb_Ckk = ROOT.TH1F("h_lb_Ckk", "(lb) C_{kk};C_{kk};Events", 6, -1, 1)
### Entaglement Witnesses
h_lb_trC      = ROOT.TH1F("h_lb_trC", "Trace of Correlation Matrix;Tr(C);Events", 12, -3, 3)
h_lb_cHel     = ROOT.TH1F("h_lb_cHel", "(lb) Cosine Helicity Angle;cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n = ROOT.TH1F("h_lb_cHel_P3n", "(lb) Cosine Helicity Angle w/P_3n;cos(#theta_{l(P_{3}b});Events", 6, -1, 1)
# lepton/down-type W-daughter analyzers
h_ld_Cnn = ROOT.TH1F("h_ld_Cnn", "(ld) C_{nn};C_{nn};Events", 6, -1, 1)
h_ld_Cnr = ROOT.TH1F("h_ld_Cnr", "(ld) C_{nr};C_{nr};Events", 6, -1, 1)
h_ld_Cnk = ROOT.TH1F("h_ld_Cnk", "(ld) C_{nk};C_{nk};Events", 6, -1, 1)
h_ld_Crn = ROOT.TH1F("h_ld_Crn", "(ld) C_{rn};C_{rn};Events", 6, -1, 1)
h_ld_Crr = ROOT.TH1F("h_ld_Crr", "(ld) C_{rr};C_{rr};Events", 6, -1, 1)
h_ld_Crk = ROOT.TH1F("h_ld_Crk", "(ld) C_{rk};C_{rk};Events", 6, -1, 1)
h_ld_Ckn = ROOT.TH1F("h_ld_Ckn", "(ld) C_{kn};C_{kn};Events", 6, -1, 1)
h_ld_Ckr = ROOT.TH1F("h_ld_Ckr", "(ld) C_{kr};C_{kr};Events", 6, -1, 1)
h_ld_Ckk = ROOT.TH1F("h_ld_Ckk", "(ld) C_{kk};C_{kk};Events", 6, -1, 1)
### Entaglement Witnesses
h_ld_trC      = ROOT.TH1F("h_ld_trC", "Trace of Correlation Matrix;Tr(C);Events", 12, -3, 3)
h_ld_cHel     = ROOT.TH1F("h_ld_cHel", "(ld) Cosine Helicity Angle;cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n = ROOT.TH1F("h_ld_cHel_P3n", "(ld) Cosine Helicity Angle w/P_3n;cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

### Baumgart&Tweedie variables ###
##################################
h_lb_sigmaPhi = ROOT.TH1F("h_lb_sigmaPhi", "(lb) #Sigma#phi_{#hat{n}#hat{r}};#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi = ROOT.TH1F("h_lb_deltaPhi", "(lb) #Delta#phi_{#hat{n}#hat{r}};#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi = ROOT.TH1F("h_ld_sigmaPhi", "(ld) #Sigma#phi_{#hat{n}#hat{r}};#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi = ROOT.TH1F("h_ld_deltaPhi", "(ld) #Delta#phi_{#hat{n}#hat{r}};#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)


### Bins of mttbar ###
### mtt [300, 400] GeV ### (include a separate bin with beta<0.9 cut ONLY for lowest mass bin) ###
h_cos_theta1n_antilepton_mtt300to400 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt300to400", "antilepton #hat{n}-polarization (300 < m_{tt} < 400 GeV);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt300to400 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt300to400", "antilepton #hat{r}-polarization (300 < m_{tt} < 400 GeV);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt300to400 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt300to400", "antilepton #hat{k}-polarization (300 < m_{tt} < 400 GeV);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt300to400 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt300to400", "antilepton #hat{r}*-polarization (300 < m_{tt} < 400 GeV);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt300to400 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt300to400", "antilepton #hat{k}*-polarization (300 < m_{tt} < 400 GeV);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt300to400 = ROOT.TH1F("h_cos_theta2n_lepton_mtt300to400", "lepton #hat{n}-polarization (300 < m_{tt} < 400 GeV);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt300to400 = ROOT.TH1F("h_cos_theta2r_lepton_mtt300to400", "lepton #hat{r}-polarization (300 < m_{tt} < 400 GeV);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt300to400 = ROOT.TH1F("h_cos_theta2k_lepton_mtt300to400", "lepton #hat{k}-polarization (300 < m_{tt} < 400 GeV);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt300to400 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt300to400", "lepton #hat{r}*-polarization (300 < m_{tt} < 400 GeV);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt300to400 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt300to400", "lepton #hat{k}*-polarization (300 < m_{tt} < 400 GeV);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt300to400 = ROOT.TH1F("h_lb_cos_theta1n_mtt300to400", "top decay (lb) #hat{n}-polarization (300 < m_{tt} < 400 GeV);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt300to400 = ROOT.TH1F("h_lb_cos_theta1r_mtt300to400", "top decay (lb) #hat{r}-polarization (300 < m_{tt} < 400 GeV);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt300to400 = ROOT.TH1F("h_lb_cos_theta1k_mtt300to400", "top decay (lb) #hat{k}-polarization (300 < m_{tt} < 400 GeV);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt300to400 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt300to400", "top decay (lb) #hat{r}*-polarization (300 < m_{tt} < 400 GeV);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt300to400 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt300to400", "top decay (lb) #hat{k}*-polarization (300 < m_{tt} < 400 GeV);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt300to400 = ROOT.TH1F("h_lb_cos_theta2n_mtt300to400", "antitop decay (lb) #hat{n}-polarization (300 < m_{tt} < 400 GeV);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt300to400 = ROOT.TH1F("h_lb_cos_theta2r_mtt300to400", "antitop decay (lb) #hat{r}-polarization (300 < m_{tt} < 400 GeV);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt300to400 = ROOT.TH1F("h_lb_cos_theta2k_mtt300to400", "antitop decay (lb) #hat{k}-polarization (300 < m_{tt} < 400 GeV);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt300to400 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt300to400", "antitop decay (lb) #hat{r}*-polarization (300 < m_{tt} < 400 GeV);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt300to400 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt300to400", "antitop decay (lb) #hat{k}*-polarization (300 < m_{tt} < 400 GeV);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt300to400 = ROOT.TH1F("h_lb_Cnn_mtt300to400", "(lb) C_{nn} (300 < m_{tt} < 400 GeV);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt300to400 = ROOT.TH1F("h_lb_Cnr_mtt300to400", "(lb) C_{nr} (300 < m_{tt} < 400 GeV);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt300to400 = ROOT.TH1F("h_lb_Cnk_mtt300to400", "(lb) C_{nk} (300 < m_{tt} < 400 GeV);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt300to400 = ROOT.TH1F("h_lb_Crn_mtt300to400", "(lb) C_{rn} (300 < m_{tt} < 400 GeV);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt300to400 = ROOT.TH1F("h_lb_Crr_mtt300to400", "(lb) C_{rr} (300 < m_{tt} < 400 GeV);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt300to400 = ROOT.TH1F("h_lb_Crk_mtt300to400", "(lb) C_{rk} (300 < m_{tt} < 400 GeV);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt300to400 = ROOT.TH1F("h_lb_Ckn_mtt300to400", "(lb) C_{kn} (300 < m_{tt} < 400 GeV);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt300to400 = ROOT.TH1F("h_lb_Ckr_mtt300to400", "(lb) C_{kr} (300 < m_{tt} < 400 GeV);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt300to400 = ROOT.TH1F("h_lb_Ckk_mtt300to400", "(lb) C_{kk} (300 < m_{tt} < 400 GeV);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt300to400 = ROOT.TH1F("h_lb_trC_mtt300to400", "Trace of Correlation Matrix (300 < m_{tt} < 400 GeV);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt300to400 = ROOT.TH1F("h_lb_cHel_mtt300to400", "(lb) Cosine Helicity Angle (300 < m_{tt} < 400 GeV);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt300to400 = ROOT.TH1F("h_lb_cHel_P3n_mtt300to400", "(lb) Cosine Helicity Angle w/P_3n (300 < m_{tt} < 400 GeV);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt300to400 = ROOT.TH1F("h_ld_cos_theta1n_mtt300to400", "top decay (ld) #hat{n}-polarization (300 < m_{tt} < 400 GeV);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt300to400 = ROOT.TH1F("h_ld_cos_theta1r_mtt300to400", "top decay (ld) #hat{r}-polarization (300 < m_{tt} < 400 GeV);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt300to400 = ROOT.TH1F("h_ld_cos_theta1k_mtt300to400", "top decay (ld) #hat{k}-polarization (300 < m_{tt} < 400 GeV);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt300to400 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt300to400", "top decay (ld) #hat{r}*-polarization (300 < m_{tt} < 400 GeV);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt300to400 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt300to400", "top decay (ld) #hat{k}*-polarization (300 < m_{tt} < 400 GeV);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt300to400 = ROOT.TH1F("h_ld_cos_theta2n_mtt300to400", "antitop decay (ld) #hat{n}-polarization (300 < m_{tt} < 400 GeV);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt300to400 = ROOT.TH1F("h_ld_cos_theta2r_mtt300to400", "antitop decay (ld) #hat{r}-polarization (300 < m_{tt} < 400 GeV);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt300to400 = ROOT.TH1F("h_ld_cos_theta2k_mtt300to400", "antitop decay (ld) #hat{k}-polarization (300 < m_{tt} < 400 GeV);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt300to400 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt300to400", "antitop decay (ld) #hat{r}*-polarization (300 < m_{tt} < 400 GeV);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt300to400 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt300to400", "antitop decay (ld) #hat{k}*-polarization (300 < m_{tt} < 400 GeV);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt300to400 = ROOT.TH1F("h_ld_Cnn_mtt300to400", "(ld) C_{nn} (300 < m_{tt} < 400 GeV);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt300to400 = ROOT.TH1F("h_ld_Cnr_mtt300to400", "(ld) C_{nr} (300 < m_{tt} < 400 GeV);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt300to400 = ROOT.TH1F("h_ld_Cnk_mtt300to400", "(ld) C_{nk} (300 < m_{tt} < 400 GeV);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt300to400 = ROOT.TH1F("h_ld_Crn_mtt300to400", "(ld) C_{rn} (300 < m_{tt} < 400 GeV);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt300to400 = ROOT.TH1F("h_ld_Crr_mtt300to400", "(ld) C_{rr} (300 < m_{tt} < 400 GeV);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt300to400 = ROOT.TH1F("h_ld_Crk_mtt300to400", "(ld) C_{rk} (300 < m_{tt} < 400 GeV);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt300to400 = ROOT.TH1F("h_ld_Ckn_mtt300to400", "(ld) C_{kn} (300 < m_{tt} < 400 GeV);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt300to400 = ROOT.TH1F("h_ld_Ckr_mtt300to400", "(ld) C_{kr} (300 < m_{tt} < 400 GeV);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt300to400 = ROOT.TH1F("h_ld_Ckk_mtt300to400", "(ld) C_{kk} (300 < m_{tt} < 400 GeV);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt300to400 = ROOT.TH1F("h_ld_trC_mtt300to400", "Trace of Correlation Matrix (300 < m_{tt} < 400 GeV);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt300to400 = ROOT.TH1F("h_ld_cHel_mtt300to400", "(ld) Cosine Helicity Angle (300 < m_{tt} < 400 GeV);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt300to400 = ROOT.TH1F("h_ld_cHel_P3n_mtt300to400", "(ld) Cosine Helicity Angle w/P_3n (300 < m_{tt} < 400 GeV);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt300to400 = ROOT.TH1F("h_lb_sigmaPhi_mtt300to400", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt300to400 = ROOT.TH1F("h_lb_deltaPhi_mtt300to400", "(lb) #Delta#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt300to400 = ROOT.TH1F("h_ld_sigmaPhi_mtt300to400", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt300to400 = ROOT.TH1F("h_ld_deltaPhi_mtt300to400", "(ld) #Delta#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

        # beta < 0.9
h_cos_theta1n_antilepton_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt300to400_beta_lt_0p9", "antilepton #hat{n}-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt300to400_beta_lt_0p9", "antilepton #hat{r}-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt300to400_beta_lt_0p9", "antilepton #hat{k}-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt300to400_beta_lt_0p9", "antilepton #hat{r}*-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt300to400_beta_lt_0p9", "antilepton #hat{k}*-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2n_lepton_mtt300to400_beta_lt_0p9", "lepton #hat{n}-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2r_lepton_mtt300to400_beta_lt_0p9", "lepton #hat{r}-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2k_lepton_mtt300to400_beta_lt_0p9", "lepton #hat{k}-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt300to400_beta_lt_0p9", "lepton #hat{r}*-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt300to400_beta_lt_0p9", "lepton #hat{k}*-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1n_mtt300to400_beta_lt_0p9", "top decay (lb) #hat{n}-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1r_mtt300to400_beta_lt_0p9", "top decay (lb) #hat{r}-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1k_mtt300to400_beta_lt_0p9", "top decay (lb) #hat{k}-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt300to400_beta_lt_0p9", "top decay (lb) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt300to400_beta_lt_0p9", "top decay (lb) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2n_mtt300to400_beta_lt_0p9", "antitop decay (lb) #hat{n}-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2r_mtt300to400_beta_lt_0p9", "antitop decay (lb) #hat{r}-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2k_mtt300to400_beta_lt_0p9", "antitop decay (lb) #hat{k}-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt300to400_beta_lt_0p9", "antitop decay (lb) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt300to400_beta_lt_0p9", "antitop decay (lb) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_Cnn_mtt300to400_beta_lt_0p9", "(lb) C_{nn} (300 < m_{tt} < 400 GeV, #beta<0.9);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_Cnr_mtt300to400_beta_lt_0p9", "(lb) C_{nr} (300 < m_{tt} < 400 GeV, #beta<0.9);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_Cnk_mtt300to400_beta_lt_0p9", "(lb) C_{nk} (300 < m_{tt} < 400 GeV, #beta<0.9);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_Crn_mtt300to400_beta_lt_0p9", "(lb) C_{rn} (300 < m_{tt} < 400 GeV, #beta<0.9);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_Crr_mtt300to400_beta_lt_0p9", "(lb) C_{rr} (300 < m_{tt} < 400 GeV, #beta<0.9);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_Crk_mtt300to400_beta_lt_0p9", "(lb) C_{rk} (300 < m_{tt} < 400 GeV, #beta<0.9);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_Ckn_mtt300to400_beta_lt_0p9", "(lb) C_{kn} (300 < m_{tt} < 400 GeV, #beta<0.9);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_Ckr_mtt300to400_beta_lt_0p9", "(lb) C_{kr} (300 < m_{tt} < 400 GeV, #beta<0.9);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_Ckk_mtt300to400_beta_lt_0p9", "(lb) C_{kk} (300 < m_{tt} < 400 GeV, #beta<0.9);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_trC_mtt300to400_beta_lt_0p9", "Trace of Correlation Matrix (300 < m_{tt} < 400 GeV, #beta<0.9);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_cHel_mtt300to400_beta_lt_0p9", "(lb) Cosine Helicity Angle (300 < m_{tt} < 400 GeV, #beta < 0.9);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_cHel_P3n_mtt300to400_beta_lt_0p9", "(lb) Cosine Helicity Angle w/P_3n (300 < m_{tt} < 400 GeV, #beta < 0.9);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1n_mtt300to400_beta_lt_0p9", "top decay (ld) #hat{n}-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1r_mtt300to400_beta_lt_0p9", "top decay (ld) #hat{r}-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1k_mtt300to400_beta_lt_0p9", "top decay (ld) #hat{k}-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt300to400_beta_lt_0p9", "top decay (ld) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt300to400_beta_lt_0p9", "top decay (ld) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2n_mtt300to400_beta_lt_0p9", "antitop decay (ld) #hat{n}-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2r_mtt300to400_beta_lt_0p9", "antitop decay (ld) #hat{r}-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2k_mtt300to400_beta_lt_0p9", "antitop decay (ld) #hat{k}-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt300to400_beta_lt_0p9", "antitop decay (ld) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt300to400_beta_lt_0p9", "antitop decay (ld) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, #beta<0.9);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_Cnn_mtt300to400_beta_lt_0p9", "(ld) C_{nn} (300 < m_{tt} < 400 GeV, #beta<0.9);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_Cnr_mtt300to400_beta_lt_0p9", "(ld) C_{nr} (300 < m_{tt} < 400 GeV, #beta<0.9);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_Cnk_mtt300to400_beta_lt_0p9", "(ld) C_{nk} (300 < m_{tt} < 400 GeV, #beta<0.9);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_Crn_mtt300to400_beta_lt_0p9", "(ld) C_{rn} (300 < m_{tt} < 400 GeV, #beta<0.9);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_Crr_mtt300to400_beta_lt_0p9", "(ld) C_{rr} (300 < m_{tt} < 400 GeV, #beta<0.9);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_Crk_mtt300to400_beta_lt_0p9", "(ld) C_{rk} (300 < m_{tt} < 400 GeV, #beta<0.9);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_Ckn_mtt300to400_beta_lt_0p9", "(ld) C_{kn} (300 < m_{tt} < 400 GeV, #beta<0.9);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_Ckr_mtt300to400_beta_lt_0p9", "(ld) C_{kr} (300 < m_{tt} < 400 GeV, #beta<0.9);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_Ckk_mtt300to400_beta_lt_0p9", "(ld) C_{kk} (300 < m_{tt} < 400 GeV, #beta<0.9);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_trC_mtt300to400_beta_lt_0p9", "Trace of Correlation Matrix (300 < m_{tt} < 400 GeV, #beta<0.9);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_cHel_mtt300to400_beta_lt_0p9", "(ld) Cosine Helicity Angle (300 < m_{tt} < 400 GeV, #beta < 0.9);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_cHel_P3n_mtt300to400_beta_lt_0p9", "(ld) Cosine Helicity Angle w/P_3n (300 < m_{tt} < 400 GeV, #beta < 0.9);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_sigmaPhi_mtt300to400_beta_lt_0p9", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, #beta<0.9);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_lb_deltaPhi_mtt300to400_beta_lt_0p9", "(lb) #Delta#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, #beta<0.9);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_sigmaPhi_mtt300to400_beta_lt_0p9", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, #beta<0.9);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt300to400_beta_lt_0p9 = ROOT.TH1F("h_ld_deltaPhi_mtt300to400_beta_lt_0p9", "(ld) #Delta#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, #beta<0.9);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

    ## |cosTSA| < 0.4
h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p4", "antilepton #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p4", "antilepton #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p4", "antilepton #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p4", "antilepton #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p4", "antilepton #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p4", "lepton #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p4", "lepton #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p4", "lepton #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p4", "lepton #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p4", "lepton #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p4", "top decay (lb) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p4", "top decay (lb) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p4", "top decay (lb) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4", "top decay (lb) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4", "top decay (lb) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p4", "antitop decay (lb) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p4", "antitop decay (lb) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p4", "antitop decay (lb) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4", "antitop decay (lb) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4", "antitop decay (lb) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Cnn_mtt300to400_cosTSA_lt_0p4", "(lb) C_{nn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Cnr_mtt300to400_cosTSA_lt_0p4", "(lb) C_{nr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Cnk_mtt300to400_cosTSA_lt_0p4", "(lb) C_{nk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Crn_mtt300to400_cosTSA_lt_0p4", "(lb) C_{rn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Crr_mtt300to400_cosTSA_lt_0p4", "(lb) C_{rr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Crk_mtt300to400_cosTSA_lt_0p4", "(lb) C_{rk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Ckn_mtt300to400_cosTSA_lt_0p4", "(lb) C_{kn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Ckr_mtt300to400_cosTSA_lt_0p4", "(lb) C_{kr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Ckk_mtt300to400_cosTSA_lt_0p4", "(lb) C_{kk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_trC_mtt300to400_cosTSA_lt_0p4", "Trace of Correlation Matrix (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cHel_mtt300to400_cosTSA_lt_0p4", "(lb) Cosine Helicity Angle (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p4", "(lb) Cosine Helicity Angle w/P_3n (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p4", "top decay (ld) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p4", "top decay (ld) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p4", "top decay (ld) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4", "top decay (ld) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4", "top decay (ld) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p4", "antitop decay (ld) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p4", "antitop decay (ld) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p4", "antitop decay (ld) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4", "antitop decay (ld) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4", "antitop decay (ld) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Cnn_mtt300to400_cosTSA_lt_0p4", "(ld) C_{nn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Cnr_mtt300to400_cosTSA_lt_0p4", "(ld) C_{nr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Cnk_mtt300to400_cosTSA_lt_0p4", "(ld) C_{nk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Crn_mtt300to400_cosTSA_lt_0p4", "(ld) C_{rn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Crr_mtt300to400_cosTSA_lt_0p4", "(ld) C_{rr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Crk_mtt300to400_cosTSA_lt_0p4", "(ld) C_{rk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Ckn_mtt300to400_cosTSA_lt_0p4", "(ld) C_{kn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Ckr_mtt300to400_cosTSA_lt_0p4", "(ld) C_{kr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Ckk_mtt300to400_cosTSA_lt_0p4", "(ld) C_{kk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_trC_mtt300to400_cosTSA_lt_0p4", "Trace of Correlation Matrix (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cHel_mtt300to400_cosTSA_lt_0p4", "(ld) Cosine Helicity Angle (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p4", "(ld) Cosine Helicity Angle w/P_3n (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_sigmaPhi_mtt300to400_cosTSA_lt_0p4", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_deltaPhi_mtt300to400_cosTSA_lt_0p4", "(lb) #Delta#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_sigmaPhi_mtt300to400_cosTSA_lt_0p4", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt300to400_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_deltaPhi_mtt300to400_cosTSA_lt_0p4", "(ld) #Delta#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

        # beta < 0.9
h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "antilepton #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "antilepton #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "antilepton #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "antilepton #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "antilepton #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "lepton #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "lepton #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "lepton #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "lepton #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "lepton #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "top decay (lb) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "top decay (lb) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "top decay (lb) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "top decay (lb) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "top decay (lb) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "antitop decay (lb) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "antitop decay (lb) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "antitop decay (lb) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "antitop decay (lb) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "antitop decay (lb) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_Cnn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(lb) C_{nn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_Cnr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(lb) C_{nr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_Cnk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(lb) C_{nk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_Crn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(lb) C_{rn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_Crr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(lb) C_{rr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_Crk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(lb) C_{rk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_Ckn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(lb) C_{kn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_Ckr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(lb) C_{kr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_Ckk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(lb) C_{kk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_trC_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "Trace of Correlation Matrix (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_cHel_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(lb) Cosine Helicity Angle (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta < 0.9);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(lb) Cosine Helicity Angle w/P_3n (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "top decay (ld) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "top decay (ld) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "top decay (ld) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "top decay (ld) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "top decay (ld) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "antitop decay (ld) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "antitop decay (ld) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "antitop decay (ld) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "antitop decay (ld) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "antitop decay (ld) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_Cnn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(ld) C_{nn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_Cnr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(ld) C_{nr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_Cnk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(ld) C_{nk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_Crn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(ld) C_{rn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_Crr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(ld) C_{rr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_Crk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(ld) C_{rk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_Ckn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(ld) C_{kn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_Ckr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(ld) C_{kr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_Ckk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(ld) C_{kk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_trC_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "Trace of Correlation Matrix (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_cHel_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(ld) Cosine Helicity Angle (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta < 0.9);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(ld) Cosine Helicity Angle w/P_3n (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_sigmaPhi_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_lb_deltaPhi_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(lb) #Delta#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_sigmaPhi_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9 = ROOT.TH1F("h_ld_deltaPhi_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9", "(ld) #Delta#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|<0.4, #beta<0.9);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

    ## |cosTSA| < 0.7
h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p7", "antilepton #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p7", "antilepton #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p7", "antilepton #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p7", "antilepton #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p7", "antilepton #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p7", "lepton #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p7", "lepton #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p7", "lepton #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p7", "lepton #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p7", "lepton #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p7", "top decay (lb) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p7", "top decay (lb) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p7", "top decay (lb) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7", "top decay (lb) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7", "top decay (lb) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p7", "antitop decay (lb) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p7", "antitop decay (lb) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p7", "antitop decay (lb) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7", "antitop decay (lb) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7", "antitop decay (lb) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Cnn_mtt300to400_cosTSA_lt_0p7", "(lb) C_{nn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Cnr_mtt300to400_cosTSA_lt_0p7", "(lb) C_{nr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Cnk_mtt300to400_cosTSA_lt_0p7", "(lb) C_{nk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Crn_mtt300to400_cosTSA_lt_0p7", "(lb) C_{rn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Crr_mtt300to400_cosTSA_lt_0p7", "(lb) C_{rr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Crk_mtt300to400_cosTSA_lt_0p7", "(lb) C_{rk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Ckn_mtt300to400_cosTSA_lt_0p7", "(lb) C_{kn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Ckr_mtt300to400_cosTSA_lt_0p7", "(lb) C_{kr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Ckk_mtt300to400_cosTSA_lt_0p7", "(lb) C_{kk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_trC_mtt300to400_cosTSA_lt_0p7", "Trace of Correlation Matrix (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cHel_mtt300to400_cosTSA_lt_0p7", "(lb) Cosine Helicity Angle (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p7", "(lb) Cosine Helicity Angle w/P_3n (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p7", "top decay (ld) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p7", "top decay (ld) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p7", "top decay (ld) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7", "top decay (ld) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7", "top decay (ld) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p7", "antitop decay (ld) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p7", "antitop decay (ld) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p7", "antitop decay (ld) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7", "antitop decay (ld) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7", "antitop decay (ld) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Cnn_mtt300to400_cosTSA_lt_0p7", "(ld) C_{nn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Cnr_mtt300to400_cosTSA_lt_0p7", "(ld) C_{nr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Cnk_mtt300to400_cosTSA_lt_0p7", "(ld) C_{nk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Crn_mtt300to400_cosTSA_lt_0p7", "(ld) C_{rn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Crr_mtt300to400_cosTSA_lt_0p7", "(ld) C_{rr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Crk_mtt300to400_cosTSA_lt_0p7", "(ld) C_{rk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Ckn_mtt300to400_cosTSA_lt_0p7", "(ld) C_{kn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Ckr_mtt300to400_cosTSA_lt_0p7", "(ld) C_{kr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Ckk_mtt300to400_cosTSA_lt_0p7", "(ld) C_{kk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_trC_mtt300to400_cosTSA_lt_0p7", "Trace of Correlation Matrix (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cHel_mtt300to400_cosTSA_lt_0p7", "(ld) Cosine Helicity Angle (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p7", "(ld) Cosine Helicity Angle w/P_3n (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_sigmaPhi_mtt300to400_cosTSA_lt_0p7", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_deltaPhi_mtt300to400_cosTSA_lt_0p7", "(lb) #Delta#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_sigmaPhi_mtt300to400_cosTSA_lt_0p7", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt300to400_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_deltaPhi_mtt300to400_cosTSA_lt_0p7", "(ld) #Delta#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

        # beta < 0.9
h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "antilepton #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "antilepton #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "antilepton #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "antilepton #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "antilepton #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "lepton #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "lepton #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "lepton #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "lepton #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "lepton #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "top decay (lb) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "top decay (lb) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "top decay (lb) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "top decay (lb) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "top decay (lb) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "antitop decay (lb) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "antitop decay (lb) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "antitop decay (lb) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "antitop decay (lb) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "antitop decay (lb) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_Cnn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(lb) C_{nn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_Cnr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(lb) C_{nr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_Cnk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(lb) C_{nk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_Crn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(lb) C_{rn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_Crr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(lb) C_{rr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_Crk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(lb) C_{rk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_Ckn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(lb) C_{kn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_Ckr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(lb) C_{kr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_Ckk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(lb) C_{kk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_trC_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "Trace of Correlation Matrix (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cHel_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(lb) Cosine Helicity Angle (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta < 0.9);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(lb) Cosine Helicity Angle w/P_3n (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "top decay (ld) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "top decay (ld) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "top decay (ld) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "top decay (ld) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "top decay (ld) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "antitop decay (ld) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "antitop decay (ld) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "antitop decay (ld) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "antitop decay (ld) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "antitop decay (ld) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_Cnn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(ld) C_{nn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_Cnr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(ld) C_{nr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_Cnk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(ld) C_{nk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_Crn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(ld) C_{rn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_Crr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(ld) C_{rr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_Crk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(ld) C_{rk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_Ckn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(ld) C_{kn} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_Ckr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(ld) C_{kr} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_Ckk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(ld) C_{kk} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_trC_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "Trace of Correlation Matrix (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cHel_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(ld) Cosine Helicity Angle (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta < 0.9);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(ld) Cosine Helicity Angle w/P_3n (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_sigmaPhi_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_deltaPhi_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(lb) #Delta#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_sigmaPhi_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_deltaPhi_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9", "(ld) #Delta#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|<0.7, #beta<0.9);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

    ## |cosTSA| > 0.7
h_cos_theta1n_antilepton_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt300to400_cosTSA_gt_0p7", "antilepton #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt300to400_cosTSA_gt_0p7", "antilepton #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt300to400_cosTSA_gt_0p7", "antilepton #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_gt_0p7", "antilepton #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_gt_0p7", "antilepton #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2n_lepton_mtt300to400_cosTSA_gt_0p7", "lepton #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2r_lepton_mtt300to400_cosTSA_gt_0p7", "lepton #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2k_lepton_mtt300to400_cosTSA_gt_0p7", "lepton #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt300to400_cosTSA_gt_0p7", "lepton #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt300to400_cosTSA_gt_0p7", "lepton #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1n_mtt300to400_cosTSA_gt_0p7", "top decay (lb) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1r_mtt300to400_cosTSA_gt_0p7", "top decay (lb) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1k_mtt300to400_cosTSA_gt_0p7", "top decay (lb) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7", "top decay (lb) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7", "top decay (lb) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2n_mtt300to400_cosTSA_gt_0p7", "antitop decay (lb) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2r_mtt300to400_cosTSA_gt_0p7", "antitop decay (lb) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2k_mtt300to400_cosTSA_gt_0p7", "antitop decay (lb) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7", "antitop decay (lb) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7", "antitop decay (lb) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Cnn_mtt300to400_cosTSA_gt_0p7", "(lb) C_{nn} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Cnr_mtt300to400_cosTSA_gt_0p7", "(lb) C_{nr} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Cnk_mtt300to400_cosTSA_gt_0p7", "(lb) C_{nk} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Crn_mtt300to400_cosTSA_gt_0p7", "(lb) C_{rn} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Crr_mtt300to400_cosTSA_gt_0p7", "(lb) C_{rr} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Crk_mtt300to400_cosTSA_gt_0p7", "(lb) C_{rk} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Ckn_mtt300to400_cosTSA_gt_0p7", "(lb) C_{kn} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Ckr_mtt300to400_cosTSA_gt_0p7", "(lb) C_{kr} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Ckk_mtt300to400_cosTSA_gt_0p7", "(lb) C_{kk} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_trC_mtt300to400_cosTSA_gt_0p7", "Trace of Correlation Matrix (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cHel_mtt300to400_cosTSA_gt_0p7", "(lb) Cosine Helicity Angle (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cHel_P3n_mtt300to400_cosTSA_gt_0p7", "(lb) Cosine Helicity Angle w/P_3n (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1n_mtt300to400_cosTSA_gt_0p7", "top decay (ld) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1r_mtt300to400_cosTSA_gt_0p7", "top decay (ld) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1k_mtt300to400_cosTSA_gt_0p7", "top decay (ld) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7", "top decay (ld) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7", "top decay (ld) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2n_mtt300to400_cosTSA_gt_0p7", "antitop decay (ld) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2r_mtt300to400_cosTSA_gt_0p7", "antitop decay (ld) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2k_mtt300to400_cosTSA_gt_0p7", "antitop decay (ld) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7", "antitop decay (ld) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7", "antitop decay (ld) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Cnn_mtt300to400_cosTSA_gt_0p7", "(ld) C_{nn} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Cnr_mtt300to400_cosTSA_gt_0p7", "(ld) C_{nr} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Cnk_mtt300to400_cosTSA_gt_0p7", "(ld) C_{nk} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Crn_mtt300to400_cosTSA_gt_0p7", "(ld) C_{rn} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Crr_mtt300to400_cosTSA_gt_0p7", "(ld) C_{rr} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Crk_mtt300to400_cosTSA_gt_0p7", "(ld) C_{rk} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Ckn_mtt300to400_cosTSA_gt_0p7", "(ld) C_{kn} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Ckr_mtt300to400_cosTSA_gt_0p7", "(ld) C_{kr} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Ckk_mtt300to400_cosTSA_gt_0p7", "(ld) C_{kk} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_trC_mtt300to400_cosTSA_gt_0p7", "Trace of Correlation Matrix (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cHel_mtt300to400_cosTSA_gt_0p7", "(ld) Cosine Helicity Angle (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cHel_P3n_mtt300to400_cosTSA_gt_0p7", "(ld) Cosine Helicity Angle w/P_3n (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_sigmaPhi_mtt300to400_cosTSA_gt_0p7", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_deltaPhi_mtt300to400_cosTSA_gt_0p7", "(lb) #Delta#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_sigmaPhi_mtt300to400_cosTSA_gt_0p7", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt300to400_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_deltaPhi_mtt300to400_cosTSA_gt_0p7", "(ld) #Delta#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

        # beta < 0.9
h_cos_theta1n_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "antilepton #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "antilepton #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "antilepton #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "antilepton #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "antilepton #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2n_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "lepton #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2r_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "lepton #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2k_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "lepton #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "lepton #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "lepton #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "top decay (lb) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "top decay (lb) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0p9);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "top decay (lb) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "top decay (lb) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "top decay (lb) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "antitop decay (lb) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "antitop decay (lb) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "antitop decay (lb) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "antitop decay (lb) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "antitop decay (lb) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_Cnn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(lb) C_{nn} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_Cnr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(lb) C_{nr} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_Cnk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(lb) C_{nk} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_Crn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(lb) C_{rn} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_Crr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(lb) C_{rr} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_Crk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(lb) C_{rk} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_Ckn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(lb) C_{kn} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_Ckr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(lb) C_{kr} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_Ckk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(lb) C_{kk} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_trC_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "Trace of Correlation Matrix (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cHel_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(lb) Cosine Helicity Angle (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta < 0.9);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_cHel_P3n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(lb) Cosine Helicity Angle w/P_3n (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "top decay (ld) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "top decay (ld) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "top decay (ld) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "top decay (ld) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "top decay (ld) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "antitop decay (ld) #hat{n}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "antitop decay (ld) #hat{r}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "antitop decay (ld) #hat{k}-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "antitop decay (ld) #hat{r}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "antitop decay (ld) #hat{k}*-polarization (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_Cnn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(ld) C_{nn} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_Cnr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(ld) C_{nr} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_Cnk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(ld) C_{nk} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_Crn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(ld) C_{rn} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_Crr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(ld) C_{rr} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_Crk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(ld) C_{rk} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_Ckn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(ld) C_{kn} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_Ckr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(ld) C_{kr} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_Ckk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(ld) C_{kk} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_trC_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "Trace of Correlation Matrix (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cHel_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(ld) Cosine Helicity Angle (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta < 0.9);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_cHel_P3n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(ld) Cosine Helicity Angle w/P_3n (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_sigmaPhi_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_lb_deltaPhi_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(lb) #Delta#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_sigmaPhi_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9 = ROOT.TH1F("h_ld_deltaPhi_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9", "(ld) #Delta#phi_{#hat{n}#hat{r}} (300 < m_{tt} < 400 GeV, |cosTSA|>0.7, #beta<0.9);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

### mtt [400, 600] GeV
h_cos_theta1n_antilepton_mtt400to600 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt400to600", "antilepton #hat{n}-polarization (400 < m_{tt} < 600 GeV);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt400to600 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt400to600", "antilepton #hat{r}-polarization (400 < m_{tt} < 600 GeV);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt400to600 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt400to600", "antilepton #hat{k}-polarization (400 < m_{tt} < 600 GeV);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt400to600 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt400to600", "antilepton #hat{r}*-polarization (400 < m_{tt} < 600 GeV);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt400to600 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt400to600", "antilepton #hat{k}*-polarization (400 < m_{tt} < 600 GeV);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt400to600 = ROOT.TH1F("h_cos_theta2n_lepton_mtt400to600", "lepton #hat{n}-polarization (400 < m_{tt} < 600 GeV);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt400to600 = ROOT.TH1F("h_cos_theta2r_lepton_mtt400to600", "lepton #hat{r}-polarization (400 < m_{tt} < 600 GeV);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt400to600 = ROOT.TH1F("h_cos_theta2k_lepton_mtt400to600", "lepton #hat{k}-polarization (400 < m_{tt} < 600 GeV);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt400to600 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt400to600", "lepton #hat{r}*-polarization (400 < m_{tt} < 600 GeV);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt400to600 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt400to600", "lepton #hat{k}*-polarization (400 < m_{tt} < 600 GeV);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt400to600 = ROOT.TH1F("h_lb_cos_theta1n_mtt400to600", "top decay (lb) #hat{n}-polarization (400 < m_{tt} < 600 GeV);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt400to600 = ROOT.TH1F("h_lb_cos_theta1r_mtt400to600", "top decay (lb) #hat{r}-polarization (400 < m_{tt} < 600 GeV);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt400to600 = ROOT.TH1F("h_lb_cos_theta1k_mtt400to600", "top decay (lb) #hat{k}-polarization (400 < m_{tt} < 600 GeV);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt400to600 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt400to600", "top decay (lb) #hat{r}*-polarization (400 < m_{tt} < 600 GeV);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt400to600 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt400to600", "top decay (lb) #hat{k}*-polarization (400 < m_{tt} < 600 GeV);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt400to600 = ROOT.TH1F("h_lb_cos_theta2n_mtt400to600", "antitop decay (lb) #hat{n}-polarization (400 < m_{tt} < 600 GeV);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt400to600 = ROOT.TH1F("h_lb_cos_theta2r_mtt400to600", "antitop decay (lb) #hat{r}-polarization (400 < m_{tt} < 600 GeV);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt400to600 = ROOT.TH1F("h_lb_cos_theta2k_mtt400to600", "antitop decay (lb) #hat{k}-polarization (400 < m_{tt} < 600 GeV);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt400to600 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt400to600", "antitop decay (lb) #hat{r}*-polarization (400 < m_{tt} < 600 GeV);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt400to600 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt400to600", "antitop decay (lb) #hat{k}*-polarization (400 < m_{tt} < 600 GeV);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt400to600 = ROOT.TH1F("h_lb_Cnn_mtt400to600", "(lb) C_{nn} (400 < m_{tt} < 600 GeV);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt400to600 = ROOT.TH1F("h_lb_Cnr_mtt400to600", "(lb) C_{nr} (400 < m_{tt} < 600 GeV);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt400to600 = ROOT.TH1F("h_lb_Cnk_mtt400to600", "(lb) C_{nk} (400 < m_{tt} < 600 GeV);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt400to600 = ROOT.TH1F("h_lb_Crn_mtt400to600", "(lb) C_{rn} (400 < m_{tt} < 600 GeV);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt400to600 = ROOT.TH1F("h_lb_Crr_mtt400to600", "(lb) C_{rr} (400 < m_{tt} < 600 GeV);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt400to600 = ROOT.TH1F("h_lb_Crk_mtt400to600", "(lb) C_{rk} (400 < m_{tt} < 600 GeV);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt400to600 = ROOT.TH1F("h_lb_Ckn_mtt400to600", "(lb) C_{kn} (400 < m_{tt} < 600 GeV);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt400to600 = ROOT.TH1F("h_lb_Ckr_mtt400to600", "(lb) C_{kr} (400 < m_{tt} < 600 GeV);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt400to600 = ROOT.TH1F("h_lb_Ckk_mtt400to600", "(lb) C_{kk} (400 < m_{tt} < 600 GeV);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt400to600 = ROOT.TH1F("h_lb_trC_mtt400to600", "Trace of Correlation Matrix (400 < m_{tt} < 600 GeV);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt400to600 = ROOT.TH1F("h_lb_cHel_mtt400to600", "(lb) Cosine Helicity Angle (400 < m_{tt} < 600 GeV);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt400to600 = ROOT.TH1F("h_lb_cHel_P3n_mtt400to600", "(lb) Cosine Helicity Angle w/P_3n (400 < m_{tt} < 600 GeV);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt400to600 = ROOT.TH1F("h_ld_cos_theta1n_mtt400to600", "top decay (ld) #hat{n}-polarization (400 < m_{tt} < 600 GeV);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt400to600 = ROOT.TH1F("h_ld_cos_theta1r_mtt400to600", "top decay (ld) #hat{r}-polarization (400 < m_{tt} < 600 GeV);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt400to600 = ROOT.TH1F("h_ld_cos_theta1k_mtt400to600", "top decay (ld) #hat{k}-polarization (400 < m_{tt} < 600 GeV);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt400to600 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt400to600", "top decay (ld) #hat{r}*-polarization (400 < m_{tt} < 600 GeV);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt400to600 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt400to600", "top decay (ld) #hat{k}*-polarization (400 < m_{tt} < 600 GeV);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt400to600 = ROOT.TH1F("h_ld_cos_theta2n_mtt400to600", "antitop decay (ld) #hat{n}-polarization (400 < m_{tt} < 600 GeV);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt400to600 = ROOT.TH1F("h_ld_cos_theta2r_mtt400to600", "antitop decay (ld) #hat{r}-polarization (400 < m_{tt} < 600 GeV);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt400to600 = ROOT.TH1F("h_ld_cos_theta2k_mtt400to600", "antitop decay (ld) #hat{k}-polarization (400 < m_{tt} < 600 GeV);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt400to600 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt400to600", "antitop decay (ld) #hat{r}*-polarization (400 < m_{tt} < 600 GeV);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt400to600 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt400to600", "antitop decay (ld) #hat{k}*-polarization (400 < m_{tt} < 600 GeV);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt400to600 = ROOT.TH1F("h_ld_Cnn_mtt400to600", "(ld) C_{nn} (400 < m_{tt} < 600 GeV);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt400to600 = ROOT.TH1F("h_ld_Cnr_mtt400to600", "(ld) C_{nr} (400 < m_{tt} < 600 GeV);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt400to600 = ROOT.TH1F("h_ld_Cnk_mtt400to600", "(ld) C_{nk} (400 < m_{tt} < 600 GeV);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt400to600 = ROOT.TH1F("h_ld_Crn_mtt400to600", "(ld) C_{rn} (400 < m_{tt} < 600 GeV);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt400to600 = ROOT.TH1F("h_ld_Crr_mtt400to600", "(ld) C_{rr} (400 < m_{tt} < 600 GeV);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt400to600 = ROOT.TH1F("h_ld_Crk_mtt400to600", "(ld) C_{rk} (400 < m_{tt} < 600 GeV);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt400to600 = ROOT.TH1F("h_ld_Ckn_mtt400to600", "(ld) C_{kn} (400 < m_{tt} < 600 GeV);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt400to600 = ROOT.TH1F("h_ld_Ckr_mtt400to600", "(ld) C_{kr} (400 < m_{tt} < 600 GeV);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt400to600 = ROOT.TH1F("h_ld_Ckk_mtt400to600", "(ld) C_{kk} (400 < m_{tt} < 600 GeV);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt400to600 = ROOT.TH1F("h_ld_trC_mtt400to600", "Trace of Correlation Matrix (400 < m_{tt} < 600 GeV);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt400to600 = ROOT.TH1F("h_ld_cHel_mtt400to600", "(ld) Cosine Helicity Angle (400 < m_{tt} < 600 GeV);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt400to600 = ROOT.TH1F("h_ld_cHel_P3n_mtt400to600", "(ld) Cosine Helicity Angle w/P_3n (400 < m_{tt} < 600 GeV);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt400to600 = ROOT.TH1F("h_lb_sigmaPhi_mtt400to600", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (400 < m_{tt} < 600 GeV);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt400to600 = ROOT.TH1F("h_lb_deltaPhi_mtt400to600", "(lb) #Delta#phi_{#hat{n}#hat{r}} (400 < m_{tt} < 600 GeV);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt400to600 = ROOT.TH1F("h_ld_sigmaPhi_mtt400to600", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (400 < m_{tt} < 600 GeV);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt400to600 = ROOT.TH1F("h_ld_deltaPhi_mtt400to600", "(ld) #Delta#phi_{#hat{n}#hat{r}} (400 < m_{tt} < 600 GeV);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

    ## |cosTSA| < 0.4
h_cos_theta1n_antilepton_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt400to600_cosTSA_lt_0p4", "antilepton #hat{n}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt400to600_cosTSA_lt_0p4", "antilepton #hat{r}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt400to600_cosTSA_lt_0p4", "antilepton #hat{k}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt400to600_cosTSA_lt_0p4", "antilepton #hat{r}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt400to600_cosTSA_lt_0p4", "antilepton #hat{k}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2n_lepton_mtt400to600_cosTSA_lt_0p4", "lepton #hat{n}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2r_lepton_mtt400to600_cosTSA_lt_0p4", "lepton #hat{r}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2k_lepton_mtt400to600_cosTSA_lt_0p4", "lepton #hat{k}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt400to600_cosTSA_lt_0p4", "lepton #hat{r}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt400to600_cosTSA_lt_0p4", "lepton #hat{k}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1n_mtt400to600_cosTSA_lt_0p4", "top decay (lb) #hat{n}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1r_mtt400to600_cosTSA_lt_0p4", "top decay (lb) #hat{r}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1k_mtt400to600_cosTSA_lt_0p4", "top decay (lb) #hat{k}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt400to600_cosTSA_lt_0p4", "top decay (lb) #hat{r}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt400to600_cosTSA_lt_0p4", "top decay (lb) #hat{k}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2n_mtt400to600_cosTSA_lt_0p4", "antitop decay (lb) #hat{n}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2r_mtt400to600_cosTSA_lt_0p4", "antitop decay (lb) #hat{r}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2k_mtt400to600_cosTSA_lt_0p4", "antitop decay (lb) #hat{k}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt400to600_cosTSA_lt_0p4", "antitop decay (lb) #hat{r}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt400to600_cosTSA_lt_0p4", "antitop decay (lb) #hat{k}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Cnn_mtt400to600_cosTSA_lt_0p4", "(lb) C_{nn} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Cnr_mtt400to600_cosTSA_lt_0p4", "(lb) C_{nr} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Cnk_mtt400to600_cosTSA_lt_0p4", "(lb) C_{nk} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Crn_mtt400to600_cosTSA_lt_0p4", "(lb) C_{rn} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Crr_mtt400to600_cosTSA_lt_0p4", "(lb) C_{rr} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Crk_mtt400to600_cosTSA_lt_0p4", "(lb) C_{rk} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Ckn_mtt400to600_cosTSA_lt_0p4", "(lb) C_{kn} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Ckr_mtt400to600_cosTSA_lt_0p4", "(lb) C_{kr} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Ckk_mtt400to600_cosTSA_lt_0p4", "(lb) C_{kk} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_trC_mtt400to600_cosTSA_lt_0p4", "Trace of Correlation Matrix (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cHel_mtt400to600_cosTSA_lt_0p4", "(lb) Cosine Helicity Angle (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cHel_P3n_mtt400to600_cosTSA_lt_0p4", "(lb) Cosine Helicity Angle w/P_3n (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1n_mtt400to600_cosTSA_lt_0p4", "top decay (ld) #hat{n}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1r_mtt400to600_cosTSA_lt_0p4", "top decay (ld) #hat{r}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1k_mtt400to600_cosTSA_lt_0p4", "top decay (ld) #hat{k}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt400to600_cosTSA_lt_0p4", "top decay (ld) #hat{r}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt400to600_cosTSA_lt_0p4", "top decay (ld) #hat{k}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2n_mtt400to600_cosTSA_lt_0p4", "antitop decay (ld) #hat{n}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2r_mtt400to600_cosTSA_lt_0p4", "antitop decay (ld) #hat{r}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2k_mtt400to600_cosTSA_lt_0p4", "antitop decay (ld) #hat{k}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt400to600_cosTSA_lt_0p4", "antitop decay (ld) #hat{r}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt400to600_cosTSA_lt_0p4", "antitop decay (ld) #hat{k}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Cnn_mtt400to600_cosTSA_lt_0p4", "(ld) C_{nn} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Cnr_mtt400to600_cosTSA_lt_0p4", "(ld) C_{nr} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Cnk_mtt400to600_cosTSA_lt_0p4", "(ld) C_{nk} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Crn_mtt400to600_cosTSA_lt_0p4", "(ld) C_{rn} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Crr_mtt400to600_cosTSA_lt_0p4", "(ld) C_{rr} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Crk_mtt400to600_cosTSA_lt_0p4", "(ld) C_{rk} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Ckn_mtt400to600_cosTSA_lt_0p4", "(ld) C_{kn} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Ckr_mtt400to600_cosTSA_lt_0p4", "(ld) C_{kr} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Ckk_mtt400to600_cosTSA_lt_0p4", "(ld) C_{kk} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_trC_mtt400to600_cosTSA_lt_0p4", "Trace of Correlation Matrix (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cHel_mtt400to600_cosTSA_lt_0p4", "(ld) Cosine Helicity Angle (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cHel_P3n_mtt400to600_cosTSA_lt_0p4", "(ld) Cosine Helicity Angle w/P_3n (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_sigmaPhi_mtt400to600_cosTSA_lt_0p4", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_deltaPhi_mtt400to600_cosTSA_lt_0p4", "(lb) #Delta#phi_{#hat{n}#hat{r}} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_sigmaPhi_mtt400to600_cosTSA_lt_0p4", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt400to600_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_deltaPhi_mtt400to600_cosTSA_lt_0p4", "(ld) #Delta#phi_{#hat{n}#hat{r}} (400 < m_{tt} < 600 GeV, |cosTSA|<0.4);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

    ## |cosTSA| < 0.7
h_cos_theta1n_antilepton_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt400to600_cosTSA_lt_0p7", "antilepton #hat{n}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt400to600_cosTSA_lt_0p7", "antilepton #hat{r}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt400to600_cosTSA_lt_0p7", "antilepton #hat{k}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt400to600_cosTSA_lt_0p7", "antilepton #hat{r}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt400to600_cosTSA_lt_0p7", "antilepton #hat{k}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2n_lepton_mtt400to600_cosTSA_lt_0p7", "lepton #hat{n}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2r_lepton_mtt400to600_cosTSA_lt_0p7", "lepton #hat{r}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2k_lepton_mtt400to600_cosTSA_lt_0p7", "lepton #hat{k}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt400to600_cosTSA_lt_0p7", "lepton #hat{r}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt400to600_cosTSA_lt_0p7", "lepton #hat{k}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1n_mtt400to600_cosTSA_lt_0p7", "top decay (lb) #hat{n}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1r_mtt400to600_cosTSA_lt_0p7", "top decay (lb) #hat{r}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1k_mtt400to600_cosTSA_lt_0p7", "top decay (lb) #hat{k}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt400to600_cosTSA_lt_0p7", "top decay (lb) #hat{r}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt400to600_cosTSA_lt_0p7", "top decay (lb) #hat{k}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2n_mtt400to600_cosTSA_lt_0p7", "antitop decay (lb) #hat{n}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2r_mtt400to600_cosTSA_lt_0p7", "antitop decay (lb) #hat{r}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2k_mtt400to600_cosTSA_lt_0p7", "antitop decay (lb) #hat{k}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt400to600_cosTSA_lt_0p7", "antitop decay (lb) #hat{r}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt400to600_cosTSA_lt_0p7", "antitop decay (lb) #hat{k}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Cnn_mtt400to600_cosTSA_lt_0p7", "(lb) C_{nn} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Cnr_mtt400to600_cosTSA_lt_0p7", "(lb) C_{nr} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Cnk_mtt400to600_cosTSA_lt_0p7", "(lb) C_{nk} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Crn_mtt400to600_cosTSA_lt_0p7", "(lb) C_{rn} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Crr_mtt400to600_cosTSA_lt_0p7", "(lb) C_{rr} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Crk_mtt400to600_cosTSA_lt_0p7", "(lb) C_{rk} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Ckn_mtt400to600_cosTSA_lt_0p7", "(lb) C_{kn} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Ckr_mtt400to600_cosTSA_lt_0p7", "(lb) C_{kr} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Ckk_mtt400to600_cosTSA_lt_0p7", "(lb) C_{kk} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_trC_mtt400to600_cosTSA_lt_0p7", "Trace of Correlation Matrix (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cHel_mtt400to600_cosTSA_lt_0p7", "(lb) Cosine Helicity Angle (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cHel_P3n_mtt400to600_cosTSA_lt_0p7", "(lb) Cosine Helicity Angle w/P_3n (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1n_mtt400to600_cosTSA_lt_0p7", "top decay (ld) #hat{n}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1r_mtt400to600_cosTSA_lt_0p7", "top decay (ld) #hat{r}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1k_mtt400to600_cosTSA_lt_0p7", "top decay (ld) #hat{k}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt400to600_cosTSA_lt_0p7", "top decay (ld) #hat{r}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt400to600_cosTSA_lt_0p7", "top decay (ld) #hat{k}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2n_mtt400to600_cosTSA_lt_0p7", "antitop decay (ld) #hat{n}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2r_mtt400to600_cosTSA_lt_0p7", "antitop decay (ld) #hat{r}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2k_mtt400to600_cosTSA_lt_0p7", "antitop decay (ld) #hat{k}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt400to600_cosTSA_lt_0p7", "antitop decay (ld) #hat{r}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt400to600_cosTSA_lt_0p7", "antitop decay (ld) #hat{k}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Cnn_mtt400to600_cosTSA_lt_0p7", "(ld) C_{nn} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Cnr_mtt400to600_cosTSA_lt_0p7", "(ld) C_{nr} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Cnk_mtt400to600_cosTSA_lt_0p7", "(ld) C_{nk} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Crn_mtt400to600_cosTSA_lt_0p7", "(ld) C_{rn} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Crr_mtt400to600_cosTSA_lt_0p7", "(ld) C_{rr} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Crk_mtt400to600_cosTSA_lt_0p7", "(ld) C_{rk} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Ckn_mtt400to600_cosTSA_lt_0p7", "(ld) C_{kn} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Ckr_mtt400to600_cosTSA_lt_0p7", "(ld) C_{kr} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Ckk_mtt400to600_cosTSA_lt_0p7", "(ld) C_{kk} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_trC_mtt400to600_cosTSA_lt_0p7", "Trace of Correlation Matrix (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cHel_mtt400to600_cosTSA_lt_0p7", "(ld) Cosine Helicity Angle (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cHel_P3n_mtt400to600_cosTSA_lt_0p7", "(ld) Cosine Helicity Angle w/P_3n (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_sigmaPhi_mtt400to600_cosTSA_lt_0p7", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_deltaPhi_mtt400to600_cosTSA_lt_0p7", "(lb) #Delta#phi_{#hat{n}#hat{r}} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_sigmaPhi_mtt400to600_cosTSA_lt_0p7", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt400to600_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_deltaPhi_mtt400to600_cosTSA_lt_0p7", "(ld) #Delta#phi_{#hat{n}#hat{r}} (400 < m_{tt} < 600 GeV, |cosTSA|<0.7);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

    ## |cosTSA| > 0.7
h_cos_theta1n_antilepton_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt400to600_cosTSA_gt_0p7", "antilepton #hat{n}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt400to600_cosTSA_gt_0p7", "antilepton #hat{r}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt400to600_cosTSA_gt_0p7", "antilepton #hat{k}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt400to600_cosTSA_gt_0p7", "antilepton #hat{r}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt400to600_cosTSA_gt_0p7", "antilepton #hat{k}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2n_lepton_mtt400to600_cosTSA_gt_0p7", "lepton #hat{n}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2r_lepton_mtt400to600_cosTSA_gt_0p7", "lepton #hat{r}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2k_lepton_mtt400to600_cosTSA_gt_0p7", "lepton #hat{k}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt400to600_cosTSA_gt_0p7", "lepton #hat{r}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt400to600_cosTSA_gt_0p7", "lepton #hat{k}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1n_mtt400to600_cosTSA_gt_0p7", "top decay (lb) #hat{n}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1r_mtt400to600_cosTSA_gt_0p7", "top decay (lb) #hat{r}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1k_mtt400to600_cosTSA_gt_0p7", "top decay (lb) #hat{k}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt400to600_cosTSA_gt_0p7", "top decay (lb) #hat{r}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt400to600_cosTSA_gt_0p7", "top decay (lb) #hat{k}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2n_mtt400to600_cosTSA_gt_0p7", "antitop decay (lb) #hat{n}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2r_mtt400to600_cosTSA_gt_0p7", "antitop decay (lb) #hat{r}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2k_mtt400to600_cosTSA_gt_0p7", "antitop decay (lb) #hat{k}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt400to600_cosTSA_gt_0p7", "antitop decay (lb) #hat{r}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt400to600_cosTSA_gt_0p7", "antitop decay (lb) #hat{k}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Cnn_mtt400to600_cosTSA_gt_0p7", "(lb) C_{nn} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Cnr_mtt400to600_cosTSA_gt_0p7", "(lb) C_{nr} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Cnk_mtt400to600_cosTSA_gt_0p7", "(lb) C_{nk} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Crn_mtt400to600_cosTSA_gt_0p7", "(lb) C_{rn} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Crr_mtt400to600_cosTSA_gt_0p7", "(lb) C_{rr} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Crk_mtt400to600_cosTSA_gt_0p7", "(lb) C_{rk} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Ckn_mtt400to600_cosTSA_gt_0p7", "(lb) C_{kn} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Ckr_mtt400to600_cosTSA_gt_0p7", "(lb) C_{kr} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Ckk_mtt400to600_cosTSA_gt_0p7", "(lb) C_{kk} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_trC_mtt400to600_cosTSA_gt_0p7", "Trace of Correlation Matrix (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cHel_mtt400to600_cosTSA_gt_0p7", "(lb) Cosine Helicity Angle (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cHel_P3n_mtt400to600_cosTSA_gt_0p7", "(lb) Cosine Helicity Angle w/P_3n (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1n_mtt400to600_cosTSA_gt_0p7", "top decay (ld) #hat{n}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1r_mtt400to600_cosTSA_gt_0p7", "top decay (ld) #hat{r}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1k_mtt400to600_cosTSA_gt_0p7", "top decay (ld) #hat{k}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt400to600_cosTSA_gt_0p7", "top decay (ld) #hat{r}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt400to600_cosTSA_gt_0p7", "top decay (ld) #hat{k}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2n_mtt400to600_cosTSA_gt_0p7", "antitop decay (ld) #hat{n}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2r_mtt400to600_cosTSA_gt_0p7", "antitop decay (ld) #hat{r}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2k_mtt400to600_cosTSA_gt_0p7", "antitop decay (ld) #hat{k}-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt400to600_cosTSA_gt_0p7", "antitop decay (ld) #hat{r}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt400to600_cosTSA_gt_0p7", "antitop decay (ld) #hat{k}*-polarization (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Cnn_mtt400to600_cosTSA_gt_0p7", "(ld) C_{nn} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Cnr_mtt400to600_cosTSA_gt_0p7", "(ld) C_{nr} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Cnk_mtt400to600_cosTSA_gt_0p7", "(ld) C_{nk} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Crn_mtt400to600_cosTSA_gt_0p7", "(ld) C_{rn} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Crr_mtt400to600_cosTSA_gt_0p7", "(ld) C_{rr} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Crk_mtt400to600_cosTSA_gt_0p7", "(ld) C_{rk} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Ckn_mtt400to600_cosTSA_gt_0p7", "(ld) C_{kn} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Ckr_mtt400to600_cosTSA_gt_0p7", "(ld) C_{kr} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Ckk_mtt400to600_cosTSA_gt_0p7", "(ld) C_{kk} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_trC_mtt400to600_cosTSA_gt_0p7", "Trace of Correlation Matrix (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cHel_mtt400to600_cosTSA_gt_0p7", "(ld) Cosine Helicity Angle (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cHel_P3n_mtt400to600_cosTSA_gt_0p7", "(ld) Cosine Helicity Angle w/P_3n (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_sigmaPhi_mtt400to600_cosTSA_gt_0p7", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_deltaPhi_mtt400to600_cosTSA_gt_0p7", "(lb) #Delta#phi_{#hat{n}#hat{r}} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_sigmaPhi_mtt400to600_cosTSA_gt_0p7", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt400to600_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_deltaPhi_mtt400to600_cosTSA_gt_0p7", "(ld) #Delta#phi_{#hat{n}#hat{r}} (400 < m_{tt} < 600 GeV, |cosTSA|>0.7);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

### mtt [600, 800] GeV
h_cos_theta1n_antilepton_mtt600to800 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt600to800", "antilepton #hat{n}-polarization (600 < m_{tt} < 800 GeV);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt600to800 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt600to800", "antilepton #hat{r}-polarization (600 < m_{tt} < 800 GeV);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt600to800 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt600to800", "antilepton #hat{k}-polarization (600 < m_{tt} < 800 GeV);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt600to800 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt600to800", "antilepton #hat{r}*-polarization (600 < m_{tt} < 800 GeV);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt600to800 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt600to800", "antilepton #hat{k}*-polarization (600 < m_{tt} < 800 GeV);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt600to800 = ROOT.TH1F("h_cos_theta2n_lepton_mtt600to800", "lepton #hat{n}-polarization (600 < m_{tt} < 800 GeV);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt600to800 = ROOT.TH1F("h_cos_theta2r_lepton_mtt600to800", "lepton #hat{r}-polarization (600 < m_{tt} < 800 GeV);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt600to800 = ROOT.TH1F("h_cos_theta2k_lepton_mtt600to800", "lepton #hat{k}-polarization (600 < m_{tt} < 800 GeV);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt600to800 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt600to800", "lepton #hat{r}*-polarization (600 < m_{tt} < 800 GeV);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt600to800 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt600to800", "lepton #hat{k}*-polarization (600 < m_{tt} < 800 GeV);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt600to800 = ROOT.TH1F("h_lb_cos_theta1n_mtt600to800", "top decay (lb) #hat{n}-polarization (600 < m_{tt} < 800 GeV);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt600to800 = ROOT.TH1F("h_lb_cos_theta1r_mtt600to800", "top decay (lb) #hat{r}-polarization (600 < m_{tt} < 800 GeV);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt600to800 = ROOT.TH1F("h_lb_cos_theta1k_mtt600to800", "top decay (lb) #hat{k}-polarization (600 < m_{tt} < 800 GeV);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt600to800 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt600to800", "top decay (lb) #hat{r}*-polarization (600 < m_{tt} < 800 GeV);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt600to800 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt600to800", "top decay (lb) #hat{k}*-polarization (600 < m_{tt} < 800 GeV);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt600to800 = ROOT.TH1F("h_lb_cos_theta2n_mtt600to800", "antitop decay (lb) #hat{n}-polarization (600 < m_{tt} < 800 GeV);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt600to800 = ROOT.TH1F("h_lb_cos_theta2r_mtt600to800", "antitop decay (lb) #hat{r}-polarization (600 < m_{tt} < 800 GeV);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt600to800 = ROOT.TH1F("h_lb_cos_theta2k_mtt600to800", "antitop decay (lb) #hat{k}-polarization (600 < m_{tt} < 800 GeV);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt600to800 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt600to800", "antitop decay (lb) #hat{r}*-polarization (600 < m_{tt} < 800 GeV);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt600to800 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt600to800", "antitop decay (lb) #hat{k}*-polarization (600 < m_{tt} < 800 GeV);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt600to800 = ROOT.TH1F("h_lb_Cnn_mtt600to800", "(lb) C_{nn} (600 < m_{tt} < 800 GeV);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt600to800 = ROOT.TH1F("h_lb_Cnr_mtt600to800", "(lb) C_{nr} (600 < m_{tt} < 800 GeV);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt600to800 = ROOT.TH1F("h_lb_Cnk_mtt600to800", "(lb) C_{nk} (600 < m_{tt} < 800 GeV);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt600to800 = ROOT.TH1F("h_lb_Crn_mtt600to800", "(lb) C_{rn} (600 < m_{tt} < 800 GeV);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt600to800 = ROOT.TH1F("h_lb_Crr_mtt600to800", "(lb) C_{rr} (600 < m_{tt} < 800 GeV);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt600to800 = ROOT.TH1F("h_lb_Crk_mtt600to800", "(lb) C_{rk} (600 < m_{tt} < 800 GeV);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt600to800 = ROOT.TH1F("h_lb_Ckn_mtt600to800", "(lb) C_{kn} (600 < m_{tt} < 800 GeV);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt600to800 = ROOT.TH1F("h_lb_Ckr_mtt600to800", "(lb) C_{kr} (600 < m_{tt} < 800 GeV);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt600to800 = ROOT.TH1F("h_lb_Ckk_mtt600to800", "(lb) C_{kk} (600 < m_{tt} < 800 GeV);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt600to800 = ROOT.TH1F("h_lb_trC_mtt600to800", "Trace of Correlation Matrix (600 < m_{tt} < 800 GeV);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt600to800 = ROOT.TH1F("h_lb_cHel_mtt600to800", "(lb) Cosine Helicity Angle (600 < m_{tt} < 800 GeV);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt600to800 = ROOT.TH1F("h_lb_cHel_P3n_mtt600to800", "(lb) Cosine Helicity Angle w/P_3n (600 < m_{tt} < 800 GeV);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt600to800 = ROOT.TH1F("h_ld_cos_theta1n_mtt600to800", "top decay (ld) #hat{n}-polarization (600 < m_{tt} < 800 GeV);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt600to800 = ROOT.TH1F("h_ld_cos_theta1r_mtt600to800", "top decay (ld) #hat{r}-polarization (600 < m_{tt} < 800 GeV);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt600to800 = ROOT.TH1F("h_ld_cos_theta1k_mtt600to800", "top decay (ld) #hat{k}-polarization (600 < m_{tt} < 800 GeV);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt600to800 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt600to800", "top decay (ld) #hat{r}*-polarization (600 < m_{tt} < 800 GeV);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt600to800 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt600to800", "top decay (ld) #hat{k}*-polarization (600 < m_{tt} < 800 GeV);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt600to800 = ROOT.TH1F("h_ld_cos_theta2n_mtt600to800", "antitop decay (ld) #hat{n}-polarization (600 < m_{tt} < 800 GeV);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt600to800 = ROOT.TH1F("h_ld_cos_theta2r_mtt600to800", "antitop decay (ld) #hat{r}-polarization (600 < m_{tt} < 800 GeV);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt600to800 = ROOT.TH1F("h_ld_cos_theta2k_mtt600to800", "antitop decay (ld) #hat{k}-polarization (600 < m_{tt} < 800 GeV);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt600to800 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt600to800", "antitop decay (ld) #hat{r}*-polarization (600 < m_{tt} < 800 GeV);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt600to800 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt600to800", "antitop decay (ld) #hat{k}*-polarization (600 < m_{tt} < 800 GeV);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt600to800 = ROOT.TH1F("h_ld_Cnn_mtt600to800", "(ld) C_{nn} (600 < m_{tt} < 800 GeV);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt600to800 = ROOT.TH1F("h_ld_Cnr_mtt600to800", "(ld) C_{nr} (600 < m_{tt} < 800 GeV);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt600to800 = ROOT.TH1F("h_ld_Cnk_mtt600to800", "(ld) C_{nk} (600 < m_{tt} < 800 GeV);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt600to800 = ROOT.TH1F("h_ld_Crn_mtt600to800", "(ld) C_{rn} (600 < m_{tt} < 800 GeV);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt600to800 = ROOT.TH1F("h_ld_Crr_mtt600to800", "(ld) C_{rr} (600 < m_{tt} < 800 GeV);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt600to800 = ROOT.TH1F("h_ld_Crk_mtt600to800", "(ld) C_{rk} (600 < m_{tt} < 800 GeV);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt600to800 = ROOT.TH1F("h_ld_Ckn_mtt600to800", "(ld) C_{kn} (600 < m_{tt} < 800 GeV);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt600to800 = ROOT.TH1F("h_ld_Ckr_mtt600to800", "(ld) C_{kr} (600 < m_{tt} < 800 GeV);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt600to800 = ROOT.TH1F("h_ld_Ckk_mtt600to800", "(ld) C_{kk} (600 < m_{tt} < 800 GeV);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt600to800 = ROOT.TH1F("h_ld_trC_mtt600to800", "Trace of Correlation Matrix (600 < m_{tt} < 800 GeV);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt600to800 = ROOT.TH1F("h_ld_cHel_mtt600to800", "(ld) Cosine Helicity Angle (600 < m_{tt} < 800 GeV);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt600to800 = ROOT.TH1F("h_ld_cHel_P3n_mtt600to800", "(ld) Cosine Helicity Angle w/P_3n (600 < m_{tt} < 800 GeV);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt600to800 = ROOT.TH1F("h_lb_sigmaPhi_mtt600to800", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (600 < m_{tt} < 800 GeV);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt600to800 = ROOT.TH1F("h_lb_deltaPhi_mtt600to800", "(lb) #Delta#phi_{#hat{n}#hat{r}} (600 < m_{tt} < 800 GeV);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt600to800 = ROOT.TH1F("h_ld_sigmaPhi_mtt600to800", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (600 < m_{tt} < 800 GeV);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt600to800 = ROOT.TH1F("h_ld_deltaPhi_mtt600to800", "(ld) #Delta#phi_{#hat{n}#hat{r}} (600 < m_{tt} < 800 GeV);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

    ## |cosTSA| < 0.4
h_cos_theta1n_antilepton_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt600to800_cosTSA_lt_0p4", "antilepton #hat{n}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt600to800_cosTSA_lt_0p4", "antilepton #hat{r}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt600to800_cosTSA_lt_0p4", "antilepton #hat{k}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt600to800_cosTSA_lt_0p4", "antilepton #hat{r}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt600to800_cosTSA_lt_0p4", "antilepton #hat{k}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2n_lepton_mtt600to800_cosTSA_lt_0p4", "lepton #hat{n}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2r_lepton_mtt600to800_cosTSA_lt_0p4", "lepton #hat{r}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2k_lepton_mtt600to800_cosTSA_lt_0p4", "lepton #hat{k}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt600to800_cosTSA_lt_0p4", "lepton #hat{r}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt600to800_cosTSA_lt_0p4", "lepton #hat{k}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1n_mtt600to800_cosTSA_lt_0p4", "top decay (lb) #hat{n}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1r_mtt600to800_cosTSA_lt_0p4", "top decay (lb) #hat{r}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1k_mtt600to800_cosTSA_lt_0p4", "top decay (lb) #hat{k}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt600to800_cosTSA_lt_0p4", "top decay (lb) #hat{r}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt600to800_cosTSA_lt_0p4", "top decay (lb) #hat{k}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2n_mtt600to800_cosTSA_lt_0p4", "antitop decay (lb) #hat{n}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2r_mtt600to800_cosTSA_lt_0p4", "antitop decay (lb) #hat{r}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2k_mtt600to800_cosTSA_lt_0p4", "antitop decay (lb) #hat{k}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt600to800_cosTSA_lt_0p4", "antitop decay (lb) #hat{r}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt600to800_cosTSA_lt_0p4", "antitop decay (lb) #hat{k}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Cnn_mtt600to800_cosTSA_lt_0p4", "(lb) C_{nn} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Cnr_mtt600to800_cosTSA_lt_0p4", "(lb) C_{nr} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Cnk_mtt600to800_cosTSA_lt_0p4", "(lb) C_{nk} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Crn_mtt600to800_cosTSA_lt_0p4", "(lb) C_{rn} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Crr_mtt600to800_cosTSA_lt_0p4", "(lb) C_{rr} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Crk_mtt600to800_cosTSA_lt_0p4", "(lb) C_{rk} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Ckn_mtt600to800_cosTSA_lt_0p4", "(lb) C_{kn} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Ckr_mtt600to800_cosTSA_lt_0p4", "(lb) C_{kr} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Ckk_mtt600to800_cosTSA_lt_0p4", "(lb) C_{kk} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_trC_mtt600to800_cosTSA_lt_0p4", "Trace of Correlation Matrix (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cHel_mtt600to800_cosTSA_lt_0p4", "(lb) Cosine Helicity Angle (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cHel_P3n_mtt600to800_cosTSA_lt_0p4", "(lb) Cosine Helicity Angle w/P_3n (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1n_mtt600to800_cosTSA_lt_0p4", "top decay (ld) #hat{n}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1r_mtt600to800_cosTSA_lt_0p4", "top decay (ld) #hat{r}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1k_mtt600to800_cosTSA_lt_0p4", "top decay (ld) #hat{k}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt600to800_cosTSA_lt_0p4", "top decay (ld) #hat{r}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt600to800_cosTSA_lt_0p4", "top decay (ld) #hat{k}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2n_mtt600to800_cosTSA_lt_0p4", "antitop decay (ld) #hat{n}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2r_mtt600to800_cosTSA_lt_0p4", "antitop decay (ld) #hat{r}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2k_mtt600to800_cosTSA_lt_0p4", "antitop decay (ld) #hat{k}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt600to800_cosTSA_lt_0p4", "antitop decay (ld) #hat{r}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt600to800_cosTSA_lt_0p4", "antitop decay (ld) #hat{k}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Cnn_mtt600to800_cosTSA_lt_0p4", "(ld) C_{nn} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Cnr_mtt600to800_cosTSA_lt_0p4", "(ld) C_{nr} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Cnk_mtt600to800_cosTSA_lt_0p4", "(ld) C_{nk} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Crn_mtt600to800_cosTSA_lt_0p4", "(ld) C_{rn} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Crr_mtt600to800_cosTSA_lt_0p4", "(ld) C_{rr} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Crk_mtt600to800_cosTSA_lt_0p4", "(ld) C_{rk} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Ckn_mtt600to800_cosTSA_lt_0p4", "(ld) C_{kn} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Ckr_mtt600to800_cosTSA_lt_0p4", "(ld) C_{kr} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Ckk_mtt600to800_cosTSA_lt_0p4", "(ld) C_{kk} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_trC_mtt600to800_cosTSA_lt_0p4", "Trace of Correlation Matrix (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cHel_mtt600to800_cosTSA_lt_0p4", "(ld) Cosine Helicity Angle (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cHel_P3n_mtt600to800_cosTSA_lt_0p4", "(ld) Cosine Helicity Angle w/P_3n (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_sigmaPhi_mtt600to800_cosTSA_lt_0p4", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_deltaPhi_mtt600to800_cosTSA_lt_0p4", "(lb) #Delta#phi_{#hat{n}#hat{r}} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_sigmaPhi_mtt600to800_cosTSA_lt_0p4", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt600to800_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_deltaPhi_mtt600to800_cosTSA_lt_0p4", "(ld) #Delta#phi_{#hat{n}#hat{r}} (600 < m_{tt} < 800 GeV, |cosTSA|<0.4);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

    ## |cosTSA| < 0.7
h_cos_theta1n_antilepton_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt600to800_cosTSA_lt_0p7", "antilepton #hat{n}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt600to800_cosTSA_lt_0p7", "antilepton #hat{r}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt600to800_cosTSA_lt_0p7", "antilepton #hat{k}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt600to800_cosTSA_lt_0p7", "antilepton #hat{r}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt600to800_cosTSA_lt_0p7", "antilepton #hat{k}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2n_lepton_mtt600to800_cosTSA_lt_0p7", "lepton #hat{n}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2r_lepton_mtt600to800_cosTSA_lt_0p7", "lepton #hat{r}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2k_lepton_mtt600to800_cosTSA_lt_0p7", "lepton #hat{k}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt600to800_cosTSA_lt_0p7", "lepton #hat{r}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt600to800_cosTSA_lt_0p7", "lepton #hat{k}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1n_mtt600to800_cosTSA_lt_0p7", "top decay (lb) #hat{n}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1r_mtt600to800_cosTSA_lt_0p7", "top decay (lb) #hat{r}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1k_mtt600to800_cosTSA_lt_0p7", "top decay (lb) #hat{k}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt600to800_cosTSA_lt_0p7", "top decay (lb) #hat{r}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt600to800_cosTSA_lt_0p7", "top decay (lb) #hat{k}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2n_mtt600to800_cosTSA_lt_0p7", "antitop decay (lb) #hat{n}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2r_mtt600to800_cosTSA_lt_0p7", "antitop decay (lb) #hat{r}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2k_mtt600to800_cosTSA_lt_0p7", "antitop decay (lb) #hat{k}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt600to800_cosTSA_lt_0p7", "antitop decay (lb) #hat{r}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt600to800_cosTSA_lt_0p7", "antitop decay (lb) #hat{k}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Cnn_mtt600to800_cosTSA_lt_0p7", "(lb) C_{nn} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Cnr_mtt600to800_cosTSA_lt_0p7", "(lb) C_{nr} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Cnk_mtt600to800_cosTSA_lt_0p7", "(lb) C_{nk} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Crn_mtt600to800_cosTSA_lt_0p7", "(lb) C_{rn} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Crr_mtt600to800_cosTSA_lt_0p7", "(lb) C_{rr} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Crk_mtt600to800_cosTSA_lt_0p7", "(lb) C_{rk} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Ckn_mtt600to800_cosTSA_lt_0p7", "(lb) C_{kn} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Ckr_mtt600to800_cosTSA_lt_0p7", "(lb) C_{kr} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Ckk_mtt600to800_cosTSA_lt_0p7", "(lb) C_{kk} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_trC_mtt600to800_cosTSA_lt_0p7", "Trace of Correlation Matrix (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cHel_mtt600to800_cosTSA_lt_0p7", "(lb) Cosine Helicity Angle (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cHel_P3n_mtt600to800_cosTSA_lt_0p7", "(lb) Cosine Helicity Angle w/P_3n (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1n_mtt600to800_cosTSA_lt_0p7", "top decay (ld) #hat{n}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1r_mtt600to800_cosTSA_lt_0p7", "top decay (ld) #hat{r}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1k_mtt600to800_cosTSA_lt_0p7", "top decay (ld) #hat{k}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt600to800_cosTSA_lt_0p7", "top decay (ld) #hat{r}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt600to800_cosTSA_lt_0p7", "top decay (ld) #hat{k}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2n_mtt600to800_cosTSA_lt_0p7", "antitop decay (ld) #hat{n}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2r_mtt600to800_cosTSA_lt_0p7", "antitop decay (ld) #hat{r}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2k_mtt600to800_cosTSA_lt_0p7", "antitop decay (ld) #hat{k}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt600to800_cosTSA_lt_0p7", "antitop decay (ld) #hat{r}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt600to800_cosTSA_lt_0p7", "antitop decay (ld) #hat{k}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Cnn_mtt600to800_cosTSA_lt_0p7", "(ld) C_{nn} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Cnr_mtt600to800_cosTSA_lt_0p7", "(ld) C_{nr} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Cnk_mtt600to800_cosTSA_lt_0p7", "(ld) C_{nk} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Crn_mtt600to800_cosTSA_lt_0p7", "(ld) C_{rn} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Crr_mtt600to800_cosTSA_lt_0p7", "(ld) C_{rr} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Crk_mtt600to800_cosTSA_lt_0p7", "(ld) C_{rk} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Ckn_mtt600to800_cosTSA_lt_0p7", "(ld) C_{kn} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Ckr_mtt600to800_cosTSA_lt_0p7", "(ld) C_{kr} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Ckk_mtt600to800_cosTSA_lt_0p7", "(ld) C_{kk} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_trC_mtt600to800_cosTSA_lt_0p7", "Trace of Correlation Matrix (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cHel_mtt600to800_cosTSA_lt_0p7", "(ld) Cosine Helicity Angle (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cHel_P3n_mtt600to800_cosTSA_lt_0p7", "(ld) Cosine Helicity Angle w/P_3n (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_sigmaPhi_mtt600to800_cosTSA_lt_0p7", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_deltaPhi_mtt600to800_cosTSA_lt_0p7", "(lb) #Delta#phi_{#hat{n}#hat{r}} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_sigmaPhi_mtt600to800_cosTSA_lt_0p7", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt600to800_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_deltaPhi_mtt600to800_cosTSA_lt_0p7", "(ld) #Delta#phi_{#hat{n}#hat{r}} (600 < m_{tt} < 800 GeV, |cosTSA|<0.7);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

    ## |cosTSA| > 0.7
h_cos_theta1n_antilepton_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt600to800_cosTSA_gt_0p7", "antilepton #hat{n}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt600to800_cosTSA_gt_0p7", "antilepton #hat{r}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt600to800_cosTSA_gt_0p7", "antilepton #hat{k}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt600to800_cosTSA_gt_0p7", "antilepton #hat{r}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt600to800_cosTSA_gt_0p7", "antilepton #hat{k}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2n_lepton_mtt600to800_cosTSA_gt_0p7", "lepton #hat{n}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2r_lepton_mtt600to800_cosTSA_gt_0p7", "lepton #hat{r}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2k_lepton_mtt600to800_cosTSA_gt_0p7", "lepton #hat{k}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt600to800_cosTSA_gt_0p7", "lepton #hat{r}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt600to800_cosTSA_gt_0p7", "lepton #hat{k}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1n_mtt600to800_cosTSA_gt_0p7", "top decay (lb) #hat{n}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1r_mtt600to800_cosTSA_gt_0p7", "top decay (lb) #hat{r}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1k_mtt600to800_cosTSA_gt_0p7", "top decay (lb) #hat{k}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt600to800_cosTSA_gt_0p7", "top decay (lb) #hat{r}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt600to800_cosTSA_gt_0p7", "top decay (lb) #hat{k}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2n_mtt600to800_cosTSA_gt_0p7", "antitop decay (lb) #hat{n}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2r_mtt600to800_cosTSA_gt_0p7", "antitop decay (lb) #hat{r}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2k_mtt600to800_cosTSA_gt_0p7", "antitop decay (lb) #hat{k}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt600to800_cosTSA_gt_0p7", "antitop decay (lb) #hat{r}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt600to800_cosTSA_gt_0p7", "antitop decay (lb) #hat{k}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Cnn_mtt600to800_cosTSA_gt_0p7", "(lb) C_{nn} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Cnr_mtt600to800_cosTSA_gt_0p7", "(lb) C_{nr} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Cnk_mtt600to800_cosTSA_gt_0p7", "(lb) C_{nk} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Crn_mtt600to800_cosTSA_gt_0p7", "(lb) C_{rn} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Crr_mtt600to800_cosTSA_gt_0p7", "(lb) C_{rr} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Crk_mtt600to800_cosTSA_gt_0p7", "(lb) C_{rk} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Ckn_mtt600to800_cosTSA_gt_0p7", "(lb) C_{kn} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Ckr_mtt600to800_cosTSA_gt_0p7", "(lb) C_{kr} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Ckk_mtt600to800_cosTSA_gt_0p7", "(lb) C_{kk} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_trC_mtt600to800_cosTSA_gt_0p7", "Trace of Correlation Matrix (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cHel_mtt600to800_cosTSA_gt_0p7", "(lb) Cosine Helicity Angle (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cHel_P3n_mtt600to800_cosTSA_gt_0p7", "(lb) Cosine Helicity Angle w/P_3n (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1n_mtt600to800_cosTSA_gt_0p7", "top decay (ld) #hat{n}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1r_mtt600to800_cosTSA_gt_0p7", "top decay (ld) #hat{r}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1k_mtt600to800_cosTSA_gt_0p7", "top decay (ld) #hat{k}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt600to800_cosTSA_gt_0p7", "top decay (ld) #hat{r}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt600to800_cosTSA_gt_0p7", "top decay (ld) #hat{k}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2n_mtt600to800_cosTSA_gt_0p7", "antitop decay (ld) #hat{n}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2r_mtt600to800_cosTSA_gt_0p7", "antitop decay (ld) #hat{r}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2k_mtt600to800_cosTSA_gt_0p7", "antitop decay (ld) #hat{k}-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt600to800_cosTSA_gt_0p7", "antitop decay (ld) #hat{r}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt600to800_cosTSA_gt_0p7", "antitop decay (ld) #hat{k}*-polarization (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Cnn_mtt600to800_cosTSA_gt_0p7", "(ld) C_{nn} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Cnr_mtt600to800_cosTSA_gt_0p7", "(ld) C_{nr} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Cnk_mtt600to800_cosTSA_gt_0p7", "(ld) C_{nk} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Crn_mtt600to800_cosTSA_gt_0p7", "(ld) C_{rn} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Crr_mtt600to800_cosTSA_gt_0p7", "(ld) C_{rr} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Crk_mtt600to800_cosTSA_gt_0p7", "(ld) C_{rk} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Ckn_mtt600to800_cosTSA_gt_0p7", "(ld) C_{kn} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Ckr_mtt600to800_cosTSA_gt_0p7", "(ld) C_{kr} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Ckk_mtt600to800_cosTSA_gt_0p7", "(ld) C_{kk} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_trC_mtt600to800_cosTSA_gt_0p7", "Trace of Correlation Matrix (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cHel_mtt600to800_cosTSA_gt_0p7", "(ld) Cosine Helicity Angle (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cHel_P3n_mtt600to800_cosTSA_gt_0p7", "(ld) Cosine Helicity Angle w/P_3n (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_sigmaPhi_mtt600to800_cosTSA_gt_0p7", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_deltaPhi_mtt600to800_cosTSA_gt_0p7", "(lb) #Delta#phi_{#hat{n}#hat{r}} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_sigmaPhi_mtt600to800_cosTSA_gt_0p7", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt600to800_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_deltaPhi_mtt600to800_cosTSA_gt_0p7", "(ld) #Delta#phi_{#hat{n}#hat{r}} (600 < m_{tt} < 800 GeV, |cosTSA|>0.7);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

### mtt [800, Inf] GeV
h_cos_theta1n_antilepton_mtt800toInf = ROOT.TH1F("h_cos_theta1n_antilepton_mtt800toInf", "antilepton #hat{n}-polarization (m_{tt} > 800 GeV);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt800toInf = ROOT.TH1F("h_cos_theta1r_antilepton_mtt800toInf", "antilepton #hat{r}-polarization (m_{tt} > 800 GeV);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt800toInf = ROOT.TH1F("h_cos_theta1k_antilepton_mtt800toInf", "antilepton #hat{k}-polarization (m_{tt} > 800 GeV);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt800toInf = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt800toInf", "antilepton #hat{r}*-polarization (m_{tt} > 800 GeV);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt800toInf = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt800toInf", "antilepton #hat{k}*-polarization (m_{tt} > 800 GeV);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt800toInf = ROOT.TH1F("h_cos_theta2n_lepton_mtt800toInf", "lepton #hat{n}-polarization (m_{tt} > 800 GeV);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt800toInf = ROOT.TH1F("h_cos_theta2r_lepton_mtt800toInf", "lepton #hat{r}-polarization (m_{tt} > 800 GeV);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt800toInf = ROOT.TH1F("h_cos_theta2k_lepton_mtt800toInf", "lepton #hat{k}-polarization (m_{tt} > 800 GeV);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt800toInf = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt800toInf", "lepton #hat{r}*-polarization (m_{tt} > 800 GeV);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt800toInf = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt800toInf", "lepton #hat{k}*-polarization (m_{tt} > 800 GeV);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt800toInf = ROOT.TH1F("h_lb_cos_theta1n_mtt800toInf", "top decay (lb) #hat{n}-polarization (m_{tt} > 800 GeV);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt800toInf = ROOT.TH1F("h_lb_cos_theta1r_mtt800toInf", "top decay (lb) #hat{r}-polarization (m_{tt} > 800 GeV);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt800toInf = ROOT.TH1F("h_lb_cos_theta1k_mtt800toInf", "top decay (lb) #hat{k}-polarization (m_{tt} > 800 GeV);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt800toInf = ROOT.TH1F("h_lb_cos_theta1rStar_mtt800toInf", "top decay (lb) #hat{r}*-polarization (m_{tt} > 800 GeV);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt800toInf = ROOT.TH1F("h_lb_cos_theta1kStar_mtt800toInf", "top decay (lb) #hat{k}*-polarization (m_{tt} > 800 GeV);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt800toInf = ROOT.TH1F("h_lb_cos_theta2n_mtt800toInf", "antitop decay (lb) #hat{n}-polarization (m_{tt} > 800 GeV);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt800toInf = ROOT.TH1F("h_lb_cos_theta2r_mtt800toInf", "antitop decay (lb) #hat{r}-polarization (m_{tt} > 800 GeV);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt800toInf = ROOT.TH1F("h_lb_cos_theta2k_mtt800toInf", "antitop decay (lb) #hat{k}-polarization (m_{tt} > 800 GeV);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt800toInf = ROOT.TH1F("h_lb_cos_theta2rStar_mtt800toInf", "antitop decay (lb) #hat{r}*-polarization (m_{tt} > 800 GeV);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt800toInf = ROOT.TH1F("h_lb_cos_theta2kStar_mtt800toInf", "antitop decay (lb) #hat{k}*-polarization (m_{tt} > 800 GeV);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt800toInf = ROOT.TH1F("h_lb_Cnn_mtt800toInf", "(lb) C_{nn} (m_{tt} > 800 GeV);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt800toInf = ROOT.TH1F("h_lb_Cnr_mtt800toInf", "(lb) C_{nr} (m_{tt} > 800 GeV);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt800toInf = ROOT.TH1F("h_lb_Cnk_mtt800toInf", "(lb) C_{nk} (m_{tt} > 800 GeV);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt800toInf = ROOT.TH1F("h_lb_Crn_mtt800toInf", "(lb) C_{rn} (m_{tt} > 800 GeV);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt800toInf = ROOT.TH1F("h_lb_Crr_mtt800toInf", "(lb) C_{rr} (m_{tt} > 800 GeV);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt800toInf = ROOT.TH1F("h_lb_Crk_mtt800toInf", "(lb) C_{rk} (m_{tt} > 800 GeV);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt800toInf = ROOT.TH1F("h_lb_Ckn_mtt800toInf", "(lb) C_{kn} (m_{tt} > 800 GeV);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt800toInf = ROOT.TH1F("h_lb_Ckr_mtt800toInf", "(lb) C_{kr} (m_{tt} > 800 GeV);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt800toInf = ROOT.TH1F("h_lb_Ckk_mtt800toInf", "(lb) C_{kk} (m_{tt} > 800 GeV);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt800toInf = ROOT.TH1F("h_lb_trC_mtt800toInf", "Trace of Correlation Matrix (m_{tt} > 800 GeV);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt800toInf = ROOT.TH1F("h_lb_cHel_mtt800toInf", "(lb) Cosine Helicity Angle (m_{tt} > 800 GeV);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt800toInf = ROOT.TH1F("h_lb_cHel_P3n_mtt800toInf", "(lb) Cosine Helicity Angle w/P_3n (m_{tt} > 800 GeV);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt800toInf = ROOT.TH1F("h_ld_cos_theta1n_mtt800toInf", "top decay (ld) #hat{n}-polarization (m_{tt} > 800 GeV);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt800toInf = ROOT.TH1F("h_ld_cos_theta1r_mtt800toInf", "top decay (ld) #hat{r}-polarization (m_{tt} > 800 GeV);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt800toInf = ROOT.TH1F("h_ld_cos_theta1k_mtt800toInf", "top decay (ld) #hat{k}-polarization (m_{tt} > 800 GeV);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt800toInf = ROOT.TH1F("h_ld_cos_theta1rStar_mtt800toInf", "top decay (ld) #hat{r}*-polarization (m_{tt} > 800 GeV);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt800toInf = ROOT.TH1F("h_ld_cos_theta1kStar_mtt800toInf", "top decay (ld) #hat{k}*-polarization (m_{tt} > 800 GeV);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt800toInf = ROOT.TH1F("h_ld_cos_theta2n_mtt800toInf", "antitop decay (ld) #hat{n}-polarization (m_{tt} > 800 GeV);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt800toInf = ROOT.TH1F("h_ld_cos_theta2r_mtt800toInf", "antitop decay (ld) #hat{r}-polarization (m_{tt} > 800 GeV);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt800toInf = ROOT.TH1F("h_ld_cos_theta2k_mtt800toInf", "antitop decay (ld) #hat{k}-polarization (m_{tt} > 800 GeV);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt800toInf = ROOT.TH1F("h_ld_cos_theta2rStar_mtt800toInf", "antitop decay (ld) #hat{r}*-polarization (m_{tt} > 800 GeV);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt800toInf = ROOT.TH1F("h_ld_cos_theta2kStar_mtt800toInf", "antitop decay (ld) #hat{k}*-polarization (m_{tt} > 800 GeV);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt800toInf = ROOT.TH1F("h_ld_Cnn_mtt800toInf", "(ld) C_{nn} (m_{tt} > 800 GeV);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt800toInf = ROOT.TH1F("h_ld_Cnr_mtt800toInf", "(ld) C_{nr} (m_{tt} > 800 GeV);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt800toInf = ROOT.TH1F("h_ld_Cnk_mtt800toInf", "(ld) C_{nk} (m_{tt} > 800 GeV);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt800toInf = ROOT.TH1F("h_ld_Crn_mtt800toInf", "(ld) C_{rn} (m_{tt} > 800 GeV);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt800toInf = ROOT.TH1F("h_ld_Crr_mtt800toInf", "(ld) C_{rr} (m_{tt} > 800 GeV);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt800toInf = ROOT.TH1F("h_ld_Crk_mtt800toInf", "(ld) C_{rk} (m_{tt} > 800 GeV);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt800toInf = ROOT.TH1F("h_ld_Ckn_mtt800toInf", "(ld) C_{kn} (m_{tt} > 800 GeV);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt800toInf = ROOT.TH1F("h_ld_Ckr_mtt800toInf", "(ld) C_{kr} (m_{tt} > 800 GeV);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt800toInf = ROOT.TH1F("h_ld_Ckk_mtt800toInf", "(ld) C_{kk} (m_{tt} > 800 GeV);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt800toInf = ROOT.TH1F("h_ld_trC_mtt800toInf", "Trace of Correlation Matrix (m_{tt} > 800 GeV);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt800toInf = ROOT.TH1F("h_ld_cHel_mtt800toInf", "(ld) Cosine Helicity Angle (m_{tt} > 800 GeV);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt800toInf = ROOT.TH1F("h_ld_cHel_P3n_mtt800toInf", "(ld) Cosine Helicity Angle w/P_3n (m_{tt} > 800 GeV);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt800toInf = ROOT.TH1F("h_lb_sigmaPhi_mtt800toInf", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (m_{tt} > 800 GeV);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt800toInf = ROOT.TH1F("h_lb_deltaPhi_mtt800toInf", "(lb) #Delta#phi_{#hat{n}#hat{r}} (m_{tt} > 800 GeV);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt800toInf = ROOT.TH1F("h_ld_sigmaPhi_mtt800toInf", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (m_{tt} > 800 GeV);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt800toInf = ROOT.TH1F("h_ld_deltaPhi_mtt800toInf", "(ld) #Delta#phi_{#hat{n}#hat{r}} (m_{tt} > 800 GeV);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

    ## |cosTSA| < 0.4
h_cos_theta1n_antilepton_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt800toInf_cosTSA_lt_0p4", "antilepton #hat{n}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt800toInf_cosTSA_lt_0p4", "antilepton #hat{r}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt800toInf_cosTSA_lt_0p4", "antilepton #hat{k}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt800toInf_cosTSA_lt_0p4", "antilepton #hat{r}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt800toInf_cosTSA_lt_0p4", "antilepton #hat{k}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2n_lepton_mtt800toInf_cosTSA_lt_0p4", "lepton #hat{n}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2r_lepton_mtt800toInf_cosTSA_lt_0p4", "lepton #hat{r}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2k_lepton_mtt800toInf_cosTSA_lt_0p4", "lepton #hat{k}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt800toInf_cosTSA_lt_0p4", "lepton #hat{r}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt800toInf_cosTSA_lt_0p4", "lepton #hat{k}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1n_mtt800toInf_cosTSA_lt_0p4", "top decay (lb) #hat{n}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1r_mtt800toInf_cosTSA_lt_0p4", "top decay (lb) #hat{r}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1k_mtt800toInf_cosTSA_lt_0p4", "top decay (lb) #hat{k}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p4", "top decay (lb) #hat{r}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p4", "top decay (lb) #hat{k}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2n_mtt800toInf_cosTSA_lt_0p4", "antitop decay (lb) #hat{n}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2r_mtt800toInf_cosTSA_lt_0p4", "antitop decay (lb) #hat{r}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2k_mtt800toInf_cosTSA_lt_0p4", "antitop decay (lb) #hat{k}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p4", "antitop decay (lb) #hat{r}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p4", "antitop decay (lb) #hat{k}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Cnn_mtt800toInf_cosTSA_lt_0p4", "(lb) C_{nn} (m_{tt} > 800 GeV, |cosTSA|<0.4);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Cnr_mtt800toInf_cosTSA_lt_0p4", "(lb) C_{nr} (m_{tt} > 800 GeV, |cosTSA|<0.4);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Cnk_mtt800toInf_cosTSA_lt_0p4", "(lb) C_{nk} (m_{tt} > 800 GeV, |cosTSA|<0.4);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Crn_mtt800toInf_cosTSA_lt_0p4", "(lb) C_{rn} (m_{tt} > 800 GeV, |cosTSA|<0.4);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Crr_mtt800toInf_cosTSA_lt_0p4", "(lb) C_{rr} (m_{tt} > 800 GeV, |cosTSA|<0.4);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Crk_mtt800toInf_cosTSA_lt_0p4", "(lb) C_{rk} (m_{tt} > 800 GeV, |cosTSA|<0.4);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Ckn_mtt800toInf_cosTSA_lt_0p4", "(lb) C_{kn} (m_{tt} > 800 GeV, |cosTSA|<0.4);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Ckr_mtt800toInf_cosTSA_lt_0p4", "(lb) C_{kr} (m_{tt} > 800 GeV, |cosTSA|<0.4);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_Ckk_mtt800toInf_cosTSA_lt_0p4", "(lb) C_{kk} (m_{tt} > 800 GeV, |cosTSA|<0.4);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_trC_mtt800toInf_cosTSA_lt_0p4", "Trace of Correlation Matrix (m_{tt} > 800 GeV, |cosTSA|<0.4);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cHel_mtt800toInf_cosTSA_lt_0p4", "(lb) Cosine Helicity Angle (m_{tt} > 800 GeV, |cosTSA|<0.4);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_cHel_P3n_mtt800toInf_cosTSA_lt_0p4", "(lb) Cosine Helicity Angle w/P_3n (m_{tt} > 800 GeV, |cosTSA|<0.4);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1n_mtt800toInf_cosTSA_lt_0p4", "top decay (ld) #hat{n}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1r_mtt800toInf_cosTSA_lt_0p4", "top decay (ld) #hat{r}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1k_mtt800toInf_cosTSA_lt_0p4", "top decay (ld) #hat{k}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p4", "top decay (ld) #hat{r}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p4", "top decay (ld) #hat{k}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2n_mtt800toInf_cosTSA_lt_0p4", "antitop decay (ld) #hat{n}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2r_mtt800toInf_cosTSA_lt_0p4", "antitop decay (ld) #hat{r}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2k_mtt800toInf_cosTSA_lt_0p4", "antitop decay (ld) #hat{k}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p4", "antitop decay (ld) #hat{r}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p4", "antitop decay (ld) #hat{k}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.4);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Cnn_mtt800toInf_cosTSA_lt_0p4", "(ld) C_{nn} (m_{tt} > 800 GeV, |cosTSA|<0.4);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Cnr_mtt800toInf_cosTSA_lt_0p4", "(ld) C_{nr} (m_{tt} > 800 GeV, |cosTSA|<0.4);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Cnk_mtt800toInf_cosTSA_lt_0p4", "(ld) C_{nk} (m_{tt} > 800 GeV, |cosTSA|<0.4);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Crn_mtt800toInf_cosTSA_lt_0p4", "(ld) C_{rn} (m_{tt} > 800 GeV, |cosTSA|<0.4);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Crr_mtt800toInf_cosTSA_lt_0p4", "(ld) C_{rr} (m_{tt} > 800 GeV, |cosTSA|<0.4);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Crk_mtt800toInf_cosTSA_lt_0p4", "(ld) C_{rk} (m_{tt} > 800 GeV, |cosTSA|<0.4);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Ckn_mtt800toInf_cosTSA_lt_0p4", "(ld) C_{kn} (m_{tt} > 800 GeV, |cosTSA|<0.4);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Ckr_mtt800toInf_cosTSA_lt_0p4", "(ld) C_{kr} (m_{tt} > 800 GeV, |cosTSA|<0.4);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_Ckk_mtt800toInf_cosTSA_lt_0p4", "(ld) C_{kk} (m_{tt} > 800 GeV, |cosTSA|<0.4);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_trC_mtt800toInf_cosTSA_lt_0p4", "Trace of Correlation Matrix (m_{tt} > 800 GeV, |cosTSA|<0.4);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cHel_mtt800toInf_cosTSA_lt_0p4", "(ld) Cosine Helicity Angle (m_{tt} > 800 GeV, |cosTSA|<0.4);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_cHel_P3n_mtt800toInf_cosTSA_lt_0p4", "(ld) Cosine Helicity Angle w/P_3n (m_{tt} > 800 GeV, |cosTSA|<0.4);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_sigmaPhi_mtt800toInf_cosTSA_lt_0p4", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (m_{tt} > 800 GeV, |cosTSA|<0.4);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_lb_deltaPhi_mtt800toInf_cosTSA_lt_0p4", "(lb) #Delta#phi_{#hat{n}#hat{r}} (m_{tt} > 800 GeV, |cosTSA|<0.4);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_sigmaPhi_mtt800toInf_cosTSA_lt_0p4", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (m_{tt} > 800 GeV, |cosTSA|<0.4);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt800toInf_cosTSA_lt_0p4 = ROOT.TH1F("h_ld_deltaPhi_mtt800toInf_cosTSA_lt_0p4", "(ld) #Delta#phi_{#hat{n}#hat{r}} (m_{tt} > 800 GeV, |cosTSA|<0.4);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

    ## |cosTSA| < 0.7
h_cos_theta1n_antilepton_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt800toInf_cosTSA_lt_0p7", "antilepton #hat{n}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt800toInf_cosTSA_lt_0p7", "antilepton #hat{r}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt800toInf_cosTSA_lt_0p7", "antilepton #hat{k}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt800toInf_cosTSA_lt_0p7", "antilepton #hat{r}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt800toInf_cosTSA_lt_0p7", "antilepton #hat{k}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2n_lepton_mtt800toInf_cosTSA_lt_0p7", "lepton #hat{n}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2r_lepton_mtt800toInf_cosTSA_lt_0p7", "lepton #hat{r}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2k_lepton_mtt800toInf_cosTSA_lt_0p7", "lepton #hat{k}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt800toInf_cosTSA_lt_0p7", "lepton #hat{r}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt800toInf_cosTSA_lt_0p7", "lepton #hat{k}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1n_mtt800toInf_cosTSA_lt_0p7", "top decay (lb) #hat{n}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1r_mtt800toInf_cosTSA_lt_0p7", "top decay (lb) #hat{r}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1k_mtt800toInf_cosTSA_lt_0p7", "top decay (lb) #hat{k}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p7", "top decay (lb) #hat{r}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p7", "top decay (lb) #hat{k}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2n_mtt800toInf_cosTSA_lt_0p7", "antitop decay (lb) #hat{n}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2r_mtt800toInf_cosTSA_lt_0p7", "antitop decay (lb) #hat{r}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2k_mtt800toInf_cosTSA_lt_0p7", "antitop decay (lb) #hat{k}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p7", "antitop decay (lb) #hat{r}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p7", "antitop decay (lb) #hat{k}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Cnn_mtt800toInf_cosTSA_lt_0p7", "(lb) C_{nn} (m_{tt} > 800 GeV, |cosTSA|<0.7);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Cnr_mtt800toInf_cosTSA_lt_0p7", "(lb) C_{nr} (m_{tt} > 800 GeV, |cosTSA|<0.7);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Cnk_mtt800toInf_cosTSA_lt_0p7", "(lb) C_{nk} (m_{tt} > 800 GeV, |cosTSA|<0.7);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Crn_mtt800toInf_cosTSA_lt_0p7", "(lb) C_{rn} (m_{tt} > 800 GeV, |cosTSA|<0.7);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Crr_mtt800toInf_cosTSA_lt_0p7", "(lb) C_{rr} (m_{tt} > 800 GeV, |cosTSA|<0.7);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Crk_mtt800toInf_cosTSA_lt_0p7", "(lb) C_{rk} (m_{tt} > 800 GeV, |cosTSA|<0.7);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Ckn_mtt800toInf_cosTSA_lt_0p7", "(lb) C_{kn} (m_{tt} > 800 GeV, |cosTSA|<0.7);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Ckr_mtt800toInf_cosTSA_lt_0p7", "(lb) C_{kr} (m_{tt} > 800 GeV, |cosTSA|<0.7);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_Ckk_mtt800toInf_cosTSA_lt_0p7", "(lb) C_{kk} (m_{tt} > 800 GeV, |cosTSA|<0.7);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_trC_mtt800toInf_cosTSA_lt_0p7", "Trace of Correlation Matrix (m_{tt} > 800 GeV, |cosTSA|<0.7);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cHel_mtt800toInf_cosTSA_lt_0p7", "(lb) Cosine Helicity Angle (m_{tt} > 800 GeV, |cosTSA|<0.7);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_cHel_P3n_mtt800toInf_cosTSA_lt_0p7", "(lb) Cosine Helicity Angle w/P_3n (m_{tt} > 800 GeV, |cosTSA|<0.7);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1n_mtt800toInf_cosTSA_lt_0p7", "top decay (ld) #hat{n}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1r_mtt800toInf_cosTSA_lt_0p7", "top decay (ld) #hat{r}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1k_mtt800toInf_cosTSA_lt_0p7", "top decay (ld) #hat{k}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p7", "top decay (ld) #hat{r}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p7", "top decay (ld) #hat{k}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2n_mtt800toInf_cosTSA_lt_0p7", "antitop decay (ld) #hat{n}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2r_mtt800toInf_cosTSA_lt_0p7", "antitop decay (ld) #hat{r}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2k_mtt800toInf_cosTSA_lt_0p7", "antitop decay (ld) #hat{k}-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p7", "antitop decay (ld) #hat{r}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p7", "antitop decay (ld) #hat{k}*-polarization (m_{tt} > 800 GeV, |cosTSA|<0.7);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Cnn_mtt800toInf_cosTSA_lt_0p7", "(ld) C_{nn} (m_{tt} > 800 GeV, |cosTSA|<0.7);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Cnr_mtt800toInf_cosTSA_lt_0p7", "(ld) C_{nr} (m_{tt} > 800 GeV, |cosTSA|<0.7);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Cnk_mtt800toInf_cosTSA_lt_0p7", "(ld) C_{nk} (m_{tt} > 800 GeV, |cosTSA|<0.7);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Crn_mtt800toInf_cosTSA_lt_0p7", "(ld) C_{rn} (m_{tt} > 800 GeV, |cosTSA|<0.7);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Crr_mtt800toInf_cosTSA_lt_0p7", "(ld) C_{rr} (m_{tt} > 800 GeV, |cosTSA|<0.7);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Crk_mtt800toInf_cosTSA_lt_0p7", "(ld) C_{rk} (m_{tt} > 800 GeV, |cosTSA|<0.7);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Ckn_mtt800toInf_cosTSA_lt_0p7", "(ld) C_{kn} (m_{tt} > 800 GeV, |cosTSA|<0.7);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Ckr_mtt800toInf_cosTSA_lt_0p7", "(ld) C_{kr} (m_{tt} > 800 GeV, |cosTSA|<0.7);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_Ckk_mtt800toInf_cosTSA_lt_0p7", "(ld) C_{kk} (m_{tt} > 800 GeV, |cosTSA|<0.7);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_trC_mtt800toInf_cosTSA_lt_0p7", "Trace of Correlation Matrix (m_{tt} > 800 GeV, |cosTSA|<0.7);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cHel_mtt800toInf_cosTSA_lt_0p7", "(ld) Cosine Helicity Angle (m_{tt} > 800 GeV, |cosTSA|<0.7);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_cHel_P3n_mtt800toInf_cosTSA_lt_0p7", "(ld) Cosine Helicity Angle w/P_3n (m_{tt} > 800 GeV, |cosTSA|<0.7);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_sigmaPhi_mtt800toInf_cosTSA_lt_0p7", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (m_{tt} > 800 GeV, |cosTSA|<0.7);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_lb_deltaPhi_mtt800toInf_cosTSA_lt_0p7", "(lb) #Delta#phi_{#hat{n}#hat{r}} (m_{tt} > 800 GeV, |cosTSA|<0.7);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_sigmaPhi_mtt800toInf_cosTSA_lt_0p7", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (m_{tt} > 800 GeV, |cosTSA|<0.7);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt800toInf_cosTSA_lt_0p7 = ROOT.TH1F("h_ld_deltaPhi_mtt800toInf_cosTSA_lt_0p7", "(ld) #Delta#phi_{#hat{n}#hat{r}} (m_{tt} > 800 GeV, |cosTSA|<0.7);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

    ## |cosTSA| > 0.7
h_cos_theta1n_antilepton_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1n_antilepton_mtt800toInf_cosTSA_gt_0p7", "antilepton #hat{n}-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta1r_antilepton_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1r_antilepton_mtt800toInf_cosTSA_gt_0p7", "antilepton #hat{r}-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1k_antilepton_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1k_antilepton_mtt800toInf_cosTSA_gt_0p7", "antilepton #hat{k}-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1rStar_antilepton_mtt800toInf_cosTSA_gt_0p7", "antilepton #hat{r}*-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta1kStar_antilepton_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta1kStar_antilepton_mtt800toInf_cosTSA_gt_0p7", "antilepton #hat{k}*-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta2n_lepton_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2n_lepton_mtt800toInf_cosTSA_gt_0p7", "lepton #hat{n}-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);cos(#theta_{ln});Events", 6, -1, 1)
h_cos_theta2r_lepton_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2r_lepton_mtt800toInf_cosTSA_gt_0p7", "lepton #hat{r}-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2k_lepton_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2k_lepton_mtt800toInf_cosTSA_gt_0p7", "lepton #hat{k}-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2rStar_lepton_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2rStar_lepton_mtt800toInf_cosTSA_gt_0p7", "lepton #hat{r}*-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);cos(#theta_{lr*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_cos_theta2kStar_lepton_mtt800toInf_cosTSA_gt_0p7", "lepton #hat{k}*-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);cos(#theta_{lk*});Events", 6, -1, 1)

h_lb_cos_theta1n_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1n_mtt800toInf_cosTSA_gt_0p7", "top decay (lb) #hat{n}-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta1r_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1r_mtt800toInf_cosTSA_gt_0p7", "top decay (lb) #hat{r}-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1k_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1k_mtt800toInf_cosTSA_gt_0p7", "top decay (lb) #hat{k}-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1rStar_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1rStar_mtt800toInf_cosTSA_gt_0p7", "top decay (lb) #hat{r}*-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta1kStar_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta1kStar_mtt800toInf_cosTSA_gt_0p7", "top decay (lb) #hat{k}*-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta2n_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2n_mtt800toInf_cosTSA_gt_0p7", "antitop decay (lb) #hat{n}-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2n});Events", 6, -1, 1)
h_lb_cos_theta2r_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2r_mtt800toInf_cosTSA_gt_0p7", "antitop decay (lb) #hat{r}-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2k_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2k_mtt800toInf_cosTSA_gt_0p7", "antitop decay (lb) #hat{k}-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2rStar_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2rStar_mtt800toInf_cosTSA_gt_0p7", "antitop decay (lb) #hat{r}*-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cos_theta2kStar_mtt800toInf_cosTSA_gt_0p7", "antitop decay (lb) #hat{k}*-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_Cnn_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Cnn_mtt800toInf_cosTSA_gt_0p7", "(lb) C_{nn} (m_{tt} > 800 GeV, |cosTSA|>0.7);C_{nn};Events", 6, -1, 1)
h_lb_Cnr_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Cnr_mtt800toInf_cosTSA_gt_0p7", "(lb) C_{nr} (m_{tt} > 800 GeV, |cosTSA|>0.7);C_{nr};Events", 6, -1, 1)
h_lb_Cnk_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Cnk_mtt800toInf_cosTSA_gt_0p7", "(lb) C_{nk} (m_{tt} > 800 GeV, |cosTSA|>0.7);C_{nk};Events", 6, -1, 1)
h_lb_Crn_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Crn_mtt800toInf_cosTSA_gt_0p7", "(lb) C_{rn} (m_{tt} > 800 GeV, |cosTSA|>0.7);C_{rn};Events", 6, -1, 1)
h_lb_Crr_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Crr_mtt800toInf_cosTSA_gt_0p7", "(lb) C_{rr} (m_{tt} > 800 GeV, |cosTSA|>0.7);C_{rr};Events", 6, -1, 1)
h_lb_Crk_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Crk_mtt800toInf_cosTSA_gt_0p7", "(lb) C_{rk} (m_{tt} > 800 GeV, |cosTSA|>0.7);C_{rk};Events", 6, -1, 1)
h_lb_Ckn_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Ckn_mtt800toInf_cosTSA_gt_0p7", "(lb) C_{kn} (m_{tt} > 800 GeV, |cosTSA|>0.7);C_{kn};Events", 6, -1, 1)
h_lb_Ckr_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Ckr_mtt800toInf_cosTSA_gt_0p7", "(lb) C_{kr} (m_{tt} > 800 GeV, |cosTSA|>0.7);C_{kr};Events", 6, -1, 1)
h_lb_Ckk_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_Ckk_mtt800toInf_cosTSA_gt_0p7", "(lb) C_{kk} (m_{tt} > 800 GeV, |cosTSA|>0.7);C_{kk};Events", 6, -1, 1)
h_lb_trC_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_trC_mtt800toInf_cosTSA_gt_0p7", "Trace of Correlation Matrix (m_{tt} > 800 GeV, |cosTSA|>0.7);Tr(C);Events", 12, -3, 3)
h_lb_cHel_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cHel_mtt800toInf_cosTSA_gt_0p7", "(lb) Cosine Helicity Angle (m_{tt} > 800 GeV, |cosTSA|>0.7);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_cHel_P3n_mtt800toInf_cosTSA_gt_0p7", "(lb) Cosine Helicity Angle w/P_3n (m_{tt} > 800 GeV, |cosTSA|>0.7);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_ld_cos_theta1n_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1n_mtt800toInf_cosTSA_gt_0p7", "top decay (ld) #hat{n}-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta1r_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1r_mtt800toInf_cosTSA_gt_0p7", "top decay (ld) #hat{r}-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1k_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1k_mtt800toInf_cosTSA_gt_0p7", "top decay (ld) #hat{k}-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1rStar_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1rStar_mtt800toInf_cosTSA_gt_0p7", "top decay (ld) #hat{r}*-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta1kStar_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta1kStar_mtt800toInf_cosTSA_gt_0p7", "top decay (ld) #hat{k}*-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta2n_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2n_mtt800toInf_cosTSA_gt_0p7", "antitop decay (ld) #hat{n}-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2n});Events", 6, -1, 1)
h_ld_cos_theta2r_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2r_mtt800toInf_cosTSA_gt_0p7", "antitop decay (ld) #hat{r}-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2k_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2k_mtt800toInf_cosTSA_gt_0p7", "antitop decay (ld) #hat{k}-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2rStar_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2rStar_mtt800toInf_cosTSA_gt_0p7", "antitop decay (ld) #hat{r}*-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cos_theta2kStar_mtt800toInf_cosTSA_gt_0p7", "antitop decay (ld) #hat{k}*-polarization (m_{tt} > 800 GeV, |cosTSA|>0.7);(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_Cnn_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Cnn_mtt800toInf_cosTSA_gt_0p7", "(ld) C_{nn} (m_{tt} > 800 GeV, |cosTSA|>0.7);C_{nn};Events", 6, -1, 1)
h_ld_Cnr_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Cnr_mtt800toInf_cosTSA_gt_0p7", "(ld) C_{nr} (m_{tt} > 800 GeV, |cosTSA|>0.7);C_{nr};Events", 6, -1, 1)
h_ld_Cnk_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Cnk_mtt800toInf_cosTSA_gt_0p7", "(ld) C_{nk} (m_{tt} > 800 GeV, |cosTSA|>0.7);C_{nk};Events", 6, -1, 1)
h_ld_Crn_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Crn_mtt800toInf_cosTSA_gt_0p7", "(ld) C_{rn} (m_{tt} > 800 GeV, |cosTSA|>0.7);C_{rn};Events", 6, -1, 1)
h_ld_Crr_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Crr_mtt800toInf_cosTSA_gt_0p7", "(ld) C_{rr} (m_{tt} > 800 GeV, |cosTSA|>0.7);C_{rr};Events", 6, -1, 1)
h_ld_Crk_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Crk_mtt800toInf_cosTSA_gt_0p7", "(ld) C_{rk} (m_{tt} > 800 GeV, |cosTSA|>0.7);C_{rk};Events", 6, -1, 1)
h_ld_Ckn_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Ckn_mtt800toInf_cosTSA_gt_0p7", "(ld) C_{kn} (m_{tt} > 800 GeV, |cosTSA|>0.7);C_{kn};Events", 6, -1, 1)
h_ld_Ckr_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Ckr_mtt800toInf_cosTSA_gt_0p7", "(ld) C_{kr} (m_{tt} > 800 GeV, |cosTSA|>0.7);C_{kr};Events", 6, -1, 1)
h_ld_Ckk_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_Ckk_mtt800toInf_cosTSA_gt_0p7", "(ld) C_{kk} (m_{tt} > 800 GeV, |cosTSA|>0.7);C_{kk};Events", 6, -1, 1)
h_ld_trC_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_trC_mtt800toInf_cosTSA_gt_0p7", "Trace of Correlation Matrix (m_{tt} > 800 GeV, |cosTSA|>0.7);Tr(C);Events", 12, -3, 3)
h_ld_cHel_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cHel_mtt800toInf_cosTSA_gt_0p7", "(ld) Cosine Helicity Angle (m_{tt} > 800 GeV, |cosTSA|>0.7);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_cHel_P3n_mtt800toInf_cosTSA_gt_0p7", "(ld) Cosine Helicity Angle w/P_3n (m_{tt} > 800 GeV, |cosTSA|>0.7);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)

h_lb_sigmaPhi_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_sigmaPhi_mtt800toInf_cosTSA_gt_0p7", "(lb) #Sigma#phi_{#hat{n}#hat{r}} (m_{tt} > 800 GeV, |cosTSA|>0.7);#Sigma#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_lb_deltaPhi_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_lb_deltaPhi_mtt800toInf_cosTSA_gt_0p7", "(lb) #Delta#phi_{#hat{n}#hat{r}} (m_{tt} > 800 GeV, |cosTSA|>0.7);#Delta#phi_{#hat{n}#hat{r}}^{lb};Events", 12, -3.14, 3.14)
h_ld_sigmaPhi_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_sigmaPhi_mtt800toInf_cosTSA_gt_0p7", "(ld) #Sigma#phi_{#hat{n}#hat{r}} (m_{tt} > 800 GeV, |cosTSA|>0.7);#Sigma#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)
h_ld_deltaPhi_mtt800toInf_cosTSA_gt_0p7 = ROOT.TH1F("h_ld_deltaPhi_mtt800toInf_cosTSA_gt_0p7", "(ld) #Delta#phi_{#hat{n}#hat{r}} (m_{tt} > 800 GeV, |cosTSA|>0.7);#Delta#phi_{#hat{n}#hat{r}}^{ld};Events", 12, -3.14, 3.14)

### Bins of pT_t ###
### pT_t [0, 50] GeV
        # beta < 0.9
    ## |cosTSA| < 0.4
        # beta < 0.9
    ## |cosTSA| < 0.7
        # beta < 0.9
    ## |cosTSA| > 0.7
        # beta < 0.9

### pT_t [50, 150] GeV
    ## |cosTSA| < 0.4
    ## |cosTSA| < 0.7
    ## |cosTSA| > 0.7

### pT_t [150, 300] GeV
    ## |cosTSA| < 0.4
    ## |cosTSA| < 0.7
    ## |cosTSA| > 0.7

### pT_t [300, Inf] GeV
    ## |cosTSA| < 0.4
    ## |cosTSA| < 0.7
    ## |cosTSA| > 0.7



# Store histograms in a dictionary for easy access
histogram_defs = {
    ##########################
    ### Particle kinematics###
    ##########################
    # Top quarks
    'h_topPt': h_topPt,
    'h_topEta': h_topEta,
    'h_topPhi': h_topPhi,
    'h_topMass': h_topMass,
    'h_antitopPt': h_antitopPt,
    'h_antitopEta': h_antitopEta,
    'h_antitopPhi': h_antitopPhi,
    'h_antitopMass': h_antitopMass,
    'h_invariantMass': h_invariantMass,
    "h_scattering_angle": h_scattering_angle,
    'h_beta': h_beta,
    'h_deltaAbsY': h_deltaAbsY,
    'h_hypTan_deltaAbsY': h_hypTan_deltaAbsY,
    # Bottom quarks
    "h_bquark_pt" : h_bquark_pt,
    "h_bquark_eta": h_bquark_eta,
    "h_bquark_phi": h_bquark_phi,
    "h_antibquark_pt": h_antibquark_pt,
    "h_antibquark_eta": h_antibquark_eta,
    "h_antibquark_phi": h_antibquark_phi,
    "h_Had_bquark_pt": h_Had_bquark_pt,
    "h_Had_bquark_eta": h_Had_bquark_eta,
    "h_Had_bquark_phi": h_Had_bquark_phi,
    "h_Had_antibquark_pt": h_Had_antibquark_pt,
    "h_Had_antibquark_eta": h_Had_antibquark_eta,
    "h_Had_antibquark_phi": h_Had_antibquark_phi,
    # W bosons
    "h_Wplus_pt": h_Wplus_pt,
    "h_Wplus_eta": h_Wplus_eta,
    "h_Wplus_phi": h_Wplus_phi,
    "h_Wplus_mass": h_Wplus_mass,
    "h_Wminus_pt": h_Wminus_pt,
    "h_Wminus_eta": h_Wminus_eta,
    "h_Wminus_phi": h_Wminus_phi,
    "h_Wminus_mass": h_Wminus_mass,
    # Leptons
    "h_leptonPt": h_lepton_pt,
    "h_leptoneta": h_lepton_eta,
    "h_leptonphi": h_lepton_phi,
    "h_antiLeptonPt": h_antilepton_pt,
    "h_antiLeptoneta": h_antilepton_eta,
    "h_antiLeptonphi": h_antilepton_phi,
    "h_neutrinoPt": h_neutrino_pt,
    "h_neutrinoeta": h_neutrino_eta,
    "h_neutrinophi": h_neutrino_phi,
    "h_antiNeutrinoPt": h_antineutrino_pt,
    "h_antiNeutrinoeta": h_antineutrino_eta,
    "h_antiNeutrinophi": h_antineutrino_phi,
    # Light quarks from hadronic W decay
    "h_utype_quark_pt": h_utype_quark_pt,
    "h_utype_quark_eta": h_utype_quark_eta,
    "h_utype_quark_phi": h_utype_quark_phi,
    "h_antiUtype_quark_pt": h_antiUtype_quark_pt,
    "h_antiUtype_quark_eta": h_antiUtype_quark_eta,
    "h_antiUtype_quark_phi": h_antiUtype_quark_phi,
    "h_dtype_quark_pt": h_dtype_quark_pt,
    "h_dtype_quark_eta": h_dtype_quark_eta,
    "h_dtype_quark_phi": h_dtype_quark_phi,
    "h_antiDtype_quark_pt": h_antiDtype_quark_pt,
    "h_antiDtype_quark_eta": h_antiDtype_quark_eta,
    "h_antiDtype_quark_phi": h_antiDtype_quark_phi,
    
    ##################################
    ### Spin correlation variables ###
    ##################################
    # lepton exclusive polarization
    "h_cos_theta1n_antilepton": h_cos_theta1n_antilepton,
    "h_cos_theta1r_antilepton": h_cos_theta1r_antilepton,
    "h_cos_theta1k_antilepton": h_cos_theta1k_antilepton,
    "h_cos_theta1rStar_antilepton": h_cos_theta1rStar_antilepton,
    "h_cos_theta1kStar_antilepton": h_cos_theta1kStar_antilepton,
    "h_cos_theta2n_lepton": h_cos_theta2n_lepton,
    "h_cos_theta2r_lepton": h_cos_theta2r_lepton,
    "h_cos_theta2k_lepton": h_cos_theta2k_lepton,
    "h_cos_theta2rStar_lepton": h_cos_theta2rStar_lepton,    
    "h_cos_theta2kStar_lepton": h_cos_theta2kStar_lepton,
    # Polarization
    "h_lb_cos_theta1n": h_lb_cos_theta1n,
    "h_lb_cos_theta1r": h_lb_cos_theta1r,
    "h_lb_cos_theta1k": h_lb_cos_theta1k,
    "h_lb_cos_theta1rStar": h_lb_cos_theta1rStar,
    "h_lb_cos_theta1kStar": h_lb_cos_theta1kStar,
    "h_lb_cos_theta2n": h_lb_cos_theta2n,
    "h_lb_cos_theta2r": h_lb_cos_theta2r,
    "h_lb_cos_theta2k": h_lb_cos_theta2k,
    "h_lb_cos_theta2rStar": h_lb_cos_theta2rStar,
    "h_lb_cos_theta2kStar": h_lb_cos_theta2kStar,

    "h_ld_cos_theta1n": h_ld_cos_theta1n,
    "h_ld_cos_theta1r": h_ld_cos_theta1r,
    "h_ld_cos_theta1k": h_ld_cos_theta1k,
    "h_ld_cos_theta1rStar": h_ld_cos_theta1rStar,
    "h_ld_cos_theta1kStar": h_ld_cos_theta1kStar,
    "h_ld_cos_theta2n": h_ld_cos_theta2n,
    "h_ld_cos_theta2r": h_ld_cos_theta2r,
    "h_ld_cos_theta2k": h_ld_cos_theta2k,
    "h_ld_cos_theta2rStar": h_ld_cos_theta2rStar,
    "h_ld_cos_theta2kStar": h_ld_cos_theta2kStar,
    # Correlation Matrix elements
    "h_lb_Cnn": h_lb_Cnn,
    "h_lb_Cnr": h_lb_Cnr,
    "h_lb_Cnk": h_lb_Cnk,
    "h_lb_Crn": h_lb_Crn,
    "h_lb_Crr": h_lb_Crr,
    "h_lb_Crk": h_lb_Crk,
    "h_lb_Ckn": h_lb_Ckn,
    "h_lb_Ckr": h_lb_Ckr,
    "h_lb_Ckk": h_lb_Ckk,
    
    "h_ld_Cnn": h_ld_Cnn,
    "h_ld_Cnr": h_ld_Cnr,
    "h_ld_Cnk": h_ld_Cnk,
    "h_ld_Crn": h_ld_Crn,
    "h_ld_Crr": h_ld_Crr,
    "h_ld_Crk": h_ld_Crk,
    "h_ld_Ckn": h_ld_Ckn,
    "h_ld_Ckr": h_ld_Ckr,
    "h_ld_Ckk": h_ld_Ckk,
    # Entanglement Witness
    "h_lb_trC": h_lb_trC,
    "h_lb_cHel": h_lb_cHel,
    "h_lb_cHel_P3n": h_lb_cHel_P3n,

    "h_ld_trC": h_ld_trC,
    "h_ld_cHel": h_ld_cHel,
    "h_ld_cHel_P3n": h_ld_cHel_P3n,


    ## Bernreuther variables ##

    "h_lb_sigmaPhi": h_lb_sigmaPhi,
    "h_lb_deltaPhi": h_lb_deltaPhi,
    "h_ld_sigmaPhi": h_ld_sigmaPhi,
    "h_ld_deltaPhi": h_ld_deltaPhi,

    ### Bins of mttbar ###
    ######################
    
    ### mtt [300, 400] GeV
    "h_cos_theta1n_antilepton_mtt300to400": h_cos_theta1n_antilepton_mtt300to400,
    "h_cos_theta1r_antilepton_mtt300to400": h_cos_theta1r_antilepton_mtt300to400,
    "h_cos_theta1k_antilepton_mtt300to400": h_cos_theta1k_antilepton_mtt300to400,
    "h_cos_theta1rStar_antilepton_mtt300to400": h_cos_theta1rStar_antilepton_mtt300to400,
    "h_cos_theta1kStar_antilepton_mtt300to400": h_cos_theta1kStar_antilepton_mtt300to400,
    "h_cos_theta2n_lepton_mtt300to400": h_cos_theta2n_lepton_mtt300to400,
    "h_cos_theta2r_lepton_mtt300to400": h_cos_theta2r_lepton_mtt300to400,
    "h_cos_theta2k_lepton_mtt300to400": h_cos_theta2k_lepton_mtt300to400,
    "h_cos_theta2rStar_lepton_mtt300to400": h_cos_theta2rStar_lepton_mtt300to400,
    "h_cos_theta2kStar_lepton_mtt300to400": h_cos_theta2kStar_lepton_mtt300to400,

    "h_lb_cos_theta1n_mtt300to400": h_lb_cos_theta1n_mtt300to400,
    "h_lb_cos_theta1r_mtt300to400": h_lb_cos_theta1r_mtt300to400,
    "h_lb_cos_theta1k_mtt300to400": h_lb_cos_theta1k_mtt300to400,
    "h_lb_cos_theta1rStar_mtt300to400": h_lb_cos_theta1rStar_mtt300to400,
    "h_lb_cos_theta1kStar_mtt300to400": h_lb_cos_theta1kStar_mtt300to400,
    "h_lb_cos_theta2n_mtt300to400": h_lb_cos_theta2n_mtt300to400,
    "h_lb_cos_theta2r_mtt300to400": h_lb_cos_theta2r_mtt300to400,
    "h_lb_cos_theta2k_mtt300to400": h_lb_cos_theta2k_mtt300to400,
    "h_lb_cos_theta2rStar_mtt300to400": h_lb_cos_theta2rStar_mtt300to400,
    "h_lb_cos_theta2kStar_mtt300to400": h_lb_cos_theta2kStar_mtt300to400,
    "h_lb_Cnn_mtt300to400": h_lb_Cnn_mtt300to400,
    "h_lb_Cnr_mtt300to400": h_lb_Cnr_mtt300to400,
    "h_lb_Cnk_mtt300to400": h_lb_Cnk_mtt300to400,
    "h_lb_Crn_mtt300to400": h_lb_Crn_mtt300to400,
    "h_lb_Crr_mtt300to400": h_lb_Crr_mtt300to400,
    "h_lb_Crk_mtt300to400": h_lb_Crk_mtt300to400,
    "h_lb_Ckn_mtt300to400": h_lb_Ckn_mtt300to400,
    "h_lb_Ckr_mtt300to400": h_lb_Ckr_mtt300to400,
    "h_lb_Ckk_mtt300to400": h_lb_Ckk_mtt300to400,
    "h_lb_trC_mtt300to400": h_lb_trC_mtt300to400,
    "h_lb_cHel_mtt300to400": h_lb_cHel_mtt300to400,
    "h_lb_cHel_P3n_mtt300to400": h_lb_cHel_P3n_mtt300to400,
    
    "h_ld_cos_theta1n_mtt300to400": h_ld_cos_theta1n_mtt300to400,
    "h_ld_cos_theta1r_mtt300to400": h_ld_cos_theta1r_mtt300to400,
    "h_ld_cos_theta1k_mtt300to400": h_ld_cos_theta1k_mtt300to400,
    "h_ld_cos_theta1rStar_mtt300to400": h_ld_cos_theta1rStar_mtt300to400,
    "h_ld_cos_theta1kStar_mtt300to400": h_ld_cos_theta1kStar_mtt300to400,
    "h_ld_cos_theta2n_mtt300to400": h_ld_cos_theta2n_mtt300to400,
    "h_ld_cos_theta2r_mtt300to400": h_ld_cos_theta2r_mtt300to400,
    "h_ld_cos_theta2k_mtt300to400": h_ld_cos_theta2k_mtt300to400,
    "h_ld_cos_theta2rStar_mtt300to400": h_ld_cos_theta2rStar_mtt300to400,
    "h_ld_cos_theta2kStar_mtt300to400": h_ld_cos_theta2kStar_mtt300to400,
    "h_ld_Cnn_mtt300to400": h_ld_Cnn_mtt300to400,
    "h_ld_Cnr_mtt300to400": h_ld_Cnr_mtt300to400,
    "h_ld_Cnk_mtt300to400": h_ld_Cnk_mtt300to400,
    "h_ld_Crn_mtt300to400": h_ld_Crn_mtt300to400,
    "h_ld_Crr_mtt300to400": h_ld_Crr_mtt300to400,
    "h_ld_Crk_mtt300to400": h_ld_Crk_mtt300to400,
    "h_ld_Ckn_mtt300to400": h_ld_Ckn_mtt300to400,
    "h_ld_Ckr_mtt300to400": h_ld_Ckr_mtt300to400,
    "h_ld_Ckk_mtt300to400": h_ld_Ckk_mtt300to400,
    "h_ld_trC_mtt300to400": h_ld_trC_mtt300to400,
    "h_ld_cHel_mtt300to400": h_ld_cHel_mtt300to400,
    "h_ld_cHel_P3n_mtt300to400": h_ld_cHel_P3n_mtt300to400,

    "h_lb_sigmaPhi_mtt300to400": h_lb_sigmaPhi_mtt300to400,
    "h_lb_deltaPhi_mtt300to400": h_lb_deltaPhi_mtt300to400,
    "h_ld_sigmaPhi_mtt300to400": h_ld_sigmaPhi_mtt300to400,
    "h_ld_deltaPhi_mtt300to400": h_ld_deltaPhi_mtt300to400,

            # beta < 0.9
    "h_cos_theta1n_antilepton_mtt300to400_beta_lt_0p9": h_cos_theta1n_antilepton_mtt300to400_beta_lt_0p9,
    "h_cos_theta1r_antilepton_mtt300to400_beta_lt_0p9": h_cos_theta1r_antilepton_mtt300to400_beta_lt_0p9,
    "h_cos_theta1k_antilepton_mtt300to400_beta_lt_0p9": h_cos_theta1k_antilepton_mtt300to400_beta_lt_0p9,
    "h_cos_theta1rStar_antilepton_mtt300to400_beta_lt_0p9": h_cos_theta1rStar_antilepton_mtt300to400_beta_lt_0p9,
    "h_cos_theta1kStar_antilepton_mtt300to400_beta_lt_0p9": h_cos_theta1kStar_antilepton_mtt300to400_beta_lt_0p9,
    "h_cos_theta2n_lepton_mtt300to400_beta_lt_0p9": h_cos_theta2n_lepton_mtt300to400_beta_lt_0p9,
    "h_cos_theta2r_lepton_mtt300to400_beta_lt_0p9": h_cos_theta2r_lepton_mtt300to400_beta_lt_0p9,
    "h_cos_theta2k_lepton_mtt300to400_beta_lt_0p9": h_cos_theta2k_lepton_mtt300to400_beta_lt_0p9,
    "h_cos_theta2rStar_lepton_mtt300to400_beta_lt_0p9": h_cos_theta2rStar_lepton_mtt300to400_beta_lt_0p9,
    "h_cos_theta2kStar_lepton_mtt300to400_beta_lt_0p9": h_cos_theta2kStar_lepton_mtt300to400_beta_lt_0p9,

    "h_lb_cos_theta1n_mtt300to400_beta_lt_0p9": h_lb_cos_theta1n_mtt300to400_beta_lt_0p9,
    "h_lb_cos_theta1r_mtt300to400_beta_lt_0p9": h_lb_cos_theta1r_mtt300to400_beta_lt_0p9,
    "h_lb_cos_theta1k_mtt300to400_beta_lt_0p9": h_lb_cos_theta1k_mtt300to400_beta_lt_0p9,
    "h_lb_cos_theta1rStar_mtt300to400_beta_lt_0p9": h_lb_cos_theta1rStar_mtt300to400_beta_lt_0p9,
    "h_lb_cos_theta1kStar_mtt300to400_beta_lt_0p9": h_lb_cos_theta1kStar_mtt300to400_beta_lt_0p9,
    "h_lb_cos_theta2n_mtt300to400_beta_lt_0p9": h_lb_cos_theta2n_mtt300to400_beta_lt_0p9,
    "h_lb_cos_theta2r_mtt300to400_beta_lt_0p9": h_lb_cos_theta2r_mtt300to400_beta_lt_0p9,
    "h_lb_cos_theta2k_mtt300to400_beta_lt_0p9": h_lb_cos_theta2k_mtt300to400_beta_lt_0p9,
    "h_lb_cos_theta2rStar_mtt300to400_beta_lt_0p9": h_lb_cos_theta2rStar_mtt300to400_beta_lt_0p9,
    "h_lb_cos_theta2kStar_mtt300to400_beta_lt_0p9": h_lb_cos_theta2kStar_mtt300to400_beta_lt_0p9,
    "h_lb_Cnn_mtt300to400_beta_lt_0p9": h_lb_Cnn_mtt300to400_beta_lt_0p9,
    "h_lb_Cnr_mtt300to400_beta_lt_0p9": h_lb_Cnr_mtt300to400_beta_lt_0p9,
    "h_lb_Cnk_mtt300to400_beta_lt_0p9": h_lb_Cnk_mtt300to400_beta_lt_0p9,
    "h_lb_Crn_mtt300to400_beta_lt_0p9": h_lb_Crn_mtt300to400_beta_lt_0p9,
    "h_lb_Crr_mtt300to400_beta_lt_0p9": h_lb_Crr_mtt300to400_beta_lt_0p9,
    "h_lb_Crk_mtt300to400_beta_lt_0p9": h_lb_Crk_mtt300to400_beta_lt_0p9,
    "h_lb_Ckn_mtt300to400_beta_lt_0p9": h_lb_Ckn_mtt300to400_beta_lt_0p9,
    "h_lb_Ckr_mtt300to400_beta_lt_0p9": h_lb_Ckr_mtt300to400_beta_lt_0p9,
    "h_lb_Ckk_mtt300to400_beta_lt_0p9": h_lb_Ckk_mtt300to400_beta_lt_0p9,
    "h_lb_trC_mtt300to400_beta_lt_0p9": h_lb_trC_mtt300to400_beta_lt_0p9,
    "h_lb_cHel_mtt300to400_beta_lt_0p9": h_lb_cHel_mtt300to400_beta_lt_0p9,
    "h_lb_cHel_P3n_mtt300to400_beta_lt_0p9": h_lb_cHel_P3n_mtt300to400_beta_lt_0p9,

    "h_ld_cos_theta1n_mtt300to400_beta_lt_0p9": h_ld_cos_theta1n_mtt300to400_beta_lt_0p9,
    "h_ld_cos_theta1r_mtt300to400_beta_lt_0p9": h_ld_cos_theta1r_mtt300to400_beta_lt_0p9,
    "h_ld_cos_theta1k_mtt300to400_beta_lt_0p9": h_ld_cos_theta1k_mtt300to400_beta_lt_0p9,
    "h_ld_cos_theta1rStar_mtt300to400_beta_lt_0p9": h_ld_cos_theta1rStar_mtt300to400_beta_lt_0p9,
    "h_ld_cos_theta1kStar_mtt300to400_beta_lt_0p9": h_ld_cos_theta1kStar_mtt300to400_beta_lt_0p9,
    "h_ld_cos_theta2n_mtt300to400_beta_lt_0p9": h_ld_cos_theta2n_mtt300to400_beta_lt_0p9,
    "h_ld_cos_theta2r_mtt300to400_beta_lt_0p9": h_ld_cos_theta2r_mtt300to400_beta_lt_0p9,
    "h_ld_cos_theta2k_mtt300to400_beta_lt_0p9": h_ld_cos_theta2k_mtt300to400_beta_lt_0p9,
    "h_ld_cos_theta2rStar_mtt300to400_beta_lt_0p9": h_ld_cos_theta2rStar_mtt300to400_beta_lt_0p9,
    "h_ld_cos_theta2kStar_mtt300to400_beta_lt_0p9": h_ld_cos_theta2kStar_mtt300to400_beta_lt_0p9,
    "h_ld_Cnn_mtt300to400_beta_lt_0p9": h_ld_Cnn_mtt300to400_beta_lt_0p9,
    "h_ld_Cnr_mtt300to400_beta_lt_0p9": h_ld_Cnr_mtt300to400_beta_lt_0p9,
    "h_ld_Cnk_mtt300to400_beta_lt_0p9": h_ld_Cnk_mtt300to400_beta_lt_0p9,
    "h_ld_Crn_mtt300to400_beta_lt_0p9": h_ld_Crn_mtt300to400_beta_lt_0p9,
    "h_ld_Crr_mtt300to400_beta_lt_0p9": h_ld_Crr_mtt300to400_beta_lt_0p9,
    "h_ld_Crk_mtt300to400_beta_lt_0p9": h_ld_Crk_mtt300to400_beta_lt_0p9,
    "h_ld_Ckn_mtt300to400_beta_lt_0p9": h_ld_Ckn_mtt300to400_beta_lt_0p9,
    "h_ld_Ckr_mtt300to400_beta_lt_0p9": h_ld_Ckr_mtt300to400_beta_lt_0p9,
    "h_ld_Ckk_mtt300to400_beta_lt_0p9": h_ld_Ckk_mtt300to400_beta_lt_0p9,
    "h_ld_trC_mtt300to400_beta_lt_0p9": h_ld_trC_mtt300to400_beta_lt_0p9,
    "h_ld_cHel_mtt300to400_beta_lt_0p9": h_ld_cHel_mtt300to400_beta_lt_0p9,
    "h_ld_cHel_P3n_mtt300to400_beta_lt_0p9": h_ld_cHel_P3n_mtt300to400_beta_lt_0p9,

    "h_lb_sigmaPhi_mtt300to400_beta_lt_0p9": h_lb_sigmaPhi_mtt300to400_beta_lt_0p9,
    "h_lb_deltaPhi_mtt300to400_beta_lt_0p9": h_lb_deltaPhi_mtt300to400_beta_lt_0p9,
    "h_ld_sigmaPhi_mtt300to400_beta_lt_0p9": h_ld_sigmaPhi_mtt300to400_beta_lt_0p9,
    "h_ld_deltaPhi_mtt300to400_beta_lt_0p9": h_ld_deltaPhi_mtt300to400_beta_lt_0p9,

        ## |cosTSA| < 0.4
    "h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p4": h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p4,
    "h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p4": h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p4,
    "h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p4": h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p4,
    "h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p4": h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p4,
    "h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p4": h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p4,
    "h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p4": h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p4,
    "h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p4": h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p4,
    "h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p4": h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p4,
    "h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p4": h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p4,
    "h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p4": h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p4,

    "h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p4": h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p4,
    "h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p4": h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p4,
    "h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p4": h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p4,
    "h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4": h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4,
    "h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4": h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4,
    "h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p4": h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p4,
    "h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p4": h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p4,
    "h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p4": h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p4,
    "h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4": h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4,
    "h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4": h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4,
    "h_lb_Cnn_mtt300to400_cosTSA_lt_0p4": h_lb_Cnn_mtt300to400_cosTSA_lt_0p4,
    "h_lb_Cnr_mtt300to400_cosTSA_lt_0p4": h_lb_Cnr_mtt300to400_cosTSA_lt_0p4,
    "h_lb_Cnk_mtt300to400_cosTSA_lt_0p4": h_lb_Cnk_mtt300to400_cosTSA_lt_0p4,
    "h_lb_Crn_mtt300to400_cosTSA_lt_0p4": h_lb_Crn_mtt300to400_cosTSA_lt_0p4,
    "h_lb_Crr_mtt300to400_cosTSA_lt_0p4": h_lb_Crr_mtt300to400_cosTSA_lt_0p4,
    "h_lb_Crk_mtt300to400_cosTSA_lt_0p4": h_lb_Crk_mtt300to400_cosTSA_lt_0p4,
    "h_lb_Ckn_mtt300to400_cosTSA_lt_0p4": h_lb_Ckn_mtt300to400_cosTSA_lt_0p4,
    "h_lb_Ckr_mtt300to400_cosTSA_lt_0p4": h_lb_Ckr_mtt300to400_cosTSA_lt_0p4,
    "h_lb_Ckk_mtt300to400_cosTSA_lt_0p4": h_lb_Ckk_mtt300to400_cosTSA_lt_0p4,
    "h_lb_trC_mtt300to400_cosTSA_lt_0p4": h_lb_trC_mtt300to400_cosTSA_lt_0p4,
    "h_lb_cHel_mtt300to400_cosTSA_lt_0p4": h_lb_cHel_mtt300to400_cosTSA_lt_0p4,
    "h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p4": h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p4,

    "h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p4": h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p4,
    "h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p4": h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p4,
    "h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p4": h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p4,
    "h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4": h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4,
    "h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4": h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4,
    "h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p4": h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p4,
    "h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p4": h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p4,
    "h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p4": h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p4,
    "h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4": h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4,
    "h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4": h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4,   
    "h_ld_Cnn_mtt300to400_cosTSA_lt_0p4": h_ld_Cnn_mtt300to400_cosTSA_lt_0p4,
    "h_ld_Cnr_mtt300to400_cosTSA_lt_0p4": h_ld_Cnr_mtt300to400_cosTSA_lt_0p4,
    "h_ld_Cnk_mtt300to400_cosTSA_lt_0p4": h_ld_Cnk_mtt300to400_cosTSA_lt_0p4,
    "h_ld_Crn_mtt300to400_cosTSA_lt_0p4": h_ld_Crn_mtt300to400_cosTSA_lt_0p4,
    "h_ld_Crr_mtt300to400_cosTSA_lt_0p4": h_ld_Crr_mtt300to400_cosTSA_lt_0p4,
    "h_ld_Crk_mtt300to400_cosTSA_lt_0p4": h_ld_Crk_mtt300to400_cosTSA_lt_0p4,
    "h_ld_Ckn_mtt300to400_cosTSA_lt_0p4": h_ld_Ckn_mtt300to400_cosTSA_lt_0p4,
    "h_ld_Ckr_mtt300to400_cosTSA_lt_0p4": h_ld_Ckr_mtt300to400_cosTSA_lt_0p4,
    "h_ld_Ckk_mtt300to400_cosTSA_lt_0p4": h_ld_Ckk_mtt300to400_cosTSA_lt_0p4,
    "h_ld_trC_mtt300to400_cosTSA_lt_0p4": h_ld_trC_mtt300to400_cosTSA_lt_0p4,
    "h_ld_cHel_mtt300to400_cosTSA_lt_0p4": h_ld_cHel_mtt300to400_cosTSA_lt_0p4,
    "h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p4": h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p4,

    "h_lb_sigmaPhi_mtt300to400_cosTSA_lt_0p4": h_lb_sigmaPhi_mtt300to400_cosTSA_lt_0p4,
    "h_lb_deltaPhi_mtt300to400_cosTSA_lt_0p4": h_lb_deltaPhi_mtt300to400_cosTSA_lt_0p4,
    "h_ld_sigmaPhi_mtt300to400_cosTSA_lt_0p4": h_ld_sigmaPhi_mtt300to400_cosTSA_lt_0p4,
    "h_ld_deltaPhi_mtt300to400_cosTSA_lt_0p4": h_ld_deltaPhi_mtt300to400_cosTSA_lt_0p4,

            # beta < 0.9
    "h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,

    "h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_Cnn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_Cnn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_Cnr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_Cnr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_Cnk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_Cnk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_Crn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_Crn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_Crr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_Crr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_Crk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_Crk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_Ckn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_Ckn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_Ckr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_Ckr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_Ckk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_Ckk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_trC_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_trC_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_cHel_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_cHel_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,

    "h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_Cnn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_Cnn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_Cnr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_Cnr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_Cnk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_Cnk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_Crn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_Crn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_Crr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_Crr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_Crk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_Crk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_Ckn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_Ckn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_Ckr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_Ckr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_Ckk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_Ckk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_trC_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_trC_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_cHel_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_cHel_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,

    "h_lb_sigmaPhi_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_sigmaPhi_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_lb_deltaPhi_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_lb_deltaPhi_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_sigmaPhi_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_sigmaPhi_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,
    "h_ld_deltaPhi_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9": h_ld_deltaPhi_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9,

        ## |cosTSA| < 0.7
    "h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p7": h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p7,
    "h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p7": h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p7,
    "h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p7": h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p7,
    "h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p7": h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p7,
    "h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p7": h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p7,
    "h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p7": h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p7,
    "h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p7": h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p7,
    "h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p7": h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p7,
    "h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p7": h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p7,
    "h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p7": h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p7,

    "h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p7": h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p7,
    "h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p7": h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p7,
    "h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p7": h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p7,
    "h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7": h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7,
    "h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7": h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7,
    "h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p7": h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p7,
    "h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p7": h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p7,
    "h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p7": h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p7,
    "h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7": h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7,
    "h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7": h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7,
    "h_lb_Cnn_mtt300to400_cosTSA_lt_0p7": h_lb_Cnn_mtt300to400_cosTSA_lt_0p7,
    "h_lb_Cnr_mtt300to400_cosTSA_lt_0p7": h_lb_Cnr_mtt300to400_cosTSA_lt_0p7,
    "h_lb_Cnk_mtt300to400_cosTSA_lt_0p7": h_lb_Cnk_mtt300to400_cosTSA_lt_0p7,
    "h_lb_Crn_mtt300to400_cosTSA_lt_0p7": h_lb_Crn_mtt300to400_cosTSA_lt_0p7,
    "h_lb_Crr_mtt300to400_cosTSA_lt_0p7": h_lb_Crr_mtt300to400_cosTSA_lt_0p7,
    "h_lb_Crk_mtt300to400_cosTSA_lt_0p7": h_lb_Crk_mtt300to400_cosTSA_lt_0p7,
    "h_lb_Ckn_mtt300to400_cosTSA_lt_0p7": h_lb_Ckn_mtt300to400_cosTSA_lt_0p7,
    "h_lb_Ckr_mtt300to400_cosTSA_lt_0p7": h_lb_Ckr_mtt300to400_cosTSA_lt_0p7,
    "h_lb_Ckk_mtt300to400_cosTSA_lt_0p7": h_lb_Ckk_mtt300to400_cosTSA_lt_0p7,
    "h_lb_trC_mtt300to400_cosTSA_lt_0p7": h_lb_trC_mtt300to400_cosTSA_lt_0p7,
    "h_lb_cHel_mtt300to400_cosTSA_lt_0p7": h_lb_cHel_mtt300to400_cosTSA_lt_0p7,
    "h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p7": h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p7,
    
    "h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p7": h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p7,
    "h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p7": h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p7,
    "h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p7": h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p7,
    "h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7": h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7,
    "h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7": h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7,
    "h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p7": h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p7,
    "h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p7": h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p7,
    "h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p7": h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p7,
    "h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7": h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7,
    "h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7": h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7,
    "h_ld_Cnn_mtt300to400_cosTSA_lt_0p7": h_ld_Cnn_mtt300to400_cosTSA_lt_0p7,
    "h_ld_Cnr_mtt300to400_cosTSA_lt_0p7": h_ld_Cnr_mtt300to400_cosTSA_lt_0p7,
    "h_ld_Cnk_mtt300to400_cosTSA_lt_0p7": h_ld_Cnk_mtt300to400_cosTSA_lt_0p7,
    "h_ld_Crn_mtt300to400_cosTSA_lt_0p7": h_ld_Crn_mtt300to400_cosTSA_lt_0p7,
    "h_ld_Crr_mtt300to400_cosTSA_lt_0p7": h_ld_Crr_mtt300to400_cosTSA_lt_0p7,
    "h_ld_Crk_mtt300to400_cosTSA_lt_0p7": h_ld_Crk_mtt300to400_cosTSA_lt_0p7,
    "h_ld_Ckn_mtt300to400_cosTSA_lt_0p7": h_ld_Ckn_mtt300to400_cosTSA_lt_0p7,
    "h_ld_Ckr_mtt300to400_cosTSA_lt_0p7": h_ld_Ckr_mtt300to400_cosTSA_lt_0p7,
    "h_ld_Ckk_mtt300to400_cosTSA_lt_0p7": h_ld_Ckk_mtt300to400_cosTSA_lt_0p7,
    "h_ld_trC_mtt300to400_cosTSA_lt_0p7": h_ld_trC_mtt300to400_cosTSA_lt_0p7,
    "h_ld_cHel_mtt300to400_cosTSA_lt_0p7": h_ld_cHel_mtt300to400_cosTSA_lt_0p7,
    "h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p7": h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p7,

    "h_lb_sigmaPhi_mtt300to400_cosTSA_lt_0p7": h_lb_sigmaPhi_mtt300to400_cosTSA_lt_0p7,
    "h_lb_deltaPhi_mtt300to400_cosTSA_lt_0p7": h_lb_deltaPhi_mtt300to400_cosTSA_lt_0p7,
    "h_ld_sigmaPhi_mtt300to400_cosTSA_lt_0p7": h_ld_sigmaPhi_mtt300to400_cosTSA_lt_0p7,
    "h_ld_deltaPhi_mtt300to400_cosTSA_lt_0p7": h_ld_deltaPhi_mtt300to400_cosTSA_lt_0p7,

            # beta < 0.9
    "h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,

    "h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_Cnn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_Cnn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_Cnr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_Cnr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_Cnk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_Cnk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_Crn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_Crn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_Crr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_Crr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_Crk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_Crk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_Ckn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_Ckn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_Ckr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_Ckr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_Ckk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_Ckk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_trC_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_trC_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_cHel_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_cHel_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,

    "h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_Cnn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_Cnn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_Cnr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_Cnr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_Cnk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_Cnk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_Crn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_Crn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_Crr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_Crr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_Crk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_Crk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_Ckn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_Ckn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_Ckr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_Ckr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_Ckk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_Ckk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_trC_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_trC_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_cHel_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_cHel_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,

    "h_lb_sigmaPhi_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_sigmaPhi_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_lb_deltaPhi_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_lb_deltaPhi_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_sigmaPhi_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_sigmaPhi_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,
    "h_ld_deltaPhi_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9": h_ld_deltaPhi_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9,

        ## |cosTSA| > 0.7
    "h_cos_theta1n_antilepton_mtt300to400_cosTSA_gt_0p7": h_cos_theta1n_antilepton_mtt300to400_cosTSA_gt_0p7,
    "h_cos_theta1r_antilepton_mtt300to400_cosTSA_gt_0p7": h_cos_theta1r_antilepton_mtt300to400_cosTSA_gt_0p7,
    "h_cos_theta1k_antilepton_mtt300to400_cosTSA_gt_0p7": h_cos_theta1k_antilepton_mtt300to400_cosTSA_gt_0p7,
    "h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_gt_0p7": h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_gt_0p7,
    "h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_gt_0p7": h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_gt_0p7,
    "h_cos_theta2n_lepton_mtt300to400_cosTSA_gt_0p7": h_cos_theta2n_lepton_mtt300to400_cosTSA_gt_0p7,
    "h_cos_theta2r_lepton_mtt300to400_cosTSA_gt_0p7": h_cos_theta2r_lepton_mtt300to400_cosTSA_gt_0p7,
    "h_cos_theta2k_lepton_mtt300to400_cosTSA_gt_0p7": h_cos_theta2k_lepton_mtt300to400_cosTSA_gt_0p7,
    "h_cos_theta2rStar_lepton_mtt300to400_cosTSA_gt_0p7": h_cos_theta2rStar_lepton_mtt300to400_cosTSA_gt_0p7,
    "h_cos_theta2kStar_lepton_mtt300to400_cosTSA_gt_0p7": h_cos_theta2kStar_lepton_mtt300to400_cosTSA_gt_0p7,

    "h_lb_cos_theta1n_mtt300to400_cosTSA_gt_0p7": h_lb_cos_theta1n_mtt300to400_cosTSA_gt_0p7,
    "h_lb_cos_theta1r_mtt300to400_cosTSA_gt_0p7": h_lb_cos_theta1r_mtt300to400_cosTSA_gt_0p7,
    "h_lb_cos_theta1k_mtt300to400_cosTSA_gt_0p7": h_lb_cos_theta1k_mtt300to400_cosTSA_gt_0p7,
    "h_lb_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7": h_lb_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7,
    "h_lb_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7": h_lb_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7,
    "h_lb_cos_theta2n_mtt300to400_cosTSA_gt_0p7": h_lb_cos_theta2n_mtt300to400_cosTSA_gt_0p7,
    "h_lb_cos_theta2r_mtt300to400_cosTSA_gt_0p7": h_lb_cos_theta2r_mtt300to400_cosTSA_gt_0p7,
    "h_lb_cos_theta2k_mtt300to400_cosTSA_gt_0p7": h_lb_cos_theta2k_mtt300to400_cosTSA_gt_0p7,
    "h_lb_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7": h_lb_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7,
    "h_lb_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7": h_lb_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7,
    "h_lb_Cnn_mtt300to400_cosTSA_gt_0p7": h_lb_Cnn_mtt300to400_cosTSA_gt_0p7,
    "h_lb_Cnr_mtt300to400_cosTSA_gt_0p7": h_lb_Cnr_mtt300to400_cosTSA_gt_0p7,
    "h_lb_Cnk_mtt300to400_cosTSA_gt_0p7": h_lb_Cnk_mtt300to400_cosTSA_gt_0p7,
    "h_lb_Crn_mtt300to400_cosTSA_gt_0p7": h_lb_Crn_mtt300to400_cosTSA_gt_0p7,
    "h_lb_Crr_mtt300to400_cosTSA_gt_0p7": h_lb_Crr_mtt300to400_cosTSA_gt_0p7,
    "h_lb_Crk_mtt300to400_cosTSA_gt_0p7": h_lb_Crk_mtt300to400_cosTSA_gt_0p7,
    "h_lb_Ckn_mtt300to400_cosTSA_gt_0p7": h_lb_Ckn_mtt300to400_cosTSA_gt_0p7,
    "h_lb_Ckr_mtt300to400_cosTSA_gt_0p7": h_lb_Ckr_mtt300to400_cosTSA_gt_0p7,
    "h_lb_Ckk_mtt300to400_cosTSA_gt_0p7": h_lb_Ckk_mtt300to400_cosTSA_gt_0p7,
    "h_lb_trC_mtt300to400_cosTSA_gt_0p7": h_lb_trC_mtt300to400_cosTSA_gt_0p7,
    "h_lb_cHel_mtt300to400_cosTSA_gt_0p7": h_lb_cHel_mtt300to400_cosTSA_gt_0p7,
    "h_lb_cHel_P3n_mtt300to400_cosTSA_gt_0p7": h_lb_cHel_P3n_mtt300to400_cosTSA_gt_0p7,

    "h_ld_cos_theta1n_mtt300to400_cosTSA_gt_0p7": h_ld_cos_theta1n_mtt300to400_cosTSA_gt_0p7,
    "h_ld_cos_theta1r_mtt300to400_cosTSA_gt_0p7": h_ld_cos_theta1r_mtt300to400_cosTSA_gt_0p7,
    "h_ld_cos_theta1k_mtt300to400_cosTSA_gt_0p7": h_ld_cos_theta1k_mtt300to400_cosTSA_gt_0p7,
    "h_ld_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7": h_ld_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7,
    "h_ld_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7": h_ld_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7,
    "h_ld_cos_theta2n_mtt300to400_cosTSA_gt_0p7": h_ld_cos_theta2n_mtt300to400_cosTSA_gt_0p7,
    "h_ld_cos_theta2r_mtt300to400_cosTSA_gt_0p7": h_ld_cos_theta2r_mtt300to400_cosTSA_gt_0p7,
    "h_ld_cos_theta2k_mtt300to400_cosTSA_gt_0p7": h_ld_cos_theta2k_mtt300to400_cosTSA_gt_0p7,
    "h_ld_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7": h_ld_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7,
    "h_ld_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7": h_ld_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7,
    "h_ld_Cnn_mtt300to400_cosTSA_gt_0p7": h_ld_Cnn_mtt300to400_cosTSA_gt_0p7,
    "h_ld_Cnr_mtt300to400_cosTSA_gt_0p7": h_ld_Cnr_mtt300to400_cosTSA_gt_0p7,
    "h_ld_Cnk_mtt300to400_cosTSA_gt_0p7": h_ld_Cnk_mtt300to400_cosTSA_gt_0p7,
    "h_ld_Crn_mtt300to400_cosTSA_gt_0p7": h_ld_Crn_mtt300to400_cosTSA_gt_0p7,
    "h_ld_Crr_mtt300to400_cosTSA_gt_0p7": h_ld_Crr_mtt300to400_cosTSA_gt_0p7,
    "h_ld_Crk_mtt300to400_cosTSA_gt_0p7": h_ld_Crk_mtt300to400_cosTSA_gt_0p7,
    "h_ld_Ckn_mtt300to400_cosTSA_gt_0p7": h_ld_Ckn_mtt300to400_cosTSA_gt_0p7,
    "h_ld_Ckr_mtt300to400_cosTSA_gt_0p7": h_ld_Ckr_mtt300to400_cosTSA_gt_0p7,
    "h_ld_Ckk_mtt300to400_cosTSA_gt_0p7": h_ld_Ckk_mtt300to400_cosTSA_gt_0p7,
    "h_ld_trC_mtt300to400_cosTSA_gt_0p7": h_ld_trC_mtt300to400_cosTSA_gt_0p7,
    "h_ld_cHel_mtt300to400_cosTSA_gt_0p7": h_ld_cHel_mtt300to400_cosTSA_gt_0p7,
    "h_ld_cHel_P3n_mtt300to400_cosTSA_gt_0p7": h_ld_cHel_P3n_mtt300to400_cosTSA_gt_0p7,

    "h_lb_sigmaPhi_mtt300to400_cosTSA_gt_0p7": h_lb_sigmaPhi_mtt300to400_cosTSA_gt_0p7,
    "h_lb_deltaPhi_mtt300to400_cosTSA_gt_0p7": h_lb_deltaPhi_mtt300to400_cosTSA_gt_0p7,
    "h_ld_sigmaPhi_mtt300to400_cosTSA_gt_0p7": h_ld_sigmaPhi_mtt300to400_cosTSA_gt_0p7,
    "h_ld_deltaPhi_mtt300to400_cosTSA_gt_0p7": h_ld_deltaPhi_mtt300to400_cosTSA_gt_0p7,

            # beta < 0.9
    "h_cos_theta1n_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_cos_theta1n_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_cos_theta1r_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_cos_theta1r_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_cos_theta1k_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_cos_theta1k_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_cos_theta2n_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_cos_theta2n_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_cos_theta2r_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_cos_theta2r_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_cos_theta2k_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_cos_theta2k_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_cos_theta2rStar_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_cos_theta2rStar_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_cos_theta2kStar_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_cos_theta2kStar_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,

    "h_lb_cos_theta1n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_cos_theta1n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_cos_theta1r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_cos_theta1r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_cos_theta1k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_cos_theta1k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_cos_theta2n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_cos_theta2n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_cos_theta2r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_cos_theta2r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_cos_theta2k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_cos_theta2k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_Cnn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_Cnn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_Cnr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_Cnr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_Cnk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_Cnk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_Crn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_Crn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_Crr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_Crr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_Crk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_Crk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_Ckn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_Ckn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_Ckr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_Ckr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_Ckk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_Ckk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_trC_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_trC_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_cHel_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_cHel_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_cHel_P3n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_cHel_P3n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,

    "h_ld_cos_theta1n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_cos_theta1n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_cos_theta1r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_cos_theta1r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_cos_theta1k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_cos_theta1k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_cos_theta2n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_cos_theta2n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_cos_theta2r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_cos_theta2r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_cos_theta2k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_cos_theta2k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_Cnn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_Cnn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_Cnr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_Cnr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_Cnk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_Cnk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_Crn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_Crn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_Crr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_Crr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_Crk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_Crk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_Ckn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_Ckn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_Ckr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_Ckr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_Ckk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_Ckk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_trC_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_trC_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_cHel_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_cHel_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_cHel_P3n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_cHel_P3n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,

    "h_lb_sigmaPhi_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_sigmaPhi_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_lb_deltaPhi_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_lb_deltaPhi_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_sigmaPhi_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_sigmaPhi_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,
    "h_ld_deltaPhi_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9": h_ld_deltaPhi_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9,

    ### mtt [400, 600] GeV
    "h_cos_theta1n_antilepton_mtt400to600": h_cos_theta1n_antilepton_mtt400to600,
    "h_cos_theta1r_antilepton_mtt400to600": h_cos_theta1r_antilepton_mtt400to600,
    "h_cos_theta1k_antilepton_mtt400to600": h_cos_theta1k_antilepton_mtt400to600,
    "h_cos_theta1rStar_antilepton_mtt400to600": h_cos_theta1rStar_antilepton_mtt400to600,
    "h_cos_theta1kStar_antilepton_mtt400to600": h_cos_theta1kStar_antilepton_mtt400to600,
    "h_cos_theta2n_lepton_mtt400to600": h_cos_theta2n_lepton_mtt400to600,
    "h_cos_theta2r_lepton_mtt400to600": h_cos_theta2r_lepton_mtt400to600,
    "h_cos_theta2k_lepton_mtt400to600": h_cos_theta2k_lepton_mtt400to600,
    "h_cos_theta2rStar_lepton_mtt400to600": h_cos_theta2rStar_lepton_mtt400to600,
    "h_cos_theta2kStar_lepton_mtt400to600": h_cos_theta2kStar_lepton_mtt400to600,

    "h_lb_cos_theta1n_mtt400to600": h_lb_cos_theta1n_mtt400to600,
    "h_lb_cos_theta1r_mtt400to600": h_lb_cos_theta1r_mtt400to600,
    "h_lb_cos_theta1k_mtt400to600": h_lb_cos_theta1k_mtt400to600,
    "h_lb_cos_theta1rStar_mtt400to600": h_lb_cos_theta1rStar_mtt400to600,
    "h_lb_cos_theta1kStar_mtt400to600": h_lb_cos_theta1kStar_mtt400to600,
    "h_lb_cos_theta2n_mtt400to600": h_lb_cos_theta2n_mtt400to600,
    "h_lb_cos_theta2r_mtt400to600": h_lb_cos_theta2r_mtt400to600,
    "h_lb_cos_theta2k_mtt400to600": h_lb_cos_theta2k_mtt400to600,
    "h_lb_cos_theta2rStar_mtt400to600": h_lb_cos_theta2rStar_mtt400to600,
    "h_lb_cos_theta2kStar_mtt400to600": h_lb_cos_theta2kStar_mtt400to600,
    "h_lb_Cnn_mtt400to600": h_lb_Cnn_mtt400to600,
    "h_lb_Cnr_mtt400to600": h_lb_Cnr_mtt400to600,
    "h_lb_Cnk_mtt400to600": h_lb_Cnk_mtt400to600,
    "h_lb_Crn_mtt400to600": h_lb_Crn_mtt400to600,
    "h_lb_Crr_mtt400to600": h_lb_Crr_mtt400to600,
    "h_lb_Crk_mtt400to600": h_lb_Crk_mtt400to600,
    "h_lb_Ckn_mtt400to600": h_lb_Ckn_mtt400to600,
    "h_lb_Ckr_mtt400to600": h_lb_Ckr_mtt400to600,
    "h_lb_Ckk_mtt400to600": h_lb_Ckk_mtt400to600,
    "h_lb_trC_mtt400to600": h_lb_trC_mtt400to600,
    "h_lb_cHel_mtt400to600": h_lb_cHel_mtt400to600,
    "h_lb_cHel_P3n_mtt400to600": h_lb_cHel_P3n_mtt400to600,

    "h_ld_cos_theta1n_mtt400to600": h_ld_cos_theta1n_mtt400to600,
    "h_ld_cos_theta1r_mtt400to600": h_ld_cos_theta1r_mtt400to600,
    "h_ld_cos_theta1k_mtt400to600": h_ld_cos_theta1k_mtt400to600,
    "h_ld_cos_theta1rStar_mtt400to600": h_ld_cos_theta1rStar_mtt400to600,
    "h_ld_cos_theta1kStar_mtt400to600": h_ld_cos_theta1kStar_mtt400to600,
    "h_ld_cos_theta2n_mtt400to600": h_ld_cos_theta2n_mtt400to600,
    "h_ld_cos_theta2r_mtt400to600": h_ld_cos_theta2r_mtt400to600,
    "h_ld_cos_theta2k_mtt400to600": h_ld_cos_theta2k_mtt400to600,
    "h_ld_cos_theta2rStar_mtt400to600": h_ld_cos_theta2rStar_mtt400to600,
    "h_ld_cos_theta2kStar_mtt400to600": h_ld_cos_theta2kStar_mtt400to600,
    "h_ld_Cnn_mtt400to600": h_ld_Cnn_mtt400to600,
    "h_ld_Cnr_mtt400to600": h_ld_Cnr_mtt400to600,
    "h_ld_Cnk_mtt400to600": h_ld_Cnk_mtt400to600,
    "h_ld_Crn_mtt400to600": h_ld_Crn_mtt400to600,
    "h_ld_Crr_mtt400to600": h_ld_Crr_mtt400to600,
    "h_ld_Crk_mtt400to600": h_ld_Crk_mtt400to600,
    "h_ld_Ckn_mtt400to600": h_ld_Ckn_mtt400to600,
    "h_ld_Ckr_mtt400to600": h_ld_Ckr_mtt400to600,
    "h_ld_Ckk_mtt400to600": h_ld_Ckk_mtt400to600,
    "h_ld_trC_mtt400to600": h_ld_trC_mtt400to600,
    "h_ld_cHel_mtt400to600": h_ld_cHel_mtt400to600,
    "h_ld_cHel_P3n_mtt400to600": h_ld_cHel_P3n_mtt400to600,

    "h_lb_sigmaPhi_mtt400to600": h_lb_sigmaPhi_mtt400to600,
    "h_lb_deltaPhi_mtt400to600": h_lb_deltaPhi_mtt400to600,
    "h_ld_sigmaPhi_mtt400to600": h_ld_sigmaPhi_mtt400to600,
    "h_ld_deltaPhi_mtt400to600": h_ld_deltaPhi_mtt400to600,

        ## |cosTSA| < 0.4
    "h_cos_theta1n_antilepton_mtt400to600_cosTSA_lt_0p4": h_cos_theta1n_antilepton_mtt400to600_cosTSA_lt_0p4,
    "h_cos_theta1r_antilepton_mtt400to600_cosTSA_lt_0p4": h_cos_theta1r_antilepton_mtt400to600_cosTSA_lt_0p4,
    "h_cos_theta1k_antilepton_mtt400to600_cosTSA_lt_0p4": h_cos_theta1k_antilepton_mtt400to600_cosTSA_lt_0p4,
    "h_cos_theta1rStar_antilepton_mtt400to600_cosTSA_lt_0p4": h_cos_theta1rStar_antilepton_mtt400to600_cosTSA_lt_0p4,
    "h_cos_theta1kStar_antilepton_mtt400to600_cosTSA_lt_0p4": h_cos_theta1kStar_antilepton_mtt400to600_cosTSA_lt_0p4,
    "h_cos_theta2n_lepton_mtt400to600_cosTSA_lt_0p4": h_cos_theta2n_lepton_mtt400to600_cosTSA_lt_0p4,
    "h_cos_theta2r_lepton_mtt400to600_cosTSA_lt_0p4": h_cos_theta2r_lepton_mtt400to600_cosTSA_lt_0p4,
    "h_cos_theta2k_lepton_mtt400to600_cosTSA_lt_0p4": h_cos_theta2k_lepton_mtt400to600_cosTSA_lt_0p4,
    "h_cos_theta2rStar_lepton_mtt400to600_cosTSA_lt_0p4": h_cos_theta2rStar_lepton_mtt400to600_cosTSA_lt_0p4,
    "h_cos_theta2kStar_lepton_mtt400to600_cosTSA_lt_0p4": h_cos_theta2kStar_lepton_mtt400to600_cosTSA_lt_0p4,

    "h_lb_cos_theta1n_mtt400to600_cosTSA_lt_0p4": h_lb_cos_theta1n_mtt400to600_cosTSA_lt_0p4,
    "h_lb_cos_theta1r_mtt400to600_cosTSA_lt_0p4": h_lb_cos_theta1r_mtt400to600_cosTSA_lt_0p4,
    "h_lb_cos_theta1k_mtt400to600_cosTSA_lt_0p4": h_lb_cos_theta1k_mtt400to600_cosTSA_lt_0p4,
    "h_lb_cos_theta1rStar_mtt400to600_cosTSA_lt_0p4": h_lb_cos_theta1rStar_mtt400to600_cosTSA_lt_0p4,
    "h_lb_cos_theta1kStar_mtt400to600_cosTSA_lt_0p4": h_lb_cos_theta1kStar_mtt400to600_cosTSA_lt_0p4,
    "h_lb_cos_theta2n_mtt400to600_cosTSA_lt_0p4": h_lb_cos_theta2n_mtt400to600_cosTSA_lt_0p4,
    "h_lb_cos_theta2r_mtt400to600_cosTSA_lt_0p4": h_lb_cos_theta2r_mtt400to600_cosTSA_lt_0p4,
    "h_lb_cos_theta2k_mtt400to600_cosTSA_lt_0p4": h_lb_cos_theta2k_mtt400to600_cosTSA_lt_0p4,
    "h_lb_cos_theta2rStar_mtt400to600_cosTSA_lt_0p4": h_lb_cos_theta2rStar_mtt400to600_cosTSA_lt_0p4,
    "h_lb_cos_theta2kStar_mtt400to600_cosTSA_lt_0p4": h_lb_cos_theta2kStar_mtt400to600_cosTSA_lt_0p4,
    "h_lb_Cnn_mtt400to600_cosTSA_lt_0p4": h_lb_Cnn_mtt400to600_cosTSA_lt_0p4,
    "h_lb_Cnr_mtt400to600_cosTSA_lt_0p4": h_lb_Cnr_mtt400to600_cosTSA_lt_0p4,
    "h_lb_Cnk_mtt400to600_cosTSA_lt_0p4": h_lb_Cnk_mtt400to600_cosTSA_lt_0p4,
    "h_lb_Crn_mtt400to600_cosTSA_lt_0p4": h_lb_Crn_mtt400to600_cosTSA_lt_0p4,
    "h_lb_Crr_mtt400to600_cosTSA_lt_0p4": h_lb_Crr_mtt400to600_cosTSA_lt_0p4,
    "h_lb_Crk_mtt400to600_cosTSA_lt_0p4": h_lb_Crk_mtt400to600_cosTSA_lt_0p4,
    "h_lb_Ckn_mtt400to600_cosTSA_lt_0p4": h_lb_Ckn_mtt400to600_cosTSA_lt_0p4,
    "h_lb_Ckr_mtt400to600_cosTSA_lt_0p4": h_lb_Ckr_mtt400to600_cosTSA_lt_0p4,
    "h_lb_Ckk_mtt400to600_cosTSA_lt_0p4": h_lb_Ckk_mtt400to600_cosTSA_lt_0p4,
    "h_lb_trC_mtt400to600_cosTSA_lt_0p4": h_lb_trC_mtt400to600_cosTSA_lt_0p4,
    "h_lb_cHel_mtt400to600_cosTSA_lt_0p4": h_lb_cHel_mtt400to600_cosTSA_lt_0p4,
    "h_lb_cHel_P3n_mtt400to600_cosTSA_lt_0p4": h_lb_cHel_P3n_mtt400to600_cosTSA_lt_0p4,

    "h_ld_cos_theta1n_mtt400to600_cosTSA_lt_0p4": h_ld_cos_theta1n_mtt400to600_cosTSA_lt_0p4,
    "h_ld_cos_theta1r_mtt400to600_cosTSA_lt_0p4": h_ld_cos_theta1r_mtt400to600_cosTSA_lt_0p4,
    "h_ld_cos_theta1k_mtt400to600_cosTSA_lt_0p4": h_ld_cos_theta1k_mtt400to600_cosTSA_lt_0p4,
    "h_ld_cos_theta1rStar_mtt400to600_cosTSA_lt_0p4": h_ld_cos_theta1rStar_mtt400to600_cosTSA_lt_0p4,
    "h_ld_cos_theta1kStar_mtt400to600_cosTSA_lt_0p4": h_ld_cos_theta1kStar_mtt400to600_cosTSA_lt_0p4,
    "h_ld_cos_theta2n_mtt400to600_cosTSA_lt_0p4": h_ld_cos_theta2n_mtt400to600_cosTSA_lt_0p4,
    "h_ld_cos_theta2r_mtt400to600_cosTSA_lt_0p4": h_ld_cos_theta2r_mtt400to600_cosTSA_lt_0p4,
    "h_ld_cos_theta2k_mtt400to600_cosTSA_lt_0p4": h_ld_cos_theta2k_mtt400to600_cosTSA_lt_0p4,
    "h_ld_cos_theta2rStar_mtt400to600_cosTSA_lt_0p4": h_ld_cos_theta2rStar_mtt400to600_cosTSA_lt_0p4,
    "h_ld_cos_theta2kStar_mtt400to600_cosTSA_lt_0p4": h_ld_cos_theta2kStar_mtt400to600_cosTSA_lt_0p4,
    "h_ld_Cnn_mtt400to600_cosTSA_lt_0p4": h_ld_Cnn_mtt400to600_cosTSA_lt_0p4,
    "h_ld_Cnr_mtt400to600_cosTSA_lt_0p4": h_ld_Cnr_mtt400to600_cosTSA_lt_0p4,
    "h_ld_Cnk_mtt400to600_cosTSA_lt_0p4": h_ld_Cnk_mtt400to600_cosTSA_lt_0p4,
    "h_ld_Crn_mtt400to600_cosTSA_lt_0p4": h_ld_Crn_mtt400to600_cosTSA_lt_0p4,
    "h_ld_Crr_mtt400to600_cosTSA_lt_0p4": h_ld_Crr_mtt400to600_cosTSA_lt_0p4,
    "h_ld_Crk_mtt400to600_cosTSA_lt_0p4": h_ld_Crk_mtt400to600_cosTSA_lt_0p4,
    "h_ld_Ckn_mtt400to600_cosTSA_lt_0p4": h_ld_Ckn_mtt400to600_cosTSA_lt_0p4,
    "h_ld_Ckr_mtt400to600_cosTSA_lt_0p4": h_ld_Ckr_mtt400to600_cosTSA_lt_0p4,
    "h_ld_Ckk_mtt400to600_cosTSA_lt_0p4": h_ld_Ckk_mtt400to600_cosTSA_lt_0p4,
    "h_ld_trC_mtt400to600_cosTSA_lt_0p4": h_ld_trC_mtt400to600_cosTSA_lt_0p4,
    "h_ld_cHel_mtt400to600_cosTSA_lt_0p4": h_ld_cHel_mtt400to600_cosTSA_lt_0p4,
    "h_ld_cHel_P3n_mtt400to600_cosTSA_lt_0p4": h_ld_cHel_P3n_mtt400to600_cosTSA_lt_0p4,

    "h_lb_sigmaPhi_mtt400to600_cosTSA_lt_0p4": h_lb_sigmaPhi_mtt400to600_cosTSA_lt_0p4,
    "h_lb_deltaPhi_mtt400to600_cosTSA_lt_0p4": h_lb_deltaPhi_mtt400to600_cosTSA_lt_0p4,
    "h_ld_sigmaPhi_mtt400to600_cosTSA_lt_0p4": h_ld_sigmaPhi_mtt400to600_cosTSA_lt_0p4,
    "h_ld_deltaPhi_mtt400to600_cosTSA_lt_0p4": h_ld_deltaPhi_mtt400to600_cosTSA_lt_0p4,

        ## |cosTSA| < 0.7
    "h_cos_theta1n_antilepton_mtt400to600_cosTSA_lt_0p7": h_cos_theta1n_antilepton_mtt400to600_cosTSA_lt_0p7,
    "h_cos_theta1r_antilepton_mtt400to600_cosTSA_lt_0p7": h_cos_theta1r_antilepton_mtt400to600_cosTSA_lt_0p7,
    "h_cos_theta1k_antilepton_mtt400to600_cosTSA_lt_0p7": h_cos_theta1k_antilepton_mtt400to600_cosTSA_lt_0p7,
    "h_cos_theta1rStar_antilepton_mtt400to600_cosTSA_lt_0p7": h_cos_theta1rStar_antilepton_mtt400to600_cosTSA_lt_0p7,
    "h_cos_theta1kStar_antilepton_mtt400to600_cosTSA_lt_0p7": h_cos_theta1kStar_antilepton_mtt400to600_cosTSA_lt_0p7,
    "h_cos_theta2n_lepton_mtt400to600_cosTSA_lt_0p7": h_cos_theta2n_lepton_mtt400to600_cosTSA_lt_0p7,
    "h_cos_theta2r_lepton_mtt400to600_cosTSA_lt_0p7": h_cos_theta2r_lepton_mtt400to600_cosTSA_lt_0p7,
    "h_cos_theta2k_lepton_mtt400to600_cosTSA_lt_0p7": h_cos_theta2k_lepton_mtt400to600_cosTSA_lt_0p7,
    "h_cos_theta2rStar_lepton_mtt400to600_cosTSA_lt_0p7": h_cos_theta2rStar_lepton_mtt400to600_cosTSA_lt_0p7,
    "h_cos_theta2kStar_lepton_mtt400to600_cosTSA_lt_0p7": h_cos_theta2kStar_lepton_mtt400to600_cosTSA_lt_0p7,

    "h_lb_cos_theta1n_mtt400to600_cosTSA_lt_0p7": h_lb_cos_theta1n_mtt400to600_cosTSA_lt_0p7,
    "h_lb_cos_theta1r_mtt400to600_cosTSA_lt_0p7": h_lb_cos_theta1r_mtt400to600_cosTSA_lt_0p7,
    "h_lb_cos_theta1k_mtt400to600_cosTSA_lt_0p7": h_lb_cos_theta1k_mtt400to600_cosTSA_lt_0p7,
    "h_lb_cos_theta1rStar_mtt400to600_cosTSA_lt_0p7": h_lb_cos_theta1rStar_mtt400to600_cosTSA_lt_0p7,
    "h_lb_cos_theta1kStar_mtt400to600_cosTSA_lt_0p7": h_lb_cos_theta1kStar_mtt400to600_cosTSA_lt_0p7,
    "h_lb_cos_theta2n_mtt400to600_cosTSA_lt_0p7": h_lb_cos_theta2n_mtt400to600_cosTSA_lt_0p7,
    "h_lb_cos_theta2r_mtt400to600_cosTSA_lt_0p7": h_lb_cos_theta2r_mtt400to600_cosTSA_lt_0p7,
    "h_lb_cos_theta2k_mtt400to600_cosTSA_lt_0p7": h_lb_cos_theta2k_mtt400to600_cosTSA_lt_0p7,
    "h_lb_cos_theta2rStar_mtt400to600_cosTSA_lt_0p7": h_lb_cos_theta2rStar_mtt400to600_cosTSA_lt_0p7,
    "h_lb_cos_theta2kStar_mtt400to600_cosTSA_lt_0p7": h_lb_cos_theta2kStar_mtt400to600_cosTSA_lt_0p7,
    "h_lb_Cnn_mtt400to600_cosTSA_lt_0p7": h_lb_Cnn_mtt400to600_cosTSA_lt_0p7,
    "h_lb_Cnr_mtt400to600_cosTSA_lt_0p7": h_lb_Cnr_mtt400to600_cosTSA_lt_0p7,
    "h_lb_Cnk_mtt400to600_cosTSA_lt_0p7": h_lb_Cnk_mtt400to600_cosTSA_lt_0p7,
    "h_lb_Crn_mtt400to600_cosTSA_lt_0p7": h_lb_Crn_mtt400to600_cosTSA_lt_0p7,
    "h_lb_Crr_mtt400to600_cosTSA_lt_0p7": h_lb_Crr_mtt400to600_cosTSA_lt_0p7,
    "h_lb_Crk_mtt400to600_cosTSA_lt_0p7": h_lb_Crk_mtt400to600_cosTSA_lt_0p7,
    "h_lb_Ckn_mtt400to600_cosTSA_lt_0p7": h_lb_Ckn_mtt400to600_cosTSA_lt_0p7,
    "h_lb_Ckr_mtt400to600_cosTSA_lt_0p7": h_lb_Ckr_mtt400to600_cosTSA_lt_0p7,
    "h_lb_Ckk_mtt400to600_cosTSA_lt_0p7": h_lb_Ckk_mtt400to600_cosTSA_lt_0p7,
    "h_lb_trC_mtt400to600_cosTSA_lt_0p7": h_lb_trC_mtt400to600_cosTSA_lt_0p7,
    "h_lb_cHel_mtt400to600_cosTSA_lt_0p7": h_lb_cHel_mtt400to600_cosTSA_lt_0p7,
    "h_lb_cHel_P3n_mtt400to600_cosTSA_lt_0p7": h_lb_cHel_P3n_mtt400to600_cosTSA_lt_0p7,

    "h_ld_cos_theta1n_mtt400to600_cosTSA_lt_0p7": h_ld_cos_theta1n_mtt400to600_cosTSA_lt_0p7,
    "h_ld_cos_theta1r_mtt400to600_cosTSA_lt_0p7": h_ld_cos_theta1r_mtt400to600_cosTSA_lt_0p7,
    "h_ld_cos_theta1k_mtt400to600_cosTSA_lt_0p7": h_ld_cos_theta1k_mtt400to600_cosTSA_lt_0p7,
    "h_ld_cos_theta1rStar_mtt400to600_cosTSA_lt_0p7": h_ld_cos_theta1rStar_mtt400to600_cosTSA_lt_0p7,
    "h_ld_cos_theta1kStar_mtt400to600_cosTSA_lt_0p7": h_ld_cos_theta1kStar_mtt400to600_cosTSA_lt_0p7,
    "h_ld_cos_theta2n_mtt400to600_cosTSA_lt_0p7": h_ld_cos_theta2n_mtt400to600_cosTSA_lt_0p7,
    "h_ld_cos_theta2r_mtt400to600_cosTSA_lt_0p7": h_ld_cos_theta2r_mtt400to600_cosTSA_lt_0p7,
    "h_ld_cos_theta2k_mtt400to600_cosTSA_lt_0p7": h_ld_cos_theta2k_mtt400to600_cosTSA_lt_0p7,
    "h_ld_cos_theta2rStar_mtt400to600_cosTSA_lt_0p7": h_ld_cos_theta2rStar_mtt400to600_cosTSA_lt_0p7,
    "h_ld_cos_theta2kStar_mtt400to600_cosTSA_lt_0p7": h_ld_cos_theta2kStar_mtt400to600_cosTSA_lt_0p7,
    "h_ld_Cnn_mtt400to600_cosTSA_lt_0p7": h_ld_Cnn_mtt400to600_cosTSA_lt_0p7,
    "h_ld_Cnr_mtt400to600_cosTSA_lt_0p7": h_ld_Cnr_mtt400to600_cosTSA_lt_0p7,
    "h_ld_Cnk_mtt400to600_cosTSA_lt_0p7": h_ld_Cnk_mtt400to600_cosTSA_lt_0p7,
    "h_ld_Crn_mtt400to600_cosTSA_lt_0p7": h_ld_Crn_mtt400to600_cosTSA_lt_0p7,
    "h_ld_Crr_mtt400to600_cosTSA_lt_0p7": h_ld_Crr_mtt400to600_cosTSA_lt_0p7,
    "h_ld_Crk_mtt400to600_cosTSA_lt_0p7": h_ld_Crk_mtt400to600_cosTSA_lt_0p7,
    "h_ld_Ckn_mtt400to600_cosTSA_lt_0p7": h_ld_Ckn_mtt400to600_cosTSA_lt_0p7,
    "h_ld_Ckr_mtt400to600_cosTSA_lt_0p7": h_ld_Ckr_mtt400to600_cosTSA_lt_0p7,
    "h_ld_Ckk_mtt400to600_cosTSA_lt_0p7": h_ld_Ckk_mtt400to600_cosTSA_lt_0p7,
    "h_ld_trC_mtt400to600_cosTSA_lt_0p7": h_ld_trC_mtt400to600_cosTSA_lt_0p7,
    "h_ld_cHel_mtt400to600_cosTSA_lt_0p7": h_ld_cHel_mtt400to600_cosTSA_lt_0p7,
    "h_ld_cHel_P3n_mtt400to600_cosTSA_lt_0p7": h_ld_cHel_P3n_mtt400to600_cosTSA_lt_0p7,

    "h_lb_sigmaPhi_mtt400to600_cosTSA_lt_0p7": h_lb_sigmaPhi_mtt400to600_cosTSA_lt_0p7,
    "h_lb_deltaPhi_mtt400to600_cosTSA_lt_0p7": h_lb_deltaPhi_mtt400to600_cosTSA_lt_0p7,
    "h_ld_sigmaPhi_mtt400to600_cosTSA_lt_0p7": h_ld_sigmaPhi_mtt400to600_cosTSA_lt_0p7,
    "h_ld_deltaPhi_mtt400to600_cosTSA_lt_0p7": h_ld_deltaPhi_mtt400to600_cosTSA_lt_0p7,

        ## |cosTSA| > 0.7
    "h_cos_theta1n_antilepton_mtt400to600_cosTSA_gt_0p7": h_cos_theta1n_antilepton_mtt400to600_cosTSA_gt_0p7,
    "h_cos_theta1r_antilepton_mtt400to600_cosTSA_gt_0p7": h_cos_theta1r_antilepton_mtt400to600_cosTSA_gt_0p7,
    "h_cos_theta1k_antilepton_mtt400to600_cosTSA_gt_0p7": h_cos_theta1k_antilepton_mtt400to600_cosTSA_gt_0p7,
    "h_cos_theta1rStar_antilepton_mtt400to600_cosTSA_gt_0p7": h_cos_theta1rStar_antilepton_mtt400to600_cosTSA_gt_0p7,
    "h_cos_theta1kStar_antilepton_mtt400to600_cosTSA_gt_0p7": h_cos_theta1kStar_antilepton_mtt400to600_cosTSA_gt_0p7,
    "h_cos_theta2n_lepton_mtt400to600_cosTSA_gt_0p7": h_cos_theta2n_lepton_mtt400to600_cosTSA_gt_0p7,
    "h_cos_theta2r_lepton_mtt400to600_cosTSA_gt_0p7": h_cos_theta2r_lepton_mtt400to600_cosTSA_gt_0p7,
    "h_cos_theta2k_lepton_mtt400to600_cosTSA_gt_0p7": h_cos_theta2k_lepton_mtt400to600_cosTSA_gt_0p7,
    "h_cos_theta2rStar_lepton_mtt400to600_cosTSA_gt_0p7": h_cos_theta2rStar_lepton_mtt400to600_cosTSA_gt_0p7,
    "h_cos_theta2kStar_lepton_mtt400to600_cosTSA_gt_0p7": h_cos_theta2kStar_lepton_mtt400to600_cosTSA_gt_0p7,

    "h_lb_cos_theta1n_mtt400to600_cosTSA_gt_0p7": h_lb_cos_theta1n_mtt400to600_cosTSA_gt_0p7,
    "h_lb_cos_theta1r_mtt400to600_cosTSA_gt_0p7": h_lb_cos_theta1r_mtt400to600_cosTSA_gt_0p7,
    "h_lb_cos_theta1k_mtt400to600_cosTSA_gt_0p7": h_lb_cos_theta1k_mtt400to600_cosTSA_gt_0p7,
    "h_lb_cos_theta1rStar_mtt400to600_cosTSA_gt_0p7": h_lb_cos_theta1rStar_mtt400to600_cosTSA_gt_0p7,
    "h_lb_cos_theta1kStar_mtt400to600_cosTSA_gt_0p7": h_lb_cos_theta1kStar_mtt400to600_cosTSA_gt_0p7,
    "h_lb_cos_theta2n_mtt400to600_cosTSA_gt_0p7": h_lb_cos_theta2n_mtt400to600_cosTSA_gt_0p7,
    "h_lb_cos_theta2r_mtt400to600_cosTSA_gt_0p7": h_lb_cos_theta2r_mtt400to600_cosTSA_gt_0p7,
    "h_lb_cos_theta2k_mtt400to600_cosTSA_gt_0p7": h_lb_cos_theta2k_mtt400to600_cosTSA_gt_0p7,
    "h_lb_cos_theta2rStar_mtt400to600_cosTSA_gt_0p7": h_lb_cos_theta2rStar_mtt400to600_cosTSA_gt_0p7,
    "h_lb_cos_theta2kStar_mtt400to600_cosTSA_gt_0p7": h_lb_cos_theta2kStar_mtt400to600_cosTSA_gt_0p7,
    "h_lb_Cnn_mtt400to600_cosTSA_gt_0p7": h_lb_Cnn_mtt400to600_cosTSA_gt_0p7,
    "h_lb_Cnr_mtt400to600_cosTSA_gt_0p7": h_lb_Cnr_mtt400to600_cosTSA_gt_0p7,
    "h_lb_Cnk_mtt400to600_cosTSA_gt_0p7": h_lb_Cnk_mtt400to600_cosTSA_gt_0p7,
    "h_lb_Crn_mtt400to600_cosTSA_gt_0p7": h_lb_Crn_mtt400to600_cosTSA_gt_0p7,
    "h_lb_Crr_mtt400to600_cosTSA_gt_0p7": h_lb_Crr_mtt400to600_cosTSA_gt_0p7,
    "h_lb_Crk_mtt400to600_cosTSA_gt_0p7": h_lb_Crk_mtt400to600_cosTSA_gt_0p7,
    "h_lb_Ckn_mtt400to600_cosTSA_gt_0p7": h_lb_Ckn_mtt400to600_cosTSA_gt_0p7,
    "h_lb_Ckr_mtt400to600_cosTSA_gt_0p7": h_lb_Ckr_mtt400to600_cosTSA_gt_0p7,
    "h_lb_Ckk_mtt400to600_cosTSA_gt_0p7": h_lb_Ckk_mtt400to600_cosTSA_gt_0p7,
    "h_lb_trC_mtt400to600_cosTSA_gt_0p7": h_lb_trC_mtt400to600_cosTSA_gt_0p7,
    "h_lb_cHel_mtt400to600_cosTSA_gt_0p7": h_lb_cHel_mtt400to600_cosTSA_gt_0p7,
    "h_lb_cHel_P3n_mtt400to600_cosTSA_gt_0p7": h_lb_cHel_P3n_mtt400to600_cosTSA_gt_0p7,

    "h_ld_cos_theta1n_mtt400to600_cosTSA_gt_0p7": h_ld_cos_theta1n_mtt400to600_cosTSA_gt_0p7,
    "h_ld_cos_theta1r_mtt400to600_cosTSA_gt_0p7": h_ld_cos_theta1r_mtt400to600_cosTSA_gt_0p7,
    "h_ld_cos_theta1k_mtt400to600_cosTSA_gt_0p7": h_ld_cos_theta1k_mtt400to600_cosTSA_gt_0p7,
    "h_ld_cos_theta1rStar_mtt400to600_cosTSA_gt_0p7": h_ld_cos_theta1rStar_mtt400to600_cosTSA_gt_0p7,
    "h_ld_cos_theta1kStar_mtt400to600_cosTSA_gt_0p7": h_ld_cos_theta1kStar_mtt400to600_cosTSA_gt_0p7,
    "h_ld_cos_theta2n_mtt400to600_cosTSA_gt_0p7": h_ld_cos_theta2n_mtt400to600_cosTSA_gt_0p7,
    "h_ld_cos_theta2r_mtt400to600_cosTSA_gt_0p7": h_ld_cos_theta2r_mtt400to600_cosTSA_gt_0p7,
    "h_ld_cos_theta2k_mtt400to600_cosTSA_gt_0p7": h_ld_cos_theta2k_mtt400to600_cosTSA_gt_0p7,
    "h_ld_cos_theta2rStar_mtt400to600_cosTSA_gt_0p7": h_ld_cos_theta2rStar_mtt400to600_cosTSA_gt_0p7,
    "h_ld_cos_theta2kStar_mtt400to600_cosTSA_gt_0p7": h_ld_cos_theta2kStar_mtt400to600_cosTSA_gt_0p7,
    "h_ld_Cnn_mtt400to600_cosTSA_gt_0p7": h_ld_Cnn_mtt400to600_cosTSA_gt_0p7,
    "h_ld_Cnr_mtt400to600_cosTSA_gt_0p7": h_ld_Cnr_mtt400to600_cosTSA_gt_0p7,
    "h_ld_Cnk_mtt400to600_cosTSA_gt_0p7": h_ld_Cnk_mtt400to600_cosTSA_gt_0p7,
    "h_ld_Crn_mtt400to600_cosTSA_gt_0p7": h_ld_Crn_mtt400to600_cosTSA_gt_0p7,
    "h_ld_Crr_mtt400to600_cosTSA_gt_0p7": h_ld_Crr_mtt400to600_cosTSA_gt_0p7,
    "h_ld_Crk_mtt400to600_cosTSA_gt_0p7": h_ld_Crk_mtt400to600_cosTSA_gt_0p7,
    "h_ld_Ckn_mtt400to600_cosTSA_gt_0p7": h_ld_Ckn_mtt400to600_cosTSA_gt_0p7,
    "h_ld_Ckr_mtt400to600_cosTSA_gt_0p7": h_ld_Ckr_mtt400to600_cosTSA_gt_0p7,
    "h_ld_Ckk_mtt400to600_cosTSA_gt_0p7": h_ld_Ckk_mtt400to600_cosTSA_gt_0p7,
    "h_ld_trC_mtt400to600_cosTSA_gt_0p7": h_ld_trC_mtt400to600_cosTSA_gt_0p7,
    "h_ld_cHel_mtt400to600_cosTSA_gt_0p7": h_ld_cHel_mtt400to600_cosTSA_gt_0p7,
    "h_ld_cHel_P3n_mtt400to600_cosTSA_gt_0p7": h_ld_cHel_P3n_mtt400to600_cosTSA_gt_0p7,

    "h_lb_sigmaPhi_mtt400to600_cosTSA_gt_0p7": h_lb_sigmaPhi_mtt400to600_cosTSA_gt_0p7,
    "h_lb_deltaPhi_mtt400to600_cosTSA_gt_0p7": h_lb_deltaPhi_mtt400to600_cosTSA_gt_0p7,
    "h_ld_sigmaPhi_mtt400to600_cosTSA_gt_0p7": h_ld_sigmaPhi_mtt400to600_cosTSA_gt_0p7,
    "h_ld_deltaPhi_mtt400to600_cosTSA_gt_0p7": h_ld_deltaPhi_mtt400to600_cosTSA_gt_0p7,

    ### mtt [600, 800] GeV
    "h_cos_theta1n_antilepton_mtt600to800": h_cos_theta1n_antilepton_mtt600to800,
    "h_cos_theta1r_antilepton_mtt600to800": h_cos_theta1r_antilepton_mtt600to800,
    "h_cos_theta1k_antilepton_mtt600to800": h_cos_theta1k_antilepton_mtt600to800,
    "h_cos_theta1rStar_antilepton_mtt600to800": h_cos_theta1rStar_antilepton_mtt600to800,
    "h_cos_theta1kStar_antilepton_mtt600to800": h_cos_theta1kStar_antilepton_mtt600to800,
    "h_cos_theta2n_lepton_mtt600to800": h_cos_theta2n_lepton_mtt600to800,
    "h_cos_theta2r_lepton_mtt600to800": h_cos_theta2r_lepton_mtt600to800,
    "h_cos_theta2k_lepton_mtt600to800": h_cos_theta2k_lepton_mtt600to800,
    "h_cos_theta2rStar_lepton_mtt600to800": h_cos_theta2rStar_lepton_mtt600to800,
    "h_cos_theta2kStar_lepton_mtt600to800": h_cos_theta2kStar_lepton_mtt600to800,

    "h_lb_cos_theta1n_mtt600to800": h_lb_cos_theta1n_mtt600to800,
    "h_lb_cos_theta1r_mtt600to800": h_lb_cos_theta1r_mtt600to800,
    "h_lb_cos_theta1k_mtt600to800": h_lb_cos_theta1k_mtt600to800,
    "h_lb_cos_theta1rStar_mtt600to800": h_lb_cos_theta1rStar_mtt600to800,
    "h_lb_cos_theta1kStar_mtt600to800": h_lb_cos_theta1kStar_mtt600to800,
    "h_lb_cos_theta2n_mtt600to800": h_lb_cos_theta2n_mtt600to800,
    "h_lb_cos_theta2r_mtt600to800": h_lb_cos_theta2r_mtt600to800,
    "h_lb_cos_theta2k_mtt600to800": h_lb_cos_theta2k_mtt600to800,
    "h_lb_cos_theta2rStar_mtt600to800": h_lb_cos_theta2rStar_mtt600to800,
    "h_lb_cos_theta2kStar_mtt600to800": h_lb_cos_theta2kStar_mtt600to800,
    "h_lb_Cnn_mtt600to800": h_lb_Cnn_mtt600to800,
    "h_lb_Cnr_mtt600to800": h_lb_Cnr_mtt600to800,
    "h_lb_Cnk_mtt600to800": h_lb_Cnk_mtt600to800,
    "h_lb_Crn_mtt600to800": h_lb_Crn_mtt600to800,
    "h_lb_Crr_mtt600to800": h_lb_Crr_mtt600to800,
    "h_lb_Crk_mtt600to800": h_lb_Crk_mtt600to800,
    "h_lb_Ckn_mtt600to800": h_lb_Ckn_mtt600to800,
    "h_lb_Ckr_mtt600to800": h_lb_Ckr_mtt600to800,
    "h_lb_Ckk_mtt600to800": h_lb_Ckk_mtt600to800,
    "h_lb_trC_mtt600to800": h_lb_trC_mtt600to800,
    "h_lb_cHel_mtt600to800": h_lb_cHel_mtt600to800,
    "h_lb_cHel_P3n_mtt600to800": h_lb_cHel_P3n_mtt600to800,

    "h_ld_cos_theta1n_mtt600to800": h_ld_cos_theta1n_mtt600to800,
    "h_ld_cos_theta1r_mtt600to800": h_ld_cos_theta1r_mtt600to800,
    "h_ld_cos_theta1k_mtt600to800": h_ld_cos_theta1k_mtt600to800,
    "h_ld_cos_theta1rStar_mtt600to800": h_ld_cos_theta1rStar_mtt600to800,
    "h_ld_cos_theta1kStar_mtt600to800": h_ld_cos_theta1kStar_mtt600to800,
    "h_ld_cos_theta2n_mtt600to800": h_ld_cos_theta2n_mtt600to800,
    "h_ld_cos_theta2r_mtt600to800": h_ld_cos_theta2r_mtt600to800,
    "h_ld_cos_theta2k_mtt600to800": h_ld_cos_theta2k_mtt600to800,
    "h_ld_cos_theta2rStar_mtt600to800": h_ld_cos_theta2rStar_mtt600to800,
    "h_ld_cos_theta2kStar_mtt600to800": h_ld_cos_theta2kStar_mtt600to800,
    "h_ld_Cnn_mtt600to800": h_ld_Cnn_mtt600to800,
    "h_ld_Cnr_mtt600to800": h_ld_Cnr_mtt600to800,
    "h_ld_Cnk_mtt600to800": h_ld_Cnk_mtt600to800,
    "h_ld_Crn_mtt600to800": h_ld_Crn_mtt600to800,
    "h_ld_Crr_mtt600to800": h_ld_Crr_mtt600to800,
    "h_ld_Crk_mtt600to800": h_ld_Crk_mtt600to800,
    "h_ld_Ckn_mtt600to800": h_ld_Ckn_mtt600to800,
    "h_ld_Ckr_mtt600to800": h_ld_Ckr_mtt600to800,
    "h_ld_Ckk_mtt600to800": h_ld_Ckk_mtt600to800,
    "h_ld_trC_mtt600to800": h_ld_trC_mtt600to800,
    "h_ld_cHel_mtt600to800": h_ld_cHel_mtt600to800,
    "h_ld_cHel_P3n_mtt600to800": h_ld_cHel_P3n_mtt600to800,

    "h_lb_sigmaPhi_mtt600to800": h_lb_sigmaPhi_mtt600to800,
    "h_lb_deltaPhi_mtt600to800": h_lb_deltaPhi_mtt600to800,
    "h_ld_sigmaPhi_mtt600to800": h_ld_sigmaPhi_mtt600to800,
    "h_ld_deltaPhi_mtt600to800": h_ld_deltaPhi_mtt600to800,

        ## |cosTSA| < 0.4
    "h_cos_theta1n_antilepton_mtt600to800_cosTSA_lt_0p4": h_cos_theta1n_antilepton_mtt600to800_cosTSA_lt_0p4,
    "h_cos_theta1r_antilepton_mtt600to800_cosTSA_lt_0p4": h_cos_theta1r_antilepton_mtt600to800_cosTSA_lt_0p4,
    "h_cos_theta1k_antilepton_mtt600to800_cosTSA_lt_0p4": h_cos_theta1k_antilepton_mtt600to800_cosTSA_lt_0p4,
    "h_cos_theta1rStar_antilepton_mtt600to800_cosTSA_lt_0p4": h_cos_theta1rStar_antilepton_mtt600to800_cosTSA_lt_0p4,
    "h_cos_theta1kStar_antilepton_mtt600to800_cosTSA_lt_0p4": h_cos_theta1kStar_antilepton_mtt600to800_cosTSA_lt_0p4,
    "h_cos_theta2n_lepton_mtt600to800_cosTSA_lt_0p4": h_cos_theta2n_lepton_mtt600to800_cosTSA_lt_0p4,
    "h_cos_theta2r_lepton_mtt600to800_cosTSA_lt_0p4": h_cos_theta2r_lepton_mtt600to800_cosTSA_lt_0p4,
    "h_cos_theta2k_lepton_mtt600to800_cosTSA_lt_0p4": h_cos_theta2k_lepton_mtt600to800_cosTSA_lt_0p4,
    "h_cos_theta2rStar_lepton_mtt600to800_cosTSA_lt_0p4": h_cos_theta2rStar_lepton_mtt600to800_cosTSA_lt_0p4,
    "h_cos_theta2kStar_lepton_mtt600to800_cosTSA_lt_0p4": h_cos_theta2kStar_lepton_mtt600to800_cosTSA_lt_0p4,

    "h_lb_cos_theta1n_mtt600to800_cosTSA_lt_0p4": h_lb_cos_theta1n_mtt600to800_cosTSA_lt_0p4,
    "h_lb_cos_theta1r_mtt600to800_cosTSA_lt_0p4": h_lb_cos_theta1r_mtt600to800_cosTSA_lt_0p4,
    "h_lb_cos_theta1k_mtt600to800_cosTSA_lt_0p4": h_lb_cos_theta1k_mtt600to800_cosTSA_lt_0p4,
    "h_lb_cos_theta1rStar_mtt600to800_cosTSA_lt_0p4": h_lb_cos_theta1rStar_mtt600to800_cosTSA_lt_0p4,
    "h_lb_cos_theta1kStar_mtt600to800_cosTSA_lt_0p4": h_lb_cos_theta1kStar_mtt600to800_cosTSA_lt_0p4,
    "h_lb_cos_theta2n_mtt600to800_cosTSA_lt_0p4": h_lb_cos_theta2n_mtt600to800_cosTSA_lt_0p4,
    "h_lb_cos_theta2r_mtt600to800_cosTSA_lt_0p4": h_lb_cos_theta2r_mtt600to800_cosTSA_lt_0p4,
    "h_lb_cos_theta2k_mtt600to800_cosTSA_lt_0p4": h_lb_cos_theta2k_mtt600to800_cosTSA_lt_0p4,
    "h_lb_cos_theta2rStar_mtt600to800_cosTSA_lt_0p4": h_lb_cos_theta2rStar_mtt600to800_cosTSA_lt_0p4,
    "h_lb_cos_theta2kStar_mtt600to800_cosTSA_lt_0p4": h_lb_cos_theta2kStar_mtt600to800_cosTSA_lt_0p4,
    "h_lb_Cnn_mtt600to800_cosTSA_lt_0p4": h_lb_Cnn_mtt600to800_cosTSA_lt_0p4,
    "h_lb_Cnr_mtt600to800_cosTSA_lt_0p4": h_lb_Cnr_mtt600to800_cosTSA_lt_0p4,
    "h_lb_Cnk_mtt600to800_cosTSA_lt_0p4": h_lb_Cnk_mtt600to800_cosTSA_lt_0p4,
    "h_lb_Crn_mtt600to800_cosTSA_lt_0p4": h_lb_Crn_mtt600to800_cosTSA_lt_0p4,
    "h_lb_Crr_mtt600to800_cosTSA_lt_0p4": h_lb_Crr_mtt600to800_cosTSA_lt_0p4,
    "h_lb_Crk_mtt600to800_cosTSA_lt_0p4": h_lb_Crk_mtt600to800_cosTSA_lt_0p4,
    "h_lb_Ckn_mtt600to800_cosTSA_lt_0p4": h_lb_Ckn_mtt600to800_cosTSA_lt_0p4,
    "h_lb_Ckr_mtt600to800_cosTSA_lt_0p4": h_lb_Ckr_mtt600to800_cosTSA_lt_0p4,
    "h_lb_Ckk_mtt600to800_cosTSA_lt_0p4": h_lb_Ckk_mtt600to800_cosTSA_lt_0p4,
    "h_lb_trC_mtt600to800_cosTSA_lt_0p4": h_lb_trC_mtt600to800_cosTSA_lt_0p4,
    "h_lb_cHel_mtt600to800_cosTSA_lt_0p4": h_lb_cHel_mtt600to800_cosTSA_lt_0p4,
    "h_lb_cHel_P3n_mtt600to800_cosTSA_lt_0p4": h_lb_cHel_P3n_mtt600to800_cosTSA_lt_0p4,

    "h_ld_cos_theta1n_mtt600to800_cosTSA_lt_0p4": h_ld_cos_theta1n_mtt600to800_cosTSA_lt_0p4,
    "h_ld_cos_theta1r_mtt600to800_cosTSA_lt_0p4": h_ld_cos_theta1r_mtt600to800_cosTSA_lt_0p4,
    "h_ld_cos_theta1k_mtt600to800_cosTSA_lt_0p4": h_ld_cos_theta1k_mtt600to800_cosTSA_lt_0p4,
    "h_ld_cos_theta1rStar_mtt600to800_cosTSA_lt_0p4": h_ld_cos_theta1rStar_mtt600to800_cosTSA_lt_0p4,
    "h_ld_cos_theta1kStar_mtt600to800_cosTSA_lt_0p4": h_ld_cos_theta1kStar_mtt600to800_cosTSA_lt_0p4,
    "h_ld_cos_theta2n_mtt600to800_cosTSA_lt_0p4": h_ld_cos_theta2n_mtt600to800_cosTSA_lt_0p4,
    "h_ld_cos_theta2r_mtt600to800_cosTSA_lt_0p4": h_ld_cos_theta2r_mtt600to800_cosTSA_lt_0p4,
    "h_ld_cos_theta2k_mtt600to800_cosTSA_lt_0p4": h_ld_cos_theta2k_mtt600to800_cosTSA_lt_0p4,
    "h_ld_cos_theta2rStar_mtt600to800_cosTSA_lt_0p4": h_ld_cos_theta2rStar_mtt600to800_cosTSA_lt_0p4,
    "h_ld_cos_theta2kStar_mtt600to800_cosTSA_lt_0p4": h_ld_cos_theta2kStar_mtt600to800_cosTSA_lt_0p4,
    "h_ld_Cnn_mtt600to800_cosTSA_lt_0p4": h_ld_Cnn_mtt600to800_cosTSA_lt_0p4,
    "h_ld_Cnr_mtt600to800_cosTSA_lt_0p4": h_ld_Cnr_mtt600to800_cosTSA_lt_0p4,
    "h_ld_Cnk_mtt600to800_cosTSA_lt_0p4": h_ld_Cnk_mtt600to800_cosTSA_lt_0p4,
    "h_ld_Crn_mtt600to800_cosTSA_lt_0p4": h_ld_Crn_mtt600to800_cosTSA_lt_0p4,
    "h_ld_Crr_mtt600to800_cosTSA_lt_0p4": h_ld_Crr_mtt600to800_cosTSA_lt_0p4,
    "h_ld_Crk_mtt600to800_cosTSA_lt_0p4": h_ld_Crk_mtt600to800_cosTSA_lt_0p4,
    "h_ld_Ckn_mtt600to800_cosTSA_lt_0p4": h_ld_Ckn_mtt600to800_cosTSA_lt_0p4,
    "h_ld_Ckr_mtt600to800_cosTSA_lt_0p4": h_ld_Ckr_mtt600to800_cosTSA_lt_0p4,
    "h_ld_Ckk_mtt600to800_cosTSA_lt_0p4": h_ld_Ckk_mtt600to800_cosTSA_lt_0p4,
    "h_ld_trC_mtt600to800_cosTSA_lt_0p4": h_ld_trC_mtt600to800_cosTSA_lt_0p4,
    "h_ld_cHel_mtt600to800_cosTSA_lt_0p4": h_ld_cHel_mtt600to800_cosTSA_lt_0p4,
    "h_ld_cHel_P3n_mtt600to800_cosTSA_lt_0p4": h_ld_cHel_P3n_mtt600to800_cosTSA_lt_0p4,

    "h_lb_sigmaPhi_mtt600to800_cosTSA_lt_0p4": h_lb_sigmaPhi_mtt600to800_cosTSA_lt_0p4,
    "h_lb_deltaPhi_mtt600to800_cosTSA_lt_0p4": h_lb_deltaPhi_mtt600to800_cosTSA_lt_0p4,
    "h_ld_sigmaPhi_mtt600to800_cosTSA_lt_0p4": h_ld_sigmaPhi_mtt600to800_cosTSA_lt_0p4,
    "h_ld_deltaPhi_mtt600to800_cosTSA_lt_0p4": h_ld_deltaPhi_mtt600to800_cosTSA_lt_0p4,

        ## |cosTSA| < 0.7
    "h_cos_theta1n_antilepton_mtt600to800_cosTSA_lt_0p7": h_cos_theta1n_antilepton_mtt600to800_cosTSA_lt_0p7,
    "h_cos_theta1r_antilepton_mtt600to800_cosTSA_lt_0p7": h_cos_theta1r_antilepton_mtt600to800_cosTSA_lt_0p7,
    "h_cos_theta1k_antilepton_mtt600to800_cosTSA_lt_0p7": h_cos_theta1k_antilepton_mtt600to800_cosTSA_lt_0p7,
    "h_cos_theta1rStar_antilepton_mtt600to800_cosTSA_lt_0p7": h_cos_theta1rStar_antilepton_mtt600to800_cosTSA_lt_0p7,
    "h_cos_theta1kStar_antilepton_mtt600to800_cosTSA_lt_0p7": h_cos_theta1kStar_antilepton_mtt600to800_cosTSA_lt_0p7,
    "h_cos_theta2n_lepton_mtt600to800_cosTSA_lt_0p7": h_cos_theta2n_lepton_mtt600to800_cosTSA_lt_0p7,
    "h_cos_theta2r_lepton_mtt600to800_cosTSA_lt_0p7": h_cos_theta2r_lepton_mtt600to800_cosTSA_lt_0p7,
    "h_cos_theta2k_lepton_mtt600to800_cosTSA_lt_0p7": h_cos_theta2k_lepton_mtt600to800_cosTSA_lt_0p7,
    "h_cos_theta2rStar_lepton_mtt600to800_cosTSA_lt_0p7": h_cos_theta2rStar_lepton_mtt600to800_cosTSA_lt_0p7,
    "h_cos_theta2kStar_lepton_mtt600to800_cosTSA_lt_0p7": h_cos_theta2kStar_lepton_mtt600to800_cosTSA_lt_0p7,

    "h_lb_cos_theta1n_mtt600to800_cosTSA_lt_0p7": h_lb_cos_theta1n_mtt600to800_cosTSA_lt_0p7,
    "h_lb_cos_theta1r_mtt600to800_cosTSA_lt_0p7": h_lb_cos_theta1r_mtt600to800_cosTSA_lt_0p7,
    "h_lb_cos_theta1k_mtt600to800_cosTSA_lt_0p7": h_lb_cos_theta1k_mtt600to800_cosTSA_lt_0p7,
    "h_lb_cos_theta1rStar_mtt600to800_cosTSA_lt_0p7": h_lb_cos_theta1rStar_mtt600to800_cosTSA_lt_0p7,
    "h_lb_cos_theta1kStar_mtt600to800_cosTSA_lt_0p7": h_lb_cos_theta1kStar_mtt600to800_cosTSA_lt_0p7,
    "h_lb_cos_theta2n_mtt600to800_cosTSA_lt_0p7": h_lb_cos_theta2n_mtt600to800_cosTSA_lt_0p7,
    "h_lb_cos_theta2r_mtt600to800_cosTSA_lt_0p7": h_lb_cos_theta2r_mtt600to800_cosTSA_lt_0p7,
    "h_lb_cos_theta2k_mtt600to800_cosTSA_lt_0p7": h_lb_cos_theta2k_mtt600to800_cosTSA_lt_0p7,
    "h_lb_cos_theta2rStar_mtt600to800_cosTSA_lt_0p7": h_lb_cos_theta2rStar_mtt600to800_cosTSA_lt_0p7,
    "h_lb_cos_theta2kStar_mtt600to800_cosTSA_lt_0p7": h_lb_cos_theta2kStar_mtt600to800_cosTSA_lt_0p7,
    "h_lb_Cnn_mtt600to800_cosTSA_lt_0p7": h_lb_Cnn_mtt600to800_cosTSA_lt_0p7,
    "h_lb_Cnr_mtt600to800_cosTSA_lt_0p7": h_lb_Cnr_mtt600to800_cosTSA_lt_0p7,
    "h_lb_Cnk_mtt600to800_cosTSA_lt_0p7": h_lb_Cnk_mtt600to800_cosTSA_lt_0p7,
    "h_lb_Crn_mtt600to800_cosTSA_lt_0p7": h_lb_Crn_mtt600to800_cosTSA_lt_0p7,
    "h_lb_Crr_mtt600to800_cosTSA_lt_0p7": h_lb_Crr_mtt600to800_cosTSA_lt_0p7,
    "h_lb_Crk_mtt600to800_cosTSA_lt_0p7": h_lb_Crk_mtt600to800_cosTSA_lt_0p7,
    "h_lb_Ckn_mtt600to800_cosTSA_lt_0p7": h_lb_Ckn_mtt600to800_cosTSA_lt_0p7,
    "h_lb_Ckr_mtt600to800_cosTSA_lt_0p7": h_lb_Ckr_mtt600to800_cosTSA_lt_0p7,
    "h_lb_Ckk_mtt600to800_cosTSA_lt_0p7": h_lb_Ckk_mtt600to800_cosTSA_lt_0p7,
    "h_lb_trC_mtt600to800_cosTSA_lt_0p7": h_lb_trC_mtt600to800_cosTSA_lt_0p7,
    "h_lb_cHel_mtt600to800_cosTSA_lt_0p7": h_lb_cHel_mtt600to800_cosTSA_lt_0p7,
    "h_lb_cHel_P3n_mtt600to800_cosTSA_lt_0p7": h_lb_cHel_P3n_mtt600to800_cosTSA_lt_0p7,

    "h_ld_cos_theta1n_mtt600to800_cosTSA_lt_0p7": h_ld_cos_theta1n_mtt600to800_cosTSA_lt_0p7,
    "h_ld_cos_theta1r_mtt600to800_cosTSA_lt_0p7": h_ld_cos_theta1r_mtt600to800_cosTSA_lt_0p7,
    "h_ld_cos_theta1k_mtt600to800_cosTSA_lt_0p7": h_ld_cos_theta1k_mtt600to800_cosTSA_lt_0p7,
    "h_ld_cos_theta1rStar_mtt600to800_cosTSA_lt_0p7": h_ld_cos_theta1rStar_mtt600to800_cosTSA_lt_0p7,
    "h_ld_cos_theta1kStar_mtt600to800_cosTSA_lt_0p7": h_ld_cos_theta1kStar_mtt600to800_cosTSA_lt_0p7,
    "h_ld_cos_theta2n_mtt600to800_cosTSA_lt_0p7": h_ld_cos_theta2n_mtt600to800_cosTSA_lt_0p7,
    "h_ld_cos_theta2r_mtt600to800_cosTSA_lt_0p7": h_ld_cos_theta2r_mtt600to800_cosTSA_lt_0p7,
    "h_ld_cos_theta2k_mtt600to800_cosTSA_lt_0p7": h_ld_cos_theta2k_mtt600to800_cosTSA_lt_0p7,
    "h_ld_cos_theta2rStar_mtt600to800_cosTSA_lt_0p7": h_ld_cos_theta2rStar_mtt600to800_cosTSA_lt_0p7,
    "h_ld_cos_theta2kStar_mtt600to800_cosTSA_lt_0p7": h_ld_cos_theta2kStar_mtt600to800_cosTSA_lt_0p7,
    "h_ld_Cnn_mtt600to800_cosTSA_lt_0p7": h_ld_Cnn_mtt600to800_cosTSA_lt_0p7,
    "h_ld_Cnr_mtt600to800_cosTSA_lt_0p7": h_ld_Cnr_mtt600to800_cosTSA_lt_0p7,
    "h_ld_Cnk_mtt600to800_cosTSA_lt_0p7": h_ld_Cnk_mtt600to800_cosTSA_lt_0p7,
    "h_ld_Crn_mtt600to800_cosTSA_lt_0p7": h_ld_Crn_mtt600to800_cosTSA_lt_0p7,
    "h_ld_Crr_mtt600to800_cosTSA_lt_0p7": h_ld_Crr_mtt600to800_cosTSA_lt_0p7,
    "h_ld_Crk_mtt600to800_cosTSA_lt_0p7": h_ld_Crk_mtt600to800_cosTSA_lt_0p7,
    "h_ld_Ckn_mtt600to800_cosTSA_lt_0p7": h_ld_Ckn_mtt600to800_cosTSA_lt_0p7,
    "h_ld_Ckr_mtt600to800_cosTSA_lt_0p7": h_ld_Ckr_mtt600to800_cosTSA_lt_0p7,
    "h_ld_Ckk_mtt600to800_cosTSA_lt_0p7": h_ld_Ckk_mtt600to800_cosTSA_lt_0p7,
    "h_ld_trC_mtt600to800_cosTSA_lt_0p7": h_ld_trC_mtt600to800_cosTSA_lt_0p7,
    "h_ld_cHel_mtt600to800_cosTSA_lt_0p7": h_ld_cHel_mtt600to800_cosTSA_lt_0p7,
    "h_ld_cHel_P3n_mtt600to800_cosTSA_lt_0p7": h_ld_cHel_P3n_mtt600to800_cosTSA_lt_0p7,

    "h_lb_sigmaPhi_mtt600to800_cosTSA_lt_0p7": h_lb_sigmaPhi_mtt600to800_cosTSA_lt_0p7,
    "h_lb_deltaPhi_mtt600to800_cosTSA_lt_0p7": h_lb_deltaPhi_mtt600to800_cosTSA_lt_0p7,
    "h_ld_sigmaPhi_mtt600to800_cosTSA_lt_0p7": h_ld_sigmaPhi_mtt600to800_cosTSA_lt_0p7,
    "h_ld_deltaPhi_mtt600to800_cosTSA_lt_0p7": h_ld_deltaPhi_mtt600to800_cosTSA_lt_0p7,

        ## |cosTSA| > 0.7
    "h_cos_theta1n_antilepton_mtt600to800_cosTSA_gt_0p7": h_cos_theta1n_antilepton_mtt600to800_cosTSA_gt_0p7,
    "h_cos_theta1r_antilepton_mtt600to800_cosTSA_gt_0p7": h_cos_theta1r_antilepton_mtt600to800_cosTSA_gt_0p7,
    "h_cos_theta1k_antilepton_mtt600to800_cosTSA_gt_0p7": h_cos_theta1k_antilepton_mtt600to800_cosTSA_gt_0p7,
    "h_cos_theta1rStar_antilepton_mtt600to800_cosTSA_gt_0p7": h_cos_theta1rStar_antilepton_mtt600to800_cosTSA_gt_0p7,
    "h_cos_theta1kStar_antilepton_mtt600to800_cosTSA_gt_0p7": h_cos_theta1kStar_antilepton_mtt600to800_cosTSA_gt_0p7,
    "h_cos_theta2n_lepton_mtt600to800_cosTSA_gt_0p7": h_cos_theta2n_lepton_mtt600to800_cosTSA_gt_0p7,
    "h_cos_theta2r_lepton_mtt600to800_cosTSA_gt_0p7": h_cos_theta2r_lepton_mtt600to800_cosTSA_gt_0p7,
    "h_cos_theta2k_lepton_mtt600to800_cosTSA_gt_0p7": h_cos_theta2k_lepton_mtt600to800_cosTSA_gt_0p7,
    "h_cos_theta2rStar_lepton_mtt600to800_cosTSA_gt_0p7": h_cos_theta2rStar_lepton_mtt600to800_cosTSA_gt_0p7,
    "h_cos_theta2kStar_lepton_mtt600to800_cosTSA_gt_0p7": h_cos_theta2kStar_lepton_mtt600to800_cosTSA_gt_0p7,

    "h_lb_cos_theta1n_mtt600to800_cosTSA_gt_0p7": h_lb_cos_theta1n_mtt600to800_cosTSA_gt_0p7,
    "h_lb_cos_theta1r_mtt600to800_cosTSA_gt_0p7": h_lb_cos_theta1r_mtt600to800_cosTSA_gt_0p7,
    "h_lb_cos_theta1k_mtt600to800_cosTSA_gt_0p7": h_lb_cos_theta1k_mtt600to800_cosTSA_gt_0p7,
    "h_lb_cos_theta1rStar_mtt600to800_cosTSA_gt_0p7": h_lb_cos_theta1rStar_mtt600to800_cosTSA_gt_0p7,
    "h_lb_cos_theta1kStar_mtt600to800_cosTSA_gt_0p7": h_lb_cos_theta1kStar_mtt600to800_cosTSA_gt_0p7,
    "h_lb_cos_theta2n_mtt600to800_cosTSA_gt_0p7": h_lb_cos_theta2n_mtt600to800_cosTSA_gt_0p7,
    "h_lb_cos_theta2r_mtt600to800_cosTSA_gt_0p7": h_lb_cos_theta2r_mtt600to800_cosTSA_gt_0p7,
    "h_lb_cos_theta2k_mtt600to800_cosTSA_gt_0p7": h_lb_cos_theta2k_mtt600to800_cosTSA_gt_0p7,
    "h_lb_cos_theta2rStar_mtt600to800_cosTSA_gt_0p7": h_lb_cos_theta2rStar_mtt600to800_cosTSA_gt_0p7,
    "h_lb_cos_theta2kStar_mtt600to800_cosTSA_gt_0p7": h_lb_cos_theta2kStar_mtt600to800_cosTSA_gt_0p7,
    "h_lb_Cnn_mtt600to800_cosTSA_gt_0p7": h_lb_Cnn_mtt600to800_cosTSA_gt_0p7,
    "h_lb_Cnr_mtt600to800_cosTSA_gt_0p7": h_lb_Cnr_mtt600to800_cosTSA_gt_0p7,
    "h_lb_Cnk_mtt600to800_cosTSA_gt_0p7": h_lb_Cnk_mtt600to800_cosTSA_gt_0p7,
    "h_lb_Crn_mtt600to800_cosTSA_gt_0p7": h_lb_Crn_mtt600to800_cosTSA_gt_0p7,
    "h_lb_Crr_mtt600to800_cosTSA_gt_0p7": h_lb_Crr_mtt600to800_cosTSA_gt_0p7,
    "h_lb_Crk_mtt600to800_cosTSA_gt_0p7": h_lb_Crk_mtt600to800_cosTSA_gt_0p7,
    "h_lb_Ckn_mtt600to800_cosTSA_gt_0p7": h_lb_Ckn_mtt600to800_cosTSA_gt_0p7,
    "h_lb_Ckr_mtt600to800_cosTSA_gt_0p7": h_lb_Ckr_mtt600to800_cosTSA_gt_0p7,
    "h_lb_Ckk_mtt600to800_cosTSA_gt_0p7": h_lb_Ckk_mtt600to800_cosTSA_gt_0p7,
    "h_lb_trC_mtt600to800_cosTSA_gt_0p7": h_lb_trC_mtt600to800_cosTSA_gt_0p7,
    "h_lb_cHel_mtt600to800_cosTSA_gt_0p7": h_lb_cHel_mtt600to800_cosTSA_gt_0p7,
    "h_lb_cHel_P3n_mtt600to800_cosTSA_gt_0p7": h_lb_cHel_P3n_mtt600to800_cosTSA_gt_0p7,

    "h_ld_cos_theta1n_mtt600to800_cosTSA_gt_0p7": h_ld_cos_theta1n_mtt600to800_cosTSA_gt_0p7,
    "h_ld_cos_theta1r_mtt600to800_cosTSA_gt_0p7": h_ld_cos_theta1r_mtt600to800_cosTSA_gt_0p7,
    "h_ld_cos_theta1k_mtt600to800_cosTSA_gt_0p7": h_ld_cos_theta1k_mtt600to800_cosTSA_gt_0p7,
    "h_ld_cos_theta1rStar_mtt600to800_cosTSA_gt_0p7": h_ld_cos_theta1rStar_mtt600to800_cosTSA_gt_0p7,
    "h_ld_cos_theta1kStar_mtt600to800_cosTSA_gt_0p7": h_ld_cos_theta1kStar_mtt600to800_cosTSA_gt_0p7,
    "h_ld_cos_theta2n_mtt600to800_cosTSA_gt_0p7": h_ld_cos_theta2n_mtt600to800_cosTSA_gt_0p7,
    "h_ld_cos_theta2r_mtt600to800_cosTSA_gt_0p7": h_ld_cos_theta2r_mtt600to800_cosTSA_gt_0p7,
    "h_ld_cos_theta2k_mtt600to800_cosTSA_gt_0p7": h_ld_cos_theta2k_mtt600to800_cosTSA_gt_0p7,
    "h_ld_cos_theta2rStar_mtt600to800_cosTSA_gt_0p7": h_ld_cos_theta2rStar_mtt600to800_cosTSA_gt_0p7,
    "h_ld_cos_theta2kStar_mtt600to800_cosTSA_gt_0p7": h_ld_cos_theta2kStar_mtt600to800_cosTSA_gt_0p7,
    "h_ld_Cnn_mtt600to800_cosTSA_gt_0p7": h_ld_Cnn_mtt600to800_cosTSA_gt_0p7,
    "h_ld_Cnr_mtt600to800_cosTSA_gt_0p7": h_ld_Cnr_mtt600to800_cosTSA_gt_0p7,
    "h_ld_Cnk_mtt600to800_cosTSA_gt_0p7": h_ld_Cnk_mtt600to800_cosTSA_gt_0p7,
    "h_ld_Crn_mtt600to800_cosTSA_gt_0p7": h_ld_Crn_mtt600to800_cosTSA_gt_0p7,
    "h_ld_Crr_mtt600to800_cosTSA_gt_0p7": h_ld_Crr_mtt600to800_cosTSA_gt_0p7,
    "h_ld_Crk_mtt600to800_cosTSA_gt_0p7": h_ld_Crk_mtt600to800_cosTSA_gt_0p7,
    "h_ld_Ckn_mtt600to800_cosTSA_gt_0p7": h_ld_Ckn_mtt600to800_cosTSA_gt_0p7,
    "h_ld_Ckr_mtt600to800_cosTSA_gt_0p7": h_ld_Ckr_mtt600to800_cosTSA_gt_0p7,
    "h_ld_Ckk_mtt600to800_cosTSA_gt_0p7": h_ld_Ckk_mtt600to800_cosTSA_gt_0p7,
    "h_ld_trC_mtt600to800_cosTSA_gt_0p7": h_ld_trC_mtt600to800_cosTSA_gt_0p7,
    "h_ld_cHel_mtt600to800_cosTSA_gt_0p7": h_ld_cHel_mtt600to800_cosTSA_gt_0p7,
    "h_ld_cHel_P3n_mtt600to800_cosTSA_gt_0p7": h_ld_cHel_P3n_mtt600to800_cosTSA_gt_0p7,

    "h_lb_sigmaPhi_mtt600to800_cosTSA_gt_0p7": h_lb_sigmaPhi_mtt600to800_cosTSA_gt_0p7,
    "h_lb_deltaPhi_mtt600to800_cosTSA_gt_0p7": h_lb_deltaPhi_mtt600to800_cosTSA_gt_0p7,
    "h_ld_sigmaPhi_mtt600to800_cosTSA_gt_0p7": h_ld_sigmaPhi_mtt600to800_cosTSA_gt_0p7,
    "h_ld_deltaPhi_mtt600to800_cosTSA_gt_0p7": h_ld_deltaPhi_mtt600to800_cosTSA_gt_0p7,

    ### mtt [800, Inf] GeV
    "h_cos_theta1n_antilepton_mtt800toInf": h_cos_theta1n_antilepton_mtt800toInf,
    "h_cos_theta1r_antilepton_mtt800toInf": h_cos_theta1r_antilepton_mtt800toInf,
    "h_cos_theta1k_antilepton_mtt800toInf": h_cos_theta1k_antilepton_mtt800toInf,
    "h_cos_theta1rStar_antilepton_mtt800toInf": h_cos_theta1rStar_antilepton_mtt800toInf,
    "h_cos_theta1kStar_antilepton_mtt800toInf": h_cos_theta1kStar_antilepton_mtt800toInf,
    "h_cos_theta2n_lepton_mtt800toInf": h_cos_theta2n_lepton_mtt800toInf,
    "h_cos_theta2r_lepton_mtt800toInf": h_cos_theta2r_lepton_mtt800toInf,
    "h_cos_theta2k_lepton_mtt800toInf": h_cos_theta2k_lepton_mtt800toInf,
    "h_cos_theta2rStar_lepton_mtt800toInf": h_cos_theta2rStar_lepton_mtt800toInf,
    "h_cos_theta2kStar_lepton_mtt800toInf": h_cos_theta2kStar_lepton_mtt800toInf,

    "h_lb_cos_theta1n_mtt800toInf": h_lb_cos_theta1n_mtt800toInf,
    "h_lb_cos_theta1r_mtt800toInf": h_lb_cos_theta1r_mtt800toInf,
    "h_lb_cos_theta1k_mtt800toInf": h_lb_cos_theta1k_mtt800toInf,
    "h_lb_cos_theta1rStar_mtt800toInf": h_lb_cos_theta1rStar_mtt800toInf,
    "h_lb_cos_theta1kStar_mtt800toInf": h_lb_cos_theta1kStar_mtt800toInf,
    "h_lb_cos_theta2n_mtt800toInf": h_lb_cos_theta2n_mtt800toInf,
    "h_lb_cos_theta2r_mtt800toInf": h_lb_cos_theta2r_mtt800toInf,
    "h_lb_cos_theta2k_mtt800toInf": h_lb_cos_theta2k_mtt800toInf,
    "h_lb_cos_theta2rStar_mtt800toInf": h_lb_cos_theta2rStar_mtt800toInf,
    "h_lb_cos_theta2kStar_mtt800toInf": h_lb_cos_theta2kStar_mtt800toInf,
    "h_lb_Cnn_mtt800toInf": h_lb_Cnn_mtt800toInf,
    "h_lb_Cnr_mtt800toInf": h_lb_Cnr_mtt800toInf,
    "h_lb_Cnk_mtt800toInf": h_lb_Cnk_mtt800toInf,
    "h_lb_Crn_mtt800toInf": h_lb_Crn_mtt800toInf,
    "h_lb_Crr_mtt800toInf": h_lb_Crr_mtt800toInf,
    "h_lb_Crk_mtt800toInf": h_lb_Crk_mtt800toInf,
    "h_lb_Ckn_mtt800toInf": h_lb_Ckn_mtt800toInf,
    "h_lb_Ckr_mtt800toInf": h_lb_Ckr_mtt800toInf,
    "h_lb_Ckk_mtt800toInf": h_lb_Ckk_mtt800toInf,
    "h_lb_trC_mtt800toInf": h_lb_trC_mtt800toInf,
    "h_lb_cHel_mtt800toInf": h_lb_cHel_mtt800toInf,
    "h_lb_cHel_P3n_mtt800toInf": h_lb_cHel_P3n_mtt800toInf,

    "h_ld_cos_theta1n_mtt800toInf": h_ld_cos_theta1n_mtt800toInf,
    "h_ld_cos_theta1r_mtt800toInf": h_ld_cos_theta1r_mtt800toInf,
    "h_ld_cos_theta1k_mtt800toInf": h_ld_cos_theta1k_mtt800toInf,
    "h_ld_cos_theta1rStar_mtt800toInf": h_ld_cos_theta1rStar_mtt800toInf,
    "h_ld_cos_theta1kStar_mtt800toInf": h_ld_cos_theta1kStar_mtt800toInf,
    "h_ld_cos_theta2n_mtt800toInf": h_ld_cos_theta2n_mtt800toInf,
    "h_ld_cos_theta2r_mtt800toInf": h_ld_cos_theta2r_mtt800toInf,
    "h_ld_cos_theta2k_mtt800toInf": h_ld_cos_theta2k_mtt800toInf,
    "h_ld_cos_theta2rStar_mtt800toInf": h_ld_cos_theta2rStar_mtt800toInf,
    "h_ld_cos_theta2kStar_mtt800toInf": h_ld_cos_theta2kStar_mtt800toInf,
    "h_ld_Cnn_mtt800toInf": h_ld_Cnn_mtt800toInf,
    "h_ld_Cnr_mtt800toInf": h_ld_Cnr_mtt800toInf,
    "h_ld_Cnk_mtt800toInf": h_ld_Cnk_mtt800toInf,
    "h_ld_Crn_mtt800toInf": h_ld_Crn_mtt800toInf,
    "h_ld_Crr_mtt800toInf": h_ld_Crr_mtt800toInf,
    "h_ld_Crk_mtt800toInf": h_ld_Crk_mtt800toInf,
    "h_ld_Ckn_mtt800toInf": h_ld_Ckn_mtt800toInf,
    "h_ld_Ckr_mtt800toInf": h_ld_Ckr_mtt800toInf,
    "h_ld_Ckk_mtt800toInf": h_ld_Ckk_mtt800toInf,
    "h_ld_trC_mtt800toInf": h_ld_trC_mtt800toInf,
    "h_ld_cHel_mtt800toInf": h_ld_cHel_mtt800toInf,
    "h_ld_cHel_P3n_mtt800toInf": h_ld_cHel_P3n_mtt800toInf,

    "h_lb_sigmaPhi_mtt800toInf": h_lb_sigmaPhi_mtt800toInf,
    "h_lb_deltaPhi_mtt800toInf": h_lb_deltaPhi_mtt800toInf,
    "h_ld_sigmaPhi_mtt800toInf": h_ld_sigmaPhi_mtt800toInf,
    "h_ld_deltaPhi_mtt800toInf": h_ld_deltaPhi_mtt800toInf,

        ## |cosTSA| < 0.4
    "h_cos_theta1n_antilepton_mtt800toInf_cosTSA_lt_0p4": h_cos_theta1n_antilepton_mtt800toInf_cosTSA_lt_0p4,
    "h_cos_theta1r_antilepton_mtt800toInf_cosTSA_lt_0p4": h_cos_theta1r_antilepton_mtt800toInf_cosTSA_lt_0p4,
    "h_cos_theta1k_antilepton_mtt800toInf_cosTSA_lt_0p4": h_cos_theta1k_antilepton_mtt800toInf_cosTSA_lt_0p4,
    "h_cos_theta1rStar_antilepton_mtt800toInf_cosTSA_lt_0p4": h_cos_theta1rStar_antilepton_mtt800toInf_cosTSA_lt_0p4,
    "h_cos_theta1kStar_antilepton_mtt800toInf_cosTSA_lt_0p4": h_cos_theta1kStar_antilepton_mtt800toInf_cosTSA_lt_0p4,
    "h_cos_theta2n_lepton_mtt800toInf_cosTSA_lt_0p4": h_cos_theta2n_lepton_mtt800toInf_cosTSA_lt_0p4,
    "h_cos_theta2r_lepton_mtt800toInf_cosTSA_lt_0p4": h_cos_theta2r_lepton_mtt800toInf_cosTSA_lt_0p4,
    "h_cos_theta2k_lepton_mtt800toInf_cosTSA_lt_0p4": h_cos_theta2k_lepton_mtt800toInf_cosTSA_lt_0p4,
    "h_cos_theta2rStar_lepton_mtt800toInf_cosTSA_lt_0p4": h_cos_theta2rStar_lepton_mtt800toInf_cosTSA_lt_0p4,
    "h_cos_theta2kStar_lepton_mtt800toInf_cosTSA_lt_0p4": h_cos_theta2kStar_lepton_mtt800toInf_cosTSA_lt_0p4,

    "h_lb_cos_theta1n_mtt800toInf_cosTSA_lt_0p4": h_lb_cos_theta1n_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_cos_theta1r_mtt800toInf_cosTSA_lt_0p4": h_lb_cos_theta1r_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_cos_theta1k_mtt800toInf_cosTSA_lt_0p4": h_lb_cos_theta1k_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p4": h_lb_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p4": h_lb_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_cos_theta2n_mtt800toInf_cosTSA_lt_0p4": h_lb_cos_theta2n_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_cos_theta2r_mtt800toInf_cosTSA_lt_0p4": h_lb_cos_theta2r_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_cos_theta2k_mtt800toInf_cosTSA_lt_0p4": h_lb_cos_theta2k_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p4": h_lb_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p4": h_lb_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_Cnn_mtt800toInf_cosTSA_lt_0p4": h_lb_Cnn_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_Cnr_mtt800toInf_cosTSA_lt_0p4": h_lb_Cnr_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_Cnk_mtt800toInf_cosTSA_lt_0p4": h_lb_Cnk_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_Crn_mtt800toInf_cosTSA_lt_0p4": h_lb_Crn_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_Crr_mtt800toInf_cosTSA_lt_0p4": h_lb_Crr_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_Crk_mtt800toInf_cosTSA_lt_0p4": h_lb_Crk_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_Ckn_mtt800toInf_cosTSA_lt_0p4": h_lb_Ckn_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_Ckr_mtt800toInf_cosTSA_lt_0p4": h_lb_Ckr_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_Ckk_mtt800toInf_cosTSA_lt_0p4": h_lb_Ckk_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_trC_mtt800toInf_cosTSA_lt_0p4": h_lb_trC_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_cHel_mtt800toInf_cosTSA_lt_0p4": h_lb_cHel_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_cHel_P3n_mtt800toInf_cosTSA_lt_0p4": h_lb_cHel_P3n_mtt800toInf_cosTSA_lt_0p4,

    "h_ld_cos_theta1n_mtt800toInf_cosTSA_lt_0p4": h_ld_cos_theta1n_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_cos_theta1r_mtt800toInf_cosTSA_lt_0p4": h_ld_cos_theta1r_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_cos_theta1k_mtt800toInf_cosTSA_lt_0p4": h_ld_cos_theta1k_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p4": h_ld_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p4": h_ld_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_cos_theta2n_mtt800toInf_cosTSA_lt_0p4": h_ld_cos_theta2n_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_cos_theta2r_mtt800toInf_cosTSA_lt_0p4": h_ld_cos_theta2r_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_cos_theta2k_mtt800toInf_cosTSA_lt_0p4": h_ld_cos_theta2k_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p4": h_ld_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p4": h_ld_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_Cnn_mtt800toInf_cosTSA_lt_0p4": h_ld_Cnn_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_Cnr_mtt800toInf_cosTSA_lt_0p4": h_ld_Cnr_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_Cnk_mtt800toInf_cosTSA_lt_0p4": h_ld_Cnk_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_Crn_mtt800toInf_cosTSA_lt_0p4": h_ld_Crn_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_Crr_mtt800toInf_cosTSA_lt_0p4": h_ld_Crr_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_Crk_mtt800toInf_cosTSA_lt_0p4": h_ld_Crk_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_Ckn_mtt800toInf_cosTSA_lt_0p4": h_ld_Ckn_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_Ckr_mtt800toInf_cosTSA_lt_0p4": h_ld_Ckr_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_Ckk_mtt800toInf_cosTSA_lt_0p4": h_ld_Ckk_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_trC_mtt800toInf_cosTSA_lt_0p4": h_ld_trC_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_cHel_mtt800toInf_cosTSA_lt_0p4": h_ld_cHel_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_cHel_P3n_mtt800toInf_cosTSA_lt_0p4": h_ld_cHel_P3n_mtt800toInf_cosTSA_lt_0p4,

    "h_lb_sigmaPhi_mtt800toInf_cosTSA_lt_0p4": h_lb_sigmaPhi_mtt800toInf_cosTSA_lt_0p4,
    "h_lb_deltaPhi_mtt800toInf_cosTSA_lt_0p4": h_lb_deltaPhi_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_sigmaPhi_mtt800toInf_cosTSA_lt_0p4": h_ld_sigmaPhi_mtt800toInf_cosTSA_lt_0p4,
    "h_ld_deltaPhi_mtt800toInf_cosTSA_lt_0p4": h_ld_deltaPhi_mtt800toInf_cosTSA_lt_0p4,

        ## |cosTSA| < 0.7
    "h_cos_theta1n_antilepton_mtt800toInf_cosTSA_lt_0p7": h_cos_theta1n_antilepton_mtt800toInf_cosTSA_lt_0p7,
    "h_cos_theta1r_antilepton_mtt800toInf_cosTSA_lt_0p7": h_cos_theta1r_antilepton_mtt800toInf_cosTSA_lt_0p7,
    "h_cos_theta1k_antilepton_mtt800toInf_cosTSA_lt_0p7": h_cos_theta1k_antilepton_mtt800toInf_cosTSA_lt_0p7,
    "h_cos_theta1rStar_antilepton_mtt800toInf_cosTSA_lt_0p7": h_cos_theta1rStar_antilepton_mtt800toInf_cosTSA_lt_0p7,
    "h_cos_theta1kStar_antilepton_mtt800toInf_cosTSA_lt_0p7": h_cos_theta1kStar_antilepton_mtt800toInf_cosTSA_lt_0p7,
    "h_cos_theta2n_lepton_mtt800toInf_cosTSA_lt_0p7": h_cos_theta2n_lepton_mtt800toInf_cosTSA_lt_0p7,
    "h_cos_theta2r_lepton_mtt800toInf_cosTSA_lt_0p7": h_cos_theta2r_lepton_mtt800toInf_cosTSA_lt_0p7,
    "h_cos_theta2k_lepton_mtt800toInf_cosTSA_lt_0p7": h_cos_theta2k_lepton_mtt800toInf_cosTSA_lt_0p7,
    "h_cos_theta2rStar_lepton_mtt800toInf_cosTSA_lt_0p7": h_cos_theta2rStar_lepton_mtt800toInf_cosTSA_lt_0p7,
    "h_cos_theta2kStar_lepton_mtt800toInf_cosTSA_lt_0p7": h_cos_theta2kStar_lepton_mtt800toInf_cosTSA_lt_0p7,

    "h_lb_cos_theta1n_mtt800toInf_cosTSA_lt_0p7": h_lb_cos_theta1n_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_cos_theta1r_mtt800toInf_cosTSA_lt_0p7": h_lb_cos_theta1r_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_cos_theta1k_mtt800toInf_cosTSA_lt_0p7": h_lb_cos_theta1k_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p7": h_lb_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p7": h_lb_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_cos_theta2n_mtt800toInf_cosTSA_lt_0p7": h_lb_cos_theta2n_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_cos_theta2r_mtt800toInf_cosTSA_lt_0p7": h_lb_cos_theta2r_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_cos_theta2k_mtt800toInf_cosTSA_lt_0p7": h_lb_cos_theta2k_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p7": h_lb_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p7": h_lb_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_Cnn_mtt800toInf_cosTSA_lt_0p7": h_lb_Cnn_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_Cnr_mtt800toInf_cosTSA_lt_0p7": h_lb_Cnr_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_Cnk_mtt800toInf_cosTSA_lt_0p7": h_lb_Cnk_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_Crn_mtt800toInf_cosTSA_lt_0p7": h_lb_Crn_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_Crr_mtt800toInf_cosTSA_lt_0p7": h_lb_Crr_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_Crk_mtt800toInf_cosTSA_lt_0p7": h_lb_Crk_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_Ckn_mtt800toInf_cosTSA_lt_0p7": h_lb_Ckn_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_Ckr_mtt800toInf_cosTSA_lt_0p7": h_lb_Ckr_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_Ckk_mtt800toInf_cosTSA_lt_0p7": h_lb_Ckk_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_trC_mtt800toInf_cosTSA_lt_0p7": h_lb_trC_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_cHel_mtt800toInf_cosTSA_lt_0p7": h_lb_cHel_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_cHel_P3n_mtt800toInf_cosTSA_lt_0p7": h_lb_cHel_P3n_mtt800toInf_cosTSA_lt_0p7,

    "h_ld_cos_theta1n_mtt800toInf_cosTSA_lt_0p7": h_ld_cos_theta1n_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_cos_theta1r_mtt800toInf_cosTSA_lt_0p7": h_ld_cos_theta1r_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_cos_theta1k_mtt800toInf_cosTSA_lt_0p7": h_ld_cos_theta1k_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p7": h_ld_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p7": h_ld_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_cos_theta2n_mtt800toInf_cosTSA_lt_0p7": h_ld_cos_theta2n_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_cos_theta2r_mtt800toInf_cosTSA_lt_0p7": h_ld_cos_theta2r_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_cos_theta2k_mtt800toInf_cosTSA_lt_0p7": h_ld_cos_theta2k_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p7": h_ld_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p7": h_ld_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_Cnn_mtt800toInf_cosTSA_lt_0p7": h_ld_Cnn_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_Cnr_mtt800toInf_cosTSA_lt_0p7": h_ld_Cnr_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_Cnk_mtt800toInf_cosTSA_lt_0p7": h_ld_Cnk_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_Crn_mtt800toInf_cosTSA_lt_0p7": h_ld_Crn_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_Crr_mtt800toInf_cosTSA_lt_0p7": h_ld_Crr_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_Crk_mtt800toInf_cosTSA_lt_0p7": h_ld_Crk_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_Ckn_mtt800toInf_cosTSA_lt_0p7": h_ld_Ckn_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_Ckr_mtt800toInf_cosTSA_lt_0p7": h_ld_Ckr_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_Ckk_mtt800toInf_cosTSA_lt_0p7": h_ld_Ckk_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_trC_mtt800toInf_cosTSA_lt_0p7": h_ld_trC_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_cHel_mtt800toInf_cosTSA_lt_0p7": h_ld_cHel_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_cHel_P3n_mtt800toInf_cosTSA_lt_0p7": h_ld_cHel_P3n_mtt800toInf_cosTSA_lt_0p7,

    "h_lb_sigmaPhi_mtt800toInf_cosTSA_lt_0p7": h_lb_sigmaPhi_mtt800toInf_cosTSA_lt_0p7,
    "h_lb_deltaPhi_mtt800toInf_cosTSA_lt_0p7": h_lb_deltaPhi_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_sigmaPhi_mtt800toInf_cosTSA_lt_0p7": h_ld_sigmaPhi_mtt800toInf_cosTSA_lt_0p7,
    "h_ld_deltaPhi_mtt800toInf_cosTSA_lt_0p7": h_ld_deltaPhi_mtt800toInf_cosTSA_lt_0p7,

        ## |cosTSA| > 0.7
    "h_cos_theta1n_antilepton_mtt800toInf_cosTSA_gt_0p7": h_cos_theta1n_antilepton_mtt800toInf_cosTSA_gt_0p7,
    "h_cos_theta1r_antilepton_mtt800toInf_cosTSA_gt_0p7": h_cos_theta1r_antilepton_mtt800toInf_cosTSA_gt_0p7,
    "h_cos_theta1k_antilepton_mtt800toInf_cosTSA_gt_0p7": h_cos_theta1k_antilepton_mtt800toInf_cosTSA_gt_0p7,
    "h_cos_theta1rStar_antilepton_mtt800toInf_cosTSA_gt_0p7": h_cos_theta1rStar_antilepton_mtt800toInf_cosTSA_gt_0p7,
    "h_cos_theta1kStar_antilepton_mtt800toInf_cosTSA_gt_0p7": h_cos_theta1kStar_antilepton_mtt800toInf_cosTSA_gt_0p7,
    "h_cos_theta2n_lepton_mtt800toInf_cosTSA_gt_0p7": h_cos_theta2n_lepton_mtt800toInf_cosTSA_gt_0p7,
    "h_cos_theta2r_lepton_mtt800toInf_cosTSA_gt_0p7": h_cos_theta2r_lepton_mtt800toInf_cosTSA_gt_0p7,
    "h_cos_theta2k_lepton_mtt800toInf_cosTSA_gt_0p7": h_cos_theta2k_lepton_mtt800toInf_cosTSA_gt_0p7,
    "h_cos_theta2rStar_lepton_mtt800toInf_cosTSA_gt_0p7": h_cos_theta2rStar_lepton_mtt800toInf_cosTSA_gt_0p7,
    "h_cos_theta2kStar_lepton_mtt800toInf_cosTSA_gt_0p7": h_cos_theta2kStar_lepton_mtt800toInf_cosTSA_gt_0p7,

    "h_lb_cos_theta1n_mtt800toInf_cosTSA_gt_0p7": h_lb_cos_theta1n_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_cos_theta1r_mtt800toInf_cosTSA_gt_0p7": h_lb_cos_theta1r_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_cos_theta1k_mtt800toInf_cosTSA_gt_0p7": h_lb_cos_theta1k_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_cos_theta1rStar_mtt800toInf_cosTSA_gt_0p7": h_lb_cos_theta1rStar_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_cos_theta1kStar_mtt800toInf_cosTSA_gt_0p7": h_lb_cos_theta1kStar_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_cos_theta2n_mtt800toInf_cosTSA_gt_0p7": h_lb_cos_theta2n_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_cos_theta2r_mtt800toInf_cosTSA_gt_0p7": h_lb_cos_theta2r_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_cos_theta2k_mtt800toInf_cosTSA_gt_0p7": h_lb_cos_theta2k_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_cos_theta2rStar_mtt800toInf_cosTSA_gt_0p7": h_lb_cos_theta2rStar_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_cos_theta2kStar_mtt800toInf_cosTSA_gt_0p7": h_lb_cos_theta2kStar_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_Cnn_mtt800toInf_cosTSA_gt_0p7": h_lb_Cnn_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_Cnr_mtt800toInf_cosTSA_gt_0p7": h_lb_Cnr_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_Cnk_mtt800toInf_cosTSA_gt_0p7": h_lb_Cnk_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_Crn_mtt800toInf_cosTSA_gt_0p7": h_lb_Crn_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_Crr_mtt800toInf_cosTSA_gt_0p7": h_lb_Crr_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_Crk_mtt800toInf_cosTSA_gt_0p7": h_lb_Crk_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_Ckn_mtt800toInf_cosTSA_gt_0p7": h_lb_Ckn_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_Ckr_mtt800toInf_cosTSA_gt_0p7": h_lb_Ckr_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_Ckk_mtt800toInf_cosTSA_gt_0p7": h_lb_Ckk_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_trC_mtt800toInf_cosTSA_gt_0p7": h_lb_trC_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_cHel_mtt800toInf_cosTSA_gt_0p7": h_lb_cHel_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_cHel_P3n_mtt800toInf_cosTSA_gt_0p7": h_lb_cHel_P3n_mtt800toInf_cosTSA_gt_0p7,

    "h_ld_cos_theta1n_mtt800toInf_cosTSA_gt_0p7": h_ld_cos_theta1n_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_cos_theta1r_mtt800toInf_cosTSA_gt_0p7": h_ld_cos_theta1r_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_cos_theta1k_mtt800toInf_cosTSA_gt_0p7": h_ld_cos_theta1k_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_cos_theta1rStar_mtt800toInf_cosTSA_gt_0p7": h_ld_cos_theta1rStar_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_cos_theta1kStar_mtt800toInf_cosTSA_gt_0p7": h_ld_cos_theta1kStar_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_cos_theta2n_mtt800toInf_cosTSA_gt_0p7": h_ld_cos_theta2n_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_cos_theta2r_mtt800toInf_cosTSA_gt_0p7": h_ld_cos_theta2r_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_cos_theta2k_mtt800toInf_cosTSA_gt_0p7": h_ld_cos_theta2k_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_cos_theta2rStar_mtt800toInf_cosTSA_gt_0p7": h_ld_cos_theta2rStar_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_cos_theta2kStar_mtt800toInf_cosTSA_gt_0p7": h_ld_cos_theta2kStar_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_Cnn_mtt800toInf_cosTSA_gt_0p7": h_ld_Cnn_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_Cnr_mtt800toInf_cosTSA_gt_0p7": h_ld_Cnr_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_Cnk_mtt800toInf_cosTSA_gt_0p7": h_ld_Cnk_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_Crn_mtt800toInf_cosTSA_gt_0p7": h_ld_Crn_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_Crr_mtt800toInf_cosTSA_gt_0p7": h_ld_Crr_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_Crk_mtt800toInf_cosTSA_gt_0p7": h_ld_Crk_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_Ckn_mtt800toInf_cosTSA_gt_0p7": h_ld_Ckn_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_Ckr_mtt800toInf_cosTSA_gt_0p7": h_ld_Ckr_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_Ckk_mtt800toInf_cosTSA_gt_0p7": h_ld_Ckk_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_trC_mtt800toInf_cosTSA_gt_0p7": h_ld_trC_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_cHel_mtt800toInf_cosTSA_gt_0p7": h_ld_cHel_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_cHel_P3n_mtt800toInf_cosTSA_gt_0p7": h_ld_cHel_P3n_mtt800toInf_cosTSA_gt_0p7,

    "h_lb_sigmaPhi_mtt800toInf_cosTSA_gt_0p7": h_lb_sigmaPhi_mtt800toInf_cosTSA_gt_0p7,
    "h_lb_deltaPhi_mtt800toInf_cosTSA_gt_0p7": h_lb_deltaPhi_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_sigmaPhi_mtt800toInf_cosTSA_gt_0p7": h_ld_sigmaPhi_mtt800toInf_cosTSA_gt_0p7,
    "h_ld_deltaPhi_mtt800toInf_cosTSA_gt_0p7": h_ld_deltaPhi_mtt800toInf_cosTSA_gt_0p7
    }