#
# Per un corretto uso di moduli perl (estensione .pm)
# Mettere nel file @INC o .packlist nella directory Perl la stringa -> C:\Perl64\lib/BaseFunctions.pm type=file
# Nel file che richiede l'uso mettere all'inizio use MenuFunctions;
#

# N.B. Package in cui si collocano le funzioni principali per la creazione delle pagine inerenti al menù ristorativo
use utf8;
use strict;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use CGI::Session;

package MenuFunctions;


#
# Stampa il menù ristorativo in due differenti modi: con parametro 0 un normale html costruito sulla base xml;
#                                                    con paramtero 1 aggiunge all'html precedente form di aggiunta, modifica e rimozione.
#
sub printMenu {

   my $q = new CGI;
   my $admin = $_[0];
   my @input = $_[1];

   #inizializzazione XML
   my $filename = "..\\data\\menu.xml";   # Percorso Windows (ATTENZIONE!!!)
   my $parser = XML::LibXML->new();
   my $doc = $parser->parse_file($filename);
   
   # Variabili generali
   my $valuta = '€';
   
   # sub printCibo() Print sezione cibo (da portare in funzione)
   my $query = "/menu/cibo/portata";   # Query primaria
   my $query2 = "./piatto";            # Query secondaria
   
   # ATTENZIONE manca submit inserimento portate.
   
   #sub printPortata {}
   
   foreach my $portata ($doc->findnodes($query)) {
      my $idPortata = $portata->findnodes('@id');
      my $nomePortata = $portata->findnodes('./nome');
   
      print "<dl class='portata' id='$idPortata'>";
      print "<h3>$nomePortata";
      
      if($admin) {
         BaseFunctions::printStartForm('add-piatto', 'add-piatto.cgi', 'GET');
            print "<input class='pulsante' type='submit' name='$input[0]' value='Aggiungi' />
                <input type='hidden' name='$input[1]' value='$nomePortata' />";
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
                  BaseFunctions::printStartForm('mod-Piatto', 'mod-piatto.cgi','GET');
                  print "<span class='pulsanti'>
                           <input class='pulsante' type='submit' name='$input[2]' value='Modifica' />
                           <input type='hidden' name='$input[3]' value='$idPiatto' />";
                  BaseFunctions::printEndForm();
                  
                  BaseFunctions::printStartForm('del-piatto', 'private-menu.cgi', 'GET');
                  print "  <input class='pulsante' type='submit' name='$input[4]' value='Rimuovi' />
                           <input type='hidden' name='$input[5]' value='$idPiatto' />
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
    
   printListaBevande(1, '/menu/bevande/listaVini/vino', 'Vini', $doc);                 # listaVini e vino
   printListaBevande(1, '/menu/bevande/listaBirre/birra', 'Birre', $doc);              # listaBirre e birre
   printListaBevande(1, '/menu/bevande/listaAltreBevande/bevanda', 'Bevande', $doc);   # listaAltreBevande e Bevanda
   
}


#
#  Sub interna al modulo
#
sub printListaBevande {

      my $q = new CGI;
      
      # Variabili generali
      my $valuta = '€';

      # Raccolta parametri
      my $admin = $_[0];
      my $queryBevanda = $_[1];
      my $nomeLista = $_[2];
      my $doc = $_[3];

      print "<dl class='listaBevande' id='$nomeLista'>";
      print $q->h3($nomeLista."<span><input class='pulsante' type='submit' name='aggiungi' value='Aggiungi' /></span>");
   
   foreach my $bevanda ($doc->findnodes($queryBevanda)){
         
         my $idBevanda = $bevanda->findnodes('@id');
         my $nome = $bevanda->findnodes('./nome');
         my $prezzo = $bevanda->findnodes('./prezzo');
         my $descrizione = $bevanda->findnodes('./descrizione');
               
         print "<dt>$nome <span class='prezzo'>$valuta $prezzo</span>";
         if($admin){
            print "<span class='pulsanti'>
                  <input class='pulsante' type='submit' name='modifica' value='Modifica' />
                  <input class='pulsante' type='submit' name='rimuovi' value='Rimuovi' />
                  <input type='hidden' name='idBevanda' value='$idBevanda' />
                  </span>"; 
         }
         print "</dt>";
         
         if($descrizione){
            print "<dd>$descrizione</dd>";
         }
   }
}
   
   
1;