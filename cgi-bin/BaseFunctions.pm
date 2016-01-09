# Per un corretto uso di moduli perl (estensione .pm)
# Mettere nel file @INC o .packlist nella directory Perl la stringa -> C:\Perl64\lib/BaseFunctions.pm type=file
# Nel file che richiede l'uso mettere all'inizio use BaseFunctions;

# Package in cui si collocano le funzioni principali per la creazione delle pagine del sito
use utf8;
use strict;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

package BaseFunctions;

sub printStartHtml {

   # Raccolta parametri
   my $q = $_[0];
   my $title = $_[1];
   
   print "<!DOCTYPE html PUBLIC '-//W3C//DTD XHTML 1.0 Strict//EN' 'http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd'>
   <html xmlns='http://www.w3.org/1999/xhtml'>
	<head>
		<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />
		<title> $title </title>
	</head>";

   # Non funziona per riconoscere la u grave, servono altre opzioni che nell'HTML sopra ci sono.
   #print $q->header(
               #-content => 'text/html',
               #-charset => 'UTF-8'
               #);
   #print $q->start_html(-title => $title);

}

sub printEndHtml {
   
   # Raccolta parametri
   my $q = $_[0];

   print $q->end_html;
}

sub checkSession {}

sub checkDelete {}


1;