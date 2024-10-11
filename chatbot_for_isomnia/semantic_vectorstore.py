from utils.semantic_chunking import create_semantic_chunks_from_directory_with_overlap, reformat_semantic_chunks_with_overlap
from utils.semantic_chunking import create_summaries_from_chunks, summary_chain
from utils.utils import batch_iterator, convert_defaultdict

from semantic_encoder import BGEM3FlagEmbedEncoder
from FlagEmbedding import BGEM3FlagModel
from qdrant_client import QdrantClient, models

import argparse
import torch

client = QdrantClient("http://localhost:6333")

#Creating vectorstore (if not exist)
if not client.collection_exists(collection_name="semantic_summary_vectorstore"):
    client.create_collection(
        "semantic_summary_vectorstore",
        vectors_config={
            "dense": models.VectorParams(
                size=1024,
                distance=models.Distance.COSINE
            ),
            "colbert": models.VectorParams(
                size=1024,
                distance=models.Distance.COSINE,
                multivector_config=models.MultiVectorConfig(
                    comparator=models.MultiVectorComparator.MAX_SIM,
                )
            ),
        },
        sparse_vectors_config={
            "sparse": models.SparseVectorParams()
        }
    )

if not client.collection_exists(collection_name="semantic_original"):
    client.create_collection("semantic_original", vectors_config={})

parser = argparse.ArgumentParser(description="Qdrant Vectorstore")
parser.add_argument('--dir', default="./extracted/TÁC HẠI", help="directory to create -> adding chunks to vectorstore")

args = parser.parse_args()

if __name__ == "__main__":
    embeddings = BGEM3FlagEmbedEncoder()
    chunks = create_semantic_chunks_from_directory_with_overlap(dir=args.dir, encoder=embeddings, min_split_tokens=300, max_split_tokens=850, overlap=0)
    summaries = create_summaries_from_chunks(chunks, summary_chain)
    
    embeddings = BGEM3FlagModel('BAAI/bge-m3', use_fp16=True)
    torch.cuda.empty_cache()
    
    batch_size = 16
    for batch in batch_iterator(summaries, batch_size):
        text = [summary.page_content for summary in batch]
        res = embeddings.encode(text, return_sparse=True, return_colbert_vecs=True, batch_size=16)

        for i, _ in enumerate(batch):
            doc_id = batch[i].metadata['doc_id']
            title = batch[i].metadata['title']
            content = batch[i].page_content
            try:
                client.upload_points(
                    "semantic_summary_vectorstore",
                    points = [
                        models.PointStruct(
                            id = doc_id,
                            vector = {
                                "dense": res['dense_vecs'][i].tolist(),
                                "colbert": res['colbert_vecs'][i].tolist(),
                                "sparse": convert_defaultdict(res['lexical_weights'][i])
                            },
                            payload = {
                                "doc_id": doc_id,
                                "title": title,
                                "content": content,
                            }

                        )
                    ],
                    batch_size=1
                )
            except:
                print(f"Error when uploading - {doc_id}")
                continue

    
    for chunk in chunks:
        id = chunk.metadata['doc_id']
        try:
            client.upload_points(
                "semantic_original",
                points = [
                    models.PointStruct(
                        id = id,
                        vector = {},
                        payload = {
                            "doc_id": id,
                            "source": chunk.metadata['source'],
                            "title": chunk.metadata["Title"],
                            "page_content": chunk.page_content
                        }
                    )
                ],
                batch_size=1
            )
        except:
            print(f"Error when uploading - {id}")
            continue