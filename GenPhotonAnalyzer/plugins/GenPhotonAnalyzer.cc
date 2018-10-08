// -*- C++ -*-
//
// Package:    GenPhotonAnalyzer/GenPhotonAnalyzer
// Class:      GenPhotonAnalyzer
// 
/**\class GenPhotonAnalyzer GenPhotonAnalyzer.cc GenPhotonAnalyzer/GenPhotonAnalyzer/plugins/GenPhotonAnalyzer.cc

 Description: Analyze generated photons

 Implementation:
     Following methods used by StopTupleMaker
*/
//
// Original Author:  caleb smith
//         Created:  Mon, 08 Oct 2018 16:27:52 GMT
//
//



// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class GenPhotonAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit GenPhotonAnalyzer(const edm::ParameterSet&);
      ~GenPhotonAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
      edm::InputTag genParCollection;
      edm::EDGetTokenT<edm::View<reco::GenParticle>> genParTok_;
      edm::Service<TFileService> fs;

      // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
GenPhotonAnalyzer::GenPhotonAnalyzer(const edm::ParameterSet& iConfig):
   genParCollection(iConfig.getUntrackedParameter<edm::InputTag>("genParCollection")),
   genParTok_(consumes<edm::View<reco::GenParticle>>(genParCollection))
{
   //now do what ever initialization is needed
   usesResource("TFileService");

}


GenPhotonAnalyzer::~GenPhotonAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
GenPhotonAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

#ifdef GEN_PHOTONS
   genParCollection = cms.untracked.InputTag("prunedGenParticles");
   genParCollection(iConfig.getUntrackedParameter<InputTag>("genParCollection"));
   genParTok_(consumes<View<reco::GenParticle>>(genParCollection));
   Handle< View<reco::GenParticle> > genParticles;
   iEvent.getByToken( genParTok_,genParticles);
#endif

#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif
   
#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
#endif
}


// ------------ method called once each job just before starting event loop  ------------
void 
GenPhotonAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
GenPhotonAnalyzer::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GenPhotonAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(GenPhotonAnalyzer);
