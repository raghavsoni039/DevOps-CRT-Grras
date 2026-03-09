# Kubernetes 2-Tier Application

## Project Description

This project shows how to deploy a **simple 2-tier application in Kubernetes**.

The application has two parts:

* **Frontend** – a web server (nginx)
* **Backend** – a small API that returns a message

The frontend communicates with the backend using a **Kubernetes Service**.

---

## Architecture

```
User
  ↓
Frontend Service (NodePort)
  ↓
Frontend Pods (nginx)
  ↓
Backend Service (ClusterIP)
  ↓
Backend Pods (http-echo)
```

---

## Kubernetes Resources Used

This project uses the following Kubernetes components:

* **Namespace** – to isolate the application
* **Backend Deployment** – runs backend pods
* **Backend Service** – allows frontend to reach backend
* **Frontend Deployment** – runs nginx pods
* **Frontend Service** – exposes the application outside the cluster

---

## Project Files

```
kubernetes-two-tier-app
│
├── namespace.yaml
├── backend-deployment.yaml
├── backend-service.yaml
├── frontend-deployment.yaml
├── frontend-service.yaml
└── README.md
```

---

## How to Run the Project

### 1. Start Kubernetes (Minikube)

```
minikube start
```

Check cluster:

```
kubectl get nodes
```

---

### 2. Deploy the Application

Run the following command inside the project folder:

```
kubectl apply -f .
```

---

### 3. Check Running Resources

Check pods:

```
kubectl get pods -n two-tier-app
```

Check services:

```
kubectl get svc -n two-tier-app
```

---

## Access the Application

Get the Minikube IP:

```
minikube ip
```

Open the application in browser:

```
http://MINIKUBE-IP:30007
```

---

## Expected Output

You should see something like:

```
Frontend is running
Backend response:
Hello from Backend
```

---

