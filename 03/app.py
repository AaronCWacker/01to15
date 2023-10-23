import gradio as gr
import os
from share_btn import community_icon_html, loading_icon_html, share_js

text_gen = gr.Interface.load(name="spaces/Gustavosta/MagicPrompt-Stable-Diffusion")
stable_diffusion = gr.Blocks.load(name="spaces/runwayml/stable-diffusion-v1-5")

def get_images(prompt):
    gallery_dir = stable_diffusion(prompt, fn_index=2)
    sd_output = [os.path.join(gallery_dir, image) for image in os.listdir(gallery_dir)]
    return sd_output, gr.update(visible=True), gr.update(visible=True), gr.update(visible=True)

def get_prompts(prompt_text):
    return text_gen(prompt_text)

css = '''
.animate-spin {
    animation: spin 1s linear infinite;
}
@keyframes spin {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}
#share-btn-container {
    display: flex; padding-left: 0.5rem !important; padding-right: 0.5rem !important; background-color: #000000; justify-content: center; align-items: center; border-radius: 9999px !important; width: 13rem;
}
#share-btn {
    all: initial; color: #ffffff;font-weight: 600; cursor:pointer; font-family: 'IBM Plex Sans', sans-serif; margin-left: 0.5rem !important; padding-top: 0.25rem !important; padding-bottom: 0.25rem !important;
}
#share-btn * {
    all: unset;
}
#share-btn-container div:nth-child(-n+2){
    width: auto !important;
    min-height: 0px !important;
}
#share-btn-container .wrap {
    display: none !important;
}
a {text-decoration-line: underline;}
'''
with gr.Blocks(css=css) as demo:
    gr.HTML("""<div style="text-align: center; max-width: 700px; margin: 0 auto;">
            <div
            style="
                display: inline-flex;
                align-items: center;
                gap: 0.8rem;
                font-size: 1.75rem;
            "
            >
            <h1 style="font-weight: 900; margin-bottom: 7px; margin-top: 5px;">
                Prompt Refinery
            </h1>
            </div>
            <p style="margin-bottom: 10px; font-size: 94%">
           🏭 Prompt Refinery generates variations of your prompt using <a href="https://huggingface.co/spaces/Gustavosta/MagicPrompt-Stable-Diffusion" target="_blank">MagicPrompt and Stable Diffusion</a>
            </p>
        </div>""")
    with gr.Row():
      with gr.Column():
          input_text = gr.Textbox(label="Input text prompt", 
                                lines=2, elem_id="input-text")
          with gr.Row():
            see_prompts = gr.Button("✍️Expand my prompts")

      with gr.Column():
        text_output = gr.Textbox(
                                label="🏭 Expanded text prompts", 
                                lines=8,
                                elem_id="translated"
                            )
        with gr.Row():
            diffuse_btn = gr.Button(value="🏭 Render Images for My Prompts")
      with gr.Column(elem_id="generated-gallery"):
        sd_output = gr.Gallery().style(grid=2, height="auto")
        with gr.Group(elem_id="share-btn-container"):
            community_icon = gr.HTML(community_icon_html, visible=False)
            loading_icon = gr.HTML(loading_icon_html, visible=False)
    see_prompts.click(get_prompts, 
                            inputs = [input_text], 
                            outputs = [
                                text_output
                            ], api_name="TextAI")
    diffuse_btn.click(get_images, 
                          inputs = [
                              text_output
                              ], 
                          outputs = [sd_output, community_icon, loading_icon], api_name="TextAI2")
demo.launch(debug=True)