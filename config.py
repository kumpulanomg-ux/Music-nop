"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os

class Config:
    def __init__(self) -> None:
        # قيمك هنا مباشرة 👇
        self.API_ID: str = "24514748"
        self.API_HASH: str = "5dbe5df68358919d32cbfd341e0142f1"
        self.SESSION: str = "BAF2ELwAv2zLyzl9IFRq8gWQJ1PHtohgta19i1Pb9viK8r_ZhZFmxXyCaGk3p8keTB6mEXjePGOTKX8FrMQyx_yJa5ah15-Mh_8TfnDslYAbVB0AGR0bD97Eygu4dUZUQkRhJqNnzsB-a2zbmxLOY-frL9baVoLtnVZj5sNz8JfUntuNIJPD__grAr8Rf1FLdfx9v-g77VVypjFJCTYVEke6eug2gGAwGH_eGJ0rh1GpkhEsZQa5lgGhCiIH3hoRG2BSPszRX_aSL9fcwl6RdO0xGbHg9kjFs-pZL9Fvz_QBNBIVUfxH-p5s7oqX8vYxLP_jo7--B07jteNlVIrf-VdCWeM35wAAAAHjwpdxAA"
        self.BOT_TOKEN: str = "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"  # لو عندك بوت توكن حطه هنا
        self.SUDOERS: list = [6334408675]

        # باقي الإعدادات
        self.SPOTIFY: bool = False
        self.QUALITY: str = "high"
        self.PREFIXES: list = ["."]
        self.LANGUAGE: str = "ar"   # ← اللغة عربي
        self.STREAM_MODE: str = "audio"
        self.ADMINS_ONLY: bool = False
        self.SPOTIFY_CLIENT_ID: str = None
        self.SPOTIFY_CLIENT_SECRET: str = None


config = Config()
