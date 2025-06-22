class Amenity(BaseModel):
    def __init__(self, *args, **kwargs):
        self.name = ""
        super().__init__(*args, **kwargs)

