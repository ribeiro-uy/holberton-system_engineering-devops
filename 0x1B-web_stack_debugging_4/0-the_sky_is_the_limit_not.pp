# added option -l to make ApacheBench accept variable document length
command => "sed -i 's/15/1500/g' /etc/default/nginx; service nginx restart",
provider => 'shell'
}