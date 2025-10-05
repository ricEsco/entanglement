# -*- coding: utf-8 -*-
import ROOT
import os
import sys
import math
from histogram_definitions import histogram_defs
ROOT.gROOT.SetBatch(True)
###############################################################################################################
### Be sure to modify histogram_definitions.py accordingly when adding/removing histograms from this script ###
###############################################################################################################


#############################################################
### Loop over all events and call process_event for each  ###
#############################################################
def analyze(filename):
    print("Processing file:", filename)
    if not os.path.isfile(filename):
        print("Error: The path provided is not a file:", filename)
        return None
    try:
        file = ROOT.TFile.Open(filename)
        if not file or file.IsZombie():
            print("Error: Unable to open file:", filename)
            return None
        tree = file.Get("Events")
    except Exception as e:
        print("An error occurred while processing the file {}: {}".format(filename, str(e)))
        return None
    
    # call histogram definition function
    histograms = histogram_defs

    # loop over all events
    for entry in tree:
        # counter to monitor progress
        if entry.GetReadEntry() % 100 == 0:
            print("Processing event:", int(entry.GetReadEntry()), "/", int(tree.GetEntries()))
        # Process each event
        process_event(entry, histograms)
    file.Close()

    return histograms


# Function to identify last_copy of a particle
def is_last_copy(statusFlags):
    try:
        status_flags_int = int(statusFlags)
        return (status_flags_int & (1 << 13)) != 0
    except ValueError:
        return False
    
# Funtion to identify first_copy of a particle
def is_first_copy(statusFlags):
    try:
        status_flags_int = int(statusFlags)
        return (status_flags_int & (1 << 12)) != 0
    except ValueError:
        return False
      
