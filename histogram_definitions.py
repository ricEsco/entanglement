import ROOT

##############################################################################
### This file stores histograms to be filled in a separate analysis script ###
###                     e.g. entanglement_nanoGen.py                       ###
##############################################################################

# ROOT histogram initialization syntax:
# h_name = ROOT.TH1F("h_name", "Title;x-axis label;y-axis label", nbins, xlow, xup)
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
# lepton exclusive polarization variables
h_cos_theta1k_antilepton = ROOT.TH1F("h_cos_theta1k_antilepton", "antilepton #hat{k}-polarization;cos(#theta_{#hat{l}k});Events", 6, -1, 1)
h_cos_theta1r_antilepton = ROOT.TH1F("h_cos_theta1r_antilepton", "antilepton #hat{r}-polarization;cos(#theta_{#hat{l}r});Events", 6, -1, 1)
h_cos_theta1n_antilepton = ROOT.TH1F("h_cos_theta1n_antilepton", "antilepton #hat{n}-polarization;cos(#theta_{#hat{l}n});Events", 6, -1, 1)
h_cos_theta2k_lepton = ROOT.TH1F("h_cos_theta2k_lepton", "lepton #hat{k}-polarization;cos(#theta_{lk});Events", 6, -1, 1)
h_cos_theta2r_lepton = ROOT.TH1F("h_cos_theta2r_lepton", "lepton #hat{r}-polarization;cos(#theta_{lr});Events", 6, -1, 1)
h_cos_theta2n_lepton = ROOT.TH1F("h_cos_theta2n_lepton", "lepton #hat{n}-polarization;cos(#theta_{ln});Events", 6, -1, 1)
# CA polarizations
h_cos_theta1kStar_antilepton = ROOT.TH1F("h_cos_theta1kStar_antilepton", "antilepton #hat{k*}-polarization ;cos(#theta_{#hat{l}k*});Events", 6, -1, 1)
h_cos_theta1rStar_antilepton = ROOT.TH1F("h_cos_theta1rStar_antilepton", "antilepton #hat{r*}-polarization ;cos(#theta_{#hat{l}r*});Events", 6, -1, 1)
h_cos_theta2kStar_lepton = ROOT.TH1F("h_cos_theta2kStar_lepton", "lepton #hat{k*}-polarization ;cos(#theta_{lk*});Events", 6, -1, 1)
h_cos_theta2rStar_lepton = ROOT.TH1F("h_cos_theta2rStar_lepton", "lepton #hat{r*}-polarization ;cos(#theta_{lr*});Events", 6, -1, 1)

