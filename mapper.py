from datetime import datetime
from track import track

class mapper:
    def get_track_from_message(self, message):
        guild_id = message.guild.id
        timestamp = message.created_at
        contents = message.content
        embeds = message.embeds
        if contents:
            if contents.StartsWith('**Playing**'):


