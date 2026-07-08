import ipywidgets as widgets
from IPython.display import display, Javascript
import asyncio
from datetime import datetime
from typing import Callable, Awaitable

def build_chat_ui(send_callback: Callable[[str], Awaitable[str | dict]]):
    chat_history = widgets.Output(
        layout=widgets.Layout(
            border='none',
            padding='15px',
            width='100%',
            height='300px',
            overflow='scroll',
            background='#fafafa',
            box_sizing='border-box',
            flex='1',
            display='flex',
            flex_flow='wrap-reverse',
            margin="0"
        )
    )
    chat_history.add_class("chat-scrollbox")

    input_container = widgets.HBox([
        widgets.Text(
            value='',
            placeholder='Ask a question...',
            layout=widgets.Layout(flex='1', margin='0 10px 0 0')
        ),
        widgets.Button(
            description='Submit',
            button_style='primary',
            layout=widgets.Layout(width='80px')
        )
    ], layout=widgets.Layout(
        width='100%',
        padding='10px',
        border_top='1px solid #ddd',
        background='white',
        flex='0 0 auto'
    ))

    input_container.add_class("chat-inputbox")

    question_input = input_container.children[0]
    submit_button = input_container.children[1]

    main_container = widgets.VBox([
        chat_history,
        input_container
    ], layout=widgets.Layout(
        width='95%',
        max_width='900px',
        height='400px',
        margin='10px auto',
        border='1px solid #ccc',
        background='white',
        border_radius='8px',
        overflow='hidden',
        display='flex',
        flex_flow='column'
    ))

    def scroll_to_bottom():
        display(Javascript("""
            const out = document.querySelector('.chat-scrollbox');
            if (out) {
                out.scrollTop = out.scrollHeight;
            }
        """))

    async def handle_question(query):
        submit_button.disabled = True

        if hasattr(handle_question, 'call_count'):
            chat_history.append_stdout("─" * 40 + "\n\n")
        else:
            handle_question.call_count = 0
        handle_question.call_count += 1

        timestamp = datetime.now().strftime("%H:%M")
        chat_history.append_stdout(f"[{timestamp}] You: {query}\n\n")
        chat_history.append_stdout(f"[{timestamp}] Assistant: Thinking...\n")
        chat_history.append_stdout("\n")  # adds a subtle visual break


        try:
            response = await send_callback(query)

            if isinstance(response, dict):
                chat_history.append_stdout(f"{response['text']}\n\n")
                status_parts = []

                if response.get("cached"):
                    status_parts.append("⚡ Served from cache")
                else:
                    status_parts.append("🧠 Fresh LLM response")

                if response.get("used_memory"):
                    status_parts.append("🧠 Session memory used")

                status_parts.append(f"⏱️ Took {response['elapsed']:.2f} seconds")
                chat_history.append_stdout(" • ".join(status_parts) + "\n\n")
            else:
                chat_history.append_stdout(f"{response}\n\n")

        except Exception as e:
            chat_history.append_stdout(f"❌ Error: {type(e).__name__}: {e}\n\n")

        finally:
            submit_button.disabled = False
            scroll_to_bottom()

    def on_submit(_):
        query = question_input.value.strip()
        if query:
            question_input.value = ''
            asyncio.get_event_loop().create_task(handle_question(query))

    submit_button.on_click(on_submit)
    question_input.on_submit(lambda _: on_submit(None))

    chat_history.append_stdout("💬 Welcome! Ask me anything about Nike's 10-K filing.\n\n")
    display(main_container)