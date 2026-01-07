import re

def render_template(template, context):
    # Pattern for placeholders like {{ name }} or {{user.age}}
    pattern = re.compile(r"\{\{\s*([a-zA-Z_][\w\.]*)\s*\}\}")

    def replace(match):
        keys = match.group(1).split(".")
        value = context
        for key in keys:
            value = value.get(key, f"{{{{ {match.group(1)} }}}}")
            if not isinstance(value, dict):
                break
        return str(value)

    return pattern.sub(replace, template)


def main():
    print("=== Simple Template Engine ===")
    template = input("Enter template text (use {{ variable }} placeholders):\n")

    print("\nEnter context key=value pairs (type 'done' to finish):")
    context = {}

    while True:
        entry = input("> ").strip()
        if entry.lower() == "done":
            break
        if "=" in entry:
            key, value = entry.split("=", 1)
            context[key.strip()] = value.strip()

    output = render_template(template, context)

    print("\n--- Rendered Output ---")
    print(output)


if __name__ == "__main__":
    main()
