class track:
  def __init__(self, name, url, host, length, track_id: int=0):
    self.track_id = track_id
    self.name = name
    self.url = url
    self.host = host
    self.length = length
  
  @classmethod
  def from_database(cls, data_row):
    track_id = data_row[0]
    url = data_row[1]
    name = data_row[2]
    host = data_row[3]
    length = data_row[4]
    return cls(name, url, host, length, track_id)
