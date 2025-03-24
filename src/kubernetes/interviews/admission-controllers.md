# Admission Controllers in Kubernetes

**Admission Controllers** are powerful extensions in Kubernetes that validate or modify incoming requests to the Kubernetes API server before they are persisted in the cluster. They provide a way to enforce security, resource management, and compliance policies by validating, mutating, or rejecting requests based on predefined rules.

There are two types of Admission Controllers:
1. **Validating Admission Controllers**: These check if the request complies with certain rules and can **reject** it if needed.
2. **Mutating Admission Controllers**: These can modify the incoming request (e.g., add default values) before it is persisted.

## Scenarios of Admission Controllers

### Scenario 1: Enforcing Resource Limits for All Pods

**Problem**: You want to ensure that every Pod in the cluster has resource requests and limits (CPU and memory) set, preventing resource contention.

**Solution**: Use the `LimitRanger` Admission Controller to automatically set default resource requests and limits for any Pods that do not define them.

**Action**: This will ensure all Pods have proper resource requests and limits, improving resource management.

---

### Scenario 2: Enforcing Security Context for All Pods

**Problem**: You want to enforce that all Pods must run as non-root users to ensure security.

**Solution**: Use the `PodSecurityPolicy` (or the upcoming `PodSecurity`) Admission Controller to reject Pods that run as root.

**Action**: The Admission Controller ensures that Pods do not run as root by validating the `runAsUser` field and rejecting requests where it is set to root.

---

### Scenario 3: Preventing Creation of Dangerous Containers

**Problem**: You want to block Pods from using insecure or untrusted container images from public registries.

**Solution**: Use a **Validating Admission Controller** to validate the image being used before a Pod can be created, blocking Pods that use untrusted or insecure images.

**Action**: The controller checks the image name or registry and rejects the request if it matches a list of forbidden or untrusted images.

---

### Scenario 4: Automatically Adding Labels to Pods

**Problem**: You want to ensure that all Pods created in the cluster automatically receive a specific label for better organization (e.g., `env=production`).

**Solution**: Use a **Mutating Admission Controller** to automatically add a label (`env=production`) to every Pod creation request.

**Action**: The Admission Controller modifies the Pod’s metadata before it is persisted, ensuring that the label is applied.

---

### Scenario 5: Blocking Pods from Being Created in Deprecated Namespaces

**Problem**: Certain namespaces in the cluster are deprecated, and you want to prevent the creation of Pods in those namespaces.

**Solution**: Use a **Validating Admission Controller** to reject any request to create Pods in deprecated namespaces.

**Action**: The controller checks the namespace of the incoming request and denies the creation if the namespace is deprecated.

---

### Scenario 6: Preventing Privilege Escalation via kubectl Exec

**Problem**: You want to prevent users from escalating privileges within Pods by using `kubectl exec`.

**Solution**: Use a **Validating Admission Controller** (such as `DenyEscalatingExec`) to block any attempt to escalate privileges via `kubectl exec`.

**Action**: The controller prevents any request to run privileged commands, rejecting the request if it attempts privilege escalation.

---

### Scenario 7: Enforcing Labeling Convention for Resources

**Problem**: You want to ensure that all resources created in the cluster (e.g., Pods, Deployments) adhere to a labeling convention for organization and management.

**Solution**: Use a **Validating Admission Controller** to validate the presence of required labels on resources.

**Action**: The controller ensures that every resource created contains the required labels (e.g., `app`, `env`, `team`) and rejects any resource creation that doesn’t meet the label criteria.

---

## Conclusion

**Admission Controllers** are essential in enforcing policies and managing resources within Kubernetes clusters. They help ensure security, compliance, and resource management by validating and modifying requests before they are persisted. Admission controllers can be customized to fit specific use cases, from enforcing resource limits to blocking insecure containers or ensuring labeling conventions.
