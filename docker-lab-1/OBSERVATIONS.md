# Observations
1. What is the size of your image? Is it large or small — and why do you think that is?

My image size is 3.42 MB (based on content size of image). I think this is a very small image compared to most other Docker images. Alpine:3.19 is a lightweight version of Linux, that includes only basic tools, so the image is small and quick to download.

2. How many layers does your image have? What does each major layer add?

The image has 2 layers. The largest layer contains the Alpine Linux filesystem, which is about 8 MB. The second layer defines the default command (CMD ["/bin/sh"]) and has almost no size.

3. What operating system and architecture does your image use? (from `docker inspect`)

From `docker inspect` I understood, that my image uses the Linux operating system and the amd64 architecture. 

4. **Image-specific question:**
   - 🏔️ Alpine: What happened when you installed `curl` inside the container? After you exited and restarted, was `curl` still installed? Why?

When I installed `curl` inside the container using `apk add curl`, it was successfully installed and worked inside the running container. But after exiting the container and starting a new one, `curl` was no longer installed.
This is because containers are short-lived. Any changes made inside the container are lost when the container is deleted, unless they have been saved or moved to a new image.

5. In one paragraph: what surprised you most about this lab?

What surprised me the most about this lab is that the changes inside the container are not saved after it is stopped. I was also surprised that images can have such a small size. And I also noticed that when running `docker run alpine:3.19`, the container exits immediately.