#!\Perl64\bin\perl

use utf8;
use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use XML::LibXML;
use BaseFunctions;


#checkSession();

#Inizializzazione variabili base
my $q = new CGI; # Sarà il parametro $_[0] di ogni funzione

BaseFunctions::printStartHtml($q, 'Aggiungi portata - Area Riservata');

# Verifica parametri
if ($q->param()){
   # è stato premuto il pulsante conferma. Scrivere l'xml
   display_results($q);
}
else {
   #mostra la form - si vuole aggiungere una portata.
}

# new code...
   print $q->h3("pagina add-portata.cgi");

BaseFunctions::printEndHtml($q);

exit 0;
