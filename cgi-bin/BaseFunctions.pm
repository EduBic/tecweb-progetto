#
# Per un corretto uso di moduli perl (estensione .pm)
# Mettere nel file @INC o .packlist nella directory Perl la stringa -> C:\Perl64\lib/BaseFunctions.pm type=file
# Nel file che richiede l'uso mettere all'inizio use BaseFunctions;
#

# N.B. Package in cui si collocano le funzioni principali per la creazione delle pagine del sito
use utf8;
use strict;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use CGI::Session;

package BaseFunctions;

#
# Subroutines che si occupa della stampa html di inizio pagina (deve seguire la chiamata a printEndHtml())
#
sub printStartHtml {

   my $q = new CGI;
   my $title = $_[0];
   
   print "Content-type: text/html\n\n"; # Dico a Perl che sto stampando html  
   print "<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>
   <html xmlns='http://www.w3.org/1999/xhtml'>
   <head>
      <meta http-equiv='Content-Type' content='text/html; charset=utf-8' />
      <title> $title </title>
   </head>";
}

#
# Subroutines che si occupa della stampa html di fine pagina (deve essere chiamata dopo printStartHtml())
#
sub printEndHtml {

   my $q = new CGI;
   print $q->end_html;
}

#
# Stampa la form con i dati passati per parametro
#
sub printStartForm {

   my $q = new CGI;
   my $name = $_[0];
   my $action = $_[1];
   my $method = $_[2];

   print $q->start_form(-name => $name,
                        -action => $action,
                        -method => $method,
                        enctype => &CGI::URL_ENCODED
                        );  
}

#
# Stampa la fine della form
#
sub printEndForm {

   my $q = new CGI;
   print $q->end_form();
}


#
sub checkSession {

   my $session = $_[0];
   
   if ($session->is_expired) {
      my $avviso="La sessione &egrave; scaduta (dura 20 min). ";
      die($avviso);
      exit;
   }
   
   elsif($session->is_empty) {
		#my $avviso="Non hai ancora effettuato l'accesso all'area riservata.";
        print $session->header(-location=>"../accesso-negato.html");
        exit;
	}
    
}

# Un modulo perl termina sempre per 1
1;