
class printerError(RuntimeError):
    pass


class printer:
    def __init__(self, capacity : int, pages_per_s : float):
        self.capacity = capacity
        self.pages_per_s = pages_per_s

    def print_pages(self, pages):
        if pages > self.capacity:
            raise PrinterError ('Not sufficient pages in the printer, give a smaller number')
        self.capacity -= pages
        return f"Printed {pages} pages in {pages/self.pages_per_s:.2f} seconds."
