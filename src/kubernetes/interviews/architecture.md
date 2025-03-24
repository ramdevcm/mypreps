# Kubernetes Architecture

Kubernetes (K8s) is an open-source container orchestration platform for automating deployment, scaling, and management of containerized applications. It has a master-slave architecture with a set of components that interact to provide a robust and scalable system.

## Key Components of Kubernetes Architecture

### 1. **Master Node (Control Plane)**
   - The Master Node is the heart of the Kubernetes cluster and is responsible for managing the cluster and making global decisions (e.g., scheduling, scaling).
   - Components of the Master Node:
     - **API Server** (`kube-apiserver`): It serves as the front-end for the Kubernetes control plane. All external commands interact with the API server.
     - **Controller Manager** (`kube-controller-manager`): This component runs controllers that handle routine tasks like replication, node management, etc.
     - **Scheduler** (`kube-scheduler`): It watches for newly created Pods with no assigned node and selects a suitable node for them to run on.
     - **Etcd** (`etcd`): A key-value store that stores all the cluster data, including the configuration and state of the system.

### 2. **Worker Node (Data Plane)**
   - Worker nodes are responsible for running the containerized applications in Pods.
   - Components of the Worker Node:
     - **Kubelet**: An agent that ensures containers are running in a Pod as expected. It communicates with the API server to keep the node in sync with the master.
     - **Kube Proxy**: A network proxy that maintains network rules for Pod communication and manages internal/external access to services.
     - **Container Runtime**: It is the software responsible for running containers. Examples include Docker, containerd, etc.

### 3. **Pod**
   - A Pod is the smallest deployable unit in Kubernetes. It represents a single instance of a running process in the cluster, typically encapsulating one or more containers.
   - Pods are scheduled on Worker Nodes by the Scheduler.

### 4. **Service**
   - A Kubernetes Service is an abstraction layer that defines a logical set of Pods and provides a stable IP address and DNS name for accessing them.

---

## Kubernetes Architecture Diagram

```plaintext
+-----------------------------------------------------------------------+
|                     +--------------------+
|                     |     Master Node    |
|                     |    (Control Plane) |
|                     +--------------------+
|                              |
|      +-----------------------+---------------------------+
|      |                       |                           |
| +------------+         +---------------+           +-----------------+
| | API Server | <-----> | Controller    |   <-----> | Scheduler       |
| |(kube-apiserver)      | Manager (kube-controller) | (kube-scheduler)|
| +------------+         +---------------+           +-----------------+
|                              |
|                         +----------+
|                         |   Etcd   |
|                         | (Storage)|
|                         +----------+
+-----------------------------------------------------------------------+                             


+-----------------------------------------------------------------------+
|
|                    +--------------------+
|                    |     Worker Node    |
|                    |     (Data Plane)   |
|                    +--------------------+
|                             |
|          +------------------+------------------+
|          |                  |                  |
|    +------------+   +---------------+    +---------------+
|    |   Kubelet  |   | Kube Proxy    |    | Container     |
|    |   (Agent)  |   | (Networking)  |    | Runtime       |
|    +------------+   +---------------+    +---------------+
|          |                   |                    |
|          |                   |                    |
|          |                   |                    |
|    +-------------+      +-------------+    +-------------+
|    |    Pod      |      |    Pod      |    |    Pod      |
|    |  (Container)|      |  (Container)|    |  (Container)|
|    +-------------+      +-------------+    +-------------+
|
+-----------------------------------------------------------------------+