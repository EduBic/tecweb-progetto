#!\Perl64\bin\perl

# N.B. Alcuni documenti per questioni di sicurezza mettevano nel preambolo dopo \perl: '-Tw', ciò però non linka più BaseFunctions.
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

my @input = (  'aggiungi', # name of submit Aggiungi [0]
               'portata',  # name of hidden $nomeportata [1]
               'modifica', # name of submit Modifica [2]
               'idPiatto', # name of hidden $piatto [3]
               'rimuovi',  # name of submit Rimuovi [4]
               'idPiatto', # name of hidden $piatto [5]
);

BaseFunctions::printStartHtml('Men&ugrave; - Area Riservata');

checkDelete();

MenuFunctions::printMenu(1, @input);

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
