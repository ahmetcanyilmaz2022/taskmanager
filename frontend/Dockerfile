# Kullanacağımız base image
FROM nginx:alpine

# Uygulama dosyalarını Nginx klasörüne kopyala
COPY . /usr/share/nginx/html

# 80 portunu aç
EXPOSE 80

# Nginx çalıştır
CMD ["nginx", "-g", "daemon off;"]
