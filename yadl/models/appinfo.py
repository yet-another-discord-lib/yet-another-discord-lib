import attr
from typing import List, Optional


@attr.s(auto_attribs=True, slots=True)
class AppInfo:
    id: int
    name: str
    owner: User
    team: Optional[Team]
    icon: Optional[str]
    description: Optional[str]
    public: bool
    require_code_grant: bool
    rpc_origin_urls: Optional[List[str]]
    summary: Optional[str]
    getticket_key: Optional[str]
    guild_id: Optional[int]
    game_sku: Optional[int]
    game_url_slug: Optional[str]
    cover_image: Optional[str]

    

    