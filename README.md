# TaskManager — FastAPI, Postgres, Kubernetes, Kustomize

TaskManager, modern bir web uygulamasının konteynerize edilip Kubernetes üzerinde ölçeklenebilir şekilde çalıştırılmasını göstermek amacıyla hazırlanmış örnek bir projedir. Proje; FastAPI tabanlı bir backend, statik dosyalardan oluşan bir frontend, Postgres veritabanı ve NGINX Ingress Controller bileşenlerinden oluşan tam bir çalışma ortamı sunar.

---

## Amaç

Bu proje ile aşağıdaki hedefler uygulanmaktadır:

* Basit bir CRUD API geliştirmek
* Backend ve diğer bileşenleri Docker kullanarak konteynerize etmek
* Uygulamayı Kubernetes Deployment ve Service kaynaklarıyla çalıştırmak
* ConfigMap ve Secret kullanarak yapılandırma yönetimi sağlamak
* NGINX Ingress Controller ile route yönetimi gerçekleştirmek
* Kustomize yapısı ile manifest dosyalarını tek yerden yönetmek
* Localhost üzerinde gerçekçi bir domain yönlendirme deneyimi oluşturmak
* Postgres için stateful ve doğru tanımlanmış bir çalışma modeli kurmak

---

## Mimari

Uygulama aşağıdaki bileşenlerden oluşur:

* Ingress Controller: `/api` trafiğini backend servisine, diğer tüm trafiği frontend servisine yönlendirir.
* Backend (FastAPI): API uç noktalarını sağlar.
* Frontend: Statik HTML/JS/CSS dosyalarından oluşur.
* Postgres: Uygulamanın veritabanı bileşenidir.

Bu yapı gerçek bir üretim mimarisinin temel seviyede simülasyonunu sunar.

---

## Proje Yapısı

```
taskmanager/
 ├── app/                     # FastAPI backend
 ├── frontend/                # Statik frontend dosyaları
 ├── k8s/                     # Kubernetes manifestleri
 │    ├── backend-deployment.yaml
 │    ├── backend-service.yaml
 │    ├── frontend-deployment.yaml
 │    ├── frontend-service.yaml
 │    ├── postgres-deployment.yaml
 │    ├── postgres-service.yaml
 │    ├── configmap.yaml
 │    ├── secret.yaml
 │    ├── ingress.yaml
 │    └── kustomization.yaml
 ├── Dockerfile               # Backend Docker image tanımı
 ├── requirements.txt         # Python bağımlılıkları
 └── docker-compose.yaml      # Lokal ortam için kolay başlatma
```

---

## Docker Compose ile Lokal Çalıştırma

Aşağıdaki komut ile uygulamayı lokal ortamda çalıştırabilirsiniz:

```
docker compose up -d --build
```

Erişim adresleri:

* Backend: [http://localhost:8000](http://localhost:8000)
* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* Frontend: [http://localhost:3000](http://localhost:3000)

---

## Kubernetes Üzerinde Çalıştırma (Kustomize)

Kubernetes üzerinde çalıştırmak için:

```
kubectl apply -k k8s/
```

Erişim adresleri:

* Backend API: [http://localhost/api](http://localhost/api)
* Frontend: [http://localhost/](http://localhost/)

Ingress Controller, gerekli yönlendirmeleri otomatik olarak sağlar.

---

## API Özellikleri

Backend API aşağıdaki temel işlemleri destekler:

* Görev ekleme
* Görev listeleme
* Görev silme
* Swagger ve Redoc dokümantasyonu

---

## Güvenlik ve Yapılandırma Yönetimi

* Uygulama ayarları ConfigMap içinde yönetilir.
* Veritabanı kullanıcı adı ve parolası Secret içinde tutulur.
* Kustomize sayesinde environment veya namespace bazlı overlay eklemek kolaydır.

---

## Neden Bu Proje?

Bu proje, bir DevOps veya Cloud mühendisi için pratik ve gerçekçi bir örnek niteliğindedir.
Kubernetes kaynakları, servis yönlendirmeleri, konteynerleşme süreci ve yapılandırma yönetimi hakkında bütünsel bir bakış sunar. Ayrıca üretim ortamlarında kullanılan yapıların temelini öğrenmek için uygun bir örnek projedir.

---

## Sonuç

TaskManager, uçtan uca bir web uygulamasının Kubernetes üzerinde nasıl yapılandırılıp yönetileceğini gösteren öğretici bir altyapı projesidir. İhtiyaca göre CI/CD, monitoring, Helm
