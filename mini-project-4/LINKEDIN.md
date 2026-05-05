# Post:
I have created an application that allows real-time voting with FastAPI and WebSockets.

For this application, I have created the backend infrastructure where multiple users can participate in voting in a survey and receive notifications of changes from other participants' votes.

It should be noted that not REST API, but WebSocket connections are used here, which allow establishing continuous contact with the server and clients and sending changes from the server without reloading or additional requests.

One of the main challenges was to implement WebSocket and achieve synchronization between multiple clients. Initially, I could not connect through the browser because of certain errors; therefore, I managed to solve this issue by developing an HTML interface for a client and implementing connection management on the server side.

Through this project, I managed to understand the difference between regular request-response architecture and events in real time.

You can view the demo or the project code here:
https://github.com/Radioactive-dandelion/fastapi-journey/tree/pzimina-mini-project-4

#FastAPI #WebSockets #BackendDevelopment #100DaysOfCode

# URL
https://www.linkedin.com/posts/polina-zimina-9618663b2_fastapi-websockets-backenddevelopment-ugcPost-7457526031843794944-3QT6?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGTc09kBuMu7g6gI0jaKpJ-Dijz6gC1Qfz4