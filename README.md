# Seafile Configuration
Seafile configuration, behind Haproxy and Nginx

My home network is behind NAT and I use dyndns to provide a doman name, XXXX.dyndns.org, where XXXX is of course a placeholder.

I use Haproxy to be the end-point for a LetsEncrypt certificate, and forward the services I want to other local servers on and internal network.

I use  301 redirects from http to https, and from XXXX.dyndns.org www.XXXX.dyndns.org

The proxies and Seafile to not like these redirects, so it is important to use, https://www.XXXX.dyndns.org/sfa as the hostname.

To enable me to provide many services on this single domain I use different sub-directories, and I don't use sub-domains. Above, sfa is an example.

haproxy/haproxy.cfg
Shows a simplified configuration file showing how I proxy the services to various servers by IP number and port.

nginx/seafile.conf
Is a server clause operating on port 84, with the various location clauses to proxy Seafile. This nginx instance and Seafile are on the same server.

seafile/*
A copy of my config files for Seafile 7.1.3. Some addtional comments are in each particular file.

systemd/*
The two services form a pair. PartOf and Requires relates the two, ensuring the Seafile is started before Seahub, and stops it afterwards.

April 2020

