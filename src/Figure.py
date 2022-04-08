class Figure:
    area = None

    def add_area(self, figure):
        try:
            if isinstance(figure, Figure):
                return self.area + figure.area
            else:
                raise ValueError("ValueError Incorrect class")
        except ValueError as a:
            print(f"{a}")
