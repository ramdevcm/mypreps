# When Will Network Policy Work?

A **Network Policy** in Kubernetes works when it is explicitly defined to control the traffic flow between Pods. It restricts or allows communication based on labels and selectors. It only works if the cluster has a network plugin that supports policy enforcement, such as **Calico** or **Cilium** or **VPC CNI**.

- **Network Policies** allow or block traffic between Pods, namespaces, or services.
- By default, **Kubernetes allows all traffic** between Pods. To restrict traffic, you need to define a Network Policy.
- If no policy is applied, communication between pods/svc is unrestricted.

Network Policies are enforced at the **network layer**, meaning they control the flow of network traffic and do not affect other aspects of Pods, such as CPU or memory.


# Service A to Service B Communication Flow in Kubernetes

This diagram illustrates the communication between **Service A** and **Service B** within a Kubernetes cluster, involving **kube-proxy**, **iptables**, **network policies**, and the **Pods** representing **Service B**.

## Diagram Explanation

### Flow:
1. **Service A** initiates a request to **Service B**.
2. The request is intercepted by **Kube-Proxy**, which is responsible for managing the network routing rules using **iptables**.
3. **iptables** forwards the request to the correct **Service B Pod** based on the IP and port information.
4. **Network Policies** can be enforced here, controlling traffic flow between Pods. If no policy allows traffic from **Service A** to **Service B**, the communication is blocked.
5. The request reaches the appropriate **Service B Pod (Replica)** or is forwarded to the **Service B Endpoint**.

### Involvement of Network Policies:
- **Network Policies** are used to define which Pods or Services can communicate with each other. If a network policy is in place, it could block traffic from **Service A** to **Service B** if the policy does not allow it.
- The policies are applied before **iptables** routes the traffic to the destination Pod.

## Diagram

```plaintext
                +----------------+
                |   Service A    |
                +----------------+
                       |
                       v
                +----------------+
                |   Kube-Proxy   |
                +----------------+
                       |
                       v
                +----------------+
                |    iptables     |
                +----------------+
                       |
                       v
            +-----------------------------+
            |   Network Policies Applied  |
            +-----------------------------+
                       |
                       v
              +------------------+
              |  Service B Pod   |
              +------------------+
                       |
                       v
            +--------------------------+
            |  Service B Pod (Replica) |
            +--------------------------+
                       |
                       v
              +------------------+
              |    Service B     |
              |    Endpoint      |
              +------------------+


---
# Scenario-Based Network Policy Implementation

## Scenario: Block Traffic from Service A to Service B but Allow Service A to Service C

### Problem Statement:

You are managing a Kubernetes cluster with three services: **Service A**, **Service B**, and **Service C**, all running in the same namespace. You are tasked with implementing a network policy that:
1. **Blocks all traffic** from **Service A** to **Service B**.
2. **Allows traffic** from **Service A** to **Service C**.

### Requirements:
- **Service A** should **not** be able to access **Service B**.
- **Service A** should be able to access **Service C**.

### Solution:

To meet these requirements, you can create **two separate Network Policies**:
1. A policy to **block** traffic from **Service A** to **Service B**.
2. **Allow** traffic from **Service A** to **Service C** (This is default behaviour). 
    - Thus, need not create a seperate policy to allow traffic.

By defining these Network Policies, you can control the communication flow between the services.

### Network Policy YAML for Blocking Traffic from Service A to Service B

```yaml
# Network Policy to block traffic from Service A to Service B
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: block-service-a-to-service-b
  namespace: abc
spec:
  podSelector:
    matchLabels:
      app: service-b  # Apply to Pods with label "app=service-b"
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: service-a  # Block traffic from Pods with label "app=service-a"
  policyTypes:
  - Ingress  # This policy controls incoming traffic to Service B
