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

BaseFunctions::printStartHtml('Men&ugrave; - Area Riservata');

checkDelete();

MenuFunctions::printMenuCibi(1, \%path);

BaseFunctions::printEndHtml();


# Subroutines

sub checkDelete{
   if ($q->param('rimuovi')){
      #Rimuovi piatto nei param
      #display comment
      my $idPiatto = $q->param('idPiatto');
      print "cancellato piatto: $idPiatto";
   }
}

exit 0;