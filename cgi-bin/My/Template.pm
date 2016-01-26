#
#
#
use strict;
use warnings;

   package My::Template; # Sostituire Template con nome modulo

use Exporter qw(import);
our @EXPORT_OK = qw(method method2); # Indicare i metodi da esportare

sub method {
   print "<h1 style='color: red'>method in My::Template</h1>";
}

sub method2 {
   print "<h1 style='color: red'>method2 in My::Template</h1>";
}

1;
