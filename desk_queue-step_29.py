# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: DeskQueue
from typing import Any, Dict, List


class AppConfig:
    """Конфигурация приложения DeskQueue через словарь настроек."""

    DEFAULT_CONFIG: Dict[str, Any] = {
        "max_queue_size": 100,
        "default_priority": "normal",
        "priority_levels": ["low", "normal", "high", "critical"],
        "status_options": [
            "pending", "in_progress", "completed", "rejected", "archived"
        ],
        "label_max_count": 20,
        "task_ttl_days": 365,
        "enable_notifications": False,
        "notification_channels": ["email", "slack"],
    }

    def __init__(self) -> None:
        self._config: Dict[str, Any] = dict(self.DEFAULT_CONFIG)

    @classmethod
    def from_dict(cls, settings: Dict[str, Any]) -> "AppConfig":
        """Создать AppConfig из произвольного словаря настроек."""
        instance = cls()
        instance._config.update(settings)
        return instance

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    @property
    def config(self) -> Dict[str, Any]:
        return dict(self._config)

    @staticmethod
    def validate_priority(priority: str) -> bool:
        allowed = AppConfig.DEFAULT_CONFIG["priority_levels"]
        return priority in allowed

    @staticmethod
    def validate_status(status: str) -> bool:
        allowed = AppConfig.DEFAULT_CONFIG["status_options"]
        return status in allowed


def get_app_config() -> AppConfig:
    """Получить текущую конфигурацию приложения."""
    return AppConfig.from_dict({})


if __name__ == "__main__":
    config = get_app_config()
    print(f"Default max_queue_size: {config.get('max_queue_size')}")
    print(f"Priority levels: {config.config['priority_levels']}")

    custom = AppConfig.from_dict({"max_queue_size": 50, "enable_notifications": True})
    print(f"Custom config: {custom.config}")

    assert AppConfig.validate_priority("high"), "Should be valid"
    assert not AppConfig.validate_priority("unknown"), "Should be invalid"
    assert AppConfig.validate_status("pending"), "Should be valid"
