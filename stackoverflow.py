from enum import Enum, auto
from typing import Optional

"""
start: 4:04PM 
first draft: 5:09PM

Align with requirement:

system.create_user( ... ) 
system.post_question(user1, "something")
system.vote_question(user1, "something")
system.comment_question(user1, "something")
system.vote_answer(user1, "something")
system.search(user, "something")
system.check_user_reputation_score(user)
"""


class VoteType(Enum):
    UPVOTE = auto()
    DOWNVOTE = auto()


class User:
    def __init__(self) -> None:
        self.reputation_score = 0
        self.profile = None

class Comment:
    def __init__(self, creator, content) -> None:
        self.creator = creator
        self.content = content 
        
class Vote:
    def __init__(self, creator, value) -> None:
        self.creator = creator
        self.value = value

        
class Tag:
    def __init__(self, name) -> None:
        self.name = name


class Votable:
    def __init__(self) -> None:
        self.creator: User = None
        self.votes: list[Vote] = []

    def vote(self, user: User, type: VoteType) -> Vote:
        new_vote = Vote(user, type)
        self.votes.append(new_vote)
    
        if type == VoteType.UPVOTE:
            self.creator.reputation_score += 1
        elif type == VoteType.DOWNVOTE:
            self.creator.reputation_score -= 1
        else:
            raise ValueError("Invalid vote type")
        

class Commentable:
    def __init__(self) -> None:
        self.comments = []

    def comment(self, user: User, content: str) -> Comment:
        new_comment = Comment(user, content)
        self.comments.append(new_comment)
        return new_comment



class Question(Votable, Commentable):
    def __init__(self, creator, content) -> None:
        self.creator = creator 
        self.content = content
        self.votes: list[Vote] = []
        self.comments: list[Comment] = []
        self.tags: list[Tag] = []
        self.answers: list[Answer] = []



class Answer(Votable, Commentable):
    def __init__(self, creator, question, content) -> None:
        self.creator: User = creator
        self.question: Question = question 
        self.votes : list[Vote] = []
        self.comments: list[Comment] = []
        self.content = content
       

class StackOverflow:
    def __init__(self) -> None:
        self.questions: list[Question] = []
        self.users: list[User] = []
        self.answers: list[Answer] = []
        self.tags: list[Tag] = []

    def post_question(self, content: str, user: User, tags: Optional[list[str]] = None) -> Question:
        q = Question(user, content)
        self.questions.append(q)

        for t in tags:
            for exiting_tag in self.tags:
                if exiting_tag.name == t:
                    q.tags.append(exiting_tag)
                    continue
            q.tags.append(Tag(t))
        

    def answer_question(self, question: Question, user: User, content: str) -> None:
        for q in self.questions:
            if q == question:
                answer = Answer(user, question, content)
                q.answers.append(answer)
                self.answers.append(answer)
                return
        raise ValueError("Question not found")

    def comment_question(self, question: Question, user: User, content: str) -> None:
        for q in self.questions:
            if q == question:
                answer = q.comment(user, content)
                self.answers.append(answer)
                return
        raise ValueError("Question not found")

    def comment_answer(self, answer: Answer, user: User, content: str) -> None:
        for a in self.answers:
            if a == answer:
                a.comment(user, content)
        raise ValueError("Answer not found")


    def vote_question(self, user: User, question: Question, type: VoteType) -> None:
        for q in self.questions:
            if q == question:
                q.vote(user, type)
                return
        raise ValueError("Question not found")

    def vote_answer(self, user: User, answer: Answer, type: VoteType) -> None:
        for a in self.answers:
            if a == answer:
                a.vote(user,type)
        raise ValueError("Answer not found")

    def get_user_reputation(self, user: User) -> None:
        return user.reputation_score

    def search_question(self, search_param: str) -> list[Question]:
        results = []
        for q in self.questions:

            if search_param == q.content:
                results.append(q)
            else:
                for t in q.tags:
                    if t.content == search_param:
                        results.append(q)

        return results
            




if __name__ == "__main__":
    pass