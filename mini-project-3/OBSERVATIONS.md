# OBSERVATIONS.md
1. What is the difference between a Pod and a Deployment? Why would you use a Deployment instead of a bare Pod?

A pod is a single instance of an application (container or multiple containers).
Deployment manages Pods. It creates them, scales them, and restarts them in case of failures.

Deployment is more useful, because it automatically restores Pods and makes it easy to increase or decrease their number.

2. Why is a ConfigMap used for the MongoDB URL instead of hardcoding it in the Deployment YAML?

Because ConfigMap allows you to store configurations separately from the application.

This is useful, because you can change the MongoDB URL without editing the Deployment.

3. What happened to the original Pod when you scaled the WebApp to 3 replicas? Did it get replaced, or were new Pods added alongside it?

When we scaled the WebApp to 3 replicas, the original Pod is not replaced, just two new ones are added to it.

4. What would happen to the application if the MongoDB Pod crashed? How would Kubernetes respond?

If a MongoDB Pod crashes, Kubernetes will notice, that it is no longer working and create a new Pod.

In this moment the application may temporarily lose its connection to the database, but after launching a new Pod, everything should be restored.

5. What is one thing that surprised you or that you found confusing? How did you resolve it?

At first, I was confused about how to work with file paths in WSL. I tried to use the Windows path (C:\Users ...), but it didn't work in Ubuntu. Then I figured out that I needed to use a path like /mnt/c/Users/..., and after that I was able to successfully apply YAML files via kubectl.

Then, I was confused by Git's warning about strings (LF and CRLF) when I added files to the repository. I realized that this is due to the difference between the string formats in Windows and Linux. This did not cause any errors, but as a precaution, I made git config --global core.autocrlf input. Now there is an understanding that such warnings may appear when working in a mixed environment (Windows + WSL).

I was also interested to see that when scaling, Kubernetes does not replace the old Pod, but simply adds new ones.