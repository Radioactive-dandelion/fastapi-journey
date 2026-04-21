## OBSERVATIONS.md
1. What is the difference between running a container with `docker run` and deploying a pod with `kubectl run`? Both used the same image — what changed?

`docker run` just runs one container directly on the machine.

`kubectl run` creates a Pod in Kubernetes, and it is already managed by the cluster (scheduler, controllers, etc.).

2. In `kubectl describe pod`, what is the role of the **Scheduler** event? Which control plane component does that correspond to?

In `kubectl describe pod` the **Scheduler** selects which node to run the Pod on. This is the control plane component that distributes the workload.

3. In `kubectl get pods -n kube-system`, name two components you recognised from the lecture and describe what they do.

In `kubectl get pods -n kube-system` I saw and recognised two components:

kube-apiserver - it acts as the main entry point and handles all API requests in the cluster.

kube-scheduler - assigns Pods to nodes based on available resources and scheduling rules.

4. **Image-specific observation** (answer only the one relevant to your image):
   - 🏔️ Alpine: What happened to any changes you made inside the pod shell when you exited? Compare this to your experience in Docker Lab 1.

Changes inside the Pod are not saved after exiting. The container is temporary, and when stopped, everything disappears.
The result was similar in Docker Lab 1, any changes inside the container are temporary and are not saved.

5. Task 6 reflection: After deleting the pod, Kubernetes did **not** restart it. In one paragraph, explain why, and what Kubernetes object would change this behaviour.

After deleting the pod, Kubernetes did not restart it because it was created as a standalone Pod without any controller managing it. 

For changing this behavior, Kubernetes Deployment can be used. A Deployment would automatically recreate it.

6. What components do you see running in kube-system? Can you identify any components from the lecture (scheduler, etcd, api-server)?

In the namespace kube-system, I saw the main components of Kubernetes: kube-apiserver, etcd, kube-scheduler and kube-controller-manager.

These are the main parts of the control plane that manage the cluster.

7. In the Events section of kubectl describe, what sequence of events happened before the pod started running? Which component scheduled the pod?

First, the Pod is created in the Pending state, then the scheduler selects the node to run. After that, kubelet downloads the image and launches the container.
The Pod switches to the Running state.

8. After deleting the pod manually, did Kubernetes bring it back? Why or why not?

The Pod did not recover because it was created as a separate object without a controller (for example, Deployment).
Kubernetes does not monitor such Pods and does not recreate them automatically.

9. What would need to be different (hint: think about what you'll learn in Lecture 4) for Kubernetes to automatically restart a deleted pod?

For automatic recovery, you need to use Deployment.
Deployment monitors the number of Pods and creates new ones if they are deleted or dropped.