### Using LEPTONS and B_QUARKS as spin analyzers ###
####################################################
# Entaglement Witnesses
h_lb_cHel    = ROOT.TH1F("h_lb_cHel", "(lb) Cosine Helicity Angle;cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n = ROOT.TH1F("h_lb_cHel_P3n", "(lb) Cosine Helicity Angle w/P_3n;cos(#theta_{l(P_{3}b});Events", 6, -1, 1)
h_lb_cHel_slow    = ROOT.TH1F("h_lb_cHel_slow", "(lb) Cosine Helicity Angle (#beta<0.9);cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_slow = ROOT.TH1F("h_lb_cHel_P3n_slow", "(lb) Cosine Helicity Angle w/P_3n (#beta<0.9);cos(#theta_{l(P_{3}b});Events", 6, -1, 1)
h_lb_cHel_BoostedCentral    = ROOT.TH1F("h_lb_cHel_BoostedCentral", "(lb) Cosine Helicity Angle m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;cos(#theta_{lb});Events", 6, -1, 1)
h_lb_cHel_P3n_BoostedCentral = ROOT.TH1F("h_lb_cHel_P3n_BoostedCentral", "(lb) Cosine Helicity Angle w/P_3n m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;cos(#theta_{l(P_{3}b});Events", 6, -1, 1)
# Polarization 
h_lb_cos_theta1k = ROOT.TH1F("h_lb_cos_theta1k", "top decay (lb) #hat{k}-polarization;(lb) cos(#theta_{1k});Events", 6, -1, 1)
h_lb_cos_theta1r = ROOT.TH1F("h_lb_cos_theta1r", "top decay (lb) #hat{r}-polarization ;(lb) cos(#theta_{1r});Events", 6, -1, 1)
h_lb_cos_theta1n = ROOT.TH1F("h_lb_cos_theta1n", "top decay (lb) #hat{n}-polarization ;(lb) cos(#theta_{1n});Events", 6, -1, 1)
h_lb_cos_theta2k = ROOT.TH1F("h_lb_cos_theta2k", "antitop decay (lb) #hat{k}-polarization ;(lb) cos(#theta_{2k});Events", 6, -1, 1)
h_lb_cos_theta2r = ROOT.TH1F("h_lb_cos_theta2r", "antitop decay (lb) #hat{r}-polarization ;(lb) cos(#theta_{2r});Events", 6, -1, 1)
h_lb_cos_theta2n = ROOT.TH1F("h_lb_cos_theta2n", "antitop decay (lb) #hat{n}-polarization ;(lb) cos(#theta_{2n});Events", 6, -1, 1)
# CA polarizations
h_lb_cos_theta1kStar = ROOT.TH1F("h_lb_cos_theta1kStar", "top decay (lb) #hat{k*}-polarization;(lb) cos(#theta_{1k*});Events", 6, -1, 1)
h_lb_cos_theta1rStar = ROOT.TH1F("h_lb_cos_theta1rStar", "top decay (lb) #hat{r*}-polarization ;(lb) cos(#theta_{1r*});Events", 6, -1, 1)
h_lb_cos_theta2kStar = ROOT.TH1F("h_lb_cos_theta2kStar", "antitop decay (lb) #hat{k*}-polarization ;(lb) cos(#theta_{2k*});Events", 6, -1, 1)
h_lb_cos_theta2rStar = ROOT.TH1F("h_lb_cos_theta2rStar", "antitop decay (lb) #hat{r*}-polarization ;(lb) cos(#theta_{2r*});Events", 6, -1, 1)

# Correlation Matrix elements
h_lb_Cnn = ROOT.TH1F("h_lb_Cnn", "(lb) C_{nn};C_{nn};Events", 6, -1, 1)
h_lb_Cnr = ROOT.TH1F("h_lb_Cnr", "(lb) C_{nr};C_{nr};Events", 6, -1, 1)
h_lb_Cnk = ROOT.TH1F("h_lb_Cnk", "(lb) C_{nk};C_{nk};Events", 6, -1, 1)
h_lb_Crn = ROOT.TH1F("h_lb_Crn", "(lb) C_{rn};C_{rn};Events", 6, -1, 1)
h_lb_Crr = ROOT.TH1F("h_lb_Crr", "(lb) C_{rr};C_{rr};Events", 6, -1, 1)
h_lb_Crk = ROOT.TH1F("h_lb_Crk", "(lb) C_{rk};C_{rk};Events", 6, -1, 1)
h_lb_Ckn = ROOT.TH1F("h_lb_Ckn", "(lb) C_{kn};C_{kn};Events", 6, -1, 1)
h_lb_Ckr = ROOT.TH1F("h_lb_Ckr", "(lb) C_{kr};C_{kr};Events", 6, -1, 1)
h_lb_Ckk = ROOT.TH1F("h_lb_Ckk", "(lb) C_{kk};C_{kk};Events", 6, -1, 1)
h_lb_Cnn_slow = ROOT.TH1F("h_lb_Cnn_slow", "(lb) C_{nn} #beta<0.9;C_{nn};Events", 6, -1, 1)
h_lb_Cnr_slow = ROOT.TH1F("h_lb_Cnr_slow", "(lb) C_{nr} #beta<0.9;C_{nr};Events", 6, -1, 1)
h_lb_Cnk_slow = ROOT.TH1F("h_lb_Cnk_slow", "(lb) C_{nk} #beta<0.9;C_{nk};Events", 6, -1, 1)
h_lb_Crn_slow = ROOT.TH1F("h_lb_Crn_slow", "(lb) C_{rn} #beta<0.9;C_{rn};Events", 6, -1, 1)
h_lb_Crr_slow = ROOT.TH1F("h_lb_Crr_slow", "(lb) C_{rr} #beta<0.9;C_{rr};Events", 6, -1, 1)
h_lb_Crk_slow = ROOT.TH1F("h_lb_Crk_slow", "(lb) C_{rk} #beta<0.9;C_{rk};Events", 6, -1, 1)
h_lb_Ckn_slow = ROOT.TH1F("h_lb_Ckn_slow", "(lb) C_{kn} #beta<0.9;C_{kn};Events", 6, -1, 1)
h_lb_Ckr_slow = ROOT.TH1F("h_lb_Ckr_slow", "(lb) C_{kr} #beta<0.9;C_{kr};Events", 6, -1, 1)
h_lb_Ckk_slow = ROOT.TH1F("h_lb_Ckk_slow", "(lb) C_{kk} #beta<0.9;C_{kk};Events", 6, -1, 1)
h_lb_Cnn_BoostedCentral = ROOT.TH1F("h_lb_Cnn_BoostedCentral", "(lb) C_{nn} m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;C_{nn};Events", 6, -1, 1)
h_lb_Cnr_BoostedCentral = ROOT.TH1F("h_lb_Cnr_BoostedCentral", "(lb) C_{nr} m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;C_{nr};Events", 6, -1, 1)
h_lb_Cnk_BoostedCentral = ROOT.TH1F("h_lb_Cnk_BoostedCentral", "(lb) C_{nk} m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;C_{nk};Events", 6, -1, 1)
h_lb_Crn_BoostedCentral = ROOT.TH1F("h_lb_Crn_BoostedCentral", "(lb) C_{rn} m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;C_{rn};Events", 6, -1, 1)
h_lb_Crr_BoostedCentral = ROOT.TH1F("h_lb_Crr_BoostedCentral", "(lb) C_{rr} m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;C_{rr};Events", 6, -1, 1)
h_lb_Crk_BoostedCentral = ROOT.TH1F("h_lb_Crk_BoostedCentral", "(lb) C_{rk} m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;C_{rk};Events", 6, -1, 1)
h_lb_Ckn_BoostedCentral = ROOT.TH1F("h_lb_Ckn_BoostedCentral", "(lb) C_{kn} m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;C_{kn};Events", 6, -1, 1)
h_lb_Ckr_BoostedCentral = ROOT.TH1F("h_lb_Ckr_BoostedCentral", "(lb) C_{kr} m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;C_{kr};Events", 6, -1, 1)
h_lb_Ckk_BoostedCentral = ROOT.TH1F("h_lb_Ckk_BoostedCentral", "(lb) C_{kk} m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;C_{kk};Events", 6, -1, 1)

### Using LEPTONS and D_QUARKS as spin analyzers ###
####################################################
# Entaglement Witnesses
h_ld_cHel    = ROOT.TH1F("h_ld_cHel", "(ld) Cosine Helicity Angle;cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n = ROOT.TH1F("h_ld_cHel_P3n", "(ld) Cosine Helicity Angle w/P_3n;cos(#theta_{l(P_{3}d});Events", 6, -1, 1)
h_ld_cHel_slow    = ROOT.TH1F("h_ld_cHel_slow", "(ld) Cosine Helicity Angle (#beta<0.9);cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_slow = ROOT.TH1F("h_ld_cHel_P3n_slow", "(ld) Cosine Helicity Angle w/P_3n (#beta<0.9);cos(#theta_{l(P_{3}d});Events", 6, -1, 1)
h_ld_cHel_BoostedCentral    = ROOT.TH1F("h_ld_cHel_BoostedCentral", "(ld) Cosine Helicity Angle m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;cos(#theta_{ld});Events", 6, -1, 1)
h_ld_cHel_P3n_BoostedCentral = ROOT.TH1F("h_ld_cHel_P3n_BoostedCentral", "(ld) Cosine Helicity Angle w/P_3n m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;cos(#theta_{l(P_{3}d});Events", 6, -1, 1)
# Polarization
h_ld_cos_theta1k = ROOT.TH1F("h_ld_cos_theta1k", "top decay (ld) #hat{k}-polarization;(ld) cos(#theta_{1k});Events", 6, -1, 1)
h_ld_cos_theta1r = ROOT.TH1F("h_ld_cos_theta1r", "top decay (ld) #hat{r}-polarization;(ld) cos(#theta_{1r});Events", 6, -1, 1)
h_ld_cos_theta1n = ROOT.TH1F("h_ld_cos_theta1n", "top decay (ld) #hat{n}-polarization;(ld) cos(#theta_{1n});Events", 6, -1, 1)
h_ld_cos_theta2k = ROOT.TH1F("h_ld_cos_theta2k", "antitop decay (ld) #hat{k}-polarization;(ld) cos(#theta_{2k});Events", 6, -1, 1)
h_ld_cos_theta2r = ROOT.TH1F("h_ld_cos_theta2r", "antitop decay (ld) #hat{r}-polarization;(ld) cos(#theta_{2r});Events", 6, -1, 1)
h_ld_cos_theta2n = ROOT.TH1F("h_ld_cos_theta2n", "antitop decay (ld) #hat{n}-polarization;(ld) cos(#theta_{2n});Events", 6, -1, 1)
# CA polarizations
h_ld_cos_theta1kStar = ROOT.TH1F("h_ld_cos_theta1kStar", "top decay (ld) #hat{k*}-polarization;(ld) cos(#theta_{1k*});Events", 6, -1, 1)
h_ld_cos_theta1rStar = ROOT.TH1F("h_ld_cos_theta1rStar", "top decay (ld) #hat{r*}-polarization;(ld) cos(#theta_{1r*});Events", 6, -1, 1)
h_ld_cos_theta2kStar = ROOT.TH1F("h_ld_cos_theta2kStar", "antitop decay (ld) #hat{k*}-polarization;(ld) cos(#theta_{2k*});Events", 6, -1, 1)
h_ld_cos_theta2rStar = ROOT.TH1F("h_ld_cos_theta2rStar", "antitop decay (ld) #hat{r*}-polarization;(ld) cos(#theta_{2r*});Events", 6, -1, 1)
# Correlation Matrix elements
h_ld_Cnn = ROOT.TH1F("h_ld_Cnn", "(ld) C_{nn};C_{nn};Events", 6, -1, 1)
h_ld_Cnr = ROOT.TH1F("h_ld_Cnr", "(ld) C_{nr};C_{nr};Events", 6, -1, 1)
h_ld_Cnk = ROOT.TH1F("h_ld_Cnk", "(ld) C_{nk};C_{nk};Events", 6, -1, 1)
h_ld_Crn = ROOT.TH1F("h_ld_Crn", "(ld) C_{rn};C_{rn};Events", 6, -1, 1)
h_ld_Crr = ROOT.TH1F("h_ld_Crr", "(ld) C_{rr};C_{rr};Events", 6, -1, 1)
h_ld_Crk = ROOT.TH1F("h_ld_Crk", "(ld) C_{rk};C_{rk};Events", 6, -1, 1)
h_ld_Ckn = ROOT.TH1F("h_ld_Ckn", "(ld) C_{kn};C_{kn};Events", 6, -1, 1)
h_ld_Ckr = ROOT.TH1F("h_ld_Ckr", "(ld) C_{kr};C_{kr};Events", 6, -1, 1)
h_ld_Ckk = ROOT.TH1F("h_ld_Ckk", "(ld) C_{kk};C_{kk};Events", 6, -1, 1)
h_ld_Cnn_slow = ROOT.TH1F("h_ld_Cnn_slow", "(ld) C_{nn} #beta<0.9;C_{nn};Events", 6, -1, 1)
h_ld_Cnr_slow = ROOT.TH1F("h_ld_Cnr_slow", "(ld) C_{nr} #beta<0.9;C_{nr};Events", 6, -1, 1)
h_ld_Cnk_slow = ROOT.TH1F("h_ld_Cnk_slow", "(ld) C_{nk} #beta<0.9;C_{nk};Events", 6, -1, 1)
h_ld_Crn_slow = ROOT.TH1F("h_ld_Crn_slow", "(ld) C_{rn} #beta<0.9;C_{rn};Events", 6, -1, 1)
h_ld_Crr_slow = ROOT.TH1F("h_ld_Crr_slow", "(ld) C_{rr} #beta<0.9;C_{rr};Events", 6, -1, 1)
h_ld_Crk_slow = ROOT.TH1F("h_ld_Crk_slow", "(ld) C_{rk} #beta<0.9;C_{rk};Events", 6, -1, 1)
h_ld_Ckn_slow = ROOT.TH1F("h_ld_Ckn_slow", "(ld) C_{kn} #beta<0.9;C_{kn};Events", 6, -1, 1)
h_ld_Ckr_slow = ROOT.TH1F("h_ld_Ckr_slow", "(ld) C_{kr} #beta<0.9;C_{kr};Events", 6, -1, 1)
h_ld_Ckk_slow = ROOT.TH1F("h_ld_Ckk_slow", "(ld) C_{kk} #beta<0.9;C_{kk};Events", 6, -1, 1)
h_ld_Cnn_BoostedCentral = ROOT.TH1F("h_ld_Cnn_BoostedCentral", "(ld) C_{nn} m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;C_{nn};Events", 6, -1, 1)
h_ld_Cnr_BoostedCentral = ROOT.TH1F("h_ld_Cnr_BoostedCentral", "(ld) C_{nr} m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;C_{nr};Events", 6, -1, 1)
h_ld_Cnk_BoostedCentral = ROOT.TH1F("h_ld_Cnk_BoostedCentral", "(ld) C_{nk} m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;C_{nk};Events", 6, -1, 1)
h_ld_Crn_BoostedCentral = ROOT.TH1F("h_ld_Crn_BoostedCentral", "(ld) C_{rn} m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;C_{rn};Events", 6, -1, 1)
h_ld_Crr_BoostedCentral = ROOT.TH1F("h_ld_Crr_BoostedCentral", "(ld) C_{rr} m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;C_{rr};Events", 6, -1, 1)
h_ld_Crk_BoostedCentral = ROOT.TH1F("h_ld_Crk_BoostedCentral", "(ld) C_{rk} m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;C_{rk};Events", 6, -1, 1)
h_ld_Ckn_BoostedCentral = ROOT.TH1F("h_ld_Ckn_BoostedCentral", "(ld) C_{kn} m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;C_{kn};Events", 6, -1, 1)
h_ld_Ckr_BoostedCentral = ROOT.TH1F("h_ld_Ckr_BoostedCentral", "(ld) C_{kr} m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;C_{kr};Events", 6, -1, 1)
h_ld_Ckk_BoostedCentral = ROOT.TH1F("h_ld_Ckk_BoostedCentral", "(ld) C_{kk} m_{tt}>800 GeV & |cos(#theta^{*})|<0.6;C_{kk};Events", 6, -1, 1)

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
    # lepton exclusive polarization variables
    "h_cos_theta1k_antilepton": h_cos_theta1k_antilepton,
    "h_cos_theta1r_antilepton": h_cos_theta1r_antilepton,
    "h_cos_theta1n_antilepton": h_cos_theta1n_antilepton,
    "h_cos_theta2k_lepton": h_cos_theta2k_lepton,
    "h_cos_theta2r_lepton": h_cos_theta2r_lepton,
    "h_cos_theta2n_lepton": h_cos_theta2n_lepton,
    # CA polarizations
    "h_cos_theta1kStar_antilepton": h_cos_theta1kStar_antilepton,
    "h_cos_theta1rStar_antilepton": h_cos_theta1rStar_antilepton,
    "h_cos_theta2kStar_lepton": h_cos_theta2kStar_lepton,
    "h_cos_theta2rStar_lepton": h_cos_theta2rStar_lepton,
    
    ### Using LEPTONS and B_QUARKS as spin analyzers ###
    ####################################################
    # Entaglement Witnesses
    "h_lb_cHel": h_lb_cHel,
    "h_lb_cHel_P3n": h_lb_cHel_P3n,
    "h_lb_cHel_slow": h_lb_cHel_slow,
    "h_lb_cHel_P3n_slow": h_lb_cHel_P3n_slow,
    "h_lb_cHel_BoostedCentral": h_lb_cHel_BoostedCentral,
    "h_lb_cHel_P3n_BoostedCentral": h_lb_cHel_P3n_BoostedCentral,
    # Polarization
    "h_lb_cos_theta1k": h_lb_cos_theta1k,
    "h_lb_cos_theta1r": h_lb_cos_theta1r,
    "h_lb_cos_theta1n": h_lb_cos_theta1n,
    "h_lb_cos_theta2k": h_lb_cos_theta2k,
    "h_lb_cos_theta2r": h_lb_cos_theta2r,
    "h_lb_cos_theta2n": h_lb_cos_theta2n,
    # CA polarizations
    "h_lb_cos_theta1kStar": h_lb_cos_theta1kStar,
    "h_lb_cos_theta1rStar": h_lb_cos_theta1rStar,
    "h_lb_cos_theta2kStar": h_lb_cos_theta2kStar,
    "h_lb_cos_theta2rStar": h_lb_cos_theta2rStar,
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
    "h_lb_Cnn_slow": h_lb_Cnn_slow,
    "h_lb_Cnr_slow": h_lb_Cnr_slow,
    "h_lb_Cnk_slow": h_lb_Cnk_slow,
    "h_lb_Crn_slow": h_lb_Crn_slow,
    "h_lb_Crr_slow": h_lb_Crr_slow,
    "h_lb_Crk_slow": h_lb_Crk_slow,
    "h_lb_Ckn_slow": h_lb_Ckn_slow,
    "h_lb_Ckr_slow": h_lb_Ckr_slow,
    "h_lb_Ckk_slow": h_lb_Ckk_slow,
    "h_lb_Cnn_BoostedCentral": h_lb_Cnn_BoostedCentral,
    "h_lb_Cnr_BoostedCentral": h_lb_Cnr_BoostedCentral,
    "h_lb_Cnk_BoostedCentral": h_lb_Cnk_BoostedCentral,
    "h_lb_Crn_BoostedCentral": h_lb_Crn_BoostedCentral,
    "h_lb_Crr_BoostedCentral": h_lb_Crr_BoostedCentral,
    "h_lb_Crk_BoostedCentral": h_lb_Crk_BoostedCentral,
    "h_lb_Ckn_BoostedCentral": h_lb_Ckn_BoostedCentral,
    "h_lb_Ckr_BoostedCentral": h_lb_Ckr_BoostedCentral,
    "h_lb_Ckk_BoostedCentral": h_lb_Ckk_BoostedCentral,

    ### Using LEPTONS and D_QUARKS as spin analyzers ###
    ####################################################
    # Entaglement Witnesses
    "h_ld_cHel": h_ld_cHel,
    "h_ld_cHel_P3n": h_ld_cHel_P3n,
    "h_ld_cHel_slow": h_ld_cHel_slow,
    "h_ld_cHel_P3n_slow": h_ld_cHel_P3n_slow,
    "h_ld_cHel_BoostedCentral": h_ld_cHel_BoostedCentral,
    "h_ld_cHel_P3n_BoostedCentral": h_ld_cHel_P3n_BoostedCentral,
    # Polarization
    "h_ld_cos_theta1k": h_ld_cos_theta1k,
    "h_ld_cos_theta1r": h_ld_cos_theta1r,
    "h_ld_cos_theta1n": h_ld_cos_theta1n,
    "h_ld_cos_theta2k": h_ld_cos_theta2k,
    "h_ld_cos_theta2r": h_ld_cos_theta2r,
    "h_ld_cos_theta2n": h_ld_cos_theta2n,
    # CA polarizations
    "h_ld_cos_theta1kStar": h_ld_cos_theta1kStar,
    "h_ld_cos_theta1rStar": h_ld_cos_theta1rStar,
    "h_ld_cos_theta2kStar": h_ld_cos_theta2kStar,
    "h_ld_cos_theta2rStar": h_ld_cos_theta2rStar,
    # Correlation Matrix elements
    "h_ld_Cnn": h_ld_Cnn,
    "h_ld_Cnr": h_ld_Cnr,
    "h_ld_Cnk": h_ld_Cnk,
    "h_ld_Crn": h_ld_Crn,
    "h_ld_Crr": h_ld_Crr,
    "h_ld_Crk": h_ld_Crk,
    "h_ld_Ckn": h_ld_Ckn,
    "h_ld_Ckr": h_ld_Ckr,
    "h_ld_Ckk": h_ld_Ckk,
    "h_ld_Cnn_slow": h_ld_Cnn_slow,
    "h_ld_Cnr_slow": h_ld_Cnr_slow,
    "h_ld_Cnk_slow": h_ld_Cnk_slow,
    "h_ld_Crn_slow": h_ld_Crn_slow,
    "h_ld_Crr_slow": h_ld_Crr_slow,
    "h_ld_Crk_slow": h_ld_Crk_slow,
    "h_ld_Ckn_slow": h_ld_Ckn_slow,
    "h_ld_Ckr_slow": h_ld_Ckr_slow,
    "h_ld_Ckk_slow": h_ld_Ckk_slow,
    "h_ld_Cnn_BoostedCentral": h_ld_Cnn_BoostedCentral,
    "h_ld_Cnr_BoostedCentral": h_ld_Cnr_BoostedCentral,
    "h_ld_Cnk_BoostedCentral": h_ld_Cnk_BoostedCentral,
    "h_ld_Crn_BoostedCentral": h_ld_Crn_BoostedCentral,
    "h_ld_Crr_BoostedCentral": h_ld_Crr_BoostedCentral,
    "h_ld_Crk_BoostedCentral": h_ld_Crk_BoostedCentral,
    "h_ld_Ckn_BoostedCentral": h_ld_Ckn_BoostedCentral,
    "h_ld_Ckr_BoostedCentral": h_ld_Ckr_BoostedCentral,
    "h_ld_Ckk_BoostedCentral": h_ld_Ckk_BoostedCentral
    }