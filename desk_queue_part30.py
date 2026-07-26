# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: DeskQueue
PROFILE_REGISTRY = {
    "default": {"queue_priority": 1, "deadline_hours": 24},
}


def register_profile(name: str, profile: dict) -> None:
    """Register a custom user profile with queue priority and deadline hours."""
    global PROFILE_REGISTRY
    if not isinstance(profile, dict):
        raise TypeError("profile must be a dictionary")
    required_keys = {"queue_priority", "deadline_hours"}
    missing = required_keys - set(profile.keys())
    if missing:
        raise ValueError(f"Profile '{name}' is missing keys: {missing}")
    PROFILE_REGISTRY[name] = profile


def get_profile(name: str) -> dict:
    """Return a registered profile or the default one."""
    return PROFILE_REGISTRY.get(name, PROFILE_REGISTRY["default"])


def list_profiles() -> list[str]:
    """Return all registered profile names including 'default'."""
    return list(PROFILE_REGISTRY.keys())


def apply_profile_to_tasks(tasks: list[dict], name: str) -> list[dict]:
    """Apply a profile's queue_priority and deadline_hours to each task in-place (returned as a new list)."""
    if tasks is None:
        raise ValueError("tasks must be a non-None list")
    profile = get_profile(name)
    updated = []
    for t in tasks:
        if not isinstance(t, dict):
            raise TypeError(f"Each task must be a dict; got {type(t).__name__}")
        new_task = {"queue_priority": profile["queue_priority"], "deadline_hours": profile["deadline_hours"]}
        existing_keys = set(t.keys()) - {"queue_priority", "deadline_hours"}
        new_task.update({k: t[k] for k in existing_keys})
        updated.append(new_task)
    return updated


def remove_profile(name: str) -> bool:
    """Remove a registered profile. Returns True if it existed."""
    if name not in PROFILE_REGISTRY:
        raise KeyError(f"Profile '{name}' does not exist")
    del PROFILE_REGISTRY[name]
    return True


def validate_profiles() -> dict[str, list[str]]:
    """Return errors per profile (empty lists for valid)."""
    errors = {}
    for name in PROFILE_REGISTRY:
        if name == "default":
            continue
        p = PROFILE_REGISTRY[name]
        errs = []
        if not isinstance(p.get("queue_priority"), int) or not 1 <= p["queue_priority"] <= 10:
            errs.append("queue_priority must be an integer in [1, 10]")
        if not isinstance(p.get("deadline_hours"), (int, float)) or p["deadline_hours"] < 0.5:
            errs.append("deadline_hours must be a non-negative number >= 0.5")
        errors[name] = errs
    return errors
