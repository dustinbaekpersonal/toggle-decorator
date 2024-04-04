class ToggleDecorator:
    def __init__(self, decorator_func):
        self._enabled = False
        self._decorator_func = decorator_func
    
    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, val: bool):
        if not isinstance(val, bool):
            raise ValueError(f"{val} should be either True or False.")
        self._enabled = val
    
    def __call__(self, target_func):
        if self._enabled:
            return self._decorator_func(target_func)
        return target_func
    