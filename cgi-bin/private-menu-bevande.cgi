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

my %path = (   add_bevanda => 'add-bevanda.cgi',
               #add_listaBevande => 'add-portata.cgi', # manca
               mod_bevanda => 'mod-piatto.cgi',
               del_bevanda => 'private-menu-bevande.cgi',
);

BaseFunctions::printStartHtml('Men&ugrave; - Area Riservata');

checkDelete();

MenuFunctions::printMenuBevande(1, \%path, '/menu/bevande/listaVini', 'vino');
MenuFunctions::printMenuBevande(1, \%path, '/menu/bevande/listaBirre', 'birra');
MenuFunctions::printMenuBevande(1, \%path, '/menu/bevande/listaAltreBevande', 'bevanda');

BaseFunctions::printEndHtml();


# Subroutines

sub checkDelete{
   if ($q->param('rimuovi')){
      #Rimuovi piatto nei param
      #display comment
      my $idPiatto = $q->param('idPiatto');
      print "cancellata bevanda: $idPiatto";
   }
}

exit 0;