from sentence_transformers import SentenceTransformer


model = SentenceTransformer('all-MiniLM-L6-v2')
class EmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def generate_embeddings(self, text):
        return self.model.encode(text).tolist()
    
    def calculate_similarity(self,text1, text2):
        t1 = self.model.encode(text1)
        t2 = self.model.encode(text2)

        return self.model.similarity(t1, t2)

    


embeddingservice = EmbeddingService()