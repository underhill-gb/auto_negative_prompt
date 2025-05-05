from modules import script_callbacks, scripts, shared

# Default keyword
default_keyword = "blurry"

# Default insertion behavior: False means append, True means prepend
default_insert_at_start = False

def insert_into_negative_prompt(prompt: str, keyword: str, prepend: bool) -> str:
    if not keyword:
        return prompt
    keyword = keyword.strip().lower()
    if keyword and keyword not in prompt.lower():
        if prepend:
            return f"{keyword}, {prompt.strip()}" if prompt.strip() else keyword
        else:
            return f"{prompt.strip()}, {keyword}" if prompt.strip() else keyword
    return prompt

class InsertKeywordNegativePrompt(scripts.Script):
    def title(self):
        return "Auto Insert Negative Prompt Keyword"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def process(self, p):
        keyword = shared.opts.data.get("insert_negative_keyword", default_keyword)
        prepend = shared.opts.data.get("insert_negative_keyword_prepend", default_insert_at_start)

        # Modify the main negative prompt
        p.negative_prompt = insert_into_negative_prompt(p.negative_prompt, keyword, prepend)

        # Modify other related prompt fields
        if hasattr(p, "all_negative_prompts"):
            p.all_negative_prompts = [insert_into_negative_prompt(neg, keyword, prepend) for neg in p.all_negative_prompts]

        if getattr(p, "enable_hr", False):
            if hasattr(p, "hr_negative_prompt"):
                p.hr_negative_prompt = insert_into_negative_prompt(p.hr_negative_prompt, keyword, prepend)
            if hasattr(p, "all_hr_negative_prompts"):
                p.all_hr_negative_prompts = [insert_into_negative_prompt(neg, keyword, prepend) for neg in p.all_hr_negative_prompts]

# UI settings
def on_ui_settings():
    section = ("insert_neg_keyword", "Negative Prompt Insert")

    shared.opts.add_option(
        "insert_negative_keyword",
        shared.OptionInfo(default_keyword, "Word(s) to insert into negative prompts", section=section)
    )
    shared.opts.add_option(
        "insert_negative_keyword_prepend",
        shared.OptionInfo(default_insert_at_start, "Insert keyword(s) at beginning (instead of end)", section=section)
    )

script_callbacks.on_ui_settings(on_ui_settings)