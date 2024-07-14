#!/bin/perl -w
use CGI;
use Data::UUID;

$upload_dir = "/var/www/flowers/images";

$query = new CGI;

$og_filename = $query->param("photo");
($ext) = $og_filename =~ /(\.[^.]+)$/;
$ug = Data::UUID->new;
$filename = $ug->create_str();
$filename = "${filename}${ext}";
#$filename =~ s/.*[\/\\](.*)/$1/;
$upload_filehandle = $query->upload("photo");

open UPLOADFILE, ">$upload_dir/${filename}";

while ( <$upload_filehandle> )
{
print UPLOADFILE;
}

close UPLOADFILE;

print  $query->header ( );
print <<END_HTML;

<html>
<head>

<title>uploaded!</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

</head>
<body>

<p>thanks for uploading your photo :)</p>
<a href="/flowers/edit.cgi">back to edit</a>
<br><br>
<a href="/flowers">go to homepage</a>
<br><br>
<img height=100 width=100 src="/flowers/images/${filename}">

</body>
</html>

END_HTML
