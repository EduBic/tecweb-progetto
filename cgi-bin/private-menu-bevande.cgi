#!\Perl64\bin\perl

#use utf8;
use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use XML::LibXML;
use Encode qw(decode encode);

use BaseFunctions;
use MenuFunctions;

#Inizializzazione variabili base
my $q = new CGI;
my $session = CGI::Session->load() or die $!;

BaseFunctions::checkSession($session);

my %path = (   add_bevanda => 'add-bevanda.cgi',
               #add_listaBevande => 'add-portata.cgi', # manca
               mod_bevanda => 'mod-piatto.cgi',
               del_bevanda => 'private-menu-bevande.cgi',
);

BaseFunctions::printStartHtml('Bevande - Men&ugrave; - Area Riservata');

checkDelete();

printMenuBevande(1, \%path, '/menu/bevande/listaVini', 'vino');
#MenuFunctions::printMenuBevande(1, \%path, '/menu/bevande/listaBirre', 'birra');
#MenuFunctions::printMenuBevande(1, \%path, '/menu/bevande/listaAltreBevande', 'bevanda');

BaseFunctions::printEndHtml();


# Subroutines

sub printMenuBevande {

      my $q = new CGI;
      my ($admin, $pathR, $queryLista, $queryBevanda) = @_;
            
      my $doc = BaseFunctions::initLibXML();
      
      # Variabili generali
      my $valuta = '€';
      
      # ATTENZIONE manca submit inserimento liste bevande.
      #if($admin) {
            #  BaseFunctions::printStartForm();
      #           print $q->submit( -name => ''
      #                     -value => '');
            #BaseFunctions::printEndForm();
      #}  
      
      my $nomeLista = $doc->findnodes($queryLista."/nome");

      print "<dl class='portata' id='$nomeLista'>";
      print $q->p('Da Perl: Antonino Macrì - Da XML:'.$nomeLista);
      my $da_utf8  = decode('utf8', $nomeLista);
      print $doc->encoding();
      print "<h3>$da_utf8";
      
      if($admin) {
         BaseFunctions::printStartForm('add-bevanda', $pathR->{add_bevanda}, 'GET');
            print "<input class='pulsante' type='submit' name='aggiungi' value='Aggiungi' />
                <input type='hidden' name='portata' value='$nomeLista' />";
         BaseFunctions::printEndForm();
      }
      
      print "</h3>";

   
   foreach my $bevanda ($doc->findnodes($queryLista."/".$queryBevanda)){
         # print $queryLista."/".$queryBevanda;
         
         my $idBevanda = $bevanda->findnodes('@id');
         my $nome = $bevanda->findnodes('./nome');
         my $prezzo = $bevanda->findnodes('./prezzo');
         my $descrizione = $bevanda->findnodes('./descrizione');
               
         print "<dt>$nome <span class='prezzo'>$valuta $prezzo</span>";
         
         if($descrizione){
            print "<dd>$descrizione</dd>";
         }
         
         if($admin) {
                  BaseFunctions::printStartForm('mod-bevanda', $pathR->{mod_bevanda}, 'GET');
                  print "<span class='pulsanti'>
                           <input class='pulsante' type='submit' name='modifica' value='Modifica' />
                           <input type='hidden' name='idBevanda' value='$idBevanda' />";
                  BaseFunctions::printEndForm();
                  
                  BaseFunctions::printStartForm('del-bevanda', $pathR->{private_menu}, 'GET');
                  print "  <input class='pulsante' type='submit' name='rimuovi' value='Rimuovi' />
                           <input type='hidden' name='idBevanda' value='$idBevanda' />
                        </span>";
                  BaseFunctions::printEndForm();
               }
               
         print "</dt>";
   }
}

sub checkDelete{
   if ($q->param('rimuovi')){
      #Rimuovi piatto nei param
      #display comment
      my $idPiatto = $q->param('idPiatto');
      print "cancellata bevanda: $idPiatto";
   }
}

exit 0;
