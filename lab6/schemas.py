import pydantic as _pydantic


class _DanceBase(_pydantic.BaseModel):
    dance_name: str
    caption: str
    native_name: str
    genre: str
    year: int
    origin: str


class DanceCreate(_DanceBase):
    pass

    class Config:
        orm_mode = True


class Dance(_DanceBase):
    dance_id: int

    class Config:
        orm_mode = True


class _ArtistBase(_pydantic.BaseModel):
    name: str
    surname: str
    country: str
    gender: str
    dance_style: int


class ArtistCreate(_ArtistBase):
    pass

    class Config:
        orm_mode = True


class Artist(_ArtistBase):
    artist_id: int

    class Config:
        orm_mode = True

class _PerformanceBase(_pydantic.BaseModel):
    title: str
    date: str
    country: str
    dance_style: int
    artist: int


class PerformanceCreate(_PerformanceBase):
    pass

    class Config:
        orm_mode = True


class Performance(_PerformanceBase):
    artist_id: int

    class Config:
        orm_mode = True
