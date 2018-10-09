import FWCore.ParameterSet.Config as cms

process = cms.Process("Analyzer")

# print less
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

process.TFileService = cms.Service("TFileService",
               fileName = cms.string("analyzer_output.root"),
               )

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        # GJets_DR-0p4_HT-40To100 
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FCF05520-5EBF-E611-8802-0CC47A4D7600.root",  
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F448447D-96BE-E611-9635-FA163ED6397C.root",
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EE9B765E-5DBF-E611-9CBF-A0000420FE80.root",
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EA5D8169-9EBE-E611-8EBD-D067E5F914D3.root",
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DEB55923-98BE-E611-B1DB-0CC47A13CC7A.root",
        # GJets_DR-0p4_HT-100To200
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FEDA0C6D-3BC0-E611-92F6-001E67A3EBD8.root", 
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FCE0E523-E5BE-E611-A6EE-5065F3819221.root",
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F84F2EC3-05BF-E611-B63C-001E6779258C.root",
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/ECE6E90F-28BE-E611-BB1C-001E67456F68.root",
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EA240025-1BBE-E611-9B3B-B083FED4239C.root",
        # GJets_DR-0p4_HT-200To400
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/FCC4E7CE-A3C9-E611-A535-0CC47A7EEE96.root",  
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/FC59FD17-7DCA-E611-A825-842B2B71F663.root",
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/FA7309AB-FDC9-E611-9C67-F04DA23BCE4C.root",
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/FA06A29F-7BC7-E611-8C0A-20CF3027A613.root",
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/F8D18491-F8C5-E611-9ED8-BC305B3909FE.root",
        # GJets_DR-0p4_HT-400To600
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/005FD45A-98DC-E611-A76A-0CC47A0109A6.root", 
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/0636A031-ABDB-E611-BF6F-008CFA197CA8.root",
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/14A86B9C-9FDB-E611-B1FC-0025905A48BC.root",
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/1A8322A3-54DD-E611-8A28-14187741136B.root",
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/1E87BF48-C5DB-E611-9280-0CC47A7C3610.root",
        # GJets_DR-0p4_HT-600ToInf 
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/FC894077-2DCA-E611-8008-002590DE6E3C.root", 
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/FA06D3DD-60C8-E611-A2A2-002590DE6E74.root",
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/F83A061B-07CB-E611-B519-7845C4F91633.root",
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/F669038F-B2C7-E611-B286-D067E5F91587.root",
        "root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/F401B244-A1C5-E611-96EA-D4AE527F338C.root"
    )
)

#process.analyzer = cms.EDAnalyzer('GenPhotonAnalyzer'
#)
process.load("GenPhotonAnalyzer.GenPhotonAnalyzer.CfiFile_cfi")

process.p = cms.Path(process.analyzer)


