# Spring Boot Logging with Fluent Bit Sidecar on Kubernetes (Helm)

## Overview

This project demonstrates a **production-style logging setup for a Spring Boot application running on Kubernetes** using **Fluent Bit as a sidecar container**. The application writes logs to a file inside a shared volume, and Fluent Bit reads those logs and forwards them to an output destination.

This setup is useful when applications **write logs to files instead of stdout** or when **custom log parsing and processing** is required at the Pod level.

This repository shows how DevOps engineers can implement:

- Kubernetes logging architecture
- Helm-based application deployment
- Fluent Bit log collection
- Sidecar container pattern
- Shared volumes for log processing

---

# Architecture

```
                +----------------------------+
                |        Kubernetes          |
                |                            |
                |   +--------------------+   |
                |   |        Pod         |   |
                |   |                    |   |
                |   |  Spring Boot App   |   |
                |   |        │           |   |
                |   | writes logs        |   |
                |   |        ▼           |   |
                |   |   /logs/app.log    |   |
                |   |        ▲           |   |
                |   | reads logs         |   |
                |   |        │           |   |
                |   |    Fluent Bit      |   |
                |   |     Sidecar        |   |
                |   +--------------------+   |
                |           │                |
                |           ▼                |
                |       Log Output           |
                | (stdout / Loki / Elastic) |
                +----------------------------+
```

---

# Logging Flow

1. Spring Boot application writes logs to a file

```
/logs/app.log
```

2. A shared Kubernetes volume (`emptyDir`) is mounted to both containers.

3. Fluent Bit sidecar container tails the log file.

4. Logs are processed and sent to the configured output (stdout in this example).

---

# Repository Structure

```
springboot-fluentbit-logging
│
├── springboot-app
│   ├── src
│   ├── Dockerfile
│
├── helm-chart
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates
│       ├── deployment.yaml
│       ├── service.yaml
│       ├── configmap-fluentbit.yaml
│       └── _helpers.tpl
│
└── README.md
```

---

# Spring Boot Logging Configuration

Spring Boot uses **Logback** to write logs to a shared directory.

Example:

```
/logs/app.log
```

This allows Fluent Bit to read application logs from the same volume.

---

# Fluent Bit Configuration

Fluent Bit runs as a **sidecar container** inside the Pod and tails the application log file.

Example configuration:

```
[SERVICE]
    Flush        1
    Log_Level    info

[INPUT]
    Name tail
    Path /logs/*.log
    Tag springboot
    Refresh_Interval 5
    Read_from_Head true

[OUTPUT]
    Name stdout
    Match *
```

This configuration reads all `.log` files from the `/logs` directory.

---

# Helm Deployment

The application is deployed using **Helm**.

## Install

```
helm install springboot-logging ./helm-chart
```

## Upgrade

```
helm upgrade springboot-logging ./helm-chart
```

## Uninstall

```
helm uninstall springboot-logging
```

---

# Kubernetes Pod Structure

The Helm chart deploys a Pod containing two containers:

| Container | Purpose |
|----------|---------|
| Spring Boot | Runs the application |
| Fluent Bit | Collects application logs |

Both containers share the same volume:

```
emptyDir → /logs
```

---

# Verify Deployment

Check running pods:

```
kubectl get pods
```

View Spring Boot logs:

```
kubectl logs <pod-name> -c springboot-app
```

View Fluent Bit logs:

```
kubectl logs <pod-name> -c fluent-bit
```

Example output:

```
springboot: 2026-03-08 11:23:10 INFO Application started
```

---


# DevOps Concepts Demonstrated

This project demonstrates several important DevOps practices:

### Containerization
Packaging the Spring Boot application into a Docker container.

### Infrastructure as Code
Managing Kubernetes deployments using Helm charts.

### Observability
Collecting application logs using Fluent Bit.

### Kubernetes Architecture
Using the **sidecar container pattern**.

### Configuration Management
Managing Fluent Bit configuration through Kubernetes ConfigMaps.

---


Sidecar logging is typically used when:

- Applications write logs to files
- Custom log processing is required
- Security isolation is needed

---



