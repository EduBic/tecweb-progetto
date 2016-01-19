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

BaseFunctions::printStartHtml('Men&ugrave; - Area Riservata');

   print "<a href='private-menu-cibi.cgi'>CIBI</a> <br />
            <a href='private-menu-bevande.cgi'>BEVANDE</a> <br />
            <a href='private-menu-fissi.cgi'>MENU FISSI</a>";

BaseFunctions::printEndHtml();

exit 0;
