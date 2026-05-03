from fastapi import FastAPI, HTTPException
from .schemas import PollCreate, VoteRequest
from .models import Poll
from .storage import polls

app = FastAPI()

@app.post("/polls")
def create_poll(data: PollCreate):
    poll = Poll(data.question, data.options)
    polls[poll.id] = poll
    return {"id": poll.id, "question": poll.question, "options": poll.options}

@app.get("/polls")
def get_polls():
    return [
        {
            "id": p.id,
            "question": p.question,
            "options": p.options,
            "votes": p.votes
        }
        for p in polls.values()
    ]

@app.get("/polls/{poll_id}")
def get_poll(poll_id: str):
    poll = polls.get(poll_id)

    if not poll:
        raise HTTPException(status_code=404, detail="Poll not found")

    return {
        "id": poll.id,
        "question": poll.question,
        "options": poll.options,
        "votes": poll.votes
    }

@app.post("/polls/{poll_id}/vote")
def vote(poll_id: str, vote: VoteRequest):
    poll = polls.get(poll_id)

    if not poll:
        raise HTTPException(status_code=404, detail="Poll not found")

    if vote.option not in poll.votes:
        raise HTTPException(status_code=400, detail="Invalid option")

    poll.votes[vote.option] += 1

    return {"message": "Vote recorded", "votes": poll.votes}

@app.delete("/polls/{poll_id}")
def delete_poll(poll_id: str):
    if poll_id not in polls:
        raise HTTPException(status_code=404, detail="Poll not found")

    del polls[poll_id]
    return {"message": "Poll deleted"}

