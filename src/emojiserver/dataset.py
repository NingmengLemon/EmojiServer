import json
from typing import TypedDict


class EmojiData(TypedDict):
    name: str
    unified: str
    non_qualified: str | None
    docomo: str | None
    au: str | None
    softbank: str | None
    google: str | None
    image: str
    sheet_x: int
    sheet_y: int
    short_name: str
    short_names: list[str]
    text: str | None
    texts: list[str] | None
    category: str
    subcategory: str
    sort_order: int
    added_in: str
    has_img_apple: bool
    has_img_google: bool
    has_img_twitter: bool
    has_img_facebook: bool


class EmojiDataset:
    def __init__(
        self, datafile: str = "emoji.json", image_folder: str = "img-google-136"
    ):
        self._datafile = datafile
        self._imgfolder = image_folder
        self._emojis: list[EmojiData] = []

    def load(self):
        if self._emojis:
            raise ValueError("already loaded")
        with open(self._datafile, "r", encoding="utf-8") as fp:
            dataset = json.load(fp)
        for em in dataset:
            self._emojis.append(em)
            if "skin_variations" in em:
                for v in em["skin_variations"].values():
                    self._emojis.append({**em, **v})

    def get_emoji(self, emoji_text) -> dict[str, EmojiData] | None:
        code = "-".join(left_pad(hex(ord(char))[2:], 4, "0") for char in emoji_text)
        for e in self._emojis:
            if (
                e["unified"].lower() == code.lower()
                or e["name"].lower().replace(" ", "-") == emoji_text.lower()
            ):
                return e


def left_pad(string: str, length, character):
    return string.rjust(length, character)
