#!\Perl64\bin\perl

#use utf8;
use Encode;
use CGI;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use XML::LibXML;
 use Encode qw(decode encode);
 
 use My::Template qw(method method2); # Tra parentesi specifichi i metodi utilizzati

my $q = CGI->new;

print "Content-Type: text/html\n\n";

print "<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>
   <html xmlns='http://www.w3.org/1999/xhtml'>
   <head>
      <meta http-equiv='Content-Type' content='text/html; charset=utf-8' />
      <title> title </title>
   </head>
   <body>";

print "<p>è ò à è ò à è ì &</p>"; # OK

print "è ò à è ò à è ì "; # OK

print $q->p("è ò à è ò à è ì &  è ò à ì"); # OK 
print $q->p("è ò à è ò à è ì &  àò"); # Il simbolo dell'euro dice a perl di tenere la codifica giusta D:

my $file = "prova.xml";
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file); # Va bene
my $root = $doc->getDocumentElement; # NO!

my ($node) = $doc->findnodes('prova');
print $node;

print "<p>Codifica file xml ".$doc->encoding."</p>";

print 'da doc: '.$doc; # Stampa bene
print "<br />";
print "da root: ".$root; # Non stampa bene se non ci sono altri caratteri che forzano
print "<br />";

my @elementi = $root->getElementsByTagName('carattere'); # Va in qualche caso

#print $q->h3('da getElementByTagName: ');

print $doc->findnodes('prova');

print "<br/><br/><br/>";

print $q->h3("Prove stampe è ò à ì");

print @elementi; # Non va
print "<br/>";
print $q->p(@elementi); # Stampa BENE!!!
print $q->p("@elementi"); # Stampa BENE!!!
print $q->p('@elementi'); # Stampa @elementi
print "@elementi"; # Stampa BENE!!!
print "<br/>";
print '@elementi';  # Stampa @elementi
print "<br/><br/>";
foreach $a (@elementi) {
   my $b = encode('utf8', $a);
   print "-> $b ";
}


# la decodifica non va
# my @el  = decode('utf8', @elementi);
# print "<p>@el</p>";
#print $el[0];

print $q->p('------------------------');

print "<p>Singolo elemento: ".$elementi[0]."</p>";
print $q->p("Singolo elemento con CGI: ".$elementi[0]);

#print $q->p('CONCLUSIONE: il metodo getElementByTagName sballa');


print "<h2>Altro metodo di prelievo da XML</h2>";

my @caratteri = $doc->findnodes('prova/carattere');

print $q->h3('Da findnode()');
for $car (@caratteri) {
   my $b = encode('utf8', $car);
   print $b;
}

method();

method2();

print "</body>";