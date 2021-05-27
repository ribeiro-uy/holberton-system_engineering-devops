# added option -l to make ApacheBench accept variable document length
exec { 'sed increase ULIMIT number in concerned etc/default/nginx file':
  command => "sed -i 's/15/1024/g' /etc/default/nginx; service nginx restart",
  path    => ['/bin']
}
