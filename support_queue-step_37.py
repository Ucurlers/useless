# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: SupportQueue
import unittest
from support_queue.core.queue import SupportQueue, Ticket, Priority


class TestSupportQueue(unittest.TestCase):

    def setUp(self):
        self.q = SupportQueue()

    def test_priority_ordering(self):
        t1 = Ticket("Low", "user1", "Low")
        t2 = Ticket("High", "user2", "High")
        t3 = Ticket("Medium", "user3", "Medium")
        self.q.add(t1)
        self.q.add(t2)
        self.q.add(t3)
        self.assertEqual(self.q.next(), t2)
        self.assertEqual(self.q.next(), t3)
        self.assertEqual(self.q.next(), t1)

    def test_add_and_remove(self):
        t = Ticket("Test", "user", "Medium")
        self.q.add(t)
        self.assertEqual(len(self.q), 1)
        removed = self.q.remove(t)
        self.assertTrue(removed)
        self.assertEqual(len(self.q), 0)

    def test_remove_nonexistent(self):
        t = Ticket("Test", "user", "Medium")
        self.q.add(t)
        self.assertFalse(self.q.remove("Ghost"))

    def test_empty_queue_next(self):
        self.assertIsNone(self.q.next())

    def test_multiple_same_priority(self):
        t1 = Ticket("A", "u", "High")
        t2 = Ticket("B", "u", "High")
        self.q.add(t1)
        self.q.add(t2)
        self.assertEqual(self.q.next().text, "A")
        self.assertEqual(self.q.next().text, "B")


if __name__ == "__main__":
    unittest.main()
