class Storage:
    def __init__(self):
        self.storage = {}

    def save_transcript(self,video_id, transcript):
        if video_id in self.storage:
            return "Transcript already exists"

        else:
            self.storage[video_id]  = transcript
    

    def get_transcript(self,video_id):
        if video_id in self.storage:
            return self.storage[video_id]
        else:
            return None
        

storage = Storage()