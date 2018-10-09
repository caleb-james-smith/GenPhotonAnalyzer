import FWCore.ParameterSet.Config as cms

process = cms.Process("Analyzer")

process.TFileService = cms.Service("TFileService",
               fileName = cms.string("output.root"),
               )

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'root://xrootd.unl.edu//store/mc/RunIISummer16MiniAODv2/GJets_DR-0p4_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_qcut19_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/FC894077-2DCA-E611-8008-002590DE6E3C.root'
    )
)

#process.analyzer = cms.EDAnalyzer('GenPhotonAnalyzer'
#)
process.load("GenPhotonAnalyzer.GenPhotonAnalyzer.CfiFile_cfi")

process.p = cms.Path(process.analyzer)


