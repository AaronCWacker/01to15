from huggingface_hub import InferenceClient
import gradio as gr

client = InferenceClient(
    "mistralai/Mistral-7B-Instruct-v0.1"
)


def format_prompt(message, history):
  prompt = "<s>"
  for user_prompt, bot_response in history:
    prompt += f"[INST] {user_prompt} [/INST]"
    prompt += f" {bot_response}</s> "
  prompt += f"[INST] {message} [/INST]"
  return prompt

def generate(
    prompt, history, temperature=0.9, max_new_tokens=256, top_p=0.95, repetition_penalty=1.0,
):
    temperature = float(temperature)
    if temperature < 1e-2:
        temperature = 1e-2
    top_p = float(top_p)

    generate_kwargs = dict(
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        seed=42,
    )

    formatted_prompt = format_prompt(prompt, history)

    stream = client.text_generation(formatted_prompt, **generate_kwargs, stream=True, details=True, return_full_text=False)
    output = ""

    for response in stream:
        output += response.token.text
        yield output
    return output


additional_inputs=[
    gr.Slider(
        label="Temperature",
        value=0.9,
        minimum=0.0,
        maximum=1.0,
        step=0.05,
        interactive=True,
        info="Higher values produce more diverse outputs",
    ),
    gr.Slider(
        label="Max new tokens",
        value=256,
        minimum=0,
        maximum=1048,
        step=64,
        interactive=True,
        info="The maximum numbers of new tokens",
    ),
    gr.Slider(
        label="Top-p (nucleus sampling)",
        value=0.90,
        minimum=0.0,
        maximum=1,
        step=0.05,
        interactive=True,
        info="Higher values sample more low-probability tokens",
    ),
    gr.Slider(
        label="Repetition penalty",
        value=1.2,
        minimum=1.0,
        maximum=2.0,
        step=0.05,
        interactive=True,
        info="Penalize repeated tokens",
    )
]

css = """
  #mkd {
    height: 200px; 
    overflow: auto; 
    border: 1px solid #ccc; 
  }
"""

