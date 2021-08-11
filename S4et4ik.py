class Counter:
    def __init__(self, min_val=0, max_val=100, current_val=None):
        self.min = min_val
        self.max = max_val
        if current_val is None:
            self.current_val = self.min
        else:
            self.current_val = current_val

    def make_step(self, step=1):
        if self.current_val >= self.max:
            self.current_val = self.min
        else:
            self.current_val += step

    def get_current_val(self):
        return self.current_val
