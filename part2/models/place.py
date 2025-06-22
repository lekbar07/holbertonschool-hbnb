class Place(BaseModel):
    def __init__(self, *args, **kwargs):
        self.user_id = ""      # Owner of the place
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []  # List of Amenity IDs
        super().__init__(*args, **kwargs)

