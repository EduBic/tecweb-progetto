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
if ($q->param('add')) {

   print "<p>Parametri da inserire: ".$q->param('nome').$q->param('prezzo').$q->param('descrizione')."</p>";
   
   my $error = '';
   
   my $prezzo = $q->param('prezzo');
      $error = $error.checkPrezzo($prezzo);
   my $nome = $q->param('nome');
      $error = $error.checkNome($nome);
   my $numero = $q->param('numero');
      $error = $error.checkNumero($numero);
   my $descrizione = $q->param('descrizione');
      $error = $error.checkDesc($descrizione);
   my $id = $q->param('portata');
      # COntrollo sulla portata?

   if ($error ne '') {
      printForm('Ops! Ci sono degli errori nei dati inseriti:', $error);
   }
   else {
      my $doc = BaseFunctions::initLibXML();
      my $padre = $doc->findnodes("menu/cibo/portata[\@id = '$id']");

      my $element = "<piatto id='$nome'>
                     <nome>$nome</nome>
                     <numero>$numero</numero>
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
         open(OUT, ">".BaseFunctions::getFilename());
         flock(OUT, 2);
         print OUT $doc->toString;
         close(OUT);
      }
      
      printForm('Inserimento effettuato con successo!', $error);
   }     
}
elsif($q->param('idPortata')) {
   printForm('','');
}

BaseFunctions::printEndHtml($q);

#--------------------------------------------------------------------

sub printForm {

   my ($info, $error) = @_;
   my $idPortata = $q->param('idPortata');
   my $nomePortata = $q->param('nomePortata');

   print $q->a({-href => 'private-menu-cibi.cgi'},'Torna al men&ugrave;');

   print $q->h2("Aggiungi un piatto alla portata: ".$nomePortata);
   #mostra quale modifica si sta facendo: sto aggiungendo piatto a portata 'x'
   #mostra la form - si vuole aggiungere un piatto.
   
   if ($info ne '') {
      print $q->p($info);
   }
   
   if ($error ne '') {
      print $q->ul($error);
   }
   
   BaseFunctions::printStartForm('add-piatto','add-piatto.cgi?check=1','get');
      print "<fieldset>
               <legend>Inserisci nuovi dati per aggiungere un piatto</legend>";
      print "<p>";
         print $q->label('Nome piatto');
         print $q->textarea(-name => 'nome');
      print "</p>";
      
      print "<p>";
         print $q->label('Numero piatto');
         print $q->textarea(-name => 'numero');
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
         -value => 'Aggiungi'
         );
      
   BaseFunctions::printEndForm();
}


#------------------Sub-------

sub checkNome{
    my $ret="";
    if(!$_[0]){
        $ret=$ret."<li>Il campo nome non deve essere vuoto</li>";
    }
    if(length $_[0]>20) {
      $ret=$ret."<li>Il campo nome non deve superare i 20 caratteri</li>";
    }
    return $ret;
}

sub checkNumero {
   my $ret="";
   if(!$_[0]){
      $ret=$ret."<li>Il campo numero piatto non deve essere vuoto</li>";
   }
   if(!($_[0] =~ m/[0-9]{1,99}[a-z]*/)){
      $ret=$ret."<li>Il campo numero piatto deve essere costituito da un numero (obbligatorio) e una lettera (opzionale)</li>";
   }
}

sub checkPrezzo{
    my $ret="";
    if(!$_[0] || !($_[0] =~ m/[0-9]{1,99}/)){ # Non funziona
         $ret=$ret."<li>Il campo prezzo deve contenere un numero</li>";
    }
    return $ret;
}

sub checkDesc{
    my $ret="";
    if(length $_[0]>500){
        $ret=$ret."<li>La descrizione deve avere al massimo 50 caratteri</li>";
    }
    return $ret;
}

exit 0;
