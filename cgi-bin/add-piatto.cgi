#!\Perl64\bin\perl

use utf8;
use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use XML::LibXML;
use BaseFunctions;

my $session = CGI::Session->load() or die $!;

BaseFunctions::checkSession($session);

#Inizializzazione variabili base
my $q = new CGI; # Sarà il parametro $_[0] di ogni funzione

BaseFunctions::printStartHtml('Aggiungi Piatto - Area Riservata');

# Verifica parametri
if ($q->param('add')){
   print "Scrivo l'xml";
   print "<p>Parametri: ".$q->param('nome').$q->param('prezzo').$q->param('descrizione')."</p>";
   
   my $prezzo = $q->param('prezzo');
   #check
   my $nome = $q->param('nome');
   #check
   my $descrizione = $q->param('descrizione');
   #check
   my $id = $q->param('portata');
   #check

   my $doc = BaseFunctions::initLibXML();
   my $padre = $doc->findnodes("menu/cibo/portata[\@id = '$id']");

   my $element = "<piatto id='$nome'>
                     <nome>$nome</nome>
                     <prezzo>$prezzo</prezzo>
                     ";
      if ($descrizione ne '') {
         $element = $element."<descrizione>$descrizione</descrizione>
         ";
      }
   $element = $element."</piatto>
   ";

      if ($padre) {
      
         my $nodo;
         my $parser = XML::LibXML->new(); 
         
         eval{$nodo=$parser->parse_balanced_chunk($element)} || die ('Elemento non ben formato');
         $padre->get_node(1)->appendChild($nodo) || die('Non riesco a trovare il padre');
         
         # Scrivo sul file
         open(OUT, ">".BaseFunctions::getFilenameMenu());
         flock(OUT, 2);
         print OUT $doc->toString;
         close(OUT);
      } 
      
}
elsif($q->param('idPortata')) {

   my $idPortata = $q->param('idPortata');

   print $q->h2("Aggiungi un piatto alla portata: ".$idPortata);
   #mostra quale modifica si sta facendo: sto aggiungendo piatto a portata 'x'
   #mostra la form - si vuole aggiungere un piatto.
   
   BaseFunctions::printStartForm('add-piatto','add-piatto.cgi','get');
      print "<fieldset>
               <legend>Inserisci nuovi dati per aggiungere un piatto</legend>";
      print "<p>";
         print $q->label('Nome piatto');
         print $q->textarea(-name => 'nome');
      print "</p>";
      
      print "<p>";
         print $q->label('Prezzo (&euro;)');
         print $q->textarea(-name => 'prezzo');
      print "</p>";
      
      print "<p>";
         print $q->label('Descrizione piatto');
         print $q->textarea(-name => 'descrizione');
      print "</p>";
      
      print $q->hidden(-name => 'portata',
                        -value => $idPortata);
               
      print $q->submit(
         -name => 'add',
         -value => 'Aggiungi',
         );
      
   BaseFunctions::printEndForm();
   
}

BaseFunctions::printEndHtml($q);

exit 0;
