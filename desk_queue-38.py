# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: DeskQueue
import unittest
from deskqueue import Task, Queue, DeskQueue, Status

class TestDeskQueueEdgeCases(unittest.TestCase):
    def test_zero_deadline(self):
        q = Queue("urgent", deadline=0)
        self.assertEqual(q.deadline, 0)

    def test_negative_deadline(self):
        q = Queue("overdue", deadline=-1)
        self.assertEqual(q.deadline, -1)

    def test_empty_queue_returns_none(self):
        dq = DeskQueue()
        self.assertIsNone(dq.get_task())

    def test_get_task_returns_lowest_priority(self):
        dq = DeskQueue()
        dq.add_queue(Queue("low", priority=10))
        dq.add_queue(Queue("high", priority=1))
        self.assertEqual(dq.get_task().queue_name, "high")

    def test_duplicate_queue_names(self):
        dq = DeskQueue()
        dq.add_queue(Queue("dup", priority=1))
        dq.add_queue(Queue("dup", priority=2))
        self.assertEqual(len(dq.queues), 1)

    def test_mixed_deadlines(self):
        dq = DeskQueue()
        dq.add_queue(Queue("A", deadline=10))
        dq.add_queue(Queue("B", deadline=5))
        dq.add_queue(Queue("C", deadline=15))
        dq.add_task("A", queue="A", label="task1")
        dq.add_task("B", queue="B", label="task2")
        dq.add_task("C", queue="C", label="task3")
        self.assertEqual(dq.get_task().label, "task2")

    def test_status_transitions(self):
        task = Task(label="t1", status=Status.PENDING)
        self.assertEqual(task.status, Status.PENDING)
        task.status = Status.IN_PROGRESS
        self.assertEqual(task.status, Status.IN_PROGRESS)
        task.status = Status.COMPLETED
        self.assertEqual(task.status, Status.COMPLETED)
        task.status = Status.FAILED
        self.assertEqual(task.status, Status.FAILED)

    def test_empty_queue_name(self):
        q = Queue("", priority=1)
        self.assertEqual(q.name, "")

    def test_queue_with_spaces(self):
        q = Queue("  spaced  ", priority=1)
        self.assertEqual(q.name, "  spaced  ")

    def test_task_without_queue(self):
        task = Task(label="orphan", queue=None)
        self.assertIsNone(task.queue)

    def test_deskqueue_add_empty_task(self):
        dq = DeskQueue()
        dq.add_task(None)
        self.assertEqual(len(dq.tasks), 0)

    def test_deskqueue_get_nonexistent(self):
        dq = DeskQueue()
        self.assertIsNone(dq.get_task("ghost"))

if __name__ == "__main__":
    unittest.main()
