#!\Perl64\bin\perl

use utf8;
use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use XML::LibXML;
use BaseFunctions;

my $session = CGI::Session->load() or die $!;

BaseFunctions::checkSession($session);

#Inizializzazione variabili base
my $q = new CGI; # Sarà il parametro $_[0] di ogni funzione

BaseFunctions::printStartHtml($q, 'Aggiungi Piatto - Area Riservata');

# Verifica parametri
if ($q->param('conferma')){
   print "Scrivo l'xml";
   # è stato premuto il pulsante conferma. Scrivere l'xml
}
elsif($q->param('portata')) {
   print $q->h2("Aggiungi un piatto alla portata: ".$q->param('portata'));
   #mostra quale modifica si sta facendo: sto aggiungendo piatto a portata 'x'
   #mostra la form - si vuole aggiungere un piatto.
}

# new code...

BaseFunctions::printEndHtml($q);

exit 0;