#####################################################
### Process individual events and fill histograms ###
#####################################################
def process_event(entry, histograms):
    # Hard-process particles stored as tuples of (4vector, idx) in a list
    tops =              []
    antitops =          []
    top_idx =           -1
    antitop_idx =       -1
    bottom_quarks =              []
    antibottom_quarks =          []
    hadronic_antibottom_quarks = []
    hadronic_bottom_quarks =     []
    bottom_idx =                 -1
    antibottom_idx =             -1
    Wplus =             []
    Wminus =            []
    Wplus_idx =         -1
    Wminus_idx =        -1

    leptons =           []
    antiLeptons =       []
    lepton_idx =        -1
    antiLepton_idx =    -1
    neutrinos =         []
    antiNeutrinos =     []
    neutrino_idx =      -1
    antiNeutrino_idx =  -1

    dtype_quarks =        []
    antiDtype_quarks =    []
    dtype_quark_idx =     -1
    antiDtype_quark_idx = -1
    utype_quarks =        []
    antiUtype_quarks =    []
    utype_quark_idx =     -1
    antiUtype_quark_idx = -1

    # Decay mode flags
    has_hadronic_antiTop_decay = False
    has_hadronic_top_decay =     False

    # Decay particle 4vectors
    top_4vec =                  ROOT.TLorentzVector()
    antitop_4vec =              ROOT.TLorentzVector()
    bottom_4vec =                    ROOT.TLorentzVector()
    antibottom_4vec =                ROOT.TLorentzVector()
    hadronic_antibottom_quark_4vec = ROOT.TLorentzVector()
    hadronic_bottom_quark_4vec =     ROOT.TLorentzVector()
    Wplus_4vec =                ROOT.TLorentzVector()
    Wminus_4vec =               ROOT.TLorentzVector()

    antiLepton_4vec =   ROOT.TLorentzVector()
    lepton_4vec =       ROOT.TLorentzVector()
    neutrino_4vec =     ROOT.TLorentzVector()
    antiNeutrino_4vec = ROOT.TLorentzVector()
    
    utype_quark_4vec =     ROOT.TLorentzVector()
    antiUtype_quark_4vec = ROOT.TLorentzVector()
    dtype_quark_4vec =     ROOT.TLorentzVector()
    antiDtype_quark_4vec = ROOT.TLorentzVector()

    # TTbar system
    ttbar_4vec =       ROOT.TLorentzVector()
    scattering_angle = float('nan')
    top_E      =       float('nan')
    antitop_E  =       float('nan')
    beta       =       float('nan')
    deltaAbsY  =       float('nan')
    hypTan_deltaAbsY = float('nan')

    ## (leptonic-top scenario) spin-analyzer direction vectors ##
    #############################################################
    # top quark decay product
    mRF_antiLepton_dir = ROOT.TVector3()
    # top antiquark decay products
    mRF_hadronic_antibottom_quark_dir =     ROOT.TVector3()
    mRF_dtype_quark_4vec_dir =              ROOT.TVector3()

    ## (hadronic-top scenario) spin-analyzer direction vectors ##
    #############################################################
    # top quark decay products
    mRF_hadronic_bottom_quark_dir = ROOT.TVector3()
    mRF_antiDtype_quark_4vec_dir =  ROOT.TVector3()
    # top antiquark decay product
    mRF_lepton_4vec_dir =     ROOT.TVector3()

    # Bernreuther basis
    p_axis = ROOT.TVector3(0, 0, 1)  # proton beam direction in lab frame
    k_axis = ROOT.TVector3()
    r_axis = ROOT.TVector3()
    n_axis = ROOT.TVector3()

    # top quark reference axes
    k_top = ROOT.TVector3()
    r_top = ROOT.TVector3()
    n_top = ROOT.TVector3()
    # antitop quark reference axes
    k_antitop = ROOT.TVector3()
    r_antitop = ROOT.TVector3()
    n_antitop = ROOT.TVector3()

    # lepton exclusive polarization variables
    cos_theta1k_antilepton = float('nan')
    cos_theta1r_antilepton = float('nan')
    cos_theta1n_antilepton = float('nan')
    cos_theta2k_lepton = float('nan')
    cos_theta2r_lepton = float('nan')
    cos_theta2n_lepton = float('nan')
    # CA polarization
    cos_theta1kStar_antilepton = float('nan')
    cos_theta1rStar_antilepton = float('nan')
    cos_theta2kStar_lepton =     float('nan')
    cos_theta2rStar_lepton =     float('nan')
    
    # Spin correlation variables using lepton and b-quarks
    lb_cHel =     float('nan')
    lb_cHel_P3n = float('nan')
    lb_cos_theta1k = float('nan')
    lb_cos_theta1r = float('nan')
    lb_cos_theta1n = float('nan')
    lb_cos_theta2k = float('nan')
    lb_cos_theta2r = float('nan')
    lb_cos_theta2n = float('nan')
    # CA polarization
    lb_cos_theta1kStar = float('nan')
    lb_cos_theta1rStar = float('nan')
    lb_cos_theta2kStar = float('nan')
    lb_cos_theta2rStar = float('nan')
    lb_Cnn = float('nan')
    lb_Cnr = float('nan')
    lb_Cnk = float('nan')
    lb_Crn = float('nan')
    lb_Crr = float('nan')
    lb_Crk = float('nan')
    lb_Ckn = float('nan')
    lb_Ckr = float('nan')
    lb_Ckk = float('nan')

    # Spin correlation variables using lepton and d-quarks
    ld_cHel =     float('nan')
    ld_cHel_P3n = float('nan')
    ld_cos_theta1k = float('nan')
    ld_cos_theta1r = float('nan')
    ld_cos_theta1n = float('nan')
    ld_cos_theta2k = float('nan')
    ld_cos_theta2r = float('nan')
    ld_cos_theta2n = float('nan')
    # CA polarization
    ld_cos_theta1kStar = float('nan')
    ld_cos_theta1rStar = float('nan')
    ld_cos_theta2kStar = float('nan')
    ld_cos_theta2rStar = float('nan')
    ld_Cnn = float('nan')
    ld_Cnr = float('nan')
    ld_Cnk = float('nan')
    ld_Crn = float('nan')
    ld_Crr = float('nan')
    ld_Crk = float('nan')
    ld_Ckn = float('nan')
    ld_Ckr = float('nan')
    ld_Ckk = float('nan')


    # Find top or antitop quark
    for i in range(entry.nGenPart):
        # Check particle id and status flags
        pdgId = entry.GenPart_pdgId[i]
        statusFlags = entry.GenPart_statusFlags[i]

        # Check if particle is last_copy of top quark
        if is_last_copy(statusFlags) and abs(pdgId) == 6:
            # Top quark
            if pdgId == 6:
                top_idx = i
                top_4vec.SetPtEtaPhiM(entry.GenPart_pt[i], entry.GenPart_eta[i], entry.GenPart_phi[i], entry.GenPart_mass[i])
                tops.append((top_4vec, top_idx))
                top_E = top_4vec.E()
            # antiTop quark
            elif pdgId == -6:
                antitop_idx = i
                antitop_4vec.SetPtEtaPhiM(entry.GenPart_pt[i], entry.GenPart_eta[i], entry.GenPart_phi[i], entry.GenPart_mass[i])
                antitops.append((antitop_4vec, antitop_idx))
                antitop_E = antitop_4vec.E()

    # Compute and plot ttbar system quantities while still in the LAB FRAME
    ttbar_4vec = top_4vec + antitop_4vec
    m_tt = ttbar_4vec.M()
    beta = abs((top_4vec.Pz() + antitop_4vec.Pz()) / (top_E + antitop_E))
    histograms['h_invariantMass'].Fill(m_tt)
    histograms['h_beta'].Fill(beta)

    # Charge Asymmetry
    deltaAbsY = abs(top_4vec.Rapidity()) - abs(antitop_4vec.Rapidity())
    hypTan_deltaAbsY = ROOT.TMath.TanH(deltaAbsY)
    histograms['h_deltaAbsY'].Fill(deltaAbsY)
    histograms['h_hypTan_deltaAbsY'].Fill(hypTan_deltaAbsY)

    # Find bottom quarks from top or anti-top quark decay
    for j in range(entry.nGenPart):
        # Check if the j-th particle is a daughter of top or anti-top quark
        if entry.GenPart_genPartIdxMother[j] == top_idx or entry.GenPart_genPartIdxMother[j] == antitop_idx:
            daughter_pdgId = entry.GenPart_pdgId[j]

            # Top quark daughter is bottom quark
            if daughter_pdgId == 5 and is_first_copy(entry.GenPart_statusFlags[j]):
                bottom_idx = j
                bottom_4vec.SetPtEtaPhiM(entry.GenPart_pt[bottom_idx], entry.GenPart_eta[bottom_idx], entry.GenPart_phi[bottom_idx], entry.GenPart_mass[bottom_idx])
                bottom_quarks.append((bottom_4vec, j))
                
            # antiTop quark daughter is antibottom quark
            elif daughter_pdgId == -5 and is_first_copy(entry.GenPart_statusFlags[j]):
                antibottom_idx = j
                antibottom_4vec.SetPtEtaPhiM(entry.GenPart_pt[antibottom_idx], entry.GenPart_eta[antibottom_idx], entry.GenPart_phi[antibottom_idx], entry.GenPart_mass[antibottom_idx])
                antibottom_quarks.append((antibottom_4vec, j))    
   
    # Find W bosons
    for k in range(entry.nGenPart):
        # Check particle mother idx and status flag
        _pdgId = entry.GenPart_pdgId[k]
        _statusFlags = entry.GenPart_statusFlags[k]

        # Check if particle is last_copy of W boson
        if is_last_copy(_statusFlags) and abs(_pdgId) == 24:
            # Top quark daughter
            if _pdgId == 24:
                Wplus_idx = k
                Wplus_4vec.SetPtEtaPhiM(entry.GenPart_pt[Wplus_idx], entry.GenPart_eta[Wplus_idx], entry.GenPart_phi[Wplus_idx], entry.GenPart_mass[Wplus_idx])
                Wplus.append((Wplus_4vec, Wplus_idx))
            # Anti-top quark daughter
            elif _pdgId == -24:
                Wminus_idx = k
                Wminus_4vec.SetPtEtaPhiM(entry.GenPart_pt[Wminus_idx], entry.GenPart_eta[Wminus_idx], entry.GenPart_phi[Wminus_idx], entry.GenPart_mass[Wminus_idx])
                Wminus.append((Wminus_4vec, Wminus_idx))
                
    # Find W boson daughters
    for l in range(entry.nGenPart):
        # Check if the l-th particle is a daughter of W boson
        if entry.GenPart_genPartIdxMother[l] == Wplus_idx or entry.GenPart_genPartIdxMother[l] == Wminus_idx:
            _daughter_pdgId = entry.GenPart_pdgId[l]
            _daughter_statusFlags = entry.GenPart_statusFlags[l]

            # leptonic-top scenario => (t+ -> W+,b- -> l+v, b-) and (t- -> W-,b+ -> q_ubar-, q_d-, b+)
            # antilepton from leptonic W+ decay
            if _daughter_pdgId in [-11, -13, -15] and is_first_copy(_daughter_statusFlags):
                has_hadronic_antiTop_decay = True
                antiLepton_idx = l
                antiLepton_4vec.SetPtEtaPhiM(entry.GenPart_pt[antiLepton_idx], entry.GenPart_eta[antiLepton_idx], entry.GenPart_phi[antiLepton_idx], entry.GenPart_mass[antiLepton_idx])
                antiLeptons.append((antiLepton_4vec, antiLepton_idx))
            # neutrino from leptonic W+ decay
            elif _daughter_pdgId in [12, 14, 16] and is_first_copy(_daughter_statusFlags):
                neutrino_idx = l
                neutrino_4vec.SetPtEtaPhiM(entry.GenPart_pt[l], entry.GenPart_eta[l], entry.GenPart_phi[l], entry.GenPart_mass[l])
                neutrinos.append((neutrino_4vec, neutrino_idx))
            # antiup-type quark from hadronically decaying W-
            elif _daughter_pdgId in [-2, -4] and is_first_copy(_daughter_statusFlags):
                antiUtype_quark_idx = l
                antiUtype_quark_4vec.SetPtEtaPhiM(entry.GenPart_pt[l], entry.GenPart_eta[l], entry.GenPart_phi[l], entry.GenPart_mass[l])
                antiUtype_quarks.append((antiUtype_quark_4vec, antiUtype_quark_idx))
            # down-type quark from hadronically decaying W-
            elif _daughter_pdgId in [1, 3] and is_first_copy(_daughter_statusFlags):
                dtype_quark_idx = l
                dtype_quark_4vec.SetPtEtaPhiM(entry.GenPart_pt[l], entry.GenPart_eta[l], entry.GenPart_phi[l], entry.GenPart_mass[l])
                dtype_quarks.append((dtype_quark_4vec, dtype_quark_idx))
                
            # hadronic-top scenario => (t+ -> W+,b- -> q+, q+, b-) and (t- -> W-,b+ -> l-v, b+)
            # lepton from leptonic W- decay
            elif _daughter_pdgId in [11, 13, 15] and is_first_copy(_daughter_statusFlags):
                has_hadronic_top_decay = True
                lepton_idx = l
                lepton_4vec.SetPtEtaPhiM(entry.GenPart_pt[lepton_idx], entry.GenPart_eta[lepton_idx], entry.GenPart_phi[lepton_idx], entry.GenPart_mass[lepton_idx])
                leptons.append((lepton_4vec, lepton_idx))
            # anti-neutrino from leptonic W- decay
            elif _daughter_pdgId in [-12, -14, -16] and is_first_copy(_daughter_statusFlags):
                antiNeutrino_idx = l
                antiNeutrino_4vec.SetPtEtaPhiM(entry.GenPart_pt[l], entry.GenPart_eta[l], entry.GenPart_phi[l], entry.GenPart_mass[l])
                antiNeutrinos.append((antiNeutrino_4vec, antiNeutrino_idx))
            # up-type quark from hadronically decaying W+
            elif _daughter_pdgId in [2, 4] and is_first_copy(_daughter_statusFlags):
                utype_quark_idx = l
                utype_quark_4vec.SetPtEtaPhiM(entry.GenPart_pt[l], entry.GenPart_eta[l], entry.GenPart_phi[l], entry.GenPart_mass[l])
                utype_quarks.append((utype_quark_4vec, utype_quark_idx))
            # antidown-type quark from hadronically decaying W+
            elif _daughter_pdgId in [-1, -3] and is_first_copy(_daughter_statusFlags):
                antiDtype_quark_idx = l
                antiDtype_quark_4vec.SetPtEtaPhiM(entry.GenPart_pt[l], entry.GenPart_eta[l], entry.GenPart_phi[l], entry.GenPart_mass[l])
                antiDtype_quarks.append((antiDtype_quark_4vec, antiDtype_quark_idx))

    if has_hadronic_antiTop_decay: # implies hadronically decaying antitop quark has antibottom quark daughter
        hadronic_antibottom_quark_4vec.SetPtEtaPhiM(entry.GenPart_pt[antibottom_idx], entry.GenPart_eta[antibottom_idx], entry.GenPart_phi[antibottom_idx], entry.GenPart_mass[antibottom_idx])
        hadronic_antibottom_quarks.append((hadronic_antibottom_quark_4vec, antibottom_idx))
    elif has_hadronic_top_decay: # implies hadronically decaying top quarks has bottom quark daughter
        hadronic_bottom_quark_4vec.SetPtEtaPhiM(entry.GenPart_pt[bottom_idx], entry.GenPart_eta[bottom_idx], entry.GenPart_phi[bottom_idx], entry.GenPart_mass[bottom_idx])
        hadronic_bottom_quarks.append((hadronic_bottom_quark_4vec, bottom_idx))


    ##############################################
    ### Fill kinematic histograms in LAB FRAME ###
    ##############################################
    # top quark histograms
    for top_4vec, top_idx in tops:
        histograms['h_topPt'].Fill(top_4vec.Pt())
        histograms['h_topEta'].Fill(top_4vec.Eta())
        histograms['h_topPhi'].Fill(top_4vec.Phi())
        histograms['h_topMass'].Fill(top_4vec.M())
    for antitop_4vec, antitop_idx in antitops:
        histograms['h_antitopPt'].Fill(antitop_4vec.Pt())
        histograms['h_antitopEta'].Fill(antitop_4vec.Eta())
        histograms['h_antitopPhi'].Fill(antitop_4vec.Phi())
        histograms['h_antitopMass'].Fill(antitop_4vec.M())

    # bottom quark histograms
    for b_4vector, bottom_idx in bottom_quarks:
        histograms['h_bquark_pt'].Fill(b_4vector.Pt())
        histograms['h_bquark_eta'].Fill(b_4vector.Eta())
        histograms['h_bquark_phi'].Fill(b_4vector.Phi())
    for antib_4vector, antibottom_idx in antibottom_quarks:
        histograms['h_antibquark_pt'].Fill(antib_4vector.Pt())
        histograms['h_antibquark_eta'].Fill(antib_4vector.Eta())
        histograms['h_antibquark_phi'].Fill(antib_4vector.Phi())
    if has_hadronic_antiTop_decay:
        for hadronic_antibottom_quark_4vec, antibottom_idx in hadronic_antibottom_quarks:
            histograms['h_Had_antibquark_pt'].Fill(hadronic_antibottom_quark_4vec.Pt())
            histograms['h_Had_antibquark_eta'].Fill(hadronic_antibottom_quark_4vec.Eta())
            histograms['h_Had_antibquark_phi'].Fill(hadronic_antibottom_quark_4vec.Phi())
    elif has_hadronic_top_decay:
        for hadronic_bottom_quark_4vec, bottom_idx in hadronic_bottom_quarks:
            histograms['h_Had_bquark_pt'].Fill(hadronic_bottom_quark_4vec.Pt())
            histograms['h_Had_bquark_eta'].Fill(hadronic_bottom_quark_4vec.Eta())
            histograms['h_Had_bquark_phi'].Fill(hadronic_bottom_quark_4vec.Phi())

    # W boson histograms
    for Wplus_4vec, Wplus_idx in Wplus:
        histograms['h_Wplus_pt'].Fill(Wplus_4vec.Pt())
        histograms['h_Wplus_eta'].Fill(Wplus_4vec.Eta())
        histograms['h_Wplus_phi'].Fill(Wplus_4vec.Phi())
        histograms['h_Wplus_mass'].Fill(Wplus_4vec.M())
    for Wminus_4vec, Wminus_idx in Wminus:
        histograms['h_Wminus_pt'].Fill(Wminus_4vec.Pt())
        histograms['h_Wminus_eta'].Fill(Wminus_4vec.Eta())
        histograms['h_Wminus_phi'].Fill(Wminus_4vec.Phi())
        histograms['h_Wminus_mass'].Fill(Wminus_4vec.M())

    # lepton histograms
    for lepton_4vec, lepton_idx in leptons:
        histograms['h_leptonPt'].Fill(lepton_4vec.Pt())
        histograms['h_leptoneta'].Fill(lepton_4vec.Eta())
        histograms['h_leptonphi'].Fill(lepton_4vec.Phi())
    for antiLepton_4vec, antiLepton_idx in antiLeptons:
        histograms['h_antiLeptonPt'].Fill(antiLepton_4vec.Pt())
        histograms['h_antiLeptoneta'].Fill(antiLepton_4vec.Eta())
        histograms['h_antiLeptonphi'].Fill(antiLepton_4vec.Phi())
    for neutrino_4vec, neutrino_idx in neutrinos:
        histograms['h_neutrinoPt'].Fill(neutrino_4vec.Pt())
        histograms['h_neutrinoeta'].Fill(neutrino_4vec.Eta())
        histograms['h_neutrinophi'].Fill(neutrino_4vec.Phi())
    for antiNeutrino_4vec, antiNeutrino_idx in antiNeutrinos:
        histograms['h_antiNeutrinoPt'].Fill(antiNeutrino_4vec.Pt())
        histograms['h_antiNeutrinoeta'].Fill(antiNeutrino_4vec.Eta())
        histograms['h_antiNeutrinophi'].Fill(antiNeutrino_4vec.Phi())

    # light quark histograms
    for utype_quark_4vec, utype_quark_idx in utype_quarks:
        histograms['h_utype_quark_pt'].Fill(utype_quark_4vec.Pt())
        histograms['h_utype_quark_eta'].Fill(utype_quark_4vec.Eta())
        histograms['h_utype_quark_phi'].Fill(utype_quark_4vec.Phi())
    for antiUtype_quark_4vec, antiUtype_quark_idx in antiUtype_quarks:
        histograms['h_antiUtype_quark_pt'].Fill(antiUtype_quark_4vec.Pt())
        histograms['h_antiUtype_quark_eta'].Fill(antiUtype_quark_4vec.Eta())
        histograms['h_antiUtype_quark_phi'].Fill(antiUtype_quark_4vec.Phi())
    for dtype_quark_4vec, dtype_quark_idx in dtype_quarks:
        histograms['h_dtype_quark_pt'].Fill(dtype_quark_4vec.Pt())
        histograms['h_dtype_quark_eta'].Fill(dtype_quark_4vec.Eta())
        histograms['h_dtype_quark_phi'].Fill(dtype_quark_4vec.Phi())
    for antiDtype_quark_4vec, antiDtype_quark_idx in antiDtype_quarks:
        histograms['h_antiDtype_quark_pt'].Fill(antiDtype_quark_4vec.Pt())
        histograms['h_antiDtype_quark_eta'].Fill(antiDtype_quark_4vec.Eta())
        histograms['h_antiDtype_quark_phi'].Fill(antiDtype_quark_4vec.Phi())

    
    ### Boost ttbar system to the ttbar REST FRAME i.e. CoM Frame ###
    #################################################################
    top_4vec.Boost(-ttbar_4vec.BoostVector())
    antitop_4vec.Boost(-ttbar_4vec.BoostVector())
    ### leptonic-top scenario ###
    if has_hadronic_antiTop_decay:
        # top quark decay product
        antiLepton_4vec.Boost(-ttbar_4vec.BoostVector())
        # top antiquark decay products
        hadronic_antibottom_quark_4vec.Boost(-ttbar_4vec.BoostVector())
        dtype_quark_4vec.Boost(-ttbar_4vec.BoostVector())
    ### hadronic-top scenario ###
    elif has_hadronic_top_decay:
        # top quark decay products
        hadronic_bottom_quark_4vec.Boost(-ttbar_4vec.BoostVector())
        antiDtype_quark_4vec.Boost(-ttbar_4vec.BoostVector())
        # top antiquark decay product
        lepton_4vec.Boost(-ttbar_4vec.BoostVector())

    ###############################
    ### build Bernreuther basis ###
    ###############################
    k_axis = top_4vec.Vect().Unit()                        # direction of top quark in ttbar rest frame
    scattering_angle = k_axis.Angle(p_axis)                # angle between top quark direction and proton beam direction
    histograms['h_scattering_angle'].Fill(scattering_angle)
    mag_sinTSA = abs(ROOT.TMath.Sin(scattering_angle))     # magnitude of sin(Top_Scattering_Angle)
    cosTSA = ROOT.TMath.Cos(scattering_angle)              # cos(Top_Scattering_Angle)
    r_axis = (1/mag_sinTSA) * (p_axis - (cosTSA * k_axis)) # orthogonal to k_axis and lies in production plane
    n_axis = (1/mag_sinTSA) * p_axis.Cross(k_axis)         # orthogonal to production plane

    ### top quark reference axes ###
    ################################
    k_top = k_axis
    r_top = (1.0 if cosTSA >= 0 else -1.0) * r_axis
    n_top = (1.0 if cosTSA >= 0 else -1.0) * n_axis
    ### CA-polarization axes
    kStar_top = (1.0 if deltaAbsY >= 0 else -1.0) * k_axis
    rStar_top = (1.0 if deltaAbsY >= 0 else -1.0) * (1.0 if cosTSA >= 0 else -1.0) * r_axis

    ### antitop quark reference axes ###
    ####################################
    k_antitop = -1.0 * k_axis
    r_antitop = -1.0 * (1.0 if cosTSA >= 0 else -1.0) * r_axis
    n_antitop = -1.0 * (1.0 if cosTSA >= 0 else -1.0) * n_axis
    ### CA-polarization axes
    kStar_antitop = -1.0 * (1.0 if deltaAbsY >= 0 else -1.0) * k_axis
    rStar_antitop = -1.0 * (1.0 if deltaAbsY >= 0 else -1.0) * (1.0 if cosTSA >= 0 else -1.0) * r_axis


    ### Boost decay products to their motherTop's REST FRAME ###
    ############################################################
    ### leptonic-top scenario ###
    if has_hadronic_antiTop_decay: 
        # top quark decay product
        antiLepton_4vec.Boost(-top_4vec.BoostVector())
        mRF_antiLepton_dir = antiLepton_4vec.Vect().Unit()
        # top antiquark decay products
        hadronic_antibottom_quark_4vec.Boost(-antitop_4vec.BoostVector())
        dtype_quark_4vec.Boost(-antitop_4vec.BoostVector())
        mRF_hadronic_antibottom_quark_dir = hadronic_antibottom_quark_4vec.Vect().Unit()
        mRF_dtype_quark_4vec_dir = dtype_quark_4vec.Vect().Unit()
        
    ### hadronic-top scenario ###
    elif has_hadronic_top_decay: 
        # top quark decay products
        hadronic_bottom_quark_4vec.Boost(-top_4vec.BoostVector())
        antiDtype_quark_4vec.Boost(-top_4vec.BoostVector())
        mRF_hadronic_bottom_quark_dir = hadronic_bottom_quark_4vec.Vect().Unit()
        mRF_antiDtype_quark_4vec_dir = antiDtype_quark_4vec.Vect().Unit()
        # top antiquark decay product
        lepton_4vec.Boost(-antitop_4vec.BoostVector())
        mRF_lepton_4vec_dir = lepton_4vec.Vect().Unit()


    ### Spin correlation variables ###
    ##################################
    # LEPTON Exclusive polarization variables
    if has_hadronic_antiTop_decay:
        cos_theta1k_antilepton = ROOT.TMath.Cos(mRF_antiLepton_dir.Angle(k_top))
        cos_theta1r_antilepton = ROOT.TMath.Cos(mRF_antiLepton_dir.Angle(r_top))
        cos_theta1n_antilepton = ROOT.TMath.Cos(mRF_antiLepton_dir.Angle(n_top))
        cos_theta1kStar_antilepton = ROOT.TMath.Cos(mRF_antiLepton_dir.Angle(kStar_top))
        cos_theta1rStar_antilepton = ROOT.TMath.Cos(mRF_antiLepton_dir.Angle(rStar_top))
    elif has_hadronic_top_decay:
        cos_theta2k_lepton = ROOT.TMath.Cos(mRF_lepton_4vec_dir.Angle(k_antitop))
        cos_theta2r_lepton = ROOT.TMath.Cos(mRF_lepton_4vec_dir.Angle(r_antitop))
        cos_theta2n_lepton = ROOT.TMath.Cos(mRF_lepton_4vec_dir.Angle(n_antitop))
        cos_theta2kStar_lepton = ROOT.TMath.Cos(mRF_lepton_4vec_dir.Angle(kStar_antitop))
        cos_theta2rStar_lepton = ROOT.TMath.Cos(mRF_lepton_4vec_dir.Angle(rStar_antitop))

    # Using leptons and (b- OR d-quarks) as spin analyzers
    ### leptonic-top scenario ###
    if has_hadronic_antiTop_decay: 
        ### Polarizations coefficients ###
        ##################################
        # top quark decay product
        lb_cos_theta1k = ROOT.TMath.Cos(mRF_antiLepton_dir.Angle(k_top))
        lb_cos_theta1r = ROOT.TMath.Cos(mRF_antiLepton_dir.Angle(r_top))
        lb_cos_theta1n = ROOT.TMath.Cos(mRF_antiLepton_dir.Angle(n_top))
        lb_cos_theta1kStar = ROOT.TMath.Cos(mRF_antiLepton_dir.Angle(kStar_top))
        lb_cos_theta1rStar = ROOT.TMath.Cos(mRF_antiLepton_dir.Angle(rStar_top))
        ld_cos_theta1k = ROOT.TMath.Cos(mRF_antiLepton_dir.Angle(k_top))
        ld_cos_theta1r = ROOT.TMath.Cos(mRF_antiLepton_dir.Angle(r_top))
        ld_cos_theta1n = ROOT.TMath.Cos(mRF_antiLepton_dir.Angle(n_top))
        ld_cos_theta1kStar = ROOT.TMath.Cos(mRF_antiLepton_dir.Angle(kStar_top))
        ld_cos_theta1rStar = ROOT.TMath.Cos(mRF_antiLepton_dir.Angle(rStar_top))
        # top antiquark decay products
        lb_cos_theta2k = ROOT.TMath.Cos(mRF_hadronic_antibottom_quark_dir.Angle(k_antitop))
        lb_cos_theta2r = ROOT.TMath.Cos(mRF_hadronic_antibottom_quark_dir.Angle(r_antitop))
        lb_cos_theta2n = ROOT.TMath.Cos(mRF_hadronic_antibottom_quark_dir.Angle(n_antitop))
        lb_cos_theta2kStar = ROOT.TMath.Cos(mRF_hadronic_antibottom_quark_dir.Angle(kStar_antitop))
        lb_cos_theta2rStar = ROOT.TMath.Cos(mRF_hadronic_antibottom_quark_dir.Angle(rStar_antitop))
        ld_cos_theta2k = ROOT.TMath.Cos(mRF_dtype_quark_4vec_dir.Angle(k_antitop))
        ld_cos_theta2r = ROOT.TMath.Cos(mRF_dtype_quark_4vec_dir.Angle(r_antitop))
        ld_cos_theta2n = ROOT.TMath.Cos(mRF_dtype_quark_4vec_dir.Angle(n_antitop))
        ld_cos_theta2kStar = ROOT.TMath.Cos(mRF_dtype_quark_4vec_dir.Angle(kStar_antitop))
        ld_cos_theta2rStar = ROOT.TMath.Cos(mRF_dtype_quark_4vec_dir.Angle(rStar_antitop))

        ### Entanglement variables ###
        ##############################
        lb_cHel =    ROOT.TMath.Cos(mRF_antiLepton_dir.Angle(mRF_hadronic_antibottom_quark_dir))
        ld_cHel =    ROOT.TMath.Cos(mRF_antiLepton_dir.Angle(mRF_dtype_quark_4vec_dir))
        lb_cHel_P3n = lb_cos_theta1k*lb_cos_theta2k + lb_cos_theta1r*lb_cos_theta2r - lb_cos_theta1n*lb_cos_theta2n
        ld_cHel_P3n = ld_cos_theta1k*ld_cos_theta2k + ld_cos_theta1r*ld_cos_theta2r - ld_cos_theta1n*ld_cos_theta2n

    ### hadronic-top scenario ###
    elif has_hadronic_top_decay: 
        ### Polarizations coefficients ###
        ##################################
        # top quark decay products
        lb_cos_theta1k = ROOT.TMath.Cos(mRF_hadronic_bottom_quark_dir.Angle(k_antitop))
        lb_cos_theta1r = ROOT.TMath.Cos(mRF_hadronic_bottom_quark_dir.Angle(r_antitop))
        lb_cos_theta1n = ROOT.TMath.Cos(mRF_hadronic_bottom_quark_dir.Angle(n_antitop))
        lb_cos_theta1kStar = ROOT.TMath.Cos(mRF_hadronic_bottom_quark_dir.Angle(kStar_antitop))
        lb_cos_theta1rStar = ROOT.TMath.Cos(mRF_hadronic_bottom_quark_dir.Angle(rStar_antitop))
        ld_cos_theta1k = ROOT.TMath.Cos(mRF_antiDtype_quark_4vec_dir.Angle(k_antitop))
        ld_cos_theta1r = ROOT.TMath.Cos(mRF_antiDtype_quark_4vec_dir.Angle(r_antitop))
        ld_cos_theta1n = ROOT.TMath.Cos(mRF_antiDtype_quark_4vec_dir.Angle(n_antitop))
        ld_cos_theta1kStar = ROOT.TMath.Cos(mRF_antiDtype_quark_4vec_dir.Angle(kStar_antitop))
        ld_cos_theta1rStar = ROOT.TMath.Cos(mRF_antiDtype_quark_4vec_dir.Angle(rStar_antitop))
        # top antiquark decay products
        lb_cos_theta2k = ROOT.TMath.Cos(mRF_lepton_4vec_dir.Angle(k_top))
        lb_cos_theta2r = ROOT.TMath.Cos(mRF_lepton_4vec_dir.Angle(r_top))
        lb_cos_theta2n = ROOT.TMath.Cos(mRF_lepton_4vec_dir.Angle(n_top))
        lb_cos_theta2kStar = ROOT.TMath.Cos(mRF_lepton_4vec_dir.Angle(kStar_top))
        lb_cos_theta2rStar = ROOT.TMath.Cos(mRF_lepton_4vec_dir.Angle(rStar_top))
        ld_cos_theta2k = ROOT.TMath.Cos(mRF_lepton_4vec_dir.Angle(k_top))
        ld_cos_theta2r = ROOT.TMath.Cos(mRF_lepton_4vec_dir.Angle(r_top))
        ld_cos_theta2n = ROOT.TMath.Cos(mRF_lepton_4vec_dir.Angle(n_top))
        ld_cos_theta2kStar = ROOT.TMath.Cos(mRF_lepton_4vec_dir.Angle(kStar_top))
        ld_cos_theta2rStar = ROOT.TMath.Cos(mRF_lepton_4vec_dir.Angle(rStar_top))
        ### Entanglement variables ###
        ##############################
        lb_cHel = ROOT.TMath.Cos(mRF_hadronic_bottom_quark_dir.Angle(mRF_lepton_4vec_dir))
        ld_cHel = ROOT.TMath.Cos(mRF_antiDtype_quark_4vec_dir.Angle(mRF_lepton_4vec_dir))
        lb_cHel_P3n = lb_cos_theta1k*lb_cos_theta2k + lb_cos_theta1r*lb_cos_theta2r - lb_cos_theta1n*lb_cos_theta2n
        ld_cHel_P3n = lb_cos_theta1k*lb_cos_theta2k + lb_cos_theta1r*lb_cos_theta2r - lb_cos_theta1n*lb_cos_theta2n
    ### C_ij coefficients ###
    #########################
    lb_Cnn = lb_cos_theta1n * lb_cos_theta2n
    lb_Cnr = lb_cos_theta1n * lb_cos_theta2r
    lb_Cnk = lb_cos_theta1n * lb_cos_theta2k
    lb_Crn = lb_cos_theta1r * lb_cos_theta2n
    lb_Crr = lb_cos_theta1r * lb_cos_theta2r
    lb_Crk = lb_cos_theta1r * lb_cos_theta2k
    lb_Ckn = lb_cos_theta1k * lb_cos_theta2n
    lb_Ckr = lb_cos_theta1k * lb_cos_theta2r
    lb_Ckk = lb_cos_theta1k * lb_cos_theta2k
    lb_trC = lb_Cnn + lb_Crr + lb_Ckk
    
    ld_Cnn = ld_cos_theta1n * ld_cos_theta2n
    ld_Cnr = ld_cos_theta1n * ld_cos_theta2r
    ld_Cnk = ld_cos_theta1n * ld_cos_theta2k
    ld_Crn = ld_cos_theta1r * ld_cos_theta2n
    ld_Crr = ld_cos_theta1r * ld_cos_theta2r
    ld_Crk = ld_cos_theta1r * ld_cos_theta2k
    ld_Ckn = ld_cos_theta1k * ld_cos_theta2n
    ld_Ckr = ld_cos_theta1k * ld_cos_theta2r
    ld_Ckk = ld_cos_theta1k * ld_cos_theta2k
    ld_trC = ld_Cnn + ld_Crr + ld_Ckk


    ###############################################
    ### Fill histograms in motherTop REST FRAME ###
    ###############################################
    # LEPTON Exclusive polarization variables
    histograms['h_cos_theta1n_antilepton'].Fill(cos_theta1n_antilepton)
    histograms['h_cos_theta1r_antilepton'].Fill(cos_theta1r_antilepton)
    histograms['h_cos_theta1k_antilepton'].Fill(cos_theta1k_antilepton)
    histograms['h_cos_theta1rStar_antilepton'].Fill(cos_theta1rStar_antilepton)
    histograms['h_cos_theta1kStar_antilepton'].Fill(cos_theta1kStar_antilepton)
    histograms['h_cos_theta2n_lepton'].Fill(cos_theta2n_lepton)
    histograms['h_cos_theta2r_lepton'].Fill(cos_theta2r_lepton)
    histograms['h_cos_theta2k_lepton'].Fill(cos_theta2k_lepton)
    histograms['h_cos_theta2rStar_lepton'].Fill(cos_theta2rStar_lepton)
    histograms['h_cos_theta2kStar_lepton'].Fill(cos_theta2kStar_lepton)
    # polarization variables
    histograms['h_lb_cos_theta1n'].Fill(lb_cos_theta1n)
    histograms['h_lb_cos_theta1r'].Fill(lb_cos_theta1r)
    histograms['h_lb_cos_theta1k'].Fill(lb_cos_theta1k)
    histograms['h_lb_cos_theta1rStar'].Fill(lb_cos_theta1rStar)
    histograms['h_lb_cos_theta1kStar'].Fill(lb_cos_theta1kStar)
    histograms['h_lb_cos_theta2n'].Fill(lb_cos_theta2n)
    histograms['h_lb_cos_theta2r'].Fill(lb_cos_theta2r)
    histograms['h_lb_cos_theta2k'].Fill(lb_cos_theta2k)
    histograms['h_lb_cos_theta2rStar'].Fill(lb_cos_theta2rStar)
    histograms['h_lb_cos_theta2kStar'].Fill(lb_cos_theta2kStar)
    
    histograms['h_ld_cos_theta1n'].Fill(ld_cos_theta1n)
    histograms['h_ld_cos_theta1r'].Fill(ld_cos_theta1r)
    histograms['h_ld_cos_theta1k'].Fill(ld_cos_theta1k)
    histograms['h_ld_cos_theta1rStar'].Fill(ld_cos_theta1rStar)
    histograms['h_ld_cos_theta1kStar'].Fill(ld_cos_theta1kStar)
    histograms['h_ld_cos_theta2n'].Fill(ld_cos_theta2n)
    histograms['h_ld_cos_theta2r'].Fill(ld_cos_theta2r)
    histograms['h_ld_cos_theta2k'].Fill(ld_cos_theta2k)
    histograms['h_ld_cos_theta2rStar'].Fill(ld_cos_theta2rStar)    
    histograms['h_ld_cos_theta2kStar'].Fill(ld_cos_theta2kStar)
    # Correlation Matrix elements
    histograms['h_lb_Cnn'].Fill(lb_Cnn)
    histograms['h_lb_Cnr'].Fill(lb_Cnr)
    histograms['h_lb_Cnk'].Fill(lb_Cnk)
    histograms['h_lb_Crn'].Fill(lb_Crn)
    histograms['h_lb_Crr'].Fill(lb_Crr)
    histograms['h_lb_Crk'].Fill(lb_Crk)
    histograms['h_lb_Ckn'].Fill(lb_Ckn)
    histograms['h_lb_Ckr'].Fill(lb_Ckr)
    histograms['h_lb_Ckk'].Fill(lb_Ckk)

    histograms['h_ld_Cnn'].Fill(ld_Cnn)
    histograms['h_ld_Cnr'].Fill(ld_Cnr)
    histograms['h_ld_Cnk'].Fill(ld_Cnk)
    histograms['h_ld_Crn'].Fill(ld_Crn)
    histograms['h_ld_Crr'].Fill(ld_Crr)
    histograms['h_ld_Crk'].Fill(ld_Crk)
    histograms['h_ld_Ckn'].Fill(ld_Ckn)
    histograms['h_ld_Ckr'].Fill(ld_Ckr)
    histograms['h_ld_Ckk'].Fill(ld_Ckk)
    # Entanglement witnesses
    histograms['h_lb_cHel'].Fill(lb_cHel)
    histograms['h_lb_cHel_P3n'].Fill(lb_cHel_P3n)
    histograms['h_lb_trC'].Fill(lb_trC)
    histograms['h_ld_cHel'].Fill(ld_cHel)
    histograms['h_ld_cHel_P3n'].Fill(ld_cHel_P3n)
    histograms['h_ld_trC'].Fill(ld_trC)

    ### mtt [300, 400] GeV ###
    if 300 < m_tt < 400:
        histograms['h_cos_theta1n_antilepton_mtt300to400'].Fill(cos_theta1n_antilepton)
        histograms['h_cos_theta1r_antilepton_mtt300to400'].Fill(cos_theta1r_antilepton)
        histograms['h_cos_theta1k_antilepton_mtt300to400'].Fill(cos_theta1k_antilepton)
        histograms['h_cos_theta1rStar_antilepton_mtt300to400'].Fill(cos_theta1rStar_antilepton)
        histograms['h_cos_theta1kStar_antilepton_mtt300to400'].Fill(cos_theta1kStar_antilepton)
        histograms['h_cos_theta2n_lepton_mtt300to400'].Fill(cos_theta2n_lepton)
        histograms['h_cos_theta2r_lepton_mtt300to400'].Fill(cos_theta2r_lepton)
        histograms['h_cos_theta2k_lepton_mtt300to400'].Fill(cos_theta2k_lepton)
        histograms['h_cos_theta2rStar_lepton_mtt300to400'].Fill(cos_theta2rStar_lepton)
        histograms['h_cos_theta2kStar_lepton_mtt300to400'].Fill(cos_theta2kStar_lepton)
        histograms['h_lb_cos_theta1n_mtt300to400'].Fill(lb_cos_theta1n)
        histograms['h_lb_cos_theta1r_mtt300to400'].Fill(lb_cos_theta1r)
        histograms['h_lb_cos_theta1k_mtt300to400'].Fill(lb_cos_theta1k)
        histograms['h_lb_cos_theta1rStar_mtt300to400'].Fill(lb_cos_theta1rStar)
        histograms['h_lb_cos_theta1kStar_mtt300to400'].Fill(lb_cos_theta1kStar)
        histograms['h_lb_cos_theta2n_mtt300to400'].Fill(lb_cos_theta2n)
        histograms['h_lb_cos_theta2r_mtt300to400'].Fill(lb_cos_theta2r)
        histograms['h_lb_cos_theta2k_mtt300to400'].Fill(lb_cos_theta2k)
        histograms['h_lb_cos_theta2rStar_mtt300to400'].Fill(lb_cos_theta2rStar)
        histograms['h_lb_cos_theta2kStar_mtt300to400'].Fill(lb_cos_theta2kStar)
        histograms['h_lb_Cnn_mtt300to400'].Fill(lb_Cnn)
        histograms['h_lb_Cnr_mtt300to400'].Fill(lb_Cnr)
        histograms['h_lb_Cnk_mtt300to400'].Fill(lb_Cnk)
        histograms['h_lb_Crn_mtt300to400'].Fill(lb_Crn)
        histograms['h_lb_Crr_mtt300to400'].Fill(lb_Crr)
        histograms['h_lb_Crk_mtt300to400'].Fill(lb_Crk)
        histograms['h_lb_Ckn_mtt300to400'].Fill(lb_Ckn)
        histograms['h_lb_Ckr_mtt300to400'].Fill(lb_Ckr)
        histograms['h_lb_Ckk_mtt300to400'].Fill(lb_Ckk)
        histograms['h_lb_trC_mtt300to400'].Fill(lb_trC)
        histograms['h_lb_cHel_mtt300to400'].Fill(lb_cHel)
        histograms['h_lb_cHel_P3n_mtt300to400'].Fill(lb_cHel_P3n)
        histograms['h_ld_cos_theta1n_mtt300to400'].Fill(ld_cos_theta1n)
        histograms['h_ld_cos_theta1r_mtt300to400'].Fill(ld_cos_theta1r)
        histograms['h_ld_cos_theta1k_mtt300to400'].Fill(ld_cos_theta1k)
        histograms['h_ld_cos_theta1rStar_mtt300to400'].Fill(ld_cos_theta1rStar)
        histograms['h_ld_cos_theta1kStar_mtt300to400'].Fill(ld_cos_theta1kStar)
        histograms['h_ld_cos_theta2n_mtt300to400'].Fill(ld_cos_theta2n)
        histograms['h_ld_cos_theta2r_mtt300to400'].Fill(ld_cos_theta2r)
        histograms['h_ld_cos_theta2k_mtt300to400'].Fill(ld_cos_theta2k)
        histograms['h_ld_cos_theta2rStar_mtt300to400'].Fill(ld_cos_theta2rStar)
        histograms['h_ld_cos_theta2kStar_mtt300to400'].Fill(ld_cos_theta2kStar)
        histograms['h_ld_Cnn_mtt300to400'].Fill(ld_Cnn)
        histograms['h_ld_Cnr_mtt300to400'].Fill(ld_Cnr)
        histograms['h_ld_Cnk_mtt300to400'].Fill(ld_Cnk)
        histograms['h_ld_Crn_mtt300to400'].Fill(ld_Crn)
        histograms['h_ld_Crr_mtt300to400'].Fill(ld_Crr)
        histograms['h_ld_Crk_mtt300to400'].Fill(ld_Crk)
        histograms['h_ld_Ckn_mtt300to400'].Fill(ld_Ckn)
        histograms['h_ld_Ckr_mtt300to400'].Fill(ld_Ckr)
        histograms['h_ld_Ckk_mtt300to400'].Fill(ld_Ckk)
        histograms['h_ld_trC_mtt300to400'].Fill(ld_trC)
        histograms['h_ld_cHel_mtt300to400'].Fill(ld_cHel)
        histograms['h_ld_cHel_P3n_mtt300to400'].Fill(ld_cHel_P3n)
        if beta < 0.9:
            histograms['h_cos_theta1n_antilepton_mtt300to400_beta_lt_0p9'].Fill(cos_theta1n_antilepton)
            histograms['h_cos_theta1r_antilepton_mtt300to400_beta_lt_0p9'].Fill(cos_theta1r_antilepton)
            histograms['h_cos_theta1k_antilepton_mtt300to400_beta_lt_0p9'].Fill(cos_theta1k_antilepton)
            histograms['h_cos_theta1rStar_antilepton_mtt300to400_beta_lt_0p9'].Fill(cos_theta1rStar_antilepton)
            histograms['h_cos_theta1kStar_antilepton_mtt300to400_beta_lt_0p9'].Fill(cos_theta1kStar_antilepton)
            histograms['h_cos_theta2n_lepton_mtt300to400_beta_lt_0p9'].Fill(cos_theta2n_lepton)
            histograms['h_cos_theta2r_lepton_mtt300to400_beta_lt_0p9'].Fill(cos_theta2r_lepton)
            histograms['h_cos_theta2k_lepton_mtt300to400_beta_lt_0p9'].Fill(cos_theta2k_lepton)
            histograms['h_cos_theta2rStar_lepton_mtt300to400_beta_lt_0p9'].Fill(cos_theta2rStar_lepton)
            histograms['h_cos_theta2kStar_lepton_mtt300to400_beta_lt_0p9'].Fill(cos_theta2kStar_lepton)
            histograms['h_lb_cos_theta1n_mtt300to400_beta_lt_0p9'].Fill(lb_cos_theta1n)
            histograms['h_lb_cos_theta1r_mtt300to400_beta_lt_0p9'].Fill(lb_cos_theta1r)
            histograms['h_lb_cos_theta1k_mtt300to400_beta_lt_0p9'].Fill(lb_cos_theta1k)
            histograms['h_lb_cos_theta1rStar_mtt300to400_beta_lt_0p9'].Fill(lb_cos_theta1rStar)
            histograms['h_lb_cos_theta1kStar_mtt300to400_beta_lt_0p9'].Fill(lb_cos_theta1kStar)
            histograms['h_lb_cos_theta2n_mtt300to400_beta_lt_0p9'].Fill(lb_cos_theta2n)
            histograms['h_lb_cos_theta2r_mtt300to400_beta_lt_0p9'].Fill(lb_cos_theta2r)
            histograms['h_lb_cos_theta2k_mtt300to400_beta_lt_0p9'].Fill(lb_cos_theta2k)
            histograms['h_lb_cos_theta2rStar_mtt300to400_beta_lt_0p9'].Fill(lb_cos_theta2rStar)
            histograms['h_lb_cos_theta2kStar_mtt300to400_beta_lt_0p9'].Fill(lb_cos_theta2kStar)
            histograms['h_lb_Cnn_mtt300to400_beta_lt_0p9'].Fill(lb_Cnn)
            histograms['h_lb_Cnr_mtt300to400_beta_lt_0p9'].Fill(lb_Cnr)
            histograms['h_lb_Cnk_mtt300to400_beta_lt_0p9'].Fill(lb_Cnk)
            histograms['h_lb_Crn_mtt300to400_beta_lt_0p9'].Fill(lb_Crn)
            histograms['h_lb_Crr_mtt300to400_beta_lt_0p9'].Fill(lb_Crr)
            histograms['h_lb_Crk_mtt300to400_beta_lt_0p9'].Fill(lb_Crk)
            histograms['h_lb_Ckn_mtt300to400_beta_lt_0p9'].Fill(lb_Ckn)
            histograms['h_lb_Ckr_mtt300to400_beta_lt_0p9'].Fill(lb_Ckr)
            histograms['h_lb_Ckk_mtt300to400_beta_lt_0p9'].Fill(lb_Ckk)
            histograms['h_lb_trC_mtt300to400_beta_lt_0p9'].Fill(lb_trC)
            histograms['h_lb_cHel_mtt300to400_beta_lt_0p9'].Fill(lb_cHel)
            histograms['h_lb_cHel_P3n_mtt300to400_beta_lt_0p9'].Fill(lb_cHel_P3n)
            histograms['h_ld_cos_theta1n_mtt300to400_beta_lt_0p9'].Fill(ld_cos_theta1n)
            histograms['h_ld_cos_theta1r_mtt300to400_beta_lt_0p9'].Fill(ld_cos_theta1r)
            histograms['h_ld_cos_theta1k_mtt300to400_beta_lt_0p9'].Fill(ld_cos_theta1k)
            histograms['h_ld_cos_theta1rStar_mtt300to400_beta_lt_0p9'].Fill(ld_cos_theta1rStar)
            histograms['h_ld_cos_theta1kStar_mtt300to400_beta_lt_0p9'].Fill(ld_cos_theta1kStar)
            histograms['h_ld_cos_theta2n_mtt300to400_beta_lt_0p9'].Fill(ld_cos_theta2n)
            histograms['h_ld_cos_theta2r_mtt300to400_beta_lt_0p9'].Fill(ld_cos_theta2r)
            histograms['h_ld_cos_theta2k_mtt300to400_beta_lt_0p9'].Fill(ld_cos_theta2k)
            histograms['h_ld_cos_theta2rStar_mtt300to400_beta_lt_0p9'].Fill(ld_cos_theta2rStar)
            histograms['h_ld_cos_theta2kStar_mtt300to400_beta_lt_0p9'].Fill(ld_cos_theta2kStar)
            histograms['h_ld_Cnn_mtt300to400_beta_lt_0p9'].Fill(ld_Cnn)
            histograms['h_ld_Cnr_mtt300to400_beta_lt_0p9'].Fill(ld_Cnr)
            histograms['h_ld_Cnk_mtt300to400_beta_lt_0p9'].Fill(ld_Cnk)
            histograms['h_ld_Crn_mtt300to400_beta_lt_0p9'].Fill(ld_Crn)
            histograms['h_ld_Crr_mtt300to400_beta_lt_0p9'].Fill(ld_Crr)
            histograms['h_ld_Crk_mtt300to400_beta_lt_0p9'].Fill(ld_Crk)
            histograms['h_ld_Ckn_mtt300to400_beta_lt_0p9'].Fill(ld_Ckn)
            histograms['h_ld_Ckr_mtt300to400_beta_lt_0p9'].Fill(ld_Ckr)
            histograms['h_ld_Ckk_mtt300to400_beta_lt_0p9'].Fill(ld_Ckk)
            histograms['h_ld_trC_mtt300to400_beta_lt_0p9'].Fill(ld_trC)
            histograms['h_ld_cHel_mtt300to400_beta_lt_0p9'].Fill(ld_cHel)
            histograms['h_ld_cHel_P3n_mtt300to400_beta_lt_0p9'].Fill(ld_cHel_P3n)
        if abs(cosTSA) < 0.4:
            histograms['h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p4'].Fill(cos_theta1n_antilepton)
            histograms['h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p4'].Fill(cos_theta1r_antilepton)
            histograms['h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p4'].Fill(cos_theta1k_antilepton)
            histograms['h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p4'].Fill(cos_theta1rStar_antilepton)
            histograms['h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p4'].Fill(cos_theta1kStar_antilepton)
            histograms['h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p4'].Fill(cos_theta2n_lepton)
            histograms['h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p4'].Fill(cos_theta2r_lepton)
            histograms['h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p4'].Fill(cos_theta2k_lepton)
            histograms['h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p4'].Fill(cos_theta2rStar_lepton)
            histograms['h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p4'].Fill(cos_theta2kStar_lepton)
            histograms['h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p4'].Fill(lb_cos_theta1n)
            histograms['h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p4'].Fill(lb_cos_theta1r)
            histograms['h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p4'].Fill(lb_cos_theta1k)
            histograms['h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4'].Fill(lb_cos_theta1rStar)
            histograms['h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4'].Fill(lb_cos_theta1kStar)
            histograms['h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p4'].Fill(lb_cos_theta2n)
            histograms['h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p4'].Fill(lb_cos_theta2r)
            histograms['h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p4'].Fill(lb_cos_theta2k)
            histograms['h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4'].Fill(lb_cos_theta2rStar)
            histograms['h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4'].Fill(lb_cos_theta2kStar)
            histograms['h_lb_Cnn_mtt300to400_cosTSA_lt_0p4'].Fill(lb_Cnn)
            histograms['h_lb_Cnr_mtt300to400_cosTSA_lt_0p4'].Fill(lb_Cnr)
            histograms['h_lb_Cnk_mtt300to400_cosTSA_lt_0p4'].Fill(lb_Cnk)
            histograms['h_lb_Crn_mtt300to400_cosTSA_lt_0p4'].Fill(lb_Crn)
            histograms['h_lb_Crr_mtt300to400_cosTSA_lt_0p4'].Fill(lb_Crr)
            histograms['h_lb_Crk_mtt300to400_cosTSA_lt_0p4'].Fill(lb_Crk)
            histograms['h_lb_Ckn_mtt300to400_cosTSA_lt_0p4'].Fill(lb_Ckn)
            histograms['h_lb_Ckr_mtt300to400_cosTSA_lt_0p4'].Fill(lb_Ckr)
            histograms['h_lb_Ckk_mtt300to400_cosTSA_lt_0p4'].Fill(lb_Ckk)
            histograms['h_lb_trC_mtt300to400_cosTSA_lt_0p4'].Fill(lb_trC)
            histograms['h_lb_cHel_mtt300to400_cosTSA_lt_0p4'].Fill(lb_cHel)
            histograms['h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p4'].Fill(lb_cHel_P3n)
            histograms['h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p4'].Fill(ld_cos_theta1n)
            histograms['h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p4'].Fill(ld_cos_theta1r)
            histograms['h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p4'].Fill(ld_cos_theta1k)
            histograms['h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4'].Fill(ld_cos_theta1rStar)
            histograms['h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4'].Fill(ld_cos_theta1kStar)
            histograms['h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p4'].Fill(ld_cos_theta2n)
            histograms['h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p4'].Fill(ld_cos_theta2r)
            histograms['h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p4'].Fill(ld_cos_theta2k)
            histograms['h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4'].Fill(ld_cos_theta2rStar)
            histograms['h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4'].Fill(ld_cos_theta2kStar)
            histograms['h_ld_Cnn_mtt300to400_cosTSA_lt_0p4'].Fill(ld_Cnn)
            histograms['h_ld_Cnr_mtt300to400_cosTSA_lt_0p4'].Fill(ld_Cnr)
            histograms['h_ld_Cnk_mtt300to400_cosTSA_lt_0p4'].Fill(ld_Cnk)
            histograms['h_ld_Crn_mtt300to400_cosTSA_lt_0p4'].Fill(ld_Crn)
            histograms['h_ld_Crr_mtt300to400_cosTSA_lt_0p4'].Fill(ld_Crr)
            histograms['h_ld_Crk_mtt300to400_cosTSA_lt_0p4'].Fill(ld_Crk)
            histograms['h_ld_Ckn_mtt300to400_cosTSA_lt_0p4'].Fill(ld_Ckn)
            histograms['h_ld_Ckr_mtt300to400_cosTSA_lt_0p4'].Fill(ld_Ckr)
            histograms['h_ld_Ckk_mtt300to400_cosTSA_lt_0p4'].Fill(ld_Ckk)
            histograms['h_ld_trC_mtt300to400_cosTSA_lt_0p4'].Fill(ld_trC)
            histograms['h_ld_cHel_mtt300to400_cosTSA_lt_0p4'].Fill(ld_cHel)
            histograms['h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p4'].Fill(ld_cHel_P3n)
            if beta < 0.9:
                histograms['h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(cos_theta1n_antilepton)
                histograms['h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(cos_theta1r_antilepton)
                histograms['h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(cos_theta1k_antilepton)
                histograms['h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(cos_theta1rStar_antilepton)
                histograms['h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(cos_theta1kStar_antilepton)
                histograms['h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(cos_theta2n_lepton)
                histograms['h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(cos_theta2r_lepton)
                histograms['h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(cos_theta2k_lepton)
                histograms['h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(cos_theta2rStar_lepton)
                histograms['h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(cos_theta2kStar_lepton)
                histograms['h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_cos_theta1n)
                histograms['h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_cos_theta1r)
                histograms['h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_cos_theta1k)
                histograms['h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_cos_theta1rStar)
                histograms['h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_cos_theta1kStar)
                histograms['h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_cos_theta2n)
                histograms['h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_cos_theta2r)
                histograms['h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_cos_theta2k)
                histograms['h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_cos_theta2rStar)
                histograms['h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_cos_theta2kStar)
                histograms['h_lb_Cnn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_Cnn)
                histograms['h_lb_Cnr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_Cnr)
                histograms['h_lb_Cnk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_Cnk)
                histograms['h_lb_Crn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_Crn)
                histograms['h_lb_Crr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_Crr)
                histograms['h_lb_Crk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_Crk)
                histograms['h_lb_Ckn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_Ckn)
                histograms['h_lb_Ckr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_Ckr)
                histograms['h_lb_Ckk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_Ckk)
                histograms['h_lb_trC_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_trC)
                histograms['h_lb_cHel_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_cHel)
                histograms['h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(lb_cHel_P3n)
                histograms['h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_cos_theta1n)
                histograms['h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_cos_theta1r)
                histograms['h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_cos_theta1k)
                histograms['h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_cos_theta1rStar)
                histograms['h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_cos_theta1kStar)
                histograms['h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_cos_theta2n)
                histograms['h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_cos_theta2r)
                histograms['h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_cos_theta2k)
                histograms['h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_cos_theta2rStar)
                histograms['h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_cos_theta2kStar)
                histograms['h_ld_Cnn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_Cnn)
                histograms['h_ld_Cnr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_Cnr)
                histograms['h_ld_Cnk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_Cnk)
                histograms['h_ld_Crn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_Crn)
                histograms['h_ld_Crr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_Crr)
                histograms['h_ld_Crk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_Crk)
                histograms['h_ld_Ckn_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_Ckn)
                histograms['h_ld_Ckr_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_Ckr)
                histograms['h_ld_Ckk_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_Ckk)
                histograms['h_ld_trC_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_trC)
                histograms['h_ld_cHel_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_cHel)
                histograms['h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p4_beta_lt_0p9'].Fill(ld_cHel_P3n)
        elif abs(cosTSA) < 0.7:
            histograms['h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p7'].Fill(cos_theta1n_antilepton)
            histograms['h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p7'].Fill(cos_theta1r_antilepton)
            histograms['h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p7'].Fill(cos_theta1k_antilepton)
            histograms['h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p7'].Fill(cos_theta1rStar_antilepton)
            histograms['h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p7'].Fill(cos_theta1kStar_antilepton)
            histograms['h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p7'].Fill(cos_theta2n_lepton)
            histograms['h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p7'].Fill(cos_theta2r_lepton)
            histograms['h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p7'].Fill(cos_theta2k_lepton)
            histograms['h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p7'].Fill(cos_theta2rStar_lepton)
            histograms['h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p7'].Fill(cos_theta2kStar_lepton)
            histograms['h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p7'].Fill(lb_cos_theta1n)
            histograms['h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p7'].Fill(lb_cos_theta1r)
            histograms['h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p7'].Fill(lb_cos_theta1k)
            histograms['h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7'].Fill(lb_cos_theta1rStar)
            histograms['h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7'].Fill(lb_cos_theta1kStar)
            histograms['h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p7'].Fill(lb_cos_theta2n)
            histograms['h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p7'].Fill(lb_cos_theta2r)
            histograms['h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p7'].Fill(lb_cos_theta2k)
            histograms['h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7'].Fill(lb_cos_theta2rStar)
            histograms['h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7'].Fill(lb_cos_theta2kStar)
            histograms['h_lb_Cnn_mtt300to400_cosTSA_lt_0p7'].Fill(lb_Cnn)
            histograms['h_lb_Cnr_mtt300to400_cosTSA_lt_0p7'].Fill(lb_Cnr)
            histograms['h_lb_Cnk_mtt300to400_cosTSA_lt_0p7'].Fill(lb_Cnk)
            histograms['h_lb_Crn_mtt300to400_cosTSA_lt_0p7'].Fill(lb_Crn)
            histograms['h_lb_Crr_mtt300to400_cosTSA_lt_0p7'].Fill(lb_Crr)
            histograms['h_lb_Crk_mtt300to400_cosTSA_lt_0p7'].Fill(lb_Crk)
            histograms['h_lb_Ckn_mtt300to400_cosTSA_lt_0p7'].Fill(lb_Ckn)
            histograms['h_lb_Ckr_mtt300to400_cosTSA_lt_0p7'].Fill(lb_Ckr)
            histograms['h_lb_Ckk_mtt300to400_cosTSA_lt_0p7'].Fill(lb_Ckk)
            histograms['h_lb_trC_mtt300to400_cosTSA_lt_0p7'].Fill(lb_trC)
            histograms['h_lb_cHel_mtt300to400_cosTSA_lt_0p7'].Fill(lb_cHel)
            histograms['h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p7'].Fill(lb_cHel_P3n)
            histograms['h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p7'].Fill(ld_cos_theta1n)
            histograms['h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p7'].Fill(ld_cos_theta1r)
            histograms['h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p7'].Fill(ld_cos_theta1k)
            histograms['h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7'].Fill(ld_cos_theta1rStar)
            histograms['h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7'].Fill(ld_cos_theta1kStar)
            histograms['h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p7'].Fill(ld_cos_theta2n)
            histograms['h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p7'].Fill(ld_cos_theta2r)
            histograms['h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p7'].Fill(ld_cos_theta2k)
            histograms['h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7'].Fill(ld_cos_theta2rStar)
            histograms['h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7'].Fill(ld_cos_theta2kStar)
            histograms['h_ld_Cnn_mtt300to400_cosTSA_lt_0p7'].Fill(ld_Cnn)
            histograms['h_ld_Cnr_mtt300to400_cosTSA_lt_0p7'].Fill(ld_Cnr)
            histograms['h_ld_Cnk_mtt300to400_cosTSA_lt_0p7'].Fill(ld_Cnk)
            histograms['h_ld_Crn_mtt300to400_cosTSA_lt_0p7'].Fill(ld_Crn)
            histograms['h_ld_Crr_mtt300to400_cosTSA_lt_0p7'].Fill(ld_Crr)
            histograms['h_ld_Crk_mtt300to400_cosTSA_lt_0p7'].Fill(ld_Crk)
            histograms['h_ld_Ckn_mtt300to400_cosTSA_lt_0p7'].Fill(ld_Ckn)
            histograms['h_ld_Ckr_mtt300to400_cosTSA_lt_0p7'].Fill(ld_Ckr)
            histograms['h_ld_Ckk_mtt300to400_cosTSA_lt_0p7'].Fill(ld_Ckk)
            histograms['h_ld_trC_mtt300to400_cosTSA_lt_0p7'].Fill(ld_trC)
            histograms['h_ld_cHel_mtt300to400_cosTSA_lt_0p7'].Fill(ld_cHel)
            histograms['h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p7'].Fill(ld_cHel_P3n)
            if beta < 0.9:
                histograms['h_cos_theta1n_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(cos_theta1n_antilepton)
                histograms['h_cos_theta1r_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(cos_theta1r_antilepton)
                histograms['h_cos_theta1k_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(cos_theta1k_antilepton)
                histograms['h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(cos_theta1rStar_antilepton)
                histograms['h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(cos_theta1kStar_antilepton)
                histograms['h_cos_theta2n_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(cos_theta2n_lepton)
                histograms['h_cos_theta2r_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(cos_theta2r_lepton)
                histograms['h_cos_theta2k_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(cos_theta2k_lepton)
                histograms['h_cos_theta2rStar_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(cos_theta2rStar_lepton)
                histograms['h_cos_theta2kStar_lepton_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(cos_theta2kStar_lepton)
                histograms['h_lb_cos_theta1n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_cos_theta1n)
                histograms['h_lb_cos_theta1r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_cos_theta1r)
                histograms['h_lb_cos_theta1k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_cos_theta1k)
                histograms['h_lb_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_cos_theta1rStar)
                histograms['h_lb_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_cos_theta1kStar)
                histograms['h_lb_cos_theta2n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_cos_theta2n)
                histograms['h_lb_cos_theta2r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_cos_theta2r)
                histograms['h_lb_cos_theta2k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_cos_theta2k)
                histograms['h_lb_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_cos_theta2rStar)
                histograms['h_lb_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_cos_theta2kStar)
                histograms['h_lb_Cnn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_Cnn)
                histograms['h_lb_Cnr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_Cnr)
                histograms['h_lb_Cnk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_Cnk)
                histograms['h_lb_Crn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_Crn)
                histograms['h_lb_Crr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_Crr)
                histograms['h_lb_Crk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_Crk)
                histograms['h_lb_Ckn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_Ckn)
                histograms['h_lb_Ckr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_Ckr)
                histograms['h_lb_Ckk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_Ckk)
                histograms['h_lb_trC_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_trC)
                histograms['h_lb_cHel_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_cHel)
                histograms['h_lb_cHel_P3n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(lb_cHel_P3n)
                histograms['h_ld_cos_theta1n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_cos_theta1n)
                histograms['h_ld_cos_theta1r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_cos_theta1r)
                histograms['h_ld_cos_theta1k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_cos_theta1k)
                histograms['h_ld_cos_theta1rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_cos_theta1rStar)
                histograms['h_ld_cos_theta1kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_cos_theta1kStar)
                histograms['h_ld_cos_theta2n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_cos_theta2n)
                histograms['h_ld_cos_theta2r_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_cos_theta2r)
                histograms['h_ld_cos_theta2k_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_cos_theta2k)
                histograms['h_ld_cos_theta2rStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_cos_theta2rStar)
                histograms['h_ld_cos_theta2kStar_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_cos_theta2kStar)
                histograms['h_ld_Cnn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_Cnn)
                histograms['h_ld_Cnr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_Cnr)
                histograms['h_ld_Cnk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_Cnk)
                histograms['h_ld_Crn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_Crn)
                histograms['h_ld_Crr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_Crr)
                histograms['h_ld_Crk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_Crk)
                histograms['h_ld_Ckn_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_Ckn)
                histograms['h_ld_Ckr_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_Ckr)
                histograms['h_ld_Ckk_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_Ckk)
                histograms['h_ld_trC_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_trC)
                histograms['h_ld_cHel_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_cHel)
                histograms['h_ld_cHel_P3n_mtt300to400_cosTSA_lt_0p7_beta_lt_0p9'].Fill(ld_cHel_P3n)
        elif abs(cosTSA) > 0.7:
            histograms['h_cos_theta1n_antilepton_mtt300to400_cosTSA_gt_0p7'].Fill(cos_theta1n_antilepton)
            histograms['h_cos_theta1r_antilepton_mtt300to400_cosTSA_gt_0p7'].Fill(cos_theta1r_antilepton)
            histograms['h_cos_theta1k_antilepton_mtt300to400_cosTSA_gt_0p7'].Fill(cos_theta1k_antilepton)
            histograms['h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_gt_0p7'].Fill(cos_theta1rStar_antilepton)
            histograms['h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_gt_0p7'].Fill(cos_theta1kStar_antilepton)
            histograms['h_cos_theta2n_lepton_mtt300to400_cosTSA_gt_0p7'].Fill(cos_theta2n_lepton)
            histograms['h_cos_theta2r_lepton_mtt300to400_cosTSA_gt_0p7'].Fill(cos_theta2r_lepton)
            histograms['h_cos_theta2k_lepton_mtt300to400_cosTSA_gt_0p7'].Fill(cos_theta2k_lepton)
            histograms['h_cos_theta2rStar_lepton_mtt300to400_cosTSA_gt_0p7'].Fill(cos_theta2rStar_lepton)
            histograms['h_cos_theta2kStar_lepton_mtt300to400_cosTSA_gt_0p7'].Fill(cos_theta2kStar_lepton)
            histograms['h_lb_cos_theta1n_mtt300to400_cosTSA_gt_0p7'].Fill(lb_cos_theta1n)
            histograms['h_lb_cos_theta1r_mtt300to400_cosTSA_gt_0p7'].Fill(lb_cos_theta1r)
            histograms['h_lb_cos_theta1k_mtt300to400_cosTSA_gt_0p7'].Fill(lb_cos_theta1k)
            histograms['h_lb_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7'].Fill(lb_cos_theta1rStar)
            histograms['h_lb_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7'].Fill(lb_cos_theta1kStar)
            histograms['h_lb_cos_theta2n_mtt300to400_cosTSA_gt_0p7'].Fill(lb_cos_theta2n)
            histograms['h_lb_cos_theta2r_mtt300to400_cosTSA_gt_0p7'].Fill(lb_cos_theta2r)
            histograms['h_lb_cos_theta2k_mtt300to400_cosTSA_gt_0p7'].Fill(lb_cos_theta2k)
            histograms['h_lb_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7'].Fill(lb_cos_theta2rStar)
            histograms['h_lb_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7'].Fill(lb_cos_theta2kStar)
            histograms['h_lb_Cnn_mtt300to400_cosTSA_gt_0p7'].Fill(lb_Cnn)
            histograms['h_lb_Cnr_mtt300to400_cosTSA_gt_0p7'].Fill(lb_Cnr)
            histograms['h_lb_Cnk_mtt300to400_cosTSA_gt_0p7'].Fill(lb_Cnk)
            histograms['h_lb_Crn_mtt300to400_cosTSA_gt_0p7'].Fill(lb_Crn)
            histograms['h_lb_Crr_mtt300to400_cosTSA_gt_0p7'].Fill(lb_Crr)
            histograms['h_lb_Crk_mtt300to400_cosTSA_gt_0p7'].Fill(lb_Crk)
            histograms['h_lb_Ckn_mtt300to400_cosTSA_gt_0p7'].Fill(lb_Ckn)
            histograms['h_lb_Ckr_mtt300to400_cosTSA_gt_0p7'].Fill(lb_Ckr)
            histograms['h_lb_Ckk_mtt300to400_cosTSA_gt_0p7'].Fill(lb_Ckk)
            histograms['h_lb_trC_mtt300to400_cosTSA_gt_0p7'].Fill(lb_trC)
            histograms['h_lb_cHel_mtt300to400_cosTSA_gt_0p7'].Fill(lb_cHel)
            histograms['h_lb_cHel_P3n_mtt300to400_cosTSA_gt_0p7'].Fill(lb_cHel_P3n)
            histograms['h_ld_cos_theta1n_mtt300to400_cosTSA_gt_0p7'].Fill(ld_cos_theta1n)
            histograms['h_ld_cos_theta1r_mtt300to400_cosTSA_gt_0p7'].Fill(ld_cos_theta1r)
            histograms['h_ld_cos_theta1k_mtt300to400_cosTSA_gt_0p7'].Fill(ld_cos_theta1k)
            histograms['h_ld_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7'].Fill(ld_cos_theta1rStar)
            histograms['h_ld_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7'].Fill(ld_cos_theta1kStar)
            histograms['h_ld_cos_theta2n_mtt300to400_cosTSA_gt_0p7'].Fill(ld_cos_theta2n)
            histograms['h_ld_cos_theta2r_mtt300to400_cosTSA_gt_0p7'].Fill(ld_cos_theta2r)
            histograms['h_ld_cos_theta2k_mtt300to400_cosTSA_gt_0p7'].Fill(ld_cos_theta2k)
            histograms['h_ld_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7'].Fill(ld_cos_theta2rStar)
            histograms['h_ld_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7'].Fill(ld_cos_theta2kStar)
            histograms['h_ld_Cnn_mtt300to400_cosTSA_gt_0p7'].Fill(ld_Cnn)
            histograms['h_ld_Cnr_mtt300to400_cosTSA_gt_0p7'].Fill(ld_Cnr)
            histograms['h_ld_Cnk_mtt300to400_cosTSA_gt_0p7'].Fill(ld_Cnk)
            histograms['h_ld_Crn_mtt300to400_cosTSA_gt_0p7'].Fill(ld_Crn)
            histograms['h_ld_Crr_mtt300to400_cosTSA_gt_0p7'].Fill(ld_Crr)
            histograms['h_ld_Crk_mtt300to400_cosTSA_gt_0p7'].Fill(ld_Crk)
            histograms['h_ld_Ckn_mtt300to400_cosTSA_gt_0p7'].Fill(ld_Ckn)
            histograms['h_ld_Ckr_mtt300to400_cosTSA_gt_0p7'].Fill(ld_Ckr)
            histograms['h_ld_Ckk_mtt300to400_cosTSA_gt_0p7'].Fill(ld_Ckk)
            histograms['h_ld_trC_mtt300to400_cosTSA_gt_0p7'].Fill(ld_trC)
            histograms['h_ld_cHel_mtt300to400_cosTSA_gt_0p7'].Fill(ld_cHel)
            histograms['h_ld_cHel_P3n_mtt300to400_cosTSA_gt_0p7'].Fill(ld_cHel_P3n)
            if beta < 0.9:
                histograms['h_cos_theta1n_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(cos_theta1n_antilepton)
                histograms['h_cos_theta1r_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(cos_theta1r_antilepton)
                histograms['h_cos_theta1k_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(cos_theta1k_antilepton)
                histograms['h_cos_theta1rStar_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(cos_theta1rStar_antilepton)
                histograms['h_cos_theta1kStar_antilepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(cos_theta1kStar_antilepton)
                histograms['h_cos_theta2n_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(cos_theta2n_lepton)
                histograms['h_cos_theta2r_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(cos_theta2r_lepton)
                histograms['h_cos_theta2k_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(cos_theta2k_lepton)
                histograms['h_cos_theta2rStar_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(cos_theta2rStar_lepton)
                histograms['h_cos_theta2kStar_lepton_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(cos_theta2kStar_lepton)
                histograms['h_lb_cos_theta1n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_cos_theta1n)
                histograms['h_lb_cos_theta1r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_cos_theta1r)
                histograms['h_lb_cos_theta1k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_cos_theta1k)
                histograms['h_lb_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_cos_theta1rStar)
                histograms['h_lb_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_cos_theta1kStar)
                histograms['h_lb_cos_theta2n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_cos_theta2n)
                histograms['h_lb_cos_theta2r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_cos_theta2r)
                histograms['h_lb_cos_theta2k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_cos_theta2k)
                histograms['h_lb_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_cos_theta2rStar)
                histograms['h_lb_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_cos_theta2kStar)
                histograms['h_lb_Cnn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_Cnn)
                histograms['h_lb_Cnr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_Cnr)
                histograms['h_lb_Cnk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_Cnk)
                histograms['h_lb_Crn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_Crn)
                histograms['h_lb_Crr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_Crr)
                histograms['h_lb_Crk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_Crk)
                histograms['h_lb_Ckn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_Ckn)
                histograms['h_lb_Ckr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_Ckr)
                histograms['h_lb_Ckk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_Ckk)
                histograms['h_lb_trC_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_trC)
                histograms['h_lb_cHel_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_cHel)
                histograms['h_lb_cHel_P3n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(lb_cHel_P3n)
                histograms['h_ld_cos_theta1n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_cos_theta1n)
                histograms['h_ld_cos_theta1r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_cos_theta1r)
                histograms['h_ld_cos_theta1k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_cos_theta1k)
                histograms['h_ld_cos_theta1rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_cos_theta1rStar)
                histograms['h_ld_cos_theta1kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_cos_theta1kStar)
                histograms['h_ld_cos_theta2n_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_cos_theta2n)
                histograms['h_ld_cos_theta2r_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_cos_theta2r)
                histograms['h_ld_cos_theta2k_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_cos_theta2k)
                histograms['h_ld_cos_theta2rStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_cos_theta2rStar)
                histograms['h_ld_cos_theta2kStar_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_cos_theta2kStar)
                histograms['h_ld_Cnn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_Cnn)
                histograms['h_ld_Cnr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_Cnr)
                histograms['h_ld_Cnk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_Cnk)
                histograms['h_ld_Crn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_Crn)
                histograms['h_ld_Crr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_Crr)
                histograms['h_ld_Crk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_Crk)
                histograms['h_ld_Ckn_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_Ckn)
                histograms['h_ld_Ckr_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_Ckr)
                histograms['h_ld_Ckk_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_Ckk)
                histograms['h_ld_trC_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_trC)
                histograms['h_ld_cHel_mtt300to400_cosTSA_gt_0p7_beta_lt_0p9'].Fill(ld_cHel)
    elif 400 < m_tt < 600:
        histograms['h_cos_theta1n_antilepton_mtt400to600'].Fill(cos_theta1n_antilepton)
        histograms['h_cos_theta1r_antilepton_mtt400to600'].Fill(cos_theta1r_antilepton)
        histograms['h_cos_theta1k_antilepton_mtt400to600'].Fill(cos_theta1k_antilepton)
        histograms['h_cos_theta1rStar_antilepton_mtt400to600'].Fill(cos_theta1rStar_antilepton)
        histograms['h_cos_theta1kStar_antilepton_mtt400to600'].Fill(cos_theta1kStar_antilepton)
        histograms['h_cos_theta2n_lepton_mtt400to600'].Fill(cos_theta2n_lepton)
        histograms['h_cos_theta2r_lepton_mtt400to600'].Fill(cos_theta2r_lepton)
        histograms['h_cos_theta2k_lepton_mtt400to600'].Fill(cos_theta2k_lepton)
        histograms['h_cos_theta2rStar_lepton_mtt400to600'].Fill(cos_theta2rStar_lepton)
        histograms['h_cos_theta2kStar_lepton_mtt400to600'].Fill(cos_theta2kStar_lepton)
        histograms['h_lb_cos_theta1n_mtt400to600'].Fill(lb_cos_theta1n)
        histograms['h_lb_cos_theta1r_mtt400to600'].Fill(lb_cos_theta1r)
        histograms['h_lb_cos_theta1k_mtt400to600'].Fill(lb_cos_theta1k)
        histograms['h_lb_cos_theta1rStar_mtt400to600'].Fill(lb_cos_theta1rStar)
        histograms['h_lb_cos_theta1kStar_mtt400to600'].Fill(lb_cos_theta1kStar)
        histograms['h_lb_cos_theta2n_mtt400to600'].Fill(lb_cos_theta2n)
        histograms['h_lb_cos_theta2r_mtt400to600'].Fill(lb_cos_theta2r)
        histograms['h_lb_cos_theta2k_mtt400to600'].Fill(lb_cos_theta2k)
        histograms['h_lb_cos_theta2rStar_mtt400to600'].Fill(lb_cos_theta2rStar)
        histograms['h_lb_cos_theta2kStar_mtt400to600'].Fill(lb_cos_theta2kStar)
        histograms['h_lb_Cnn_mtt400to600'].Fill(lb_Cnn)
        histograms['h_lb_Cnr_mtt400to600'].Fill(lb_Cnr)
        histograms['h_lb_Cnk_mtt400to600'].Fill(lb_Cnk)
        histograms['h_lb_Crn_mtt400to600'].Fill(lb_Crn)
        histograms['h_lb_Crr_mtt400to600'].Fill(lb_Crr)
        histograms['h_lb_Crk_mtt400to600'].Fill(lb_Crk)
        histograms['h_lb_Ckn_mtt400to600'].Fill(lb_Ckn)
        histograms['h_lb_Ckr_mtt400to600'].Fill(lb_Ckr)
        histograms['h_lb_Ckk_mtt400to600'].Fill(lb_Ckk)
        histograms['h_lb_trC_mtt400to600'].Fill(lb_trC)
        histograms['h_lb_cHel_mtt400to600'].Fill(lb_cHel)
        histograms['h_lb_cHel_P3n_mtt400to600'].Fill(lb_cHel_P3n)
        histograms['h_ld_cos_theta1n_mtt400to600'].Fill(ld_cos_theta1n)
        histograms['h_ld_cos_theta1r_mtt400to600'].Fill(ld_cos_theta1r)
        histograms['h_ld_cos_theta1k_mtt400to600'].Fill(ld_cos_theta1k)
        histograms['h_ld_cos_theta1rStar_mtt400to600'].Fill(ld_cos_theta1rStar)
        histograms['h_ld_cos_theta1kStar_mtt400to600'].Fill(ld_cos_theta1kStar)
        histograms['h_ld_cos_theta2n_mtt400to600'].Fill(ld_cos_theta2n)
        histograms['h_ld_cos_theta2r_mtt400to600'].Fill(ld_cos_theta2r)
        histograms['h_ld_cos_theta2k_mtt400to600'].Fill(ld_cos_theta2k)
        histograms['h_ld_cos_theta2rStar_mtt400to600'].Fill(ld_cos_theta2rStar)
        histograms['h_ld_cos_theta2kStar_mtt400to600'].Fill(ld_cos_theta2kStar)
        histograms['h_ld_Cnn_mtt400to600'].Fill(ld_Cnn)
        histograms['h_ld_Cnr_mtt400to600'].Fill(ld_Cnr)
        histograms['h_ld_Cnk_mtt400to600'].Fill(ld_Cnk)
        histograms['h_ld_Crn_mtt400to600'].Fill(ld_Crn)
        histograms['h_ld_Crr_mtt400to600'].Fill(ld_Crr)
        histograms['h_ld_Crk_mtt400to600'].Fill(ld_Crk)
        histograms['h_ld_Ckn_mtt400to600'].Fill(ld_Ckn)
        histograms['h_ld_Ckr_mtt400to600'].Fill(ld_Ckr)
        histograms['h_ld_Ckk_mtt400to600'].Fill(ld_Ckk)
        histograms['h_ld_trC_mtt400to600'].Fill(ld_trC)
        histograms['h_ld_cHel_mtt400to600'].Fill(ld_cHel)
        histograms['h_ld_cHel_P3n_mtt400to600'].Fill(ld_cHel_P3n)
        if abs(cosTSA) < 0.4:
            histograms['h_cos_theta1n_antilepton_mtt400to600_cosTSA_lt_0p4'].Fill(cos_theta1n_antilepton)
            histograms['h_cos_theta1r_antilepton_mtt400to600_cosTSA_lt_0p4'].Fill(cos_theta1r_antilepton)
            histograms['h_cos_theta1k_antilepton_mtt400to600_cosTSA_lt_0p4'].Fill(cos_theta1k_antilepton)
            histograms['h_cos_theta1rStar_antilepton_mtt400to600_cosTSA_lt_0p4'].Fill(cos_theta1rStar_antilepton)
            histograms['h_cos_theta1kStar_antilepton_mtt400to600_cosTSA_lt_0p4'].Fill(cos_theta1kStar_antilepton)
            histograms['h_cos_theta2n_lepton_mtt400to600_cosTSA_lt_0p4'].Fill(cos_theta2n_lepton)
            histograms['h_cos_theta2r_lepton_mtt400to600_cosTSA_lt_0p4'].Fill(cos_theta2r_lepton)
            histograms['h_cos_theta2k_lepton_mtt400to600_cosTSA_lt_0p4'].Fill(cos_theta2k_lepton)
            histograms['h_cos_theta2rStar_lepton_mtt400to600_cosTSA_lt_0p4'].Fill(cos_theta2rStar_lepton)
            histograms['h_cos_theta2kStar_lepton_mtt400to600_cosTSA_lt_0p4'].Fill(cos_theta2kStar_lepton)
            histograms['h_lb_cos_theta1n_mtt400to600_cosTSA_lt_0p4'].Fill(lb_cos_theta1n)
            histograms['h_lb_cos_theta1r_mtt400to600_cosTSA_lt_0p4'].Fill(lb_cos_theta1r)
            histograms['h_lb_cos_theta1k_mtt400to600_cosTSA_lt_0p4'].Fill(lb_cos_theta1k)
            histograms['h_lb_cos_theta1rStar_mtt400to600_cosTSA_lt_0p4'].Fill(lb_cos_theta1rStar)
            histograms['h_lb_cos_theta1kStar_mtt400to600_cosTSA_lt_0p4'].Fill(lb_cos_theta1kStar)
            histograms['h_lb_cos_theta2n_mtt400to600_cosTSA_lt_0p4'].Fill(lb_cos_theta2n)
            histograms['h_lb_cos_theta2r_mtt400to600_cosTSA_lt_0p4'].Fill(lb_cos_theta2r)
            histograms['h_lb_cos_theta2k_mtt400to600_cosTSA_lt_0p4'].Fill(lb_cos_theta2k)
            histograms['h_lb_cos_theta2rStar_mtt400to600_cosTSA_lt_0p4'].Fill(lb_cos_theta2rStar)
            histograms['h_lb_cos_theta2kStar_mtt400to600_cosTSA_lt_0p4'].Fill(lb_cos_theta2kStar)
            histograms['h_lb_Cnn_mtt400to600_cosTSA_lt_0p4'].Fill(lb_Cnn)
            histograms['h_lb_Cnr_mtt400to600_cosTSA_lt_0p4'].Fill(lb_Cnr)
            histograms['h_lb_Cnk_mtt400to600_cosTSA_lt_0p4'].Fill(lb_Cnk)
            histograms['h_lb_Crn_mtt400to600_cosTSA_lt_0p4'].Fill(lb_Crn)
            histograms['h_lb_Crr_mtt400to600_cosTSA_lt_0p4'].Fill(lb_Crr)
            histograms['h_lb_Crk_mtt400to600_cosTSA_lt_0p4'].Fill(lb_Crk)
            histograms['h_lb_Ckn_mtt400to600_cosTSA_lt_0p4'].Fill(lb_Ckn)
            histograms['h_lb_Ckr_mtt400to600_cosTSA_lt_0p4'].Fill(lb_Ckr)
            histograms['h_lb_Ckk_mtt400to600_cosTSA_lt_0p4'].Fill(lb_Ckk)
            histograms['h_lb_trC_mtt400to600_cosTSA_lt_0p4'].Fill(lb_trC)
            histograms['h_lb_cHel_mtt400to600_cosTSA_lt_0p4'].Fill(lb_cHel)
            histograms['h_lb_cHel_P3n_mtt400to600_cosTSA_lt_0p4'].Fill(lb_cHel_P3n)
            histograms['h_ld_cos_theta1n_mtt400to600_cosTSA_lt_0p4'].Fill(ld_cos_theta1n)
            histograms['h_ld_cos_theta1r_mtt400to600_cosTSA_lt_0p4'].Fill(ld_cos_theta1r)
            histograms['h_ld_cos_theta1k_mtt400to600_cosTSA_lt_0p4'].Fill(ld_cos_theta1k)
            histograms['h_ld_cos_theta1rStar_mtt400to600_cosTSA_lt_0p4'].Fill(ld_cos_theta1rStar)
            histograms['h_ld_cos_theta1kStar_mtt400to600_cosTSA_lt_0p4'].Fill(ld_cos_theta1kStar)
            histograms['h_ld_cos_theta2n_mtt400to600_cosTSA_lt_0p4'].Fill(ld_cos_theta2n)
            histograms['h_ld_cos_theta2r_mtt400to600_cosTSA_lt_0p4'].Fill(ld_cos_theta2r)
            histograms['h_ld_cos_theta2k_mtt400to600_cosTSA_lt_0p4'].Fill(ld_cos_theta2k)
            histograms['h_ld_cos_theta2rStar_mtt400to600_cosTSA_lt_0p4'].Fill(ld_cos_theta2rStar)
            histograms['h_ld_cos_theta2kStar_mtt400to600_cosTSA_lt_0p4'].Fill(ld_cos_theta2kStar)
            histograms['h_ld_Cnn_mtt400to600_cosTSA_lt_0p4'].Fill(ld_Cnn)
            histograms['h_ld_Cnr_mtt400to600_cosTSA_lt_0p4'].Fill(ld_Cnr)
            histograms['h_ld_Cnk_mtt400to600_cosTSA_lt_0p4'].Fill(ld_Cnk)
            histograms['h_ld_Crn_mtt400to600_cosTSA_lt_0p4'].Fill(ld_Crn)
            histograms['h_ld_Crr_mtt400to600_cosTSA_lt_0p4'].Fill(ld_Crr)
            histograms['h_ld_Crk_mtt400to600_cosTSA_lt_0p4'].Fill(ld_Crk)
            histograms['h_ld_Ckn_mtt400to600_cosTSA_lt_0p4'].Fill(ld_Ckn)
            histograms['h_ld_Ckr_mtt400to600_cosTSA_lt_0p4'].Fill(ld_Ckr)
            histograms['h_ld_Ckk_mtt400to600_cosTSA_lt_0p4'].Fill(ld_Ckk)
            histograms['h_ld_trC_mtt400to600_cosTSA_lt_0p4'].Fill(ld_trC)
            histograms['h_ld_cHel_mtt400to600_cosTSA_lt_0p4'].Fill(ld_cHel)
            histograms['h_ld_cHel_P3n_mtt400to600_cosTSA_lt_0p4'].Fill(ld_cHel_P3n)
        if abs(cosTSA) < 0.7:
            histograms['h_cos_theta1n_antilepton_mtt400to600_cosTSA_lt_0p7'].Fill(cos_theta1n_antilepton)
            histograms['h_cos_theta1r_antilepton_mtt400to600_cosTSA_lt_0p7'].Fill(cos_theta1r_antilepton)
            histograms['h_cos_theta1k_antilepton_mtt400to600_cosTSA_lt_0p7'].Fill(cos_theta1k_antilepton)
            histograms['h_cos_theta1rStar_antilepton_mtt400to600_cosTSA_lt_0p7'].Fill(cos_theta1rStar_antilepton)
            histograms['h_cos_theta1kStar_antilepton_mtt400to600_cosTSA_lt_0p7'].Fill(cos_theta1kStar_antilepton)
            histograms['h_cos_theta2n_lepton_mtt400to600_cosTSA_lt_0p7'].Fill(cos_theta2n_lepton)
            histograms['h_cos_theta2r_lepton_mtt400to600_cosTSA_lt_0p7'].Fill(cos_theta2r_lepton)
            histograms['h_cos_theta2k_lepton_mtt400to600_cosTSA_lt_0p7'].Fill(cos_theta2k_lepton)
            histograms['h_cos_theta2rStar_lepton_mtt400to600_cosTSA_lt_0p7'].Fill(cos_theta2rStar_lepton)
            histograms['h_cos_theta2kStar_lepton_mtt400to600_cosTSA_lt_0p7'].Fill(cos_theta2kStar_lepton)
            histograms['h_lb_cos_theta1n_mtt400to600_cosTSA_lt_0p7'].Fill(lb_cos_theta1n)
            histograms['h_lb_cos_theta1r_mtt400to600_cosTSA_lt_0p7'].Fill(lb_cos_theta1r)
            histograms['h_lb_cos_theta1k_mtt400to600_cosTSA_lt_0p7'].Fill(lb_cos_theta1k)
            histograms['h_lb_cos_theta1rStar_mtt400to600_cosTSA_lt_0p7'].Fill(lb_cos_theta1rStar)
            histograms['h_lb_cos_theta1kStar_mtt400to600_cosTSA_lt_0p7'].Fill(lb_cos_theta1kStar)
            histograms['h_lb_cos_theta2n_mtt400to600_cosTSA_lt_0p7'].Fill(lb_cos_theta2n)
            histograms['h_lb_cos_theta2r_mtt400to600_cosTSA_lt_0p7'].Fill(lb_cos_theta2r)
            histograms['h_lb_cos_theta2k_mtt400to600_cosTSA_lt_0p7'].Fill(lb_cos_theta2k)
            histograms['h_lb_cos_theta2rStar_mtt400to600_cosTSA_lt_0p7'].Fill(lb_cos_theta2rStar)
            histograms['h_lb_cos_theta2kStar_mtt400to600_cosTSA_lt_0p7'].Fill(lb_cos_theta2kStar)
            histograms['h_lb_Cnn_mtt400to600_cosTSA_lt_0p7'].Fill(lb_Cnn)
            histograms['h_lb_Cnr_mtt400to600_cosTSA_lt_0p7'].Fill(lb_Cnr)
            histograms['h_lb_Cnk_mtt400to600_cosTSA_lt_0p7'].Fill(lb_Cnk)
            histograms['h_lb_Crn_mtt400to600_cosTSA_lt_0p7'].Fill(lb_Crn)
            histograms['h_lb_Crr_mtt400to600_cosTSA_lt_0p7'].Fill(lb_Crr)
            histograms['h_lb_Crk_mtt400to600_cosTSA_lt_0p7'].Fill(lb_Crk)
            histograms['h_lb_Ckn_mtt400to600_cosTSA_lt_0p7'].Fill(lb_Ckn)
            histograms['h_lb_Ckr_mtt400to600_cosTSA_lt_0p7'].Fill(lb_Ckr)
            histograms['h_lb_Ckk_mtt400to600_cosTSA_lt_0p7'].Fill(lb_Ckk)
            histograms['h_lb_trC_mtt400to600_cosTSA_lt_0p7'].Fill(lb_trC)
            histograms['h_lb_cHel_mtt400to600_cosTSA_lt_0p7'].Fill(lb_cHel)
            histograms['h_lb_cHel_P3n_mtt400to600_cosTSA_lt_0p7'].Fill(lb_cHel_P3n)
            histograms['h_ld_cos_theta1n_mtt400to600_cosTSA_lt_0p7'].Fill(ld_cos_theta1n)
            histograms['h_ld_cos_theta1r_mtt400to600_cosTSA_lt_0p7'].Fill(ld_cos_theta1r)
            histograms['h_ld_cos_theta1k_mtt400to600_cosTSA_lt_0p7'].Fill(ld_cos_theta1k)
            histograms['h_ld_cos_theta1rStar_mtt400to600_cosTSA_lt_0p7'].Fill(ld_cos_theta1rStar)
            histograms['h_ld_cos_theta1kStar_mtt400to600_cosTSA_lt_0p7'].Fill(ld_cos_theta1kStar)
            histograms['h_ld_cos_theta2n_mtt400to600_cosTSA_lt_0p7'].Fill(ld_cos_theta2n)
            histograms['h_ld_cos_theta2r_mtt400to600_cosTSA_lt_0p7'].Fill(ld_cos_theta2r)
            histograms['h_ld_cos_theta2k_mtt400to600_cosTSA_lt_0p7'].Fill(ld_cos_theta2k)
            histograms['h_ld_cos_theta2rStar_mtt400to600_cosTSA_lt_0p7'].Fill(ld_cos_theta2rStar)
            histograms['h_ld_cos_theta2kStar_mtt400to600_cosTSA_lt_0p7'].Fill(ld_cos_theta2kStar)
            histograms['h_ld_Cnn_mtt400to600_cosTSA_lt_0p7'].Fill(ld_Cnn)
            histograms['h_ld_Cnr_mtt400to600_cosTSA_lt_0p7'].Fill(ld_Cnr)
            histograms['h_ld_Cnk_mtt400to600_cosTSA_lt_0p7'].Fill(ld_Cnk)
            histograms['h_ld_Crn_mtt400to600_cosTSA_lt_0p7'].Fill(ld_Crn)
            histograms['h_ld_Crr_mtt400to600_cosTSA_lt_0p7'].Fill(ld_Crr)
            histograms['h_ld_Crk_mtt400to600_cosTSA_lt_0p7'].Fill(ld_Crk)
            histograms['h_ld_Ckn_mtt400to600_cosTSA_lt_0p7'].Fill(ld_Ckn)
            histograms['h_ld_Ckr_mtt400to600_cosTSA_lt_0p7'].Fill(ld_Ckr)
            histograms['h_ld_Ckk_mtt400to600_cosTSA_lt_0p7'].Fill(ld_Ckk)
            histograms['h_ld_trC_mtt400to600_cosTSA_lt_0p7'].Fill(ld_trC)
            histograms['h_ld_cHel_mtt400to600_cosTSA_lt_0p7'].Fill(ld_cHel)
            histograms['h_ld_cHel_P3n_mtt400to600_cosTSA_lt_0p7'].Fill(ld_cHel_P3n)
        elif abs(cosTSA) > 0.7:
            histograms['h_cos_theta1n_antilepton_mtt400to600_cosTSA_gt_0p7'].Fill(cos_theta1n_antilepton)
            histograms['h_cos_theta1r_antilepton_mtt400to600_cosTSA_gt_0p7'].Fill(cos_theta1r_antilepton)
            histograms['h_cos_theta1k_antilepton_mtt400to600_cosTSA_gt_0p7'].Fill(cos_theta1k_antilepton)
            histograms['h_cos_theta1rStar_antilepton_mtt400to600_cosTSA_gt_0p7'].Fill(cos_theta1rStar_antilepton)
            histograms['h_cos_theta1kStar_antilepton_mtt400to600_cosTSA_gt_0p7'].Fill(cos_theta1kStar_antilepton)
            histograms['h_cos_theta2n_lepton_mtt400to600_cosTSA_gt_0p7'].Fill(cos_theta2n_lepton)
            histograms['h_cos_theta2r_lepton_mtt400to600_cosTSA_gt_0p7'].Fill(cos_theta2r_lepton)
            histograms['h_cos_theta2k_lepton_mtt400to600_cosTSA_gt_0p7'].Fill(cos_theta2k_lepton)
            histograms['h_cos_theta2rStar_lepton_mtt400to600_cosTSA_gt_0p7'].Fill(cos_theta2rStar_lepton)
            histograms['h_cos_theta2kStar_lepton_mtt400to600_cosTSA_gt_0p7'].Fill(cos_theta2kStar_lepton)
            histograms['h_lb_cos_theta1n_mtt400to600_cosTSA_gt_0p7'].Fill(lb_cos_theta1n)
            histograms['h_lb_cos_theta1r_mtt400to600_cosTSA_gt_0p7'].Fill(lb_cos_theta1r)
            histograms['h_lb_cos_theta1k_mtt400to600_cosTSA_gt_0p7'].Fill(lb_cos_theta1k)
            histograms['h_lb_cos_theta1rStar_mtt400to600_cosTSA_gt_0p7'].Fill(lb_cos_theta1rStar)
            histograms['h_lb_cos_theta1kStar_mtt400to600_cosTSA_gt_0p7'].Fill(lb_cos_theta1kStar)
            histograms['h_lb_cos_theta2n_mtt400to600_cosTSA_gt_0p7'].Fill(lb_cos_theta2n)
            histograms['h_lb_cos_theta2r_mtt400to600_cosTSA_gt_0p7'].Fill(lb_cos_theta2r)
            histograms['h_lb_cos_theta2k_mtt400to600_cosTSA_gt_0p7'].Fill(lb_cos_theta2k)
            histograms['h_lb_cos_theta2rStar_mtt400to600_cosTSA_gt_0p7'].Fill(lb_cos_theta2rStar)
            histograms['h_lb_cos_theta2kStar_mtt400to600_cosTSA_gt_0p7'].Fill(lb_cos_theta2kStar)
            histograms['h_lb_Cnn_mtt400to600_cosTSA_gt_0p7'].Fill(lb_Cnn)
            histograms['h_lb_Cnr_mtt400to600_cosTSA_gt_0p7'].Fill(lb_Cnr)
            histograms['h_lb_Cnk_mtt400to600_cosTSA_gt_0p7'].Fill(lb_Cnk)
            histograms['h_lb_Crn_mtt400to600_cosTSA_gt_0p7'].Fill(lb_Crn)
            histograms['h_lb_Crr_mtt400to600_cosTSA_gt_0p7'].Fill(lb_Crr)
            histograms['h_lb_Crk_mtt400to600_cosTSA_gt_0p7'].Fill(lb_Crk)
            histograms['h_lb_Ckn_mtt400to600_cosTSA_gt_0p7'].Fill(lb_Ckn)
            histograms['h_lb_Ckr_mtt400to600_cosTSA_gt_0p7'].Fill(lb_Ckr)
            histograms['h_lb_Ckk_mtt400to600_cosTSA_gt_0p7'].Fill(lb_Ckk)
            histograms['h_lb_trC_mtt400to600_cosTSA_gt_0p7'].Fill(lb_trC)
            histograms['h_lb_cHel_mtt400to600_cosTSA_gt_0p7'].Fill(lb_cHel)
            histograms['h_lb_cHel_P3n_mtt400to600_cosTSA_gt_0p7'].Fill(lb_cHel_P3n)
            histograms['h_ld_cos_theta1n_mtt400to600_cosTSA_gt_0p7'].Fill(ld_cos_theta1n)
            histograms['h_ld_cos_theta1r_mtt400to600_cosTSA_gt_0p7'].Fill(ld_cos_theta1r)
            histograms['h_ld_cos_theta1k_mtt400to600_cosTSA_gt_0p7'].Fill(ld_cos_theta1k)
            histograms['h_ld_cos_theta1rStar_mtt400to600_cosTSA_gt_0p7'].Fill(ld_cos_theta1rStar)
            histograms['h_ld_cos_theta1kStar_mtt400to600_cosTSA_gt_0p7'].Fill(ld_cos_theta1kStar)
            histograms['h_ld_cos_theta2n_mtt400to600_cosTSA_gt_0p7'].Fill(ld_cos_theta2n)
            histograms['h_ld_cos_theta2r_mtt400to600_cosTSA_gt_0p7'].Fill(ld_cos_theta2r)
            histograms['h_ld_cos_theta2k_mtt400to600_cosTSA_gt_0p7'].Fill(ld_cos_theta2k)
            histograms['h_ld_cos_theta2rStar_mtt400to600_cosTSA_gt_0p7'].Fill(ld_cos_theta2rStar)
            histograms['h_ld_cos_theta2kStar_mtt400to600_cosTSA_gt_0p7'].Fill(ld_cos_theta2kStar)
            histograms['h_ld_Cnn_mtt400to600_cosTSA_gt_0p7'].Fill(ld_Cnn)
            histograms['h_ld_Cnr_mtt400to600_cosTSA_gt_0p7'].Fill(ld_Cnr)
            histograms['h_ld_Cnk_mtt400to600_cosTSA_gt_0p7'].Fill(ld_Cnk)
            histograms['h_ld_Crn_mtt400to600_cosTSA_gt_0p7'].Fill(ld_Crn)
            histograms['h_ld_Crr_mtt400to600_cosTSA_gt_0p7'].Fill(ld_Crr)
            histograms['h_ld_Crk_mtt400to600_cosTSA_gt_0p7'].Fill(ld_Crk)
            histograms['h_ld_Ckn_mtt400to600_cosTSA_gt_0p7'].Fill(ld_Ckn)
            histograms['h_ld_Ckr_mtt400to600_cosTSA_gt_0p7'].Fill(ld_Ckr)
            histograms['h_ld_Ckk_mtt400to600_cosTSA_gt_0p7'].Fill(ld_Ckk)
            histograms['h_ld_trC_mtt400to600_cosTSA_gt_0p7'].Fill(ld_trC)
            histograms['h_ld_cHel_mtt400to600_cosTSA_gt_0p7'].Fill(ld_cHel)
            histograms['h_ld_cHel_P3n_mtt400to600_cosTSA_gt_0p7'].Fill(ld_cHel_P3n)
    elif 600 < m_tt < 800:
        histograms['h_cos_theta1n_antilepton_mtt600to800'].Fill(cos_theta1n_antilepton)
        histograms['h_cos_theta1r_antilepton_mtt600to800'].Fill(cos_theta1r_antilepton)
        histograms['h_cos_theta1k_antilepton_mtt600to800'].Fill(cos_theta1k_antilepton)
        histograms['h_cos_theta1rStar_antilepton_mtt600to800'].Fill(cos_theta1rStar_antilepton)
        histograms['h_cos_theta1kStar_antilepton_mtt600to800'].Fill(cos_theta1kStar_antilepton)
        histograms['h_cos_theta2n_lepton_mtt600to800'].Fill(cos_theta2n_lepton)
        histograms['h_cos_theta2r_lepton_mtt600to800'].Fill(cos_theta2r_lepton)
        histograms['h_cos_theta2k_lepton_mtt600to800'].Fill(cos_theta2k_lepton)
        histograms['h_cos_theta2rStar_lepton_mtt600to800'].Fill(cos_theta2rStar_lepton)
        histograms['h_cos_theta2kStar_lepton_mtt600to800'].Fill(cos_theta2kStar_lepton)
        histograms['h_lb_cos_theta1n_mtt600to800'].Fill(lb_cos_theta1n)
        histograms['h_lb_cos_theta1r_mtt600to800'].Fill(lb_cos_theta1r)
        histograms['h_lb_cos_theta1k_mtt600to800'].Fill(lb_cos_theta1k)
        histograms['h_lb_cos_theta1rStar_mtt600to800'].Fill(lb_cos_theta1rStar)
        histograms['h_lb_cos_theta1kStar_mtt600to800'].Fill(lb_cos_theta1kStar)
        histograms['h_lb_cos_theta2n_mtt600to800'].Fill(lb_cos_theta2n)
        histograms['h_lb_cos_theta2r_mtt600to800'].Fill(lb_cos_theta2r)
        histograms['h_lb_cos_theta2k_mtt600to800'].Fill(lb_cos_theta2k)
        histograms['h_lb_cos_theta2rStar_mtt600to800'].Fill(lb_cos_theta2rStar)
        histograms['h_lb_cos_theta2kStar_mtt600to800'].Fill(lb_cos_theta2kStar)
        histograms['h_lb_Cnn_mtt600to800'].Fill(lb_Cnn)
        histograms['h_lb_Cnr_mtt600to800'].Fill(lb_Cnr)
        histograms['h_lb_Cnk_mtt600to800'].Fill(lb_Cnk)
        histograms['h_lb_Crn_mtt600to800'].Fill(lb_Crn)
        histograms['h_lb_Crr_mtt600to800'].Fill(lb_Crr)
        histograms['h_lb_Crk_mtt600to800'].Fill(lb_Crk)
        histograms['h_lb_Ckn_mtt600to800'].Fill(lb_Ckn)
        histograms['h_lb_Ckr_mtt600to800'].Fill(lb_Ckr)
        histograms['h_lb_Ckk_mtt600to800'].Fill(lb_Ckk)
        histograms['h_lb_trC_mtt600to800'].Fill(lb_trC)
        histograms['h_lb_cHel_mtt600to800'].Fill(lb_cHel)
        histograms['h_lb_cHel_P3n_mtt600to800'].Fill(lb_cHel_P3n)
        histograms['h_ld_cos_theta1n_mtt600to800'].Fill(ld_cos_theta1n)
        histograms['h_ld_cos_theta1r_mtt600to800'].Fill(ld_cos_theta1r)
        histograms['h_ld_cos_theta1k_mtt600to800'].Fill(ld_cos_theta1k)
        histograms['h_ld_cos_theta1rStar_mtt600to800'].Fill(ld_cos_theta1rStar)
        histograms['h_ld_cos_theta1kStar_mtt600to800'].Fill(ld_cos_theta1kStar)
        histograms['h_ld_cos_theta2n_mtt600to800'].Fill(ld_cos_theta2n)
        histograms['h_ld_cos_theta2r_mtt600to800'].Fill(ld_cos_theta2r)
        histograms['h_ld_cos_theta2k_mtt600to800'].Fill(ld_cos_theta2k)
        histograms['h_ld_cos_theta2rStar_mtt600to800'].Fill(ld_cos_theta2rStar)
        histograms['h_ld_cos_theta2kStar_mtt600to800'].Fill(ld_cos_theta2kStar)
        histograms['h_ld_Cnn_mtt600to800'].Fill(ld_Cnn)
        histograms['h_ld_Cnr_mtt600to800'].Fill(ld_Cnr)
        histograms['h_ld_Cnk_mtt600to800'].Fill(ld_Cnk)
        histograms['h_ld_Crn_mtt600to800'].Fill(ld_Crn)
        histograms['h_ld_Crr_mtt600to800'].Fill(ld_Crr)
        histograms['h_ld_Crk_mtt600to800'].Fill(ld_Crk)
        histograms['h_ld_Ckn_mtt600to800'].Fill(ld_Ckn)
        histograms['h_ld_Ckr_mtt600to800'].Fill(ld_Ckr)
        histograms['h_ld_Ckk_mtt600to800'].Fill(ld_Ckk)
        histograms['h_ld_trC_mtt600to800'].Fill(ld_trC)
        histograms['h_ld_cHel_mtt600to800'].Fill(ld_cHel)
        histograms['h_ld_cHel_P3n_mtt600to800'].Fill(ld_cHel_P3n)
        if abs(cosTSA) < 0.4:
            histograms['h_cos_theta1n_antilepton_mtt600to800_cosTSA_lt_0p4'].Fill(cos_theta1n_antilepton)
            histograms['h_cos_theta1r_antilepton_mtt600to800_cosTSA_lt_0p4'].Fill(cos_theta1r_antilepton)
            histograms['h_cos_theta1k_antilepton_mtt600to800_cosTSA_lt_0p4'].Fill(cos_theta1k_antilepton)
            histograms['h_cos_theta1rStar_antilepton_mtt600to800_cosTSA_lt_0p4'].Fill(cos_theta1rStar_antilepton)
            histograms['h_cos_theta1kStar_antilepton_mtt600to800_cosTSA_lt_0p4'].Fill(cos_theta1kStar_antilepton)
            histograms['h_cos_theta2n_lepton_mtt600to800_cosTSA_lt_0p4'].Fill(cos_theta2n_lepton)
            histograms['h_cos_theta2r_lepton_mtt600to800_cosTSA_lt_0p4'].Fill(cos_theta2r_lepton)
            histograms['h_cos_theta2k_lepton_mtt600to800_cosTSA_lt_0p4'].Fill(cos_theta2k_lepton)
            histograms['h_cos_theta2rStar_lepton_mtt600to800_cosTSA_lt_0p4'].Fill(cos_theta2rStar_lepton)
            histograms['h_cos_theta2kStar_lepton_mtt600to800_cosTSA_lt_0p4'].Fill(cos_theta2kStar_lepton)
            histograms['h_lb_cos_theta1n_mtt600to800_cosTSA_lt_0p4'].Fill(lb_cos_theta1n)
            histograms['h_lb_cos_theta1r_mtt600to800_cosTSA_lt_0p4'].Fill(lb_cos_theta1r)
            histograms['h_lb_cos_theta1k_mtt600to800_cosTSA_lt_0p4'].Fill(lb_cos_theta1k)
            histograms['h_lb_cos_theta1rStar_mtt600to800_cosTSA_lt_0p4'].Fill(lb_cos_theta1rStar)
            histograms['h_lb_cos_theta1kStar_mtt600to800_cosTSA_lt_0p4'].Fill(lb_cos_theta1kStar)
            histograms['h_lb_cos_theta2n_mtt600to800_cosTSA_lt_0p4'].Fill(lb_cos_theta2n)
            histograms['h_lb_cos_theta2r_mtt600to800_cosTSA_lt_0p4'].Fill(lb_cos_theta2r)
            histograms['h_lb_cos_theta2k_mtt600to800_cosTSA_lt_0p4'].Fill(lb_cos_theta2k)
            histograms['h_lb_cos_theta2rStar_mtt600to800_cosTSA_lt_0p4'].Fill(lb_cos_theta2rStar)
            histograms['h_lb_cos_theta2kStar_mtt600to800_cosTSA_lt_0p4'].Fill(lb_cos_theta2kStar)
            histograms['h_lb_Cnn_mtt600to800_cosTSA_lt_0p4'].Fill(lb_Cnn)
            histograms['h_lb_Cnr_mtt600to800_cosTSA_lt_0p4'].Fill(lb_Cnr)
            histograms['h_lb_Cnk_mtt600to800_cosTSA_lt_0p4'].Fill(lb_Cnk)
            histograms['h_lb_Crn_mtt600to800_cosTSA_lt_0p4'].Fill(lb_Crn)
            histograms['h_lb_Crr_mtt600to800_cosTSA_lt_0p4'].Fill(lb_Crr)
            histograms['h_lb_Crk_mtt600to800_cosTSA_lt_0p4'].Fill(lb_Crk)
            histograms['h_lb_Ckn_mtt600to800_cosTSA_lt_0p4'].Fill(lb_Ckn)
            histograms['h_lb_Ckr_mtt600to800_cosTSA_lt_0p4'].Fill(lb_Ckr)
            histograms['h_lb_Ckk_mtt600to800_cosTSA_lt_0p4'].Fill(lb_Ckk)
            histograms['h_lb_trC_mtt600to800_cosTSA_lt_0p4'].Fill(lb_trC)
            histograms['h_lb_cHel_mtt600to800_cosTSA_lt_0p4'].Fill(lb_cHel)
            histograms['h_lb_cHel_P3n_mtt600to800_cosTSA_lt_0p4'].Fill(lb_cHel_P3n)
            histograms['h_ld_cos_theta1n_mtt600to800_cosTSA_lt_0p4'].Fill(ld_cos_theta1n)
            histograms['h_ld_cos_theta1r_mtt600to800_cosTSA_lt_0p4'].Fill(ld_cos_theta1r)
            histograms['h_ld_cos_theta1k_mtt600to800_cosTSA_lt_0p4'].Fill(ld_cos_theta1k)
            histograms['h_ld_cos_theta1rStar_mtt600to800_cosTSA_lt_0p4'].Fill(ld_cos_theta1rStar)
            histograms['h_ld_cos_theta1kStar_mtt600to800_cosTSA_lt_0p4'].Fill(ld_cos_theta1kStar)
            histograms['h_ld_cos_theta2n_mtt600to800_cosTSA_lt_0p4'].Fill(ld_cos_theta2n)
            histograms['h_ld_cos_theta2r_mtt600to800_cosTSA_lt_0p4'].Fill(ld_cos_theta2r)
            histograms['h_ld_cos_theta2k_mtt600to800_cosTSA_lt_0p4'].Fill(ld_cos_theta2k)
            histograms['h_ld_cos_theta2rStar_mtt600to800_cosTSA_lt_0p4'].Fill(ld_cos_theta2rStar)
            histograms['h_ld_cos_theta2kStar_mtt600to800_cosTSA_lt_0p4'].Fill(ld_cos_theta2kStar)
            histograms['h_ld_Cnn_mtt600to800_cosTSA_lt_0p4'].Fill(ld_Cnn)
            histograms['h_ld_Cnr_mtt600to800_cosTSA_lt_0p4'].Fill(ld_Cnr)
            histograms['h_ld_Cnk_mtt600to800_cosTSA_lt_0p4'].Fill(ld_Cnk)
            histograms['h_ld_Crn_mtt600to800_cosTSA_lt_0p4'].Fill(ld_Crn)
            histograms['h_ld_Crr_mtt600to800_cosTSA_lt_0p4'].Fill(ld_Crr)
            histograms['h_ld_Crk_mtt600to800_cosTSA_lt_0p4'].Fill(ld_Crk)
            histograms['h_ld_Ckn_mtt600to800_cosTSA_lt_0p4'].Fill(ld_Ckn)
            histograms['h_ld_Ckr_mtt600to800_cosTSA_lt_0p4'].Fill(ld_Ckr)
            histograms['h_ld_Ckk_mtt600to800_cosTSA_lt_0p4'].Fill(ld_Ckk)
            histograms['h_ld_trC_mtt600to800_cosTSA_lt_0p4'].Fill(ld_trC)
            histograms['h_ld_cHel_mtt600to800_cosTSA_lt_0p4'].Fill(ld_cHel)
            histograms['h_ld_cHel_P3n_mtt600to800_cosTSA_lt_0p4'].Fill(ld_cHel_P3n)
        if abs(cosTSA) < 0.7:
            histograms['h_cos_theta1n_antilepton_mtt600to800_cosTSA_lt_0p7'].Fill(cos_theta1n_antilepton)
            histograms['h_cos_theta1r_antilepton_mtt600to800_cosTSA_lt_0p7'].Fill(cos_theta1r_antilepton)
            histograms['h_cos_theta1k_antilepton_mtt600to800_cosTSA_lt_0p7'].Fill(cos_theta1k_antilepton)
            histograms['h_cos_theta1rStar_antilepton_mtt600to800_cosTSA_lt_0p7'].Fill(cos_theta1rStar_antilepton)
            histograms['h_cos_theta1kStar_antilepton_mtt600to800_cosTSA_lt_0p7'].Fill(cos_theta1kStar_antilepton)
            histograms['h_cos_theta2n_lepton_mtt600to800_cosTSA_lt_0p7'].Fill(cos_theta2n_lepton)
            histograms['h_cos_theta2r_lepton_mtt600to800_cosTSA_lt_0p7'].Fill(cos_theta2r_lepton)
            histograms['h_cos_theta2k_lepton_mtt600to800_cosTSA_lt_0p7'].Fill(cos_theta2k_lepton)
            histograms['h_cos_theta2rStar_lepton_mtt600to800_cosTSA_lt_0p7'].Fill(cos_theta2rStar_lepton)
            histograms['h_cos_theta2kStar_lepton_mtt600to800_cosTSA_lt_0p7'].Fill(cos_theta2kStar_lepton)
            histograms['h_lb_cos_theta1n_mtt600to800_cosTSA_lt_0p7'].Fill(lb_cos_theta1n)
            histograms['h_lb_cos_theta1r_mtt600to800_cosTSA_lt_0p7'].Fill(lb_cos_theta1r)
            histograms['h_lb_cos_theta1k_mtt600to800_cosTSA_lt_0p7'].Fill(lb_cos_theta1k)
            histograms['h_lb_cos_theta1rStar_mtt600to800_cosTSA_lt_0p7'].Fill(lb_cos_theta1rStar)
            histograms['h_lb_cos_theta1kStar_mtt600to800_cosTSA_lt_0p7'].Fill(lb_cos_theta1kStar)
            histograms['h_lb_cos_theta2n_mtt600to800_cosTSA_lt_0p7'].Fill(lb_cos_theta2n)
            histograms['h_lb_cos_theta2r_mtt600to800_cosTSA_lt_0p7'].Fill(lb_cos_theta2r)
            histograms['h_lb_cos_theta2k_mtt600to800_cosTSA_lt_0p7'].Fill(lb_cos_theta2k)
            histograms['h_lb_cos_theta2rStar_mtt600to800_cosTSA_lt_0p7'].Fill(lb_cos_theta2rStar)
            histograms['h_lb_cos_theta2kStar_mtt600to800_cosTSA_lt_0p7'].Fill(lb_cos_theta2kStar)
            histograms['h_lb_Cnn_mtt600to800_cosTSA_lt_0p7'].Fill(lb_Cnn)
            histograms['h_lb_Cnr_mtt600to800_cosTSA_lt_0p7'].Fill(lb_Cnr)
            histograms['h_lb_Cnk_mtt600to800_cosTSA_lt_0p7'].Fill(lb_Cnk)
            histograms['h_lb_Crn_mtt600to800_cosTSA_lt_0p7'].Fill(lb_Crn)
            histograms['h_lb_Crr_mtt600to800_cosTSA_lt_0p7'].Fill(lb_Crr)
            histograms['h_lb_Crk_mtt600to800_cosTSA_lt_0p7'].Fill(lb_Crk)
            histograms['h_lb_Ckn_mtt600to800_cosTSA_lt_0p7'].Fill(lb_Ckn)
            histograms['h_lb_Ckr_mtt600to800_cosTSA_lt_0p7'].Fill(lb_Ckr)
            histograms['h_lb_Ckk_mtt600to800_cosTSA_lt_0p7'].Fill(lb_Ckk)
            histograms['h_lb_trC_mtt600to800_cosTSA_lt_0p7'].Fill(lb_trC)
            histograms['h_lb_cHel_mtt600to800_cosTSA_lt_0p7'].Fill(lb_cHel)
            histograms['h_lb_cHel_P3n_mtt600to800_cosTSA_lt_0p7'].Fill(lb_cHel_P3n)
            histograms['h_ld_cos_theta1n_mtt600to800_cosTSA_lt_0p7'].Fill(ld_cos_theta1n)
            histograms['h_ld_cos_theta1r_mtt600to800_cosTSA_lt_0p7'].Fill(ld_cos_theta1r)
            histograms['h_ld_cos_theta1k_mtt600to800_cosTSA_lt_0p7'].Fill(ld_cos_theta1k)
            histograms['h_ld_cos_theta1rStar_mtt600to800_cosTSA_lt_0p7'].Fill(ld_cos_theta1rStar)
            histograms['h_ld_cos_theta1kStar_mtt600to800_cosTSA_lt_0p7'].Fill(ld_cos_theta1kStar)
            histograms['h_ld_cos_theta2n_mtt600to800_cosTSA_lt_0p7'].Fill(ld_cos_theta2n)
            histograms['h_ld_cos_theta2r_mtt600to800_cosTSA_lt_0p7'].Fill(ld_cos_theta2r)
            histograms['h_ld_cos_theta2k_mtt600to800_cosTSA_lt_0p7'].Fill(ld_cos_theta2k)
            histograms['h_ld_cos_theta2rStar_mtt600to800_cosTSA_lt_0p7'].Fill(ld_cos_theta2rStar)
            histograms['h_ld_cos_theta2kStar_mtt600to800_cosTSA_lt_0p7'].Fill(ld_cos_theta2kStar)
            histograms['h_ld_Cnn_mtt600to800_cosTSA_lt_0p7'].Fill(ld_Cnn)
            histograms['h_ld_Cnr_mtt600to800_cosTSA_lt_0p7'].Fill(ld_Cnr)
            histograms['h_ld_Cnk_mtt600to800_cosTSA_lt_0p7'].Fill(ld_Cnk)
            histograms['h_ld_Crn_mtt600to800_cosTSA_lt_0p7'].Fill(ld_Crn)
            histograms['h_ld_Crr_mtt600to800_cosTSA_lt_0p7'].Fill(ld_Crr)
            histograms['h_ld_Crk_mtt600to800_cosTSA_lt_0p7'].Fill(ld_Crk)
            histograms['h_ld_Ckn_mtt600to800_cosTSA_lt_0p7'].Fill(ld_Ckn)
            histograms['h_ld_Ckr_mtt600to800_cosTSA_lt_0p7'].Fill(ld_Ckr)
            histograms['h_ld_Ckk_mtt600to800_cosTSA_lt_0p7'].Fill(ld_Ckk)
            histograms['h_ld_trC_mtt600to800_cosTSA_lt_0p7'].Fill(ld_trC)
            histograms['h_ld_cHel_mtt600to800_cosTSA_lt_0p7'].Fill(ld_cHel)
            histograms['h_ld_cHel_P3n_mtt600to800_cosTSA_lt_0p7'].Fill(ld_cHel_P3n)
        if abs(cosTSA) > 0.7:
            histograms['h_cos_theta1n_antilepton_mtt600to800_cosTSA_gt_0p7'].Fill(cos_theta1n_antilepton)
            histograms['h_cos_theta1r_antilepton_mtt600to800_cosTSA_gt_0p7'].Fill(cos_theta1r_antilepton)
            histograms['h_cos_theta1k_antilepton_mtt600to800_cosTSA_gt_0p7'].Fill(cos_theta1k_antilepton)
            histograms['h_cos_theta1rStar_antilepton_mtt600to800_cosTSA_gt_0p7'].Fill(cos_theta1rStar_antilepton)
            histograms['h_cos_theta1kStar_antilepton_mtt600to800_cosTSA_gt_0p7'].Fill(cos_theta1kStar_antilepton)
            histograms['h_cos_theta2n_lepton_mtt600to800_cosTSA_gt_0p7'].Fill(cos_theta2n_lepton)
            histograms['h_cos_theta2r_lepton_mtt600to800_cosTSA_gt_0p7'].Fill(cos_theta2r_lepton)
            histograms['h_cos_theta2k_lepton_mtt600to800_cosTSA_gt_0p7'].Fill(cos_theta2k_lepton)
            histograms['h_cos_theta2rStar_lepton_mtt600to800_cosTSA_gt_0p7'].Fill(cos_theta2rStar_lepton)
            histograms['h_cos_theta2kStar_lepton_mtt600to800_cosTSA_gt_0p7'].Fill(cos_theta2kStar_lepton)
            histograms['h_lb_cos_theta1n_mtt600to800_cosTSA_gt_0p7'].Fill(lb_cos_theta1n)
            histograms['h_lb_cos_theta1r_mtt600to800_cosTSA_gt_0p7'].Fill(lb_cos_theta1r)
            histograms['h_lb_cos_theta1k_mtt600to800_cosTSA_gt_0p7'].Fill(lb_cos_theta1k)
            histograms['h_lb_cos_theta1rStar_mtt600to800_cosTSA_gt_0p7'].Fill(lb_cos_theta1rStar)
            histograms['h_lb_cos_theta1kStar_mtt600to800_cosTSA_gt_0p7'].Fill(lb_cos_theta1kStar)
            histograms['h_lb_cos_theta2n_mtt600to800_cosTSA_gt_0p7'].Fill(lb_cos_theta2n)
            histograms['h_lb_cos_theta2r_mtt600to800_cosTSA_gt_0p7'].Fill(lb_cos_theta2r)
            histograms['h_lb_cos_theta2k_mtt600to800_cosTSA_gt_0p7'].Fill(lb_cos_theta2k)
            histograms['h_lb_cos_theta2rStar_mtt600to800_cosTSA_gt_0p7'].Fill(lb_cos_theta2rStar)
            histograms['h_lb_cos_theta2kStar_mtt600to800_cosTSA_gt_0p7'].Fill(lb_cos_theta2kStar)
            histograms['h_lb_Cnn_mtt600to800_cosTSA_gt_0p7'].Fill(lb_Cnn)
            histograms['h_lb_Cnr_mtt600to800_cosTSA_gt_0p7'].Fill(lb_Cnr)
            histograms['h_lb_Cnk_mtt600to800_cosTSA_gt_0p7'].Fill(lb_Cnk)
            histograms['h_lb_Crn_mtt600to800_cosTSA_gt_0p7'].Fill(lb_Crn)
            histograms['h_lb_Crr_mtt600to800_cosTSA_gt_0p7'].Fill(lb_Crr)
            histograms['h_lb_Crk_mtt600to800_cosTSA_gt_0p7'].Fill(lb_Crk)
            histograms['h_lb_Ckn_mtt600to800_cosTSA_gt_0p7'].Fill(lb_Ckn)
            histograms['h_lb_Ckr_mtt600to800_cosTSA_gt_0p7'].Fill(lb_Ckr)
            histograms['h_lb_Ckk_mtt600to800_cosTSA_gt_0p7'].Fill(lb_Ckk)
            histograms['h_lb_trC_mtt600to800_cosTSA_gt_0p7'].Fill(lb_trC)
            histograms['h_lb_cHel_mtt600to800_cosTSA_gt_0p7'].Fill(lb_cHel)
            histograms['h_lb_cHel_P3n_mtt600to800_cosTSA_gt_0p7'].Fill(lb_cHel_P3n)
            histograms['h_ld_cos_theta1n_mtt600to800_cosTSA_gt_0p7'].Fill(ld_cos_theta1n)
            histograms['h_ld_cos_theta1r_mtt600to800_cosTSA_gt_0p7'].Fill(ld_cos_theta1r)
            histograms['h_ld_cos_theta1k_mtt600to800_cosTSA_gt_0p7'].Fill(ld_cos_theta1k)
            histograms['h_ld_cos_theta1rStar_mtt600to800_cosTSA_gt_0p7'].Fill(ld_cos_theta1rStar)
            histograms['h_ld_cos_theta1kStar_mtt600to800_cosTSA_gt_0p7'].Fill(ld_cos_theta1kStar)
            histograms['h_ld_cos_theta2n_mtt600to800_cosTSA_gt_0p7'].Fill(ld_cos_theta2n)
            histograms['h_ld_cos_theta2r_mtt600to800_cosTSA_gt_0p7'].Fill(ld_cos_theta2r)
            histograms['h_ld_cos_theta2k_mtt600to800_cosTSA_gt_0p7'].Fill(ld_cos_theta2k)
            histograms['h_ld_cos_theta2rStar_mtt600to800_cosTSA_gt_0p7'].Fill(ld_cos_theta2rStar)
            histograms['h_ld_cos_theta2kStar_mtt600to800_cosTSA_gt_0p7'].Fill(ld_cos_theta2kStar)
            histograms['h_ld_Cnn_mtt600to800_cosTSA_gt_0p7'].Fill(ld_Cnn)
            histograms['h_ld_Cnr_mtt600to800_cosTSA_gt_0p7'].Fill(ld_Cnr)
            histograms['h_ld_Cnk_mtt600to800_cosTSA_gt_0p7'].Fill(ld_Cnk)
            histograms['h_ld_Crn_mtt600to800_cosTSA_gt_0p7'].Fill(ld_Crn)
            histograms['h_ld_Crr_mtt600to800_cosTSA_gt_0p7'].Fill(ld_Crr)
            histograms['h_ld_Crk_mtt600to800_cosTSA_gt_0p7'].Fill(ld_Crk)
            histograms['h_ld_Ckn_mtt600to800_cosTSA_gt_0p7'].Fill(ld_Ckn)
            histograms['h_ld_Ckr_mtt600to800_cosTSA_gt_0p7'].Fill(ld_Ckr)
            histograms['h_ld_Ckk_mtt600to800_cosTSA_gt_0p7'].Fill(ld_Ckk)
            histograms['h_ld_trC_mtt600to800_cosTSA_gt_0p7'].Fill(ld_trC)
            histograms['h_ld_cHel_mtt600to800_cosTSA_gt_0p7'].Fill(ld_cHel)
            histograms['h_ld_cHel_P3n_mtt600to800_cosTSA_gt_0p7'].Fill(ld_cHel_P3n)
    elif m_tt > 800:
        histograms['h_cos_theta1n_antilepton_mtt800toInf'].Fill(cos_theta1n_antilepton)
        histograms['h_cos_theta1r_antilepton_mtt800toInf'].Fill(cos_theta1r_antilepton)
        histograms['h_cos_theta1k_antilepton_mtt800toInf'].Fill(cos_theta1k_antilepton)
        histograms['h_cos_theta1rStar_antilepton_mtt800toInf'].Fill(cos_theta1rStar_antilepton)
        histograms['h_cos_theta1kStar_antilepton_mtt800toInf'].Fill(cos_theta1kStar_antilepton)
        histograms['h_cos_theta2n_lepton_mtt800toInf'].Fill(cos_theta2n_lepton)
        histograms['h_cos_theta2r_lepton_mtt800toInf'].Fill(cos_theta2r_lepton)
        histograms['h_cos_theta2k_lepton_mtt800toInf'].Fill(cos_theta2k_lepton)
        histograms['h_cos_theta2rStar_lepton_mtt800toInf'].Fill(cos_theta2rStar_lepton)
        histograms['h_cos_theta2kStar_lepton_mtt800toInf'].Fill(cos_theta2kStar_lepton)
        histograms['h_lb_cos_theta1n_mtt800toInf'].Fill(lb_cos_theta1n)
        histograms['h_lb_cos_theta1r_mtt800toInf'].Fill(lb_cos_theta1r)
        histograms['h_lb_cos_theta1k_mtt800toInf'].Fill(lb_cos_theta1k)
        histograms['h_lb_cos_theta1rStar_mtt800toInf'].Fill(lb_cos_theta1rStar)
        histograms['h_lb_cos_theta1kStar_mtt800toInf'].Fill(lb_cos_theta1kStar)
        histograms['h_lb_cos_theta2n_mtt800toInf'].Fill(lb_cos_theta2n)
        histograms['h_lb_cos_theta2r_mtt800toInf'].Fill(lb_cos_theta2r)
        histograms['h_lb_cos_theta2k_mtt800toInf'].Fill(lb_cos_theta2k)
        histograms['h_lb_cos_theta2rStar_mtt800toInf'].Fill(lb_cos_theta2rStar)
        histograms['h_lb_cos_theta2kStar_mtt800toInf'].Fill(lb_cos_theta2kStar)
        histograms['h_lb_Cnn_mtt800toInf'].Fill(lb_Cnn)
        histograms['h_lb_Cnr_mtt800toInf'].Fill(lb_Cnr)
        histograms['h_lb_Cnk_mtt800toInf'].Fill(lb_Cnk)
        histograms['h_lb_Crn_mtt800toInf'].Fill(lb_Crn)
        histograms['h_lb_Crr_mtt800toInf'].Fill(lb_Crr)
        histograms['h_lb_Crk_mtt800toInf'].Fill(lb_Crk)
        histograms['h_lb_Ckn_mtt800toInf'].Fill(lb_Ckn)
        histograms['h_lb_Ckr_mtt800toInf'].Fill(lb_Ckr)
        histograms['h_lb_Ckk_mtt800toInf'].Fill(lb_Ckk)
        histograms['h_lb_trC_mtt800toInf'].Fill(lb_trC)
        histograms['h_lb_cHel_mtt800toInf'].Fill(lb_cHel)
        histograms['h_lb_cHel_P3n_mtt800toInf'].Fill(lb_cHel_P3n)
        histograms['h_ld_cos_theta1n_mtt800toInf'].Fill(ld_cos_theta1n)
        histograms['h_ld_cos_theta1r_mtt800toInf'].Fill(ld_cos_theta1r)
        histograms['h_ld_cos_theta1k_mtt800toInf'].Fill(ld_cos_theta1k)
        histograms['h_ld_cos_theta1rStar_mtt800toInf'].Fill(ld_cos_theta1rStar)
        histograms['h_ld_cos_theta1kStar_mtt800toInf'].Fill(ld_cos_theta1kStar)
        histograms['h_ld_cos_theta2n_mtt800toInf'].Fill(ld_cos_theta2n)
        histograms['h_ld_cos_theta2r_mtt800toInf'].Fill(ld_cos_theta2r)
        histograms['h_ld_cos_theta2k_mtt800toInf'].Fill(ld_cos_theta2k)
        histograms['h_ld_cos_theta2rStar_mtt800toInf'].Fill(ld_cos_theta2rStar)
        histograms['h_ld_cos_theta2kStar_mtt800toInf'].Fill(ld_cos_theta2kStar)
        histograms['h_ld_Cnn_mtt800toInf'].Fill(ld_Cnn)
        histograms['h_ld_Cnr_mtt800toInf'].Fill(ld_Cnr)
        histograms['h_ld_Cnk_mtt800toInf'].Fill(ld_Cnk)
        histograms['h_ld_Crn_mtt800toInf'].Fill(ld_Crn)
        histograms['h_ld_Crr_mtt800toInf'].Fill(ld_Crr)
        histograms['h_ld_Crk_mtt800toInf'].Fill(ld_Crk)
        histograms['h_ld_Ckn_mtt800toInf'].Fill(ld_Ckn)
        histograms['h_ld_Ckr_mtt800toInf'].Fill(ld_Ckr)
        histograms['h_ld_Ckk_mtt800toInf'].Fill(ld_Ckk)
        histograms['h_ld_trC_mtt800toInf'].Fill(ld_trC)
        histograms['h_ld_cHel_mtt800toInf'].Fill(ld_cHel)
        histograms['h_ld_cHel_P3n_mtt800toInf'].Fill(ld_cHel_P3n)
        if abs(cosTSA) < 0.4:
            histograms['h_cos_theta1n_antilepton_mtt800toInf_cosTSA_lt_0p4'].Fill(cos_theta1n_antilepton)
            histograms['h_cos_theta1r_antilepton_mtt800toInf_cosTSA_lt_0p4'].Fill(cos_theta1r_antilepton)
            histograms['h_cos_theta1k_antilepton_mtt800toInf_cosTSA_lt_0p4'].Fill(cos_theta1k_antilepton)
            histograms['h_cos_theta1rStar_antilepton_mtt800toInf_cosTSA_lt_0p4'].Fill(cos_theta1rStar_antilepton)
            histograms['h_cos_theta1kStar_antilepton_mtt800toInf_cosTSA_lt_0p4'].Fill(cos_theta1kStar_antilepton)
            histograms['h_cos_theta2n_lepton_mtt800toInf_cosTSA_lt_0p4'].Fill(cos_theta2n_lepton)
            histograms['h_cos_theta2r_lepton_mtt800toInf_cosTSA_lt_0p4'].Fill(cos_theta2r_lepton)
            histograms['h_cos_theta2k_lepton_mtt800toInf_cosTSA_lt_0p4'].Fill(cos_theta2k_lepton)
            histograms['h_cos_theta2rStar_lepton_mtt800toInf_cosTSA_lt_0p4'].Fill(cos_theta2rStar_lepton)
            histograms['h_cos_theta2kStar_lepton_mtt800toInf_cosTSA_lt_0p4'].Fill(cos_theta2kStar_lepton)
            histograms['h_lb_cos_theta1n_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_cos_theta1n)
            histograms['h_lb_cos_theta1r_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_cos_theta1r)
            histograms['h_lb_cos_theta1k_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_cos_theta1k)
            histograms['h_lb_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_cos_theta1rStar)
            histograms['h_lb_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_cos_theta1kStar)
            histograms['h_lb_cos_theta2n_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_cos_theta2n)
            histograms['h_lb_cos_theta2r_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_cos_theta2r)
            histograms['h_lb_cos_theta2k_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_cos_theta2k)
            histograms['h_lb_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_cos_theta2rStar)
            histograms['h_lb_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_cos_theta2kStar)
            histograms['h_lb_Cnn_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_Cnn)
            histograms['h_lb_Cnr_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_Cnr)
            histograms['h_lb_Cnk_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_Cnk)
            histograms['h_lb_Crn_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_Crn)
            histograms['h_lb_Crr_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_Crr)
            histograms['h_lb_Crk_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_Crk)
            histograms['h_lb_Ckn_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_Ckn)
            histograms['h_lb_Ckr_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_Ckr)
            histograms['h_lb_Ckk_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_Ckk)
            histograms['h_lb_trC_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_trC)
            histograms['h_lb_cHel_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_cHel)
            histograms['h_lb_cHel_P3n_mtt800toInf_cosTSA_lt_0p4'].Fill(lb_cHel_P3n)
            histograms['h_ld_cos_theta1n_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_cos_theta1n)
            histograms['h_ld_cos_theta1r_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_cos_theta1r)
            histograms['h_ld_cos_theta1k_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_cos_theta1k)
            histograms['h_ld_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_cos_theta1rStar)
            histograms['h_ld_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_cos_theta1kStar)
            histograms['h_ld_cos_theta2n_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_cos_theta2n)
            histograms['h_ld_cos_theta2r_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_cos_theta2r)
            histograms['h_ld_cos_theta2k_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_cos_theta2k)
            histograms['h_ld_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_cos_theta2rStar)
            histograms['h_ld_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_cos_theta2kStar)
            histograms['h_ld_Cnn_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_Cnn)
            histograms['h_ld_Cnr_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_Cnr)
            histograms['h_ld_Cnk_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_Cnk)
            histograms['h_ld_Crn_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_Crn)
            histograms['h_ld_Crr_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_Crr)
            histograms['h_ld_Crk_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_Crk)
            histograms['h_ld_Ckn_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_Ckn)
            histograms['h_ld_Ckr_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_Ckr)
            histograms['h_ld_Ckk_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_Ckk)
            histograms['h_ld_trC_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_trC)
            histograms['h_ld_cHel_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_cHel)
            histograms['h_ld_cHel_P3n_mtt800toInf_cosTSA_lt_0p4'].Fill(ld_cHel_P3n)
        if abs(cosTSA) < 0.7:
            histograms['h_cos_theta1n_antilepton_mtt800toInf_cosTSA_lt_0p7'].Fill(cos_theta1n_antilepton)
            histograms['h_cos_theta1r_antilepton_mtt800toInf_cosTSA_lt_0p7'].Fill(cos_theta1r_antilepton)
            histograms['h_cos_theta1k_antilepton_mtt800toInf_cosTSA_lt_0p7'].Fill(cos_theta1k_antilepton)
            histograms['h_cos_theta1rStar_antilepton_mtt800toInf_cosTSA_lt_0p7'].Fill(cos_theta1rStar_antilepton)
            histograms['h_cos_theta1kStar_antilepton_mtt800toInf_cosTSA_lt_0p7'].Fill(cos_theta1kStar_antilepton)
            histograms['h_cos_theta2n_lepton_mtt800toInf_cosTSA_lt_0p7'].Fill(cos_theta2n_lepton)
            histograms['h_cos_theta2r_lepton_mtt800toInf_cosTSA_lt_0p7'].Fill(cos_theta2r_lepton)
            histograms['h_cos_theta2k_lepton_mtt800toInf_cosTSA_lt_0p7'].Fill(cos_theta2k_lepton)
            histograms['h_cos_theta2rStar_lepton_mtt800toInf_cosTSA_lt_0p7'].Fill(cos_theta2rStar_lepton)
            histograms['h_cos_theta2kStar_lepton_mtt800toInf_cosTSA_lt_0p7'].Fill(cos_theta2kStar_lepton)
            histograms['h_lb_cos_theta1n_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_cos_theta1n)
            histograms['h_lb_cos_theta1r_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_cos_theta1r)
            histograms['h_lb_cos_theta1k_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_cos_theta1k)
            histograms['h_lb_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_cos_theta1rStar)
            histograms['h_lb_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_cos_theta1kStar)
            histograms['h_lb_cos_theta2n_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_cos_theta2n)
            histograms['h_lb_cos_theta2r_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_cos_theta2r)
            histograms['h_lb_cos_theta2k_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_cos_theta2k)
            histograms['h_lb_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_cos_theta2rStar)
            histograms['h_lb_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_cos_theta2kStar)
            histograms['h_lb_Cnn_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_Cnn)
            histograms['h_lb_Cnr_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_Cnr)
            histograms['h_lb_Cnk_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_Cnk)
            histograms['h_lb_Crn_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_Crn)
            histograms['h_lb_Crr_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_Crr)
            histograms['h_lb_Crk_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_Crk)
            histograms['h_lb_Ckn_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_Ckn)
            histograms['h_lb_Ckr_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_Ckr)
            histograms['h_lb_Ckk_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_Ckk)
            histograms['h_lb_trC_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_trC)
            histograms['h_lb_cHel_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_cHel)
            histograms['h_lb_cHel_P3n_mtt800toInf_cosTSA_lt_0p7'].Fill(lb_cHel_P3n)
            histograms['h_ld_cos_theta1n_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_cos_theta1n)
            histograms['h_ld_cos_theta1r_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_cos_theta1r)
            histograms['h_ld_cos_theta1k_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_cos_theta1k)
            histograms['h_ld_cos_theta1rStar_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_cos_theta1rStar)
            histograms['h_ld_cos_theta1kStar_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_cos_theta1kStar)
            histograms['h_ld_cos_theta2n_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_cos_theta2n)
            histograms['h_ld_cos_theta2r_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_cos_theta2r)
            histograms['h_ld_cos_theta2k_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_cos_theta2k)
            histograms['h_ld_cos_theta2rStar_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_cos_theta2rStar)
            histograms['h_ld_cos_theta2kStar_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_cos_theta2kStar)
            histograms['h_ld_Cnn_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_Cnn)
            histograms['h_ld_Cnr_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_Cnr)
            histograms['h_ld_Cnk_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_Cnk)
            histograms['h_ld_Crn_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_Crn)
            histograms['h_ld_Crr_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_Crr)
            histograms['h_ld_Crk_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_Crk)
            histograms['h_ld_Ckn_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_Ckn)
            histograms['h_ld_Ckr_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_Ckr)
            histograms['h_ld_Ckk_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_Ckk)
            histograms['h_ld_trC_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_trC)
            histograms['h_ld_cHel_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_cHel)
            histograms['h_ld_cHel_P3n_mtt800toInf_cosTSA_lt_0p7'].Fill(ld_cHel_P3n)
        if abs(cosTSA) > 0.7:
            histograms['h_cos_theta1n_antilepton_mtt800toInf_cosTSA_gt_0p7'].Fill(cos_theta1n_antilepton)
            histograms['h_cos_theta1r_antilepton_mtt800toInf_cosTSA_gt_0p7'].Fill(cos_theta1r_antilepton)
            histograms['h_cos_theta1k_antilepton_mtt800toInf_cosTSA_gt_0p7'].Fill(cos_theta1k_antilepton)
            histograms['h_cos_theta1rStar_antilepton_mtt800toInf_cosTSA_gt_0p7'].Fill(cos_theta1rStar_antilepton)
            histograms['h_cos_theta1kStar_antilepton_mtt800toInf_cosTSA_gt_0p7'].Fill(cos_theta1kStar_antilepton)
            histograms['h_cos_theta2n_lepton_mtt800toInf_cosTSA_gt_0p7'].Fill(cos_theta2n_lepton)
            histograms['h_cos_theta2r_lepton_mtt800toInf_cosTSA_gt_0p7'].Fill(cos_theta2r_lepton)
            histograms['h_cos_theta2k_lepton_mtt800toInf_cosTSA_gt_0p7'].Fill(cos_theta2k_lepton)
            histograms['h_cos_theta2rStar_lepton_mtt800toInf_cosTSA_gt_0p7'].Fill(cos_theta2rStar_lepton)
            histograms['h_cos_theta2kStar_lepton_mtt800toInf_cosTSA_gt_0p7'].Fill(cos_theta2kStar_lepton)
            histograms['h_lb_cos_theta1n_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_cos_theta1n)
            histograms['h_lb_cos_theta1r_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_cos_theta1r)
            histograms['h_lb_cos_theta1k_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_cos_theta1k)
            histograms['h_lb_cos_theta1rStar_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_cos_theta1rStar)
            histograms['h_lb_cos_theta1kStar_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_cos_theta1kStar)
            histograms['h_lb_cos_theta2n_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_cos_theta2n)
            histograms['h_lb_cos_theta2r_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_cos_theta2r)
            histograms['h_lb_cos_theta2k_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_cos_theta2k)
            histograms['h_lb_cos_theta2rStar_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_cos_theta2rStar)
            histograms['h_lb_cos_theta2kStar_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_cos_theta2kStar)
            histograms['h_lb_Cnn_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_Cnn)
            histograms['h_lb_Cnr_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_Cnr)
            histograms['h_lb_Cnk_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_Cnk)
            histograms['h_lb_Crn_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_Crn)
            histograms['h_lb_Crr_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_Crr)
            histograms['h_lb_Crk_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_Crk)
            histograms['h_lb_Ckn_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_Ckn)
            histograms['h_lb_Ckr_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_Ckr)
            histograms['h_lb_Ckk_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_Ckk)
            histograms['h_lb_trC_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_trC)
            histograms['h_lb_cHel_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_cHel)
            histograms['h_lb_cHel_P3n_mtt800toInf_cosTSA_gt_0p7'].Fill(lb_cHel_P3n)
            histograms['h_ld_cos_theta1n_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_cos_theta1n)
            histograms['h_ld_cos_theta1r_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_cos_theta1r)
            histograms['h_ld_cos_theta1k_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_cos_theta1k)
            histograms['h_ld_cos_theta1rStar_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_cos_theta1rStar)
            histograms['h_ld_cos_theta1kStar_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_cos_theta1kStar)
            histograms['h_ld_cos_theta2n_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_cos_theta2n)
            histograms['h_ld_cos_theta2r_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_cos_theta2r)
            histograms['h_ld_cos_theta2k_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_cos_theta2k)
            histograms['h_ld_cos_theta2rStar_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_cos_theta2rStar)
            histograms['h_ld_cos_theta2kStar_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_cos_theta2kStar)
            histograms['h_ld_Cnn_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_Cnn)
            histograms['h_ld_Cnr_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_Cnr)
            histograms['h_ld_Cnk_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_Cnk)
            histograms['h_ld_Crn_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_Crn)
            histograms['h_ld_Crr_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_Crr)
            histograms['h_ld_Crk_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_Crk)
            histograms['h_ld_Ckn_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_Ckn)
            histograms['h_ld_Ckr_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_Ckr)
            histograms['h_ld_Ckk_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_Ckk)
            histograms['h_ld_trC_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_trC)
            histograms['h_ld_cHel_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_cHel)
            histograms['h_ld_cHel_P3n_mtt800toInf_cosTSA_gt_0p7'].Fill(ld_cHel_P3n)

       
    return tops, antitops, bottom_quarks, antibottom_quarks, hadronic_bottom_quarks, hadronic_antibottom_quarks, Wplus, Wminus, leptons, antiLeptons, neutrinos, antiNeutrinos, utype_quarks, antiUtype_quarks, dtype_quarks, antiDtype_quarks


if __name__ == "__main__":
    # impose correct usage
    if len(sys.argv) < 2:
        print("Usage: python EFT_nanoGen.py <input file>")
        sys.exit(1)
    input_filename = sys.argv[1]

    # Output directory
    output_dir = "/data/dust/user/ricardo/EFT/nanoGen/CMSSW_14_1_0_pre4/src/PowhegPythia8_NLO/UL17/root_files/entanglement/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    ### call analyze function for input file ###
    ############################################
    histograms = analyze(input_filename)
    
    # Setup output file
    output_filename = os.path.basename(input_filename)
    output_file_path = os.path.join(output_dir, output_filename)
    output_file = ROOT.TFile(output_file_path, "RECREATE")

    # Write histograms to output file
    for name, hist in list(histograms.items()):
        hist.SetDirectory(output_file)
        hist.Write()
    output_file.Close()
    print("created output file: {}".format(output_file_path))