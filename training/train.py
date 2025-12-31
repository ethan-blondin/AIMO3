BASE_MODEL_PATH = "C:/Users/ebist/Qwen3-8B"

model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL_PATH,
    torch_dtype="auto",
    device_map="auto"
)

tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_PATH)
