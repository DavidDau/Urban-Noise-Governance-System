from enum import Enum


class VenueType(str, Enum):
    residential = "Residential Zone"
    commercial = "Commercial Zone"
    industrial = "Industrial Zone"
    quiet = "Quiet Zone"
    special_quiet = "Special Quiet Zone"
    soundproof = "Soundproof Venue"
    non_soundproof = "Non-Soundproof Venue"