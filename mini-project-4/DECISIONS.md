## 📝 DECISIONS.md
1. **Connection Management** — How does your connection manager track connected clients? What happens if a client disconnects mid-vote? Does your app handle this gracefully, or does it crash?

My connection manager track connected clients by storing active WebSocket connections in a dictionary. The key is poll_id, and the value is the list of connected clients.

When a client connects, it is added to the list for the appropriate poll. When disabled, it is removed from the list.

If the client disconnects during the voting, the application does not crash, because it is processed: the connection is simply deleted, and the server continues to send updates to the rest of the clients.

2. **State Storage** — You are storing vote counts in memory. Why did you choose this over writing votes to a database? What breaks if you restart the server? What would need to change to make this production-ready?

We choose to store vote counts in memory (in the form of a Python dictionary), because it's a simple way that's suitable for demonstrating real-time work.

If we restart the server, all data will be lost. 

For a production-ready, we need to use a database for saving data, then our data will not be lost after restarting the server.

3. **Concurrency** — What would happen if two users voted at exactly the same moment? Did you handle this in your implementation? If not, what is the risk?

If two users will vote at exactly the same moment, there may be problem, because both changes occur at the same moment.

In my implementation there is no special handle for this, so theoretically one voice can “overwrite” the other.

4. **REST vs WebSocket** — You now have two ways to vote: `POST /polls/{id}/vote` and the WebSocket. What is the key difference in behavior between them? When would a client prefer one over the other?

The key difference is how the data is exchanged.

REST `POST /polls/{id}/vote` in request–response way: the client sends a request and receives a response, but other clients will not know about it automatically.

WebSocket is a continuous connection through which the server can immediately send updates to all connected clients.

If we talk about rea-time connection, clients will prefer WebSocket, because it immediately sends updates and and they don't have to refresh the page every time to see the response.