from datetime import datetime

class guild:
  
# (0, "Dwq", "$", "WEFW", "weafefaf", "afwf", "qfeggg", datetime(1982,6,1))
  def __init__(self, discord_id, name, command, nickname, monitor_channel, join_user, join_date: datetime=datetime.now(), guild_id: int=0):
    self.guild_id = guild_id
    self.discord_id = discord_id
    self.name = name
    self.command = command
    self.nickname = nickname
    self.monitor_channel = monitor_channel
    self.join_user = join_user
    self.join_date = join_date
  
  @classmethod
  def from_database(cls, data_row):
    guild_id = data_row[0]
    discord_id = data_row[1]
    name = data_row[2]
    command = data_row[3]
    nickname = data_row[4]
    monitor_channel = data_row[5]
    join_user = data_row[6]
    join_date = data_row[7]
    return cls(discord_id, name, command, nickname, monitor_channel, join_user, join_date, guild_id)