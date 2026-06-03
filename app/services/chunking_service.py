class ChunkingService:
    def __init__(self, chunk_size = 500):
        self.chunk_size = chunk_size

    def create_chunks(self, transcript):
        words = transcript.split()
        chunks = []
        for i in range(0, len(words), self.chunk_size):
            chunk = " ". join(words[i:i+self.chunk_size])
            chunks.append(chunk)

        return chunks        
    

chunkingservice = ChunkingService()