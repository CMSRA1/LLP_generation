# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/SUS-RunIISummer15GS-00208-fragment_custom.py --fileout file:custom_GEN-SIM.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,SimG4Core/CustomPhysics/Exotica_HSCP_SIM_cfi.customise,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step GEN,SIM --magField 38T_PostLS1 --python_filename custom_GEN-SIM_cfg.py --no_exec -n 135000 --customise_commands process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(135000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('Configuration/GenProduction/python/SUS-RunIISummer15GS-00208-fragment_custom.py nevts:135000'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:custom_GEN-SIM.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_71_V1::All', '')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    SLHAFileForPythia8 = cms.string('Configuration/Generator/data/HSCP_gluino_1000_SLHA.spc'),
    RandomizedParameters = cms.VPSet(cms.PSet(
        ConfigDescription = cms.string('T1qqqqLL_1000_200_10.000000'),
        GridpackPath = cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/SMS-GlGl/SMS-GlGl_mGl-1000_tarball.tar.xz'),
        SLHATableForPythia8 = cms.string('\nBLOCK MASS  # Mass Spectrum\n# PDG code           mass       particle\n   1000001     1.00000000E+05   # ~d_L\n   2000001     1.00000000E+05   # ~d_R\n   1000002     1.00000000E+05   # ~u_L\n   2000002     1.00000000E+05   # ~u_R\n   1000003     1.00000000E+05   # ~s_L\n   2000003     1.00000000E+05   # ~s_R\n   1000004     1.00000000E+05   # ~c_L\n   2000004     1.00000000E+05   # ~c_R\n   1000005     1.00000000E+05   # ~b_1\n   2000005     1.00000000E+05   # ~b_2\n   1000006     1.00000000E+05   # ~t_1\n   2000006     1.00000000E+05   # ~t_2\n   1000011     1.00000000E+05   # ~e_L\n   2000011     1.00000000E+05   # ~e_R\n   1000012     1.00000000E+05   # ~nu_eL\n   1000013     1.00000000E+05   # ~mu_L\n   2000013     1.00000000E+05   # ~mu_R\n   1000014     1.00000000E+05   # ~nu_muL\n   1000015     1.00000000E+05   # ~tau_1\n   2000015     1.00000000E+05   # ~tau_2\n   1000016     1.00000000E+05   # ~nu_tauL\n   1000021     1.000000e+03           # ~g\n   1000022     2.000000e+02           # ~chi_10\n   1000023     1.00000000E+05   # ~chi_20\n   1000025     1.00000000E+05   # ~chi_30\n   1000035     1.00000000E+05   # ~chi_40\n   1000024     1.00000000E+05   # ~chi_1+\n   1000037     1.00000000E+05   # ~chi_2+\n#\n# DECAY TABLE\n#         PDG            Width\nDECAY   1000001     0.00000000E+00   # sdown_L decays\nDECAY   2000001     0.00000000E+00   # sdown_R decays\nDECAY   1000002     0.00000000E+00   # sup_L decays\nDECAY   2000002     0.00000000E+00   # sup_R decays\nDECAY   1000003     0.00000000E+00   # sstrange_L decays\nDECAY   2000003     0.00000000E+00   # sstrange_R decays\nDECAY   1000004     0.00000000E+00   # scharm_L decays\nDECAY   2000004     0.00000000E+00   # scharm_R decays\nDECAY   1000005     0.00000000E+00   # sbottom1 decays\nDECAY   2000005     0.00000000E+00   # sbottom2 decays\nDECAY   1000006     0.00000000E+00   # stop1 decays\nDECAY   2000006     0.00000000E+00   # stop2 decays\nDECAY   1000011     0.00000000E+00   # selectron_L decays\nDECAY   2000011     0.00000000E+00   # selectron_R decays\nDECAY   1000012     0.00000000E+00   # snu_elL decays\nDECAY   1000013     0.00000000E+00   # smuon_L decays\nDECAY   2000013     0.00000000E+00   # smuon_R decays\nDECAY   1000014     0.00000000E+00   # snu_muL decays\nDECAY   1000015     0.00000000E+00   # stau_1 decays\nDECAY   2000015     0.00000000E+00   # stau_2 decays\nDECAY   1000016     0.00000000E+00   # snu_tauL decays\n##### gluino decays - no offshell decays needed\nDECAY   1000021     1.973270e-14   # gluino decays\n#           BR         NDA      ID1       ID2       ID3\n      2.50000000E-01    3     1000022        -1         1   # BR(~gl -> N1 ubar u)\n      2.50000000E-01    3     1000022        -2         2   # BR(~gl -> N1 dbar d)\n      2.50000000E-01    3     1000022        -3         3   # BR(~gl -> N1 cbar c)\n      2.50000000E-01    3     1000022        -4         4   # BR(~gl -> N1 sbar s)\nDECAY   1000022     0.00000000E+00   # neutralino1 decays\nDECAY   1000023     0.00000000E+00   # neutralino2 decays\nDECAY   1000024     0.00000000E+00   # chargino1+ decays\nDECAY   1000025     0.00000000E+00   # neutralino3 decays\nDECAY   1000035     0.00000000E+00   # neutralino4 decays\nDECAY   1000037     0.00000000E+00   # chargino2+ decays\n'),
        ConfigWeight = cms.double(46.5319148936),
        PythiaParameters = cms.PSet(
            pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
                'Main:timesAllowErrors = 10000', 
                'Check:epTolErr = 0.01', 
                'Beams:setProductionScalesFromLHEF = off', 
                'SLHA:keepSM = on', 
                'SLHA:minMassSM = 1000.', 
                'ParticleDecays:limitTau0 = on', 
                'ParticleDecays:tau0Max = 10', 
                'ParticleDecays:allowPhotonRadiation = on', 
                '1000021:tau0 = 1.000000e+01', 
                'ParticleDecays:tau0Max = 1000.1', 
                'LesHouches:setLifetime = 2', 
                'RHadrons:allow = on'),
            pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
                'Tune:ee 7', 
                'MultipartonInteractions:pT0Ref=2.4024', 
                'MultipartonInteractions:ecmPow=0.25208', 
                'MultipartonInteractions:expPow=1.6'),
            JetMatchingParameters = cms.vstring('JetMatching:setMad = off', 
                'JetMatching:scheme = 1', 
                'JetMatching:merge = on', 
                'JetMatching:jetAlgorithm = 2', 
                'JetMatching:etaJetMax = 5.', 
                'JetMatching:coneRadius = 1.', 
                'JetMatching:slowJetPower = 1', 
                'JetMatching:qCut = 140', 
                'JetMatching:nQmatch = 5', 
                'JetMatching:nJetMax = 2', 
                'JetMatching:doShowerKt = off', 
                '6:m0 = 172.5', 
                'Check:abortIfVeto = on'),
            parameterSets = cms.vstring('pythia8CommonSettings', 
                'pythia8CUEP8M1Settings', 
                'JetMatchingParameters')
        )
    ), 
        cms.PSet(
            ConfigDescription = cms.string('T1qqqqLL_1000_900_10.000000'),
            GridpackPath = cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/SMS-GlGl/SMS-GlGl_mGl-1000_tarball.tar.xz'),
            SLHATableForPythia8 = cms.string('\nBLOCK MASS  # Mass Spectrum\n# PDG code           mass       particle\n   1000001     1.00000000E+05   # ~d_L\n   2000001     1.00000000E+05   # ~d_R\n   1000002     1.00000000E+05   # ~u_L\n   2000002     1.00000000E+05   # ~u_R\n   1000003     1.00000000E+05   # ~s_L\n   2000003     1.00000000E+05   # ~s_R\n   1000004     1.00000000E+05   # ~c_L\n   2000004     1.00000000E+05   # ~c_R\n   1000005     1.00000000E+05   # ~b_1\n   2000005     1.00000000E+05   # ~b_2\n   1000006     1.00000000E+05   # ~t_1\n   2000006     1.00000000E+05   # ~t_2\n   1000011     1.00000000E+05   # ~e_L\n   2000011     1.00000000E+05   # ~e_R\n   1000012     1.00000000E+05   # ~nu_eL\n   1000013     1.00000000E+05   # ~mu_L\n   2000013     1.00000000E+05   # ~mu_R\n   1000014     1.00000000E+05   # ~nu_muL\n   1000015     1.00000000E+05   # ~tau_1\n   2000015     1.00000000E+05   # ~tau_2\n   1000016     1.00000000E+05   # ~nu_tauL\n   1000021     1.000000e+03           # ~g\n   1000022     9.000000e+02           # ~chi_10\n   1000023     1.00000000E+05   # ~chi_20\n   1000025     1.00000000E+05   # ~chi_30\n   1000035     1.00000000E+05   # ~chi_40\n   1000024     1.00000000E+05   # ~chi_1+\n   1000037     1.00000000E+05   # ~chi_2+\n#\n# DECAY TABLE\n#         PDG            Width\nDECAY   1000001     0.00000000E+00   # sdown_L decays\nDECAY   2000001     0.00000000E+00   # sdown_R decays\nDECAY   1000002     0.00000000E+00   # sup_L decays\nDECAY   2000002     0.00000000E+00   # sup_R decays\nDECAY   1000003     0.00000000E+00   # sstrange_L decays\nDECAY   2000003     0.00000000E+00   # sstrange_R decays\nDECAY   1000004     0.00000000E+00   # scharm_L decays\nDECAY   2000004     0.00000000E+00   # scharm_R decays\nDECAY   1000005     0.00000000E+00   # sbottom1 decays\nDECAY   2000005     0.00000000E+00   # sbottom2 decays\nDECAY   1000006     0.00000000E+00   # stop1 decays\nDECAY   2000006     0.00000000E+00   # stop2 decays\nDECAY   1000011     0.00000000E+00   # selectron_L decays\nDECAY   2000011     0.00000000E+00   # selectron_R decays\nDECAY   1000012     0.00000000E+00   # snu_elL decays\nDECAY   1000013     0.00000000E+00   # smuon_L decays\nDECAY   2000013     0.00000000E+00   # smuon_R decays\nDECAY   1000014     0.00000000E+00   # snu_muL decays\nDECAY   1000015     0.00000000E+00   # stau_1 decays\nDECAY   2000015     0.00000000E+00   # stau_2 decays\nDECAY   1000016     0.00000000E+00   # snu_tauL decays\n##### gluino decays - no offshell decays needed\nDECAY   1000021     1.973270e-14   # gluino decays\n#           BR         NDA      ID1       ID2       ID3\n      2.50000000E-01    3     1000022        -1         1   # BR(~gl -> N1 ubar u)\n      2.50000000E-01    3     1000022        -2         2   # BR(~gl -> N1 dbar d)\n      2.50000000E-01    3     1000022        -3         3   # BR(~gl -> N1 cbar c)\n      2.50000000E-01    3     1000022        -4         4   # BR(~gl -> N1 sbar s)\nDECAY   1000022     0.00000000E+00   # neutralino1 decays\nDECAY   1000023     0.00000000E+00   # neutralino2 decays\nDECAY   1000024     0.00000000E+00   # chargino1+ decays\nDECAY   1000025     0.00000000E+00   # neutralino3 decays\nDECAY   1000035     0.00000000E+00   # neutralino4 decays\nDECAY   1000037     0.00000000E+00   # chargino2+ decays\n'),
            ConfigWeight = cms.double(46.5319148936),
            PythiaParameters = cms.PSet(
                pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
                    'Main:timesAllowErrors = 10000', 
                    'Check:epTolErr = 0.01', 
                    'Beams:setProductionScalesFromLHEF = off', 
                    'SLHA:keepSM = on', 
                    'SLHA:minMassSM = 1000.', 
                    'ParticleDecays:limitTau0 = on', 
                    'ParticleDecays:tau0Max = 10', 
                    'ParticleDecays:allowPhotonRadiation = on', 
                    '1000021:tau0 = 1.000000e+01', 
                    'ParticleDecays:tau0Max = 1000.1', 
                    'LesHouches:setLifetime = 2', 
                    'RHadrons:allow = on'),
                pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
                    'Tune:ee 7', 
                    'MultipartonInteractions:pT0Ref=2.4024', 
                    'MultipartonInteractions:ecmPow=0.25208', 
                    'MultipartonInteractions:expPow=1.6'),
                JetMatchingParameters = cms.vstring('JetMatching:setMad = off', 
                    'JetMatching:scheme = 1', 
                    'JetMatching:merge = on', 
                    'JetMatching:jetAlgorithm = 2', 
                    'JetMatching:etaJetMax = 5.', 
                    'JetMatching:coneRadius = 1.', 
                    'JetMatching:slowJetPower = 1', 
                    'JetMatching:qCut = 140', 
                    'JetMatching:nQmatch = 5', 
                    'JetMatching:nJetMax = 2', 
                    'JetMatching:doShowerKt = off', 
                    '6:m0 = 172.5', 
                    'Check:abortIfVeto = on'),
                parameterSets = cms.vstring('pythia8CommonSettings', 
                    'pythia8CUEP8M1Settings', 
                    'JetMatchingParameters')
            )
        ), 
        cms.PSet(
            ConfigDescription = cms.string('T1qqqqLL_1800_200_10.000000'),
            GridpackPath = cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/SMS-GlGl/SMS-GlGl_mGl-1800_tarball.tar.xz'),
            SLHATableForPythia8 = cms.string('\nBLOCK MASS  # Mass Spectrum\n# PDG code           mass       particle\n   1000001     1.00000000E+05   # ~d_L\n   2000001     1.00000000E+05   # ~d_R\n   1000002     1.00000000E+05   # ~u_L\n   2000002     1.00000000E+05   # ~u_R\n   1000003     1.00000000E+05   # ~s_L\n   2000003     1.00000000E+05   # ~s_R\n   1000004     1.00000000E+05   # ~c_L\n   2000004     1.00000000E+05   # ~c_R\n   1000005     1.00000000E+05   # ~b_1\n   2000005     1.00000000E+05   # ~b_2\n   1000006     1.00000000E+05   # ~t_1\n   2000006     1.00000000E+05   # ~t_2\n   1000011     1.00000000E+05   # ~e_L\n   2000011     1.00000000E+05   # ~e_R\n   1000012     1.00000000E+05   # ~nu_eL\n   1000013     1.00000000E+05   # ~mu_L\n   2000013     1.00000000E+05   # ~mu_R\n   1000014     1.00000000E+05   # ~nu_muL\n   1000015     1.00000000E+05   # ~tau_1\n   2000015     1.00000000E+05   # ~tau_2\n   1000016     1.00000000E+05   # ~nu_tauL\n   1000021     1.800000e+03           # ~g\n   1000022     2.000000e+02           # ~chi_10\n   1000023     1.00000000E+05   # ~chi_20\n   1000025     1.00000000E+05   # ~chi_30\n   1000035     1.00000000E+05   # ~chi_40\n   1000024     1.00000000E+05   # ~chi_1+\n   1000037     1.00000000E+05   # ~chi_2+\n#\n# DECAY TABLE\n#         PDG            Width\nDECAY   1000001     0.00000000E+00   # sdown_L decays\nDECAY   2000001     0.00000000E+00   # sdown_R decays\nDECAY   1000002     0.00000000E+00   # sup_L decays\nDECAY   2000002     0.00000000E+00   # sup_R decays\nDECAY   1000003     0.00000000E+00   # sstrange_L decays\nDECAY   2000003     0.00000000E+00   # sstrange_R decays\nDECAY   1000004     0.00000000E+00   # scharm_L decays\nDECAY   2000004     0.00000000E+00   # scharm_R decays\nDECAY   1000005     0.00000000E+00   # sbottom1 decays\nDECAY   2000005     0.00000000E+00   # sbottom2 decays\nDECAY   1000006     0.00000000E+00   # stop1 decays\nDECAY   2000006     0.00000000E+00   # stop2 decays\nDECAY   1000011     0.00000000E+00   # selectron_L decays\nDECAY   2000011     0.00000000E+00   # selectron_R decays\nDECAY   1000012     0.00000000E+00   # snu_elL decays\nDECAY   1000013     0.00000000E+00   # smuon_L decays\nDECAY   2000013     0.00000000E+00   # smuon_R decays\nDECAY   1000014     0.00000000E+00   # snu_muL decays\nDECAY   1000015     0.00000000E+00   # stau_1 decays\nDECAY   2000015     0.00000000E+00   # stau_2 decays\nDECAY   1000016     0.00000000E+00   # snu_tauL decays\n##### gluino decays - no offshell decays needed\nDECAY   1000021     1.973270e-14   # gluino decays\n#           BR         NDA      ID1       ID2       ID3\n      2.50000000E-01    3     1000022        -1         1   # BR(~gl -> N1 ubar u)\n      2.50000000E-01    3     1000022        -2         2   # BR(~gl -> N1 dbar d)\n      2.50000000E-01    3     1000022        -3         3   # BR(~gl -> N1 cbar c)\n      2.50000000E-01    3     1000022        -4         4   # BR(~gl -> N1 sbar s)\nDECAY   1000022     0.00000000E+00   # neutralino1 decays\nDECAY   1000023     0.00000000E+00   # neutralino2 decays\nDECAY   1000024     0.00000000E+00   # chargino1+ decays\nDECAY   1000025     0.00000000E+00   # neutralino3 decays\nDECAY   1000035     0.00000000E+00   # neutralino4 decays\nDECAY   1000037     0.00000000E+00   # chargino2+ decays\n'),
            ConfigWeight = cms.double(37.7068965517),
            PythiaParameters = cms.PSet(
                pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
                    'Main:timesAllowErrors = 10000', 
                    'Check:epTolErr = 0.01', 
                    'Beams:setProductionScalesFromLHEF = off', 
                    'SLHA:keepSM = on', 
                    'SLHA:minMassSM = 1000.', 
                    'ParticleDecays:limitTau0 = on', 
                    'ParticleDecays:tau0Max = 10', 
                    'ParticleDecays:allowPhotonRadiation = on', 
                    '1000021:tau0 = 1.000000e+01', 
                    'ParticleDecays:tau0Max = 1000.1', 
                    'LesHouches:setLifetime = 2', 
                    'RHadrons:allow = on'),
                pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
                    'Tune:ee 7', 
                    'MultipartonInteractions:pT0Ref=2.4024', 
                    'MultipartonInteractions:ecmPow=0.25208', 
                    'MultipartonInteractions:expPow=1.6'),
                JetMatchingParameters = cms.vstring('JetMatching:setMad = off', 
                    'JetMatching:scheme = 1', 
                    'JetMatching:merge = on', 
                    'JetMatching:jetAlgorithm = 2', 
                    'JetMatching:etaJetMax = 5.', 
                    'JetMatching:coneRadius = 1.', 
                    'JetMatching:slowJetPower = 1', 
                    'JetMatching:qCut = 156', 
                    'JetMatching:nQmatch = 5', 
                    'JetMatching:nJetMax = 2', 
                    'JetMatching:doShowerKt = off', 
                    '6:m0 = 172.5', 
                    'Check:abortIfVeto = on'),
                parameterSets = cms.vstring('pythia8CommonSettings', 
                    'pythia8CUEP8M1Settings', 
                    'JetMatchingParameters')
            )
        )),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(1),
    PythiaParameters = cms.PSet(
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'),
        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'),
        processParameters = cms.vstring('SUSY:all = off', 
            'SUSY:gg2gluinogluino = on', 
            'SUSY:qqbar2gluinogluino = on', 
            'RHadrons:allow  = on', 
            'RHadrons:allowDecay = off', 
            'RHadrons:setMasses = on', 
            'RHadrons:probGluinoball = 0.5'),
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CUEP8M1Settings', 
            'processParameters')
    ),
    hscpFlavor = cms.untracked.string('gluino'),
    massPoint = cms.untracked.int32(1000),
    particleFile = cms.untracked.string('Configuration/Generator/data/particles_gluino_1000_GeV.txt'),
    slhaFile = cms.untracked.string('Configuration/Generator/data/HSCP_gluino_1000_SLHA.spc'),
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    pdtFile = cms.FileInPath('Configuration/Generator/data/hscppythiapdtgluino1000.tbl'),
    useregge = cms.bool(False)
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# Automatic addition of the customisation function from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi
from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi import customise 

#call to customisation function customise imported from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi
process = customise(process)

# End of customisation functions

# Customisation from command line
process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)