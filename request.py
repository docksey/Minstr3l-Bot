from datetime import datetime

class request:
  def __init__(self, track_id, user_id, requested_date: datetime=datetime.now(), request_id: int=0):
    self.request_id = request_id
    self.track_id = track_id
    self.user_id = user_id
    self.requested_date = requested_date
  
  @classmethod
  def from_database(cls, data_row):
    request_id = data_row[0]
    track_id = data_row[1]
    user_id = data_row[2]
    requested_date = data_row[3]
    return cls(track_id, user_id, requested_date, request_id)
