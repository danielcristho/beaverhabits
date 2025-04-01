from nicegui import context

from beaverhabits.storage.storage import Habit

ROOT_PATH_KEY = "root_path"
ROOT_PATH_DEFAULT = "/"

DEMO_ROOT_PATH = "/demo"
GUI_ROOT_PATH = "/gui"


def is_page_demo() -> bool:
    path = context.client.page.path
    return path.startswith(DEMO_ROOT_PATH) or "pricing" in path


def get_root_path() -> str:
    return DEMO_ROOT_PATH if is_page_demo() else GUI_ROOT_PATH


def get_habit_page_path(habit: Habit) -> str:
    return f"{get_root_path()}/habits/{habit.id}"


def get_habit_heatmap_path(habit: Habit) -> str:
    return f"{get_root_path()}/habits/{habit.id}/streak"


def get_page_title() -> str:
    return "Demo" if is_page_demo() else "Habits"
