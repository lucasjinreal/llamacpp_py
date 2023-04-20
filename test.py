import sys
import llamapy
import sys


def progress_callback(progress):
    # print("Progress: {:.2f}%".format(progress * 100))
    # sys.stdout.flush()
    pass


params = llamapy.InferenceParams.default_with_callback(progress_callback)
params.path_model = sys.argv[1]
params.seed = 19472
params.repeat_penalty = 1.0
model = llamapy.LlamaInference(params)

prompt = " Llama is"
prompt_tokens = model.tokenize(prompt, True)
model.update_input(prompt_tokens)

model.ingest_all_pending_input()
print(model.system_info())

print(prompt, end='')
for i in range(20):
    model.eval()
    token = model.sample()
    text = model.token_to_str(token)
    print(text, end="")
    
# Flush stdout
sys.stdout.flush()
# model.print_timings()
