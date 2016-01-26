#!\Perl64\bin\perl

#use utf8;
use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use Encode;



print "Content-type: text/html\n\n";

print "<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>
   <html xmlns='http://www.w3.org/1999/xhtml'>
   <head>
      <meta http-equiv='Content-Type' content='text/html; charset=utf-8' />
      <title> title </title>
   </head>
   <body>";

print "èùàòì";

my $stringa = "Involini è Sosia dis'minmiale";

   print "<p>stringa = ".$stringa."</p>";

# Sostituzione

#$stringa =~ tr/\s\u/A-Z/;
$stringa =~ s/(?<!['])(\w+)/\u\1/g; # Mette in CamelCase la stringa
$stringa =~ s/\s//g; # Toglie gli spazi dalla stringa
# Mette in minuscolo la prima lettera ???

   #my $b = encode('utf8', $stringa);
   print "<p>newstringa = ".$stringa."</p>";

print "</body></html>";

exit 0;