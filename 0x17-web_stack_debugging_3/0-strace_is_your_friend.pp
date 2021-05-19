# Fix path name in the file wp-settings.php
exec { 'fix_line':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin']
}