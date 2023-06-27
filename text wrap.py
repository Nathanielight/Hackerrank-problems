import textwrap

def wrap(string, max_width):
    wrapped = textwrap.wrap(string, max_width)
    for i in wrapped:
        return "\n" .join(wrapped)

if __name__ == '__main__':
