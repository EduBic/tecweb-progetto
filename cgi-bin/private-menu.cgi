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

BaseFunctions::printStartHtml('Categorie - Men&ugrave; - Area Riservata');

   print $q->h3('Categorie men&ugrave;');
   print $q->p('Scegli la categoria');
   
   print "<ul>
            <li><a href='private-menu-cibi.cgi'>Cibi</a></li>
            <li><a href='private-menu-bevande.cgi'>Bevande</a></li>
            <li><a href='private-menu-fissi.cgi'>Men&ugrave; fissi</a></li>
         </ul>";
         
   # Spazio pubblicitario dei piatti che cambiano grazie a javascript

BaseFunctions::printEndHtml();

exit 0;
