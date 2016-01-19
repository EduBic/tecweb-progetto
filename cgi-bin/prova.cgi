#!\Perl64\bin\perl

use utf8;
use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use BaseFunctions;

print "Content-type: text/html\n\n";


my %form = (
      add_piatto => 'add-piatto.cgi',
      del => 'add_portata'
);

my %form2 = (
      eccomi => 'home'
);

BaseFunctions::meth(\%form, \%form2);


exit 0;