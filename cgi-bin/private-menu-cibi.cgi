#!\Perl64\bin\perl

use utf8;
use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use XML::LibXML;
use BaseFunctions;
use MenuFunctions;

#Inizializzazione variabili base
my $q = new CGI;
my $session = CGI::Session->load() or die $!;

BaseFunctions::checkSession($session);

my %path = (   add_piatto => 'add-piatto.cgi',
               add_portata => 'add-portata.cgi', # manca
               mod_piatto => 'mod-piatto.cgi',
               del_piatto => 'private-menu-cibi.cgi',
);

BaseFunctions::printStartHtml('Cibi - Men&ugrave; - Area Riservata');

my $message = checkDelete();

print $q->a({-href => 'private-menu.cgi'}, 'Torna alle categorie men&ugrave;');

print "<p>$message</p>";

MenuFunctions::printMenuCibi(1, \%path);

BaseFunctions::printEndHtml();


# Subroutines

sub checkDelete{
   if ($q->param('rimuovi')){
      
      # Raccolta parametri
      my $idPiatto = $q->param('idPiatto');
      my $nome = $q->param('nome');
      
      if (BaseFunctions::existElement("menu/cibo/portata/piatto[\@id = '$idPiatto']")) {
         # Init LibXML
         my $doc = BaseFunctions::initLibXML();
         my ($element) = $doc->findnodes("menu/cibo/portata/piatto[\@id = '$idPiatto']");
         $element->unbindNode;
         
         # Scrivo sul file
         BaseFunctions::writeFile($doc);
      
         return "Rimozione del piatto $nome effettuata con successo";
      }
      else {
      
         return "Rimozione del piatto $nome non effettuata!!!"
      }
   }
}

exit 0;