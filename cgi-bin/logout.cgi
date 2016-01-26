#!\Perl64\bin\perl

use utf8;
use strict;
use warnings;
use BaseFunctions;

my $session = CGI::Session->load() or die $!;
   $session->delete();

print "Location: ../login.html\n\n";
   
exit 0;
