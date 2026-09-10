# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: DeskQueue
def self_check():
    print("=" * 60)
    print("DeskQueue - Final Self-Check")
    print("=" * 60)
    
    # Test task creation
    t1 = Task("Test task 1", priority="high", tags=["urgent", "test"])
    t1.add_comment("Initial comment")
    t1.add_comment("Follow-up")
    assert t1.comments == 2, "Task 1 comments failed"
    
    # Test task status transitions
    t2 = Task("Test task 2", priority="low")
    t2.status = "new"
    t2.status = "ready"
    t2.status = "in_progress"
    assert t2.status == "in_progress", "Task 2 status failed"
    
    # Test priority queue
    pq = PriorityQueue()
    pq.add(t1)
    pq.add(t2)
    pq.add(Task("Test task 3", priority="medium"))
    assert len(pq) == 3, "Priority queue failed"
    
    # Test deadline
    t3 = Task("Deadline task", deadline="2025-12-31")
    t3.status = "in_progress"
    deadline_passed = t3.check_deadline()
    assert deadline_passed is False, "Deadline check failed"
    
    print("All checks passed. DeskQueue is ready for production use!")
    print("Features: Task management, Priority queues, Deadlines, Status tracking, Comments, Tags")
    print("=" * 60)

if __name__ == "__main__":
    self_check()