with gr.Blocks(css=css) as demo:
  
    gr.ChatInterface(
        generate,
        additional_inputs=additional_inputs,       
        examples = [
            ["🏰 Welcome to the Kingdom of Elandria! You are Jim and Tim, two bumbling bros with a knack for mischief. 🤴🤴 [Action: Introduce yourselves, Equipment: Scepters of Foolishness]"],
            ["🌲 You find yourselves in a forest filled with magical creatures and oddly specific 'Do Not Disturb' signs. 🦄 [Action: Proceed cautiously, Equipment: Map of Social Etiquette]"],
            ["🍻 You stumble upon a dwarf tavern. They offer you 'Beard Beer.' Do you drink it? 🍺 [Action: Chug or Pass, Equipment: Empty Mugs]"],
            ["🐉 A vegan dragon appears and chastises you for your leather boots. What do you do? 🗡️🏃 [Action: Apologize and offer kale, Equipment: Non-leather sandals]"],
            ["💎 You find a treasure chest labeled 'Not a Mimic.' Seems legit. Do you open it? 🗝️ [Action: Open or No way, Equipment: Mimic Repellent]"],
            ["🦇 You're swarmed by bats in a cave. One bat offers you 'organic guano.' How do you react? 🕯️ [Action: Politely decline, Equipment: Nose Plugs]"],
            ["🔮 A mysterious sorcerer offers you a 'Love Potion No. 9½.' Do you take a sip? 🍶 [Action: Sip or Skip, Equipment: Breath Mints]"],
            ["⚔️ Bandits demand gold, but they accept credit cards. What's your move? 💰 [Action: Pay or Pray, Equipment: Wallets]"],
            ["🚪 A door with three locks and a sign saying 'Beware of the Dog.' Do you search for the keys or try to pet the dog? 🗝️💪 [Action: Unlock or Pet, Equipment: Dog Treats]"],
            ["🌊 A river blocks your path. A mermaid offers to carry you across for a 'small' fee. 🏊‍♀️🌉 [Action: Accept or Decline, Equipment: Bargaining Skills]"],
            ["🦁 You encounter a pride of lions playing poker. Do you join the game or fold? 🤫🔄 [Action: Play or Fold, Equipment: Poker Face]"],
            ["🍎 A tree filled with golden apples and a sign saying, 'Seriously, don't eat these!' What do you do? 🤔 [Action: Eat or Retreat, Equipment: Stomach Pump]"],
            ["🌕 The moon turns red, wolves start howling, and your horoscope says 'Stay in bed.' Do you camp or go? 🏕️🚶 [Action: Camp or Scamp, Equipment: Astrology App]"],
            ["💀 The final boss is an undead warrior selling life insurance. Do you combat or sign up? ⚔️🤝 [Action: Fight or Finance, Equipment: Policy Guide]"]
        ]
    )
    gr.HTML("""<h2>🤖 Mistral Chat - Gradio 🤖</h2>
        In this demo, you can chat with <a href='https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1'>Mistral-7B-Instruct</a> model. 💬
        Learn more about the model <a href='https://huggingface.co/docs/transformers/main/model_doc/mistral'>here</a>. 📚
        <h2>🛠 Model Features 🛠</h2>
        <ul>
          <li>🪟 Sliding Window Attention with 128K tokens span</li>
          <li>🚀 GQA for faster inference</li>
          <li>📝 Byte-fallback BPE tokenizer</li>
        </ul>
        <h3>📜 License 📜  Released under Apache 2.0 License</h3>
        <h3>📦 Usage 📦</h3>
        <ul>
          <li>📚 Available on Huggingface Hub</li>
          <li>🐍 Python code snippets for easy setup</li>
          <li>📈 Expected speedups with Flash Attention 2</li>
        </ul>
    """)

    markdown="""
    | Feature | Description | Byline |
    |---------|-------------|--------|
    | 🪟 Sliding Window Attention with 128K tokens span | Enables the model to have a larger context for each token. | Increases model's understanding of context, resulting in more coherent and contextually relevant outputs. |
    | 🚀 GQA for faster inference | Graph Query Attention allows faster computation during inference. | Speeds up the model inference time without sacrificing too much on accuracy. |
    | 📝 Byte-fallback BPE tokenizer | Uses Byte Pair Encoding but can fall back to byte-level encoding. | Allows the tokenizer to handle a wider variety of input text while keeping token size manageable. |
    | 📜 License | Released under Apache 2.0 License | Gives you a permissive free software license, allowing you freedom to use, modify, and distribute the code. |
    | 📦 Usage | | |
    | 📚 Available on Huggingface Hub | The model can be easily downloaded and set up from Huggingface. | Makes it easier to integrate the model into various projects. |
    | 🐍 Python code snippets for easy setup | Provides Python code snippets for quick and easy model setup. | Facilitates rapid development and deployment, especially useful for prototyping. |
    | 📈 Expected speedups with Flash Attention 2 | Upcoming update expected to bring speed improvements. | Keep an eye out for this update to benefit from performance gains. |
# 🛠 Model Features and More 🛠

## Features

- 🪟 Sliding Window Attention with 128K tokens span  
  - **Byline**: Increases model's understanding of context, resulting in more coherent and contextually relevant outputs.

- 🚀 GQA for faster inference  
  - **Byline**: Speeds up the model inference time without sacrificing too much on accuracy.

- 📝 Byte-fallback BPE tokenizer  
  - **Byline**: Allows the tokenizer to handle a wider variety of input text while keeping token size manageable.

- 📜 License: Released under Apache 2.0 License  
  - **Byline**: Gives you a permissive free software license, allowing you freedom to use, modify, and distribute the code.

## Usage 📦

- 📚 Available on Huggingface Hub  
  - **Byline**: Makes it easier to integrate the model into various projects.

- 🐍 Python code snippets for easy setup  
  - **Byline**: Facilitates rapid development and deployment, especially useful for prototyping.

- 📈 Expected speedups with Flash Attention 2  
  - **Byline**: Keep an eye out for this update to benefit from performance gains.
    """
    gr.Markdown(markdown)  
    
demo.queue().launch(debug=True)