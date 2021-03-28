class guild_bot:
  def __init__(self, guild_id, bot_user_id, bot_command, pet_name, guild_bot_id: int=0):
    self.guild_bot_id = guild_bot_id
    self.guild_id = guild_id
    self.bot_user_id = bot_user_id
    self.bot_command = bot_command
    self.pet_name = pet_name
  
  @classmethod
  def from_database(cls, data_row):
    guild_bot_id = data_row[0]
    guild_id = data_row[1]
    bot_user_id = data_row[2]
    bot_command = data_row[3]
    pet_name = data_row[4]
    return cls(guild_id, bot_user_id, bot_command, pet_name, guild_bot_id)
