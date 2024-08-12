from transformers import AutoTokenizer
from llama_cpp import Llama
import logging

def load_model(model_id: str, model_path: str) -> Llama:
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = Llama(
            model_path=model_path,
            n_ctx=1024,
            n_gpu_layers=-1
        )
        return tokenizer, model
    except Exception as e:
        logging.exception("Failed to initialize model or tokenizer")
        raise RuntimeError(f"Error loading model or tokenizer: {str(e)}")