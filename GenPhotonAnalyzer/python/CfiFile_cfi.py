import FWCore.ParameterSet.Config as cms

analyzer = cms.EDAnalyzer('GenPhotonAnalyzer',
                  genParCollection = cms.untracked.InputTag("prunedGenParticles")
)

