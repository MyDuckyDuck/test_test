# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: DeskQueue
import unittest


class TestDeskQueue(unittest.TestCase):

    def test_queue_add_and_get(self):
        from deskqueue import DeskQueue
        q = DeskQueue()
        q.add("A", 10)
        q.add("B", 20)
        self.assertEqual(q.get(), "A")
        self.assertEqual(q.get(), "B")

    def test_queue_timeout(self):
        from deskqueue import DeskQueue
        q = DeskQueue()
        q.add("X", timeout=1.0)
        self.assertIsNone(q.get(timeout=0.5))
        self.assertIsNotNone(q.get(timeout=2.0))

    def test_task_status_flow(self):
        from deskqueue import TaskStatus
        s = TaskStatus()
        s.update(1, "PENDING")
        s.update(1, "RUNNING")
        s.update(1, "DONE")
        self.assertEqual(s.get_status(), 1)

    def test_task_tags(self):
        from deskqueue import TaskTags
        t = TaskTags()
        t.add("urgent", 42)
        t.remove("urgent", 42)
        self.assertFalse(t.contains("urgent", 42))


if __name__ == "__main__":
    unittest.main()
