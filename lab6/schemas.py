import pydantic as _pydantic


class Dance(_pydantic.BaseModel):
    dance_name: str
    caption: str
    native_name: str
    genre: str
    year: int
    origin: str


class DanceID(Dance):
    dance_id: int

    @staticmethod
    def mapper(dance: tuple):
        return DanceID(dance_id=dance[0], dance_name=dance[1], caption=dance[2],
                       native_name=dance[3], genre=dance[4], year=dance[5], origin=dance[6])

    class Config:
        orm_mode = True


class Artist(_pydantic.BaseModel):
    name: str
    surname: str
    country: str
    gender: str
    dance_style: int


class ArtistID(Artist):
    artist_id: int

    @staticmethod
    def mapper(artist: tuple):
        return ArtistID(artist_id=artist[0], name=artist[1], surname=artist[2],
                        country=artist[3], gender=artist[4], dance_style=artist[5])

    class Config:
        orm_mode = True


class Performance(_pydantic.BaseModel):
    title: str
    date: str
    country: str
    dance_style: int
    artist: int


class PerformanceID(Performance):
    performance_id: int

    @staticmethod
    def mapper(performance: tuple):
        return PerformanceID(performance_id=performance[0], title=performance[1], date=performance[2],
                             country=performance[3], dance_style=performance[4], artist=performance[5])

    class Config:
        orm_mode = True
