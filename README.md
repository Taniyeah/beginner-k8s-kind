# Beginner Kubernetes with kind

This repo is a kubernetes starter project
It shows how to run a tiny Python web app inside Kubernetes using [kind](https://kind.sigs.k8s.io/) (Kubernetes in Docker).

---

## What you’ll learn
- How to create a local kubenetes cluster with kind
- How to package a tiny **Flask** app into a Docker image
- How to deploy the app to Kubernetes with a **Deployment**
- How to expose it to your laptop with a **NodePort Service**
- How to manage config with a **ConfigMap** (and see a Secret pattern)

---

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

*(Optional: `make` if you want to use the included Makefile shortcuts.)*

---

## Quickstart (3 commands)
```bash
make cluster      # 1) create a local kind cluster
make build load   # 2) build the image and load it into kind
make deploy       # 3) apply Namespace, ConfigMap, Secret, Deployment, Service
