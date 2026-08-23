import asyncio
from dataclasses import dataclass


@dataclass
class AsyncStudentTask:
    student_name: str

    async def complete_assignment(self, topic: str, delay: int) -> str:
        print(f"{self.student_name} started: {topic}")
        await asyncio.sleep(delay)
        result = f"{self.student_name} completed {topic}"
        print(result)
        return result


class AsyncClassroom:
    def __init__(self) -> None:
        self.students = [
            AsyncStudentTask("Aman"),
            AsyncStudentTask("Priya"),
            AsyncStudentTask("Neha"),
        ]

    async def run_class(self) -> list[str]:
        tasks = [
            asyncio.create_task(self.students[0].complete_assignment("Math", 2)),
            asyncio.create_task(self.students[1].complete_assignment("Science", 1)),
            asyncio.create_task(self.students[2].complete_assignment("History", 3)),
        ]
        return await asyncio.gather(*tasks)


async def main() -> None:
    classroom = AsyncClassroom()
    report = await classroom.run_class()
    print("Final report:", report)


if __name__ == "__main__":
    asyncio.run(main())
