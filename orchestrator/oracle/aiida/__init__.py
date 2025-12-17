def __getattr__(name):
    """Lazy import to avoid requiring aiida for non-aiida workflows."""
    if name == "AiidaOracle":
        from .oracle_base import AiidaOracle
        return AiidaOracle
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "AiidaOracle",
]
