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
my $q = new CGI; 

BaseFunctions::printStartHtml('Modifica piatto - Area Riservata');

# Verifica parametri
if ($q->param('mod')){
   print "Scrivo l'xml";
   print "<p>Parametri: ".$q->param('nome').$q->param('numero').$q->param('prezzo').$q->param('descrizione')."</p>";
   
   my $error = '';
   
   my $prezzo = $q->param('prezzo');
      $error = $error.checkPrezzo($prezzo);
   my $nome = $q->param('nome');
      $error = $error.checkNome($nome);
   my $numero = $q->param('numero');
      $error = $error.checkNumero($numero);
   my $descrizione = $q->param('descrizione');
      $error = $error.checkDesc($descrizione);
   my $id = $q->param('idPiatto');
      # COntrollo sulla portata? è hidden...

   if ($error ne '') {
      print $error;
   }
   else {
      my $doc = BaseFunctions::initLibXML();
      
      #print $el;
      $doc->findnodes("menu/cibo/portata/piatto[\@id = \'$id\']/nome/text()")->get_node(1)->setData($nome);
      $doc->findnodes("menu/cibo/portata/piatto[\@id = \'$id\']/numero/text()")->get_node(1)->setData($numero);
      $doc->findnodes("menu/cibo/portata/piatto[\@id = \'$id\']/prezzo/text()")->get_node(1)->setData($prezzo);
      if ($descrizione ne '') {
         if ($doc->findnodes("menu/cibo/portata/piatto[\@id = \'$id\']/descrizione") eq '') {
            print "creo tag descrizione";
         }
         else {
            $doc->findnodes("menu/cibo/portata/piatto[\@id = \'$id\']/descrizione/text()")->get_node(1)->setData($descrizione);
         }
      }
      $doc->findnodes('menu/cibo/portata/piatto/@id["$id"]')->get_node(1)->setValue('ciao');
      
          #Scrivo sul file
         open(OUT, ">:utf8".BaseFunctions::getFilename());
         flock(OUT, 2);
         print OUT $doc->toString;
         close(OUT);
   }
      
}
elsif($q->param('idPiatto')) { # stampo la form

   my $idPiatto = $q->param('idPiatto');
   my $nome = $q->param('nome');
   my $numero = $q->param('numero');
   my $prezzo = $q->param('prezzo');
   my $descrizione = $q->param('descrizione');

   print $q->h2("Modifica il piatto: ".$nome);
   #mostra quale modifica si sta facendo: sto aggiungendo piatto a portata 'x'
   #mostra la form - si vuole aggiungere un piatto.
   
   BaseFunctions::printStartForm('mod-piatto','mod-piatto.cgi','get');
      print "<fieldset>
               <legend>Inserisci nuovi dati per modificare il piatto</legend>";
      print "<p>";
         print $q->label('Nome piatto');
         print $q->textarea(-name => 'nome',
                              -value => $nome);
      print "</p>";
      
      print "<p>";
         print $q->label('Numero piatto');
         print $q->textarea(-name => 'numero',
                              -value => $numero);
      print "</p>";
      
      print "<p>";
         print $q->label('Prezzo (&euro;)');
         print $q->textarea(-name => 'prezzo',
                              -value => $prezzo);
      print "</p>";
      
      print "<p>";
         print $q->label('Descrizione piatto');
         print $q->textarea(-name => 'descrizione',
                              -value => $descrizione);
      print "</p>";
      
      print $q->hidden(-name => 'idPiatto',
                        -value => $idPiatto);
               
      print $q->submit(
         -name => 'mod',
         -value => 'Modifica',
         );
      
   BaseFunctions::printEndForm();
   
}

BaseFunctions::printEndHtml($q);


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
        $ret=$ret."<li>La descrizione deve avere al massimo 500 caratteri</li>";
    }
    return $ret;
}

exit 0;
