#!\xampp\perl\bin\perl

use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use XML::LibXML;

my $filename = "..\\data\\db.xml";
my $q = new CGI;

#inizializzazione HTML
print $q->header(-charset => 'UTF-8');


#inizializzazione e uso di libXML

my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($filename);

#Con findnodes tramite XPath raccolgo il nodo e poi lo stampo

foreach my $book ($doc->findnodes('/library/book')) {
   my $title = $book->findnodes('./title');
   
   print $title->to_literal, "\n"
}


#--------PARTE II------------
#Trovare qualcosa

my $author = 'Cinisio';

my $query = "//book[author/text() = '$author']/author/text()";

print $_->data . "\n" foreach ($doc->findnodes($query));

print "<br>";
#--------PARTE III---------
#Modificare l'XML

my $author1 = "Cinisio";

#Metodo facile Gaggi
my $query1 = "//book[author = '$author1']/pages/text()";
my ($node1) = $doc->findnodes($query1)->get_node(1);
#Settiamo il nuovo text al nodo selezionato
$node1->setData('394');
print $doc->toString;

print "</br>";

#Metodo più complesso ma più corretto
for my $reviewer ($doc->findnodes("//book[author = '$author1']")){
my ($name) = $reviewer->findnodes('pages');
print "Before ".$name."  -  ";
$name->removeChildNodes; #evita errori se sono stati trovati nodi multipli
$name->appendText('445');  
print "After ".$name;
}

print $doc->toString;   
$doc->toFile("..\\data\\db.xml"); #salva l'xml modificato (attenzione!)
