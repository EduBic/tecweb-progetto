#!\xampp\perl\bin\perl

use strict;
use warnings;
use CGI ':standard', '-debug';
use CGI::Carp qw(fatalsToBrowser);
use XML::Simple qw(:strict);
use XML::Simple;
use XML::LibXML;

my $q = new CGI;


print $q->header(-charset => 'UTF-8');

print $q->start_html(-title => 'Form di test');


if ($q->param()){
   #display comment
   display_results($q);
}
else {
   #mostra la form - è la prima volta che apriamo la pagina
}

print $q->p('Inserisci un commento e visualizzalo qui in alto:');
#inizio costruizione form HTML
print $q->start_form(-name => 'insertForm',
                     -method => 'GET',
                     enctype => &CGI::URL_ENCODED,
                     );
                     
print $q->textarea(
         -name => 'nickname',
         -value => 'Il tuo nickname');
         
my @values = ('free', 'premium');
print $q->p();
print $q->popup_menu(
         -name => 'tipo',
         -values => \@values,
         -default => 'free'
         );
         
print $q->textarea(
         -name => 'titoloCommento',
         -value => 'Titolo del tuo commento');
         
print $q->textarea(
         -name => 'commento',
         -value => 'Il tuo commento...');
         
print $q->p('Come ti senti?');
my @values2 = ('Infastidito', 'Felice', 'Arrabbiato');
print $q->checkbox_group(
         -name => 'umore',
         -value => \@values2,
         -label => \@values2
         );
         
print $q->submit(
         -name => 'invia',
         -value => 'invia!',
         );
      
                     
print $q->end_form;

print $q->end_html;

exit 0;

#-----------------FUNCTIONS----------------

sub display_results{
   my ($q) = @_;
   
   #recupero dati della form
   my $nickname = $q->param('nickname');
   my $titoloCommento = $q->param('titoloCommento');
   my $tipo = $q->param('tipo');
   my $commento = $q->param('commento');
   my @umore = sort $q->param('umore');
   
   #stampo dati della form recuperati
   print $q->h1("$nickname utente $tipo dice:");
   print $q->p($titoloCommento);
   print $q->p($commento);
   print $q->table(
            $q->Tr($q->td(\@umore))
   );
   
   #salvo i dati della form recuperati in un foglio xml
   #my $file ="..\data\db.xml";
   
   
   print $q->h2("Il commento è stato salvato nel file db.xml")
   
   
   
}


