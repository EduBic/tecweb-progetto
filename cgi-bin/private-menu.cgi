#!\xampp\perl\bin\perl

use utf8;
use strict;
use warnings;
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use XML::LibXML;
use BaseFunctions;

#checkSession;

#Inizializzazione vaiabili base
my $q = new CGI; # Sarà il parametro $_[0] di ogni funzione

BaseFunctions::printStartHtml($q, 'Men&ugrave; - Area Riservata');

#checkDelete{
   #if ($q->param()){
      #Rimuovi piatto nei param
      #display comment
      #display_results($q);
   #}
#}

#sub printMenu(true){

   #inizializzazione XML
   my $filename = "..\\data\\menu.xml";   # Percorso Windows
   my $parser = XML::LibXML->new();
   my $doc = $parser->parse_file($filename);
   
   # Variabili globali
   my $valuta = '€';    # N.B. sui dessert che concludono con verde c'è un errore di codifica...
   
   # sub printCibo() Print sezione cibo (da portare in funzione)
   my $query = "/menu/cibo/portata";   # Query primaria
   my $query2 = "./piatto";            # Query secondaria
   
   foreach my $portata ($doc->findnodes($query)) {
      my $idPortata = $portata->findnodes('@id');
      my $nomePortata = $portata->findnodes('./nome');
   
      print "<dl class='portata' id='$idPortata'>";
      print $q->h3($nomePortata);
      
      foreach my $piatto ($portata->findnodes($query2)){
               
               my $idPiatto = $piatto->findnodes('@id');
               my $nome = $piatto->findnodes('./nome');
               my $numero = $piatto->findnodes('./numero');
               my $prezzo = $piatto->findnodes('./prezzo');
                   #$piatto->findnodes('./prezzo/@valuta')
               my $descrizione = $piatto->findnodes('./descrizione');
               
               print "<dt>$numero - $nome <span class='prezzo'>$valuta $prezzo</span>";
               #if(admin==true)
                  print "<span class='pulsanti'>
                           <input class='pulsante' type='button' name='modifica' value='Modifica' />
                           <input class='pulsante' type='button' name='rimuovi' value='Rimuovi' />
                           <input type='hidden' name='idPiatto' value='$idPiatto' />
                        </span>";
               print "</dt>";
               if($descrizione ne ""){  # Se la descrizione non è vuota (ne è il comando contrario di eq)
                  print "<dd>$descrizione</dd>";
               }      
      }
      print "</dl>";
   }
      
   # sub printBevande{}
   my $query = "/menu/bevande";  # Query primaria  
   
   # Print di liste bevande
   printListaBevande(1, $query.'/listaVini/vino', 'Vini');                       # listaVini e vino
   printListaBevande(1, '/menu/bevande/listaBirre/birra', 'Birre');              # listaBirre e birre
   printListaBevande(1, '/menu/bevande/listaAltreBevande/bevanda', 'Bevande');   # listaAltreBevande e Bevanda
   
   
   sub printListaBevande {

      # Raccolta parametri
      my $admin = $_[0];
      my $queryBevanda = $_[1];
      my $nomeLista = $_[2];

      print "<dl class='listaBevande' id='$nomeLista'>";
      print $q->h3("$nomeLista");
   
      foreach my $bevanda ($doc->findnodes($queryBevanda)){
         
         my $idBevanda = $bevanda->findnodes('@id');
         my $nome = $bevanda->findnodes('./nome');
         my $prezzo = $bevanda->findnodes('./prezzo');
         my $descrizione = $bevanda->findnodes('./descrizione');
               
         print "<dt>$nome <span class='prezzo'>$valuta $prezzo</span>";
         if($admin){
            print "<span class='pulsanti'>
                  <input class='pulsante' type='button' name='modifica' value='Modifica' />
                  <input class='pulsante' type='button' name='rimuovi' value='Rimuovi' />
                  <input type='hidden' name='idBevanda' value='$idBevanda' />
                  </span>"; 
         }
         print "</dt>";
         
         if($descrizione){
            print "<dd>$descrizione</dd>";
         }
      }
   }
   
#}


BaseFunctions::printEndHtml($q);

exit 0;
