from textnode import TextNode, TextType

print("hello world")

def main():
    node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(repr(node))

main()

