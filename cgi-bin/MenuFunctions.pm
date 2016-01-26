#
# Per un corretto uso di moduli perl (estensione .pm)
# Mettere nel file @INC o .packlist nella directory Perl la stringa -> C:\Perl64\lib/BaseFunctions.pm type=file
# Nel file che richiede l'uso mettere all'inizio use MenuFunctions;
#

# N.B. Package in cui si collocano le funzioni principali per la creazione delle pagine inerenti al menù ristorativo
#use utf8;
#use strict;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use XML::LibXML;
use CGI::Session;

package MenuFunctions;


#
# Stampa il menù ristorativo in due differenti modi: con parametro 0 un normale html costruito sulla base xml;
#                                                    con parametro 1 aggiunge all'html precedente form di aggiunta, modifica e rimozione.
#
sub printMenuCibi {

   my $q = new CGI;
   my ($admin, $pathR) = @_;
   #my @pathForm = $_[2];

   my $doc = BaseFunctions::initLibXML();
   
   # Variabili generali
   my $valuta = "€";
   
   # sub printCibo() Print sezione cibo (da portare in funzione)
   my $query = "/menu/cibo/portata";   # Query primaria
   my $query2 = "./piatto";            # Query secondaria
   
   # ATTENZIONE manca submit inserimento portate.
   #if($admin) {
    #  BaseFunctions::printStartForm();
     #    print $q->submit( -name => ''
      #                     -value => '');
      #BaseFunctions::printEndForm();
   #}
   
   #sub printPortata {}
   
   foreach my $portata ($doc->findnodes($query)) {
      my $idPortata = $portata->findnodes('@id');
      my $nomePortata = $portata->findnodes('./nome');
   
      print "<dl class='portata' id='$idPortata'>";
      print "<h3>$nomePortata";
      
      if($admin) {
         BaseFunctions::printStartForm('add-piatto', $pathR->{add_piatto}, 'GET');
            print "<input class='pulsante' type='submit' name='aggiungi' value='Aggiungi' />
                <input type='hidden' name='idPortata' value='$idPortata' />
                 <input type='hidden' name='nomePortata' value='$nomePortata' />";
         BaseFunctions::printEndForm();
      }
      
      print "</h3>";
      
      foreach my $piatto ($portata->findnodes($query2)){
               
               my $idPiatto = $piatto->findnodes('@id');
               my $nome = $piatto->findnodes('./nome');
               my $numero = $piatto->findnodes('./numero');
               my $prezzo = $piatto->findnodes('./prezzo');
                   #$piatto->findnodes('./prezzo/@valuta')
               my $descrizione = $piatto->findnodes('./descrizione');
               
               print "<dt>$numero - $nome <span class='prezzo'>$valuta $prezzo</span>";
               
               if($admin) {
                  BaseFunctions::printStartForm('mod-piatto', $pathR->{mod_piatto}, 'GET');
                  print "<span class='pulsanti'>
                           <input class='pulsante' type='submit' name='modifica' value='Modifica' />
                           <input type='hidden' name='idPiatto' value='$idPiatto' />
                           <input type='hidden' name='nome' value='$nome' />
                           <input type='hidden' name='numero' value='$numero' />
                           <input type='hidden' name='descrizione' value='$descrizione' />
                           <input type='hidden' name='prezzo' value='$prezzo' />";
                  BaseFunctions::printEndForm();
                  
                  BaseFunctions::printStartForm('del-piatto', $pathR->{private_menu}, 'GET');
                  print "  <input class='pulsante' type='submit' name='rimuovi' value='Rimuovi' />
                           <input type='hidden' name='idPiatto' value='$idPiatto' />
                           <input type='hidden' name='nome' value='$nome' />
                        </span>";
                  BaseFunctions::printEndForm();
               }
               
               print "</dt>";
               
               if($descrizione ne ""){  # Se la descrizione non è vuota ('ne' è il comando contrario di 'eq')
                  print "<dd>$descrizione</dd>";
               }      
      }
      
      print "</dl>";
   } 
}


#
#  Sub interna al modulo
#
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
      print $doc->encoding();
      print "<h3>$nomeLista";
      
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
   
   
1;