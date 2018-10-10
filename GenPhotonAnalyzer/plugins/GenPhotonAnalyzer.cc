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
      TH1F * genEta_eta5;                       
      TH1F * genEta_eta5_pt200;                  
      TH1F * genEta_eta5_pt200_pdgid22;          
      TH1F * genEta_eta5_pt200_pdgid22_status1;  
      TH1F * genEta_eta5_pt200_pdgid22_status2;  
      TH1F * genEta_eta5_pt200_pdgid22_status21; 
      TH1F * genEta_eta5_pt200_pdgid22_status22; 
      TH1F * genEta_eta5_pt200_pdgid22_status23; 
      TH1F * genEta_eta5_pt200_pdgid22_status24; 

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
    
    // create histograms
    printf("- Creating histograms\n");
    
    genEta_eta5                       =  fs->make<TH1F>("genEta_eta5","genEta_eta5", 100, -5.0, 5.0);
    genEta_eta5_pt200                  =  fs->make<TH1F>("genEta_eta5_pt200","genEta_eta5_pt200", 100, -5.0, 5.0);
    genEta_eta5_pt200_pdgid22          =  fs->make<TH1F>("genEta_eta5_pt200_pdgid22","genEta_eta5_pt200_pdgid22", 100, -5.0, 5.0);
    genEta_eta5_pt200_pdgid22_status1  =  fs->make<TH1F>("genEta_eta5_pt200_pdgid22_status1","genEta_eta5_pt200_pdgid22_status1", 100, -5.0, 5.0);
    genEta_eta5_pt200_pdgid22_status2  =  fs->make<TH1F>("genEta_eta5_pt200_pdgid22_status2","genEta_eta5_pt200_pdgid22_status2", 100, -5.0, 5.0);
    genEta_eta5_pt200_pdgid22_status21 =  fs->make<TH1F>("genEta_eta5_pt200_pdgid22_status21","genEta_eta5_pt200_pdgid22_status21", 100, -5.0, 5.0);
    genEta_eta5_pt200_pdgid22_status22 =  fs->make<TH1F>("genEta_eta5_pt200_pdgid22_status22","genEta_eta5_pt200_pdgid22_status22", 100, -5.0, 5.0);
    genEta_eta5_pt200_pdgid22_status23 =  fs->make<TH1F>("genEta_eta5_pt200_pdgid22_status23","genEta_eta5_pt200_pdgid22_status23", 100, -5.0, 5.0);
    genEta_eta5_pt200_pdgid22_status24 =  fs->make<TH1F>("genEta_eta5_pt200_pdgid22_status24","genEta_eta5_pt200_pdgid22_status24", 100, -5.0, 5.0);

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

   Handle< View<reco::GenParticle> > genParticles;
   iEvent.getByToken( genParTok_,genParticles);
   //if ( i % 100 == 0)  printf("Processing event %d\n", i);
   // behave's like an iterator
   // get the values from the TTreeReaderValues
  if (genParticles.isValid()){
    for(unsigned int ig = 0; ig < genParticles->size(); ig++) {
        float genEta = genParticles->at(ig).eta();
        float genPhi = genParticles->at(ig).phi();
        float genPt = genParticles->at(ig).pt();
        int genPdgId = genParticles->at(ig).pdgId();
        int genStatus = genParticles->at(ig).status();
        if (genEta < 5.0)
        {
            genEta_eta5->Fill(genEta);
            if (genPt > 200.0)
            {
                genEta_eta5_pt200->Fill(genEta);
                if (genPdgId == 22)
                {
                    genEta_eta5_pt200_pdgid22->Fill(genEta);
                    if (genStatus == 1)  genEta_eta5_pt200_pdgid22_status1->Fill(genEta);
                    if (genStatus == 2)  genEta_eta5_pt200_pdgid22_status2->Fill(genEta);
                    if (genStatus == 21) genEta_eta5_pt200_pdgid22_status21->Fill(genEta);
                    if (genStatus == 22) genEta_eta5_pt200_pdgid22_status22->Fill(genEta);
                    if (genStatus == 23) genEta_eta5_pt200_pdgid22_status23->Fill(genEta);
                    if (genStatus == 24) genEta_eta5_pt200_pdgid22_status24->Fill(genEta);
                }
            }
        }
    }
  }
   
        

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
