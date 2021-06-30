FROM nginx:latest

COPY /client/api /var/www/api
COPY /TS-API-INTEGRACAO/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443

ENTRYPOINT ["nginx"]

CMD ["-g", "daemon off;"]