def gen_prompt(from_lang: str, to_lang: str, code: str):
    return f"""This is a code translator from {from_lang} to {to_lang}

#start
JavaScript:
console.log("Hello world!");
Python:
print("Hello world!")
#end

#start
JavaScript:
{code}
Python:
"""