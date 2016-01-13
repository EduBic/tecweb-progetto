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

BaseFunctions::printStartHtml('Men&ugrave; - Area Riservata');

MenuFunctions::printMenu(0);

BaseFunctions::printEndHtml();

exit 0;
