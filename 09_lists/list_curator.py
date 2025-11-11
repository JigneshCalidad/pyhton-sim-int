"""Practice adding and removing list items with intention."""

journal_topics = ["gratitude", "dreams", "questions"]
print("Original topics:", journal_topics)

journal_topics.append("insights")
print("After adding insights:", journal_topics)

journal_topics.remove("questions")
print("After releasing questions:", journal_topics)

deleted_topic = journal_topics.pop()
print("Popped the last topic:", deleted_topic)
print("List now feels focused:", journal_topics)

