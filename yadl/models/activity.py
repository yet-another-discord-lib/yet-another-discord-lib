import attr
from enum import IntFlag, IntEnum
from typing import Dict, List, Optional
from typing_extensions import TypedDict

PositiveInt = int
String32 = str
String128 = str
ListMaxLen2 = List
Snowflake = int

PartyDict = TypedDict(
    "PartyDict",
    {
        "id": String128,
        "size": ListMaxLen2[PositiveInt],
    },
)

TimestampsDict = TypedDict(
    "TimestampsDict",
    {
        "start": PositiveInt,
        "end": PositiveInt,
    },
)

AssetsDict = TypedDict(
    "AssetsDict",
    {
        "large_image": String32,
        "large_text": String128,
        "small_image": String32,
        "small_text": String128,
    },
)

SecretsDict = TypedDict(
    "SecretsDict",
    {
        "match": String128,
        "join": String128,
        "spectate": String128,
    },
)

class ActivityFlags(IntFlag):
    INSTANCE = 1
    JOIN = 2
    SPECTATE = 4
    JOIN_REQUEST = 8
    SYNC = 16
    PLAY = 32


class ActivityType(IntEnum):
    unknown = -1
    playing = 0
    streaming = 1
    listening = 2
    watching = 3


@attr.s(auto_attribs=True, slots=True)
class Activity:
    name: String32
    state: Optional[String128] = None
    details: Optional[String128] = None
    timestamps: TimestampsDict = attr.Factory(TimestampsDict)
    assets: AssetsDict = attr.Factory(AssetsDict)
    party: PartyDict = attr.Factory(PartyDict)
    application_id: Optional[Snowflake]
    url: Optional[str] = None
    flags: ActivityFlags
    sync_id: Optional[Snowflake] = None
    session_id: Optional[Snowflake] = None
    instance: bool
    type: ActivityType
