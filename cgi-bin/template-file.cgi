# Template di un file appartenente all'area riservata;

# N.B. Alcuni documenti per questioni di sicurezza mettevano nel preambolo dopo \perl: '-Tw', ciò però non linka più i moduli PM.
#!\Perl64\bin\perl

use utf8;
use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use XML::LibXML;
use BaseFunctions;


# Inizializzazione varaibili base
my $q = new CGI;
my $session = CGI::Session->load() or die $!;

checkSession($session);

BaseFunctions::printStartHtml('Men&ugrave; - Area Riservata');

# new code...

BaseFunctions::printEndHtml();

exit 0;
