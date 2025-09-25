

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        output = ""
        for key in self.props:
            addString = f' {key}="{self.props[key]}"'
            output = output + addString
        return output

    def __repr__(self):
        props = self.props_to_html()
        stringRep = f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {props}"
        return stringRep

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        # self.tag = tag
        # self.value = value
        # self.props = props
    
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        props = ""
        if self.props is not None:
            props = self.props_to_html()
        html = f"<{self.tag}{props}>{self.value}</{self.tag}>"
        return html
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        props = ""
        if self.props is not None:
            props = self.props_to_html()
        return f"<{self.tag}{props}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
