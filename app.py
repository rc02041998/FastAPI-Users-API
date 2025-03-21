from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Load LLaMA-2 model
model_name = "meta-llama/Llama-2-7b-chat-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Chatbot function
def chat_with_llama(prompt):
    generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
    output = generator(prompt, max_length=200)
    return output[0]['generated_text']

# Example conversation
print(chat_with_llama("Explain AI in simple words."))