import gradio as gr


def generate(prompt, nprompt): #функция, принимающая пользовательские запросы
    return prompt + " " + nprompt


with gr.Blocks(theme=gr.themes.Glass()) as demo: #создание элемента интерфейса gr.Blocks для более гибкой настройки в отличие от gr.Interface
    with gr.Row():
        with gr.Column():
            txt = gr.Textbox(label="Yours Prompt") #текстовое поле, принимающее prompt
        with gr.Column():
            txt_2 = gr.Textbox(label="Yours Negative prompt") #текстовое поле, принимающее negative prompt
    img = gr.Image(label="Your image") #поле, позволяющее выводить сгенерированные изображения
    btn = gr.Button(value="Generate") #кнопка генерации изображения
    btn.click(generate, inputs=[txt, txt_2], outputs=[img]) #уловитель события для кнопки генерации



demo.launch(share=True